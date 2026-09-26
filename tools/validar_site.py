#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import shutil
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
DOCS_SOURCE = ROOT / "docs" / "paginas"
DOCS_PUBLIC = ROOT / "docs"
OUTPUT_LANGS = {"saida", "saída", "output", "terminal", "resultado"}
TOKEN_RE = re.compile(r'class="code-(?:key|str|num|mod|fn|comment)"')


class HtmlAuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])


def public_from_source(source: Path) -> Path:
    rel = source.relative_to(DOCS_SOURCE)
    if rel.name == "introducao.md":
        rel = rel.with_name("index.md")
    elif rel.name == "repl_cli.md":
        rel = rel.with_name("repl_cli.md")
    return DOCS_PUBLIC / rel.with_suffix(".html")


def fenced_blocks(md: str) -> list[tuple[str, str]]:
    lines = md.replace("\r\n", "\n").split("\n")
    result: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped.startswith("```"):
            i += 1
            continue
        lang = stripped[3:].strip()
        i += 1
        buf: list[str] = []
        while i < len(lines) and not lines[i].strip().startswith("```"):
            buf.append(lines[i])
            i += 1
        if i < len(lines):
            i += 1
        result.append((lang, "\n".join(buf)))
    return result


def html_code_blocks(text: str) -> list[tuple[str, str]]:
    # O resumo rápido de módulos reutiliza um exemplo já existente no Markdown.
    # Ele é uma projeção didática adicional, não um novo bloco fonte, portanto
    # deve ser ignorado pela auditoria de fidelidade 1:1.
    text = re.sub(r'<section class="module-quick-summary".*?</section>', '', text, flags=re.S)
    blocks: list[tuple[str, str]] = []
    for m in re.finditer(r'<pre><code(?: class="language-([^"]+)")?>(.*?)</code></pre>', text, re.S):
        lang = m.group(1) or ""
        body = m.group(2)
        plain = re.sub(r"<[^>]+>", "", body)
        from html import unescape
        blocks.append((lang, unescape(plain)))
    return blocks


def audit_links() -> tuple[int, list[str]]:
    errors: list[str] = []
    html_files = sorted(
        p for p in ROOT.rglob("*.html")
        if ".git" not in p.parts and "templates" not in p.parts
    )
    parsed: dict[Path, HtmlAuditParser] = {}
    for path in html_files:
        parser = HtmlAuditParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed[path.resolve()] = parser
        duplicates = sorted({x for x in parser.ids if parser.ids.count(x) > 1})
        for ident in duplicates:
            errors.append(f"ID duplicado em {path.relative_to(ROOT)}: #{ident}")

    for path, parser in parsed.items():
        for href in parser.hrefs:
            split = urlsplit(href)
            if split.scheme in {"http", "https", "mailto", "tel", "javascript"} or href.startswith("//"):
                continue
            if href == "#":
                continue
            target_path = unquote(split.path)
            fragment = unquote(split.fragment)
            if not target_path:
                target = path
            else:
                target = (path.parent / target_path).resolve()
                if target.is_dir():
                    target = target / "index.html"
            if target.suffix == "" and target.exists() and target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"Link local ausente em {path.relative_to(ROOT)}: {href}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed.get(target.resolve())
                if target_parser is None:
                    target_parser = HtmlAuditParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed[target.resolve()] = target_parser
                if fragment not in target_parser.ids:
                    errors.append(f"Âncora ausente em {path.relative_to(ROOT)}: {href}")
    return len(html_files), errors


def audit_code_fidelity() -> tuple[int, list[str]]:
    errors: list[str] = []
    checked = 0
    for source in sorted(DOCS_SOURCE.rglob("*.md")):
        public = public_from_source(source)
        if not public.exists():
            errors.append(f"HTML ausente para {source.relative_to(ROOT)}")
            continue
        md_blocks = [(lang, raw) for lang, raw in fenced_blocks(source.read_text(encoding="utf-8")) if lang.casefold() not in OUTPUT_LANGS]
        html_blocks = html_code_blocks(public.read_text(encoding="utf-8"))
        if len(md_blocks) != len(html_blocks):
            errors.append(f"Quantidade de blocos divergente em {source.relative_to(ROOT)}: {len(md_blocks)} != {len(html_blocks)}")
            continue
        for index, ((lang, raw), (html_lang, recovered)) in enumerate(zip(md_blocks, html_blocks), 1):
            checked += 1
            if raw != recovered:
                errors.append(f"Fidelidade de código falhou em {source.relative_to(ROOT)} bloco {index}")
            expected_lang = lang
            if expected_lang != html_lang:
                errors.append(f"Linguagem divergente em {source.relative_to(ROOT)} bloco {index}: {expected_lang!r} != {html_lang!r}")
        # Auditoria de whitelist é feita por regex nos blocos individuais abaixo.
        html_text = public.read_text(encoding="utf-8")
        for index, m in enumerate(re.finditer(r'<pre><code(?: class="language-([^"]+)")?>(.*?)</code></pre>', html_text, re.S), 1):
            lang = (m.group(1) or "").casefold()
            has_tokens = bool(TOKEN_RE.search(m.group(2)))
            coral = lang == "coral" or lang.startswith("coral-")
            if has_tokens and not coral:
                errors.append(f"Realce Coral aplicado em linguagem não Coral em {source.relative_to(ROOT)} bloco {index}: {lang or '(vazio)'}")
    return checked, errors


def audit_syntax_contract() -> list[str]:
    errors: list[str] = []
    path = ROOT / "docs" / "dados" / "sintaxe.json"
    if not path.exists():
        return ["docs/dados/sintaxe.json ausente"]
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["release", "esquema", "lexemas", "identificador_inicio", "identificador_continuacao", "decimal", "aspas"]
    for key in required:
        if key not in data:
            errors.append(f"campo ausente em sintaxe.json: {key}")
    if data.get("decimal") != ".":
        errors.append(f"separador decimal inesperado: {data.get('decimal')!r}")
    if set(data.get("aspas", [])) != {'"', "'"}:
        errors.append("contrato de aspas divergente da release importada")
    if not data.get("lexemas"):
        errors.append("lista de lexemas vazia")
    return errors



def audit_api_didactic() -> list[str]:
    """Valida a dupla camada da referência: leitura humana + detalhes técnicos."""
    errors: list[str] = []
    modules_path = ROOT / "docs" / "dados" / "modulos.json"
    if not modules_path.exists():
        return ["docs/dados/modulos.json ausente"]
    modules = json.loads(modules_path.read_text(encoding="utf-8"))
    expected = sum(len(m.get("api", [])) for m in modules)
    md_files = sorted((ROOT / "docs" / "paginas" / "modulos").glob("*.md"))
    md_text = "\n".join(p.read_text(encoding="utf-8") for p in md_files)
    html_files = sorted((ROOT / "docs" / "modulos").glob("*.html"))
    html_text = "\n".join(p.read_text(encoding="utf-8") for p in html_files)
    if "Entrada pública `" in md_text:
        errors.append("referência da API ainda contém descrições mecânicas 'Entrada pública'")
    details_md = md_text.count(":::details Detalhes técnicos")
    details_html = html_text.count('class="api-tech-details"')
    if details_md != expected:
        errors.append(f"detalhes técnicos no Markdown: {details_md} != {expected} símbolos")
    if details_html != expected:
        errors.append(f"detalhes técnicos no HTML: {details_html} != {expected} símbolos")
    if "| Parâmetro | Significado | Tipo | Padrão |" not in md_text:
        errors.append("tabela didática de parâmetros não encontrada")
    if "api-tech-body" not in html_text:
        errors.append("camada técnica recolhível não foi renderizada")
    return errors


def audit_qol_didatica() -> list[str]:
    """Valida os contratos da primeira fase de QoL e didática."""
    errors: list[str] = []
    template_path = ROOT / "templates" / "docs.html"
    js_path = ROOT / "assets" / "js" / "site.js"
    css_path = ROOT / "assets" / "css" / "styles.css"
    guide_md = ROOT / "docs" / "paginas" / "guias_objetivos.md"
    guide_html = ROOT / "docs" / "guias_objetivos.html"
    modules_dir = ROOT / "docs" / "modulos"

    template = template_path.read_text(encoding="utf-8") if template_path.exists() else ""
    js = js_path.read_text(encoding="utf-8") if js_path.exists() else ""
    css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

    for snippet, label in (
        ('data-reading-mode="learn"', "modo Aprender padrão"),
        ('data-reading-mode="reference"', "botão do modo Referência"),
        ('{{MODULE_QUICK_SUMMARY}}', "slot de resumo rápido"),
    ):
        if snippet not in template:
            errors.append(f"QoL didática ausente no template: {label}")

    for snippet, label in (
        ("coral-reading-mode", "persistência local do modo de leitura"),
        ("classifyReadingSections", "classificação das seções por modo"),
        ("setReadingMode", "alternância Aprender/Referência"),
    ):
        if snippet not in js:
            errors.append(f"QoL didática ausente no JavaScript: {label}")

    for snippet, label in (
        ('.module-quick-summary', "resumo rápido"),
        ('.expected-result', "resultado esperado"),
        ('data-reading-mode="reference"', "regras visuais de modo"),
    ):
        if snippet not in css:
            errors.append(f"QoL didática ausente no CSS: {label}")

    module_pages = sorted(modules_dir.glob("*.html"))
    for page in module_pages:
        text = page.read_text(encoding="utf-8")
        if 'class="module-quick-summary"' not in text:
            errors.append(f"resumo rápido ausente em {page.relative_to(ROOT)}")

    if not guide_md.exists() or not guide_html.exists():
        errors.append("guia por objetivo ausente")
    else:
        guide_text = guide_html.read_text(encoding="utf-8")
        if "O que você quer fazer?" not in guide_text:
            errors.append("guia por objetivo sem título esperado")
        if guide_text.count('class="expected-result"') < 8:
            errors.append("guia por objetivo tem poucos resultados esperados")

    expected_total = sum(
        p.read_text(encoding="utf-8").count(":::resultado")
        for p in DOCS_SOURCE.rglob("*.md")
    )
    rendered_total = sum(
        p.read_text(encoding="utf-8").count('class="expected-result"')
        for p in DOCS_PUBLIC.rglob("*.html")
    )
    if expected_total != rendered_total:
        errors.append(f"resultados esperados renderizados: {rendered_total} != {expected_total}")
    return errors


def audit_header_layout_contract() -> list[str]:
    """Impede regressão do cabeçalho claro quando rótulos ficam mais largos."""
    errors: list[str] = []
    css_path = ROOT / "assets" / "css" / "styles.css"
    if not css_path.exists():
        return ["assets/css/styles.css ausente"]
    css = css_path.read_text(encoding="utf-8")
    contracts = {
        "botões do cabeçalho não podem quebrar linha": "white-space: nowrap;",
        "ações do cabeçalho precisam poder ceder espaço à busca": "min-width: 0; flex: 1 1 auto;",
        "busca é o elemento elástico do cabeçalho": "flex: 1 1 280px;",
        "botões permanecem não encolhíveis": "flex: 0 0 auto;",
    }
    for label, snippet in contracts.items():
        if snippet not in css:
            errors.append(f"contrato visual do cabeçalho ausente: {label}")
    return errors

def cleanup_runtime_residues() -> None:
    for name in ("__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"):
        for path in ROOT.rglob(name):
            if path.is_dir():
                shutil.rmtree(path, ignore_errors=True)
    for path in ROOT.rglob("*.pyc"):
        path.unlink(missing_ok=True)


def audit_residues() -> list[str]:
    bad_names = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if any(part in bad_names for part in path.parts) or path.suffix == ".pyc":
            errors.append(f"resíduo de execução: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    failures: list[str] = []
    cleanup_runtime_residues()

    test = subprocess.run([sys.executable, str(TOOLS / "test_syntax_highlight.py")], cwd=ROOT, text=True, capture_output=True)
    if test.returncode != 0:
        failures.append("testes unitários do realce falharam:\n" + test.stdout + test.stderr)
    cleanup_runtime_residues()

    html_count, link_errors = audit_links()
    failures.extend(link_errors)
    code_count, code_errors = audit_code_fidelity()
    failures.extend(code_errors)
    failures.extend(audit_syntax_contract())
    failures.extend(audit_header_layout_contract())
    failures.extend(audit_api_didactic())
    failures.extend(audit_qol_didatica())
    failures.extend(audit_residues())

    if failures:
        print("VALIDAÇÃO DO SITE: FALHA")
        for failure in failures:
            print(" -", failure)
        return 1

    print("VALIDAÇÃO DO SITE: OK")
    print(f"HTML verificados: {html_count}")
    print(f"Blocos de código comparados: {code_count}")
    print("Realce Coral: whitelist, fidelidade, strings, comentários, números, módulos e chamadas tradicionais OK")
    print("Links, âncoras, IDs, contrato sintático, referência didática de API, QoL didática e cabeçalho responsivo: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
