#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import html
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from api_docs import enrich_modules_from_zip, render_api_markdown
from site_renderer import (
    PRIMARY_GROUP, OTHER_GROUP, PRIMARY_MODULE_ORDER,
    render_docs as render_docs_multipage, source_to_public, split_table_row,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DADOS = DOCS / "dados"
PAGINAS = DOCS / "paginas"
MODULOS_DIR = PAGINAS / "modulos"
CHANGELOG_DIR = DOCS / "changelog"
TEMPLATES = ROOT / "templates"
SNAPSHOT = DADOS / "snapshot_release.json"
VERSION_FILE = DADOS / "versao.json"
MODULES_FILE = DADOS / "modulos.json"
CLI_FILE = DADOS / "cli.json"
EXAMPLES_FILE = DADOS / "exemplos.json"
NAV_FILE = DADOS / "navegacao.json"
SINTAXE_FILE = DADOS / "sintaxe.json"

AUTO_START = "<!-- AUTO:MODULO -->"
AUTO_END = "<!-- /AUTO:MODULO -->"

# Domínio de exemplo (.example é TLD reservado para documentação).
# TROQUE via --url-base quando o domínio público da Coral existir.
SITE_URL_PADRAO = "https://coral-lang.example"

DEFAULT_HIGHLIGHTS = {"numerico", "jogos", "mundo", "rpg", "regras", "sistema", "laboratorio", "hardware"}


@dataclass
class ReleaseInfo:
    runtime: str
    extensao_vscode: str
    livro: str
    modulos: list[dict[str, Any]]
    cli: dict[str, Any]
    exemplos: list[str]
    changelog: str
    sintaxe: dict[str, Any]
    source: str


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def literal_assignment(source: str, name: str) -> Any:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name:
            return ast.literal_eval(node.value)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return ast.literal_eval(node.value)
    raise KeyError(name)


def read_zip_text(zf: zipfile.ZipFile, suffix: str) -> str:
    matches = [n for n in zf.namelist() if n.endswith(suffix)]
    if not matches:
        return ""
    matches.sort(key=len)
    return zf.read(matches[0]).decode("utf-8", errors="replace")


def parse_version_init(text: str) -> tuple[str, str]:
    runtime = re.search(r'__version__\s*=\s*["\']([^"\']+)', text)
    livro = re.search(r'EDICAO_LIVRO\s*=\s*["\']([^"\']+)', text)
    return (runtime.group(1) if runtime else "desconhecida", livro.group(1) if livro else "desconhecida")


def _assignment_expr(source: str, name: str) -> ast.expr:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name and node.value is not None:
            return node.value
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return node.value
    raise KeyError(name)


def _string_collection(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"set", "frozenset", "tuple", "list"} and node.args:
        node = node.args[0]
    if isinstance(node, (ast.Set, ast.Tuple, ast.List)):
        values: list[str] = []
        for item in node.elts:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                values.append(item.value)
        return values
    return []


def extract_syntax_contract(zf: zipfile.ZipFile, runtime: str) -> dict[str, Any]:
    """Extrai estaticamente o contrato léxico/sintático necessário ao site.

    Nenhum código da release é importado ou executado. O resultado é um artefato
    próprio da documentação, consumido pelo renderer estático.
    """
    schema = read_zip_text(zf, "Projeto/coral/esquema_sintatico.py")
    identifiers = read_zip_text(zf, "Projeto/coral/identificadores.py")
    lexical = read_zip_text(zf, "Projeto/coral/lexico.py")
    if not schema or not identifiers or not lexical:
        raise RuntimeError("release sem contrato sintático suficiente para o realce da documentação")

    try:
        schema_version = str(literal_assignment(schema, "VERSAO_ESQUEMA"))
    except Exception:
        schema_version = "desconhecida"

    ignored: set[str] = set()
    try:
        ignored = {x.casefold() for x in _string_collection(_assignment_expr(schema, "_LEXEMAS_EDITOR_IGNORADOS"))}
    except Exception:
        pass

    lexemas: set[str] = set()
    forms_expr = _assignment_expr(schema, "FORMAS")
    if isinstance(forms_expr, (ast.Tuple, ast.List)):
        for item in forms_expr.elts:
            if not isinstance(item, ast.Call) or len(item.args) < 3:
                continue
            forma_node = item.args[2]
            if not isinstance(forma_node, ast.Constant) or not isinstance(forma_node.value, str):
                continue
            for palavra in re.findall(r"[A-Za-zÀ-ÿ]+", forma_node.value):
                if palavra.isupper():
                    continue
                normal = palavra.casefold()
                if normal not in ignored:
                    lexemas.add(normal)

    inicio_ident = str(literal_assignment(identifiers, "INICIO_IDENT"))
    continuacao_ident = str(literal_assignment(identifiers, "CONT_IDENT"))

    quotes: list[str] = []
    lexical_tree = ast.parse(lexical)
    decimal = "."
    for node in ast.walk(lexical_tree):
        if not isinstance(node, ast.Compare) or len(node.ops) != 1 or len(node.comparators) != 1:
            continue
        comp = node.comparators[0]
        if isinstance(node.ops[0], ast.In) and isinstance(node.left, ast.Name) and node.left.id == "c":
            values = _string_collection(comp)
            if values and all(v in {"\"", "'"} for v in values):
                quotes = values
        if isinstance(node.ops[0], ast.Eq) and isinstance(comp, ast.Constant) and comp.value in {".", ","}:
            left = node.left
            if isinstance(left, ast.Subscript) and isinstance(left.value, ast.Name) and left.value.id == "texto":
                decimal = str(comp.value)

    return {
        "release": runtime,
        "esquema": schema_version,
        "lexemas": sorted(lexemas),
        "identificador_inicio": inicio_ident,
        "identificador_continuacao": continuacao_ident,
        "decimal": decimal,
        "aspas": quotes or ["\"", "'"],
        "linguagens": ["coral", "coral-*"],
        "origem": {
            "esquema": "Projeto/coral/esquema_sintatico.py",
            "lexico": "Projeto/coral/lexico.py",
            "identificadores": "Projeto/coral/identificadores.py",
        },
    }


def read_generated_contract(zf: zipfile.ZipFile) -> str:
    candidates = [
        name for name in zf.namelist()
        if re.search(r"Projeto/docs/CONTRATOS_GERADOS(?:_[0-9_]+)?\.md$", name)
    ]
    if not candidates:
        return ""
    candidates.sort(key=lambda n: (len(n), n), reverse=True)
    return zf.read(candidates[0]).decode("utf-8", errors="replace")


def module_exports_from_zip(zf: zipfile.ZipFile, importacao: str) -> list[str]:
    rel = importacao.replace(".", "/") + ".py"
    text = read_zip_text(zf, rel)
    if not text:
        return []
    try:
        value = literal_assignment(text, "__all__")
    except Exception:
        return []
    if isinstance(value, (list, tuple)):
        return [str(x) for x in value if str(x) and not str(x).startswith("_")]
    return []


def parse_cli_contract(text: str) -> dict[str, Any]:
    if not text:
        return {"opcoes": [], "subcomandos": []}
    section = text.split("## CLI", 1)
    if len(section) < 2:
        return {"opcoes": [], "subcomandos": []}
    cli_text = section[1].split("## ", 1)[0]
    options = re.findall(r'`(-{1,2}[A-Za-z0-9][A-Za-z0-9-]*)`', cli_text)
    sub = []
    m = re.search(r"Subcomandos de conveniência:\s*(.+)", cli_text)
    if m:
        sub = re.findall(r'`([^`]+)`', m.group(1))
    return {"opcoes": sorted(dict.fromkeys(options)), "subcomandos": sub}


def changelog_for_version(text: str, version: str) -> str:
    if not text:
        return ""
    pattern = re.compile(rf"^#\s+{re.escape(version)}\b.*?$", re.M)
    m = pattern.search(text)
    if not m:
        return ""
    start = m.start()
    nxt = re.search(r"^#\s+\d+\.\d+\.\d+\b", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[start:end].strip() + "\n"


def import_release(zip_path: Path) -> ReleaseInfo:
    with zipfile.ZipFile(zip_path) as zf:
        init_text = read_zip_text(zf, "Projeto/coral/__init__.py")
        runtime, livro = parse_version_init(init_text)

        package_text = read_zip_text(zf, "Projeto/vscode-coral/package.json")
        try:
            package = json.loads(package_text)
            ext = str(package.get("version", "desconhecida"))
        except Exception:
            ext = "desconhecida"

        std_text = read_zip_text(zf, "Projeto/coral/registro_stdlib.py")
        editor_text = read_zip_text(zf, "Projeto/coral/superficie_editor.py")
        std = literal_assignment(std_text, "REGISTRO_STDLIB") if std_text else {}
        editor = literal_assignment(editor_text, "DOMINIOS_EDITOR") if editor_text else {}

        merged: dict[str, dict[str, Any]] = {}
        for name, meta in std.items():
            item = dict(meta)
            item["nome"] = name
            item["importacao"] = item.get("importacao", f"coral.{name}")
            item["operacoes"] = list(item.get("operacoes", []))
            merged[name] = item
        for name, meta in editor.items():
            if name in merged:
                continue
            item = dict(meta)
            item["nome"] = name
            item["importacao"] = item.get("importacao", f"coral.{name}")
            item["para_livro"] = True
            item["operacoes"] = module_exports_from_zip(zf, item["importacao"])
            merged[name] = item

        modules = []
        for name in sorted(merged):
            item = merged[name]
            modules.append({
                "nome": name,
                "importacao": item.get("importacao", f"coral.{name}"),
                "categoria": item.get("categoria", "geral"),
                "finalidade": item.get("finalidade", ""),
                "para_livro": bool(item.get("para_livro", True)),
                "advertencia": item.get("advertencia", ""),
                "operacoes": list(item.get("operacoes", [])),
                "destaque": name in DEFAULT_HIGHLIGHTS,
                "pagina": f"modulos/{name}",
            })
        modules = enrich_modules_from_zip(zf, modules)
        syntax = extract_syntax_contract(zf, runtime)

        contracts = read_generated_contract(zf)
        cli = parse_cli_contract(contracts)

        examples = sorted(
            n.split("Coral/", 1)[-1]
            for n in zf.namelist()
            if n.startswith("Coral/Exemplos/") and n.endswith(".coral")
        )

        changelog_all = read_zip_text(zf, "Projeto/CHANGELOG.md")
        changelog = changelog_for_version(changelog_all, runtime)

    return ReleaseInfo(runtime, ext, livro, modules, cli, examples, changelog, syntax, zip_path.name)


def release_snapshot(info: ReleaseInfo) -> dict[str, Any]:
    return {
        "runtime": info.runtime,
        "extensao_vscode": info.extensao_vscode,
        "livro": info.livro,
        "modulos": {m["nome"]: m.get("operacoes", []) for m in info.modulos},
        "cli": info.cli,
        "exemplos": info.exemplos,
        "sintaxe": info.sintaxe,
        "source": info.source,
    }


def diff_release(old: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    old_modules = old.get("modulos", {})
    new_modules = new.get("modulos", {})
    old_names, new_names = set(old_modules), set(new_modules)
    changed = []
    for name in sorted(old_names & new_names):
        if list(old_modules.get(name, [])) != list(new_modules.get(name, [])):
            changed.append(name)
    old_ex = set(old.get("exemplos", []))
    new_ex = set(new.get("exemplos", []))
    old_cli = set(old.get("cli", {}).get("opcoes", [])) | set(old.get("cli", {}).get("subcomandos", []))
    new_cli = set(new.get("cli", {}).get("opcoes", [])) | set(new.get("cli", {}).get("subcomandos", []))
    return {
        "versao_anterior": old.get("runtime"),
        "versao_nova": new.get("runtime"),
        "modulos_novos": sorted(new_names - old_names),
        "modulos_removidos": sorted(old_names - new_names),
        "modulos_alterados": changed,
        "cli_novo": sorted(new_cli - old_cli),
        "cli_removido": sorted(old_cli - new_cli),
        "exemplos_novos": sorted(new_ex - old_ex),
        "exemplos_removidos": sorted(old_ex - new_ex),
        "sintaxe_alterada": old.get("sintaxe") != new.get("sintaxe"),
    }


def _clean_symbol_cell(text: str) -> list[str]:
    # Células da API essencial podem agrupar símbolos com `/`.
    return [part.strip().strip("`") for part in text.split("/") if part.strip().strip("`")]


def extract_api_editorial(text: str, module: dict[str, Any]) -> dict[str, Any]:
    """Extrai evidência editorial já escrita na página do módulo.

    O importador usa apenas conteúdo manual já existente como apoio didático.
    Ele não cria fatos novos sobre a API. A tabela "API essencial" fornece
    descrições curtas e os blocos Coral fornecem exemplos somente quando o
    símbolo aparece literalmente no código.
    """
    purposes: dict[str, str] = {}
    match = re.search(r"^## API essencial\s*$\n(.*?)(?=^##\s|\Z)", text, flags=re.M | re.S)
    if match:
        lines = match.group(1).splitlines()
        for i, line in enumerate(lines):
            if not line.strip().startswith("|") or i + 1 >= len(lines):
                continue
            if not re.match(r"^\s*\|?\s*:?-+", lines[i + 1]):
                continue
            headers = [re.sub(r"[`*]", "", cell).strip().lower() for cell in split_table_row(line)]
            try:
                entry_col = headers.index("entrada")
            except ValueError:
                break
            role_col = headers.index("papel") if "papel" in headers else None
            for row_line in lines[i + 2:]:
                if not row_line.strip().startswith("|"):
                    break
                row = split_table_row(row_line)
                if len(row) <= entry_col:
                    continue
                role = row[role_col].strip() if role_col is not None and len(row) > role_col else ""
                role = re.sub(r"[`*]", "", role).strip()
                for symbol in _clean_symbol_cell(row[entry_col]):
                    if symbol:
                        purposes[symbol] = role
            break

    code_blocks = re.findall(r"```coral(?:-[^\n]*)?\n(.*?)\n```", text, flags=re.S | re.I)
    examples: dict[str, str] = {}
    names = [str(entry.get("nome", "")) for entry in module.get("api", [])]
    for name in names:
        if not name:
            continue
        pattern = re.compile(rf"(?<![\wÀ-ÿ]){re.escape(name)}(?![\wÀ-ÿ])")
        for block in code_blocks:
            lines = block.strip().splitlines()
            usage_hits = [
                j for j, ln in enumerate(lines)
                if pattern.search(ln)
                and not ln.lstrip().startswith(("de ", "importe ", "#", "comentário:", "observação:"))
            ]
            if usage_hits:
                hit = usage_hits[0]
                # Exemplo curto: preserva contexto, mas evita transformar cada
                # entrada da referência em um segundo tutorial longo.
                if len(lines) <= 8:
                    examples[name] = block.strip()
                else:
                    start = max(0, hit - 2)
                    examples[name] = "\n".join(lines[start:start + 6]).strip()
                break
    return {"purposes": purposes, "examples": examples}


def module_auto_block(module: dict[str, Any]) -> str:
    ops = module.get("operacoes", [])
    lines = [AUTO_START, "", f"**Importação:** `{module['importacao']}`  ", f"**Categoria:** {module.get('categoria', 'geral')}  "]
    if module.get("finalidade"):
        lines += ["", module["finalidade"]]
    if module.get("advertencia"):
        lines += ["", f"> Aviso: {module['advertencia']}"]
    if ops:
        lines += ["", "### Superfície pública detectada", "", ", ".join(f"`{x}`" for x in ops)]
    else:
        lines += ["", "### Superfície pública detectada", "", "A release não expôs uma lista estática de operações neste módulo. Consulte a referência do runtime e o IntelliSense da extensão."]
    lines += ["", AUTO_END]
    return "\n".join(lines)


def sync_module_pages(modules: list[dict[str, Any]]) -> None:
    MODULOS_DIR.mkdir(parents=True, exist_ok=True)
    for module in modules:
        path = MODULOS_DIR / f"{module['nome']}.md"
        block = module_auto_block(module)
        module_for_api = dict(module)
        if path.exists():
            existing = path.read_text(encoding="utf-8")
            editorial = extract_api_editorial(existing, module)
            module_for_api["editorial_api"] = editorial["purposes"]
            module_for_api["editorial_examples"] = editorial["examples"]
        api_block = "<!-- AUTO:API -->\n\n" + render_api_markdown(module_for_api) + "\n\n<!-- /AUTO:API -->"
        if not path.exists():
            title = module["importacao"]
            manual = (
                f"# {title}\n\n"
                "## Visão geral\n\n"
                f"{module.get('finalidade') or 'Módulo público da Coral.'}\n\n"
                f"{block}\n\n"
                "## Quando usar\n\n"
                "Descreva aqui os cenários de uso e decisões de projeto que não devem ser sobrescritos pelo importador.\n\n"
                "## Referência da API\n\n"
                f"{api_block}\n"
            )
            path.write_text(manual, encoding="utf-8")
            continue
        text = path.read_text(encoding="utf-8")
        if AUTO_START in text and AUTO_END in text:
            text = re.sub(re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END), block, text, flags=re.S)
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
        if "<!-- AUTO:API -->" in text and "<!-- /AUTO:API -->" in text:
            text = re.sub(r"<!-- AUTO:API -->.*?<!-- /AUTO:API -->", api_block, text, flags=re.S)
        elif "## Referência da API" in text:
            text = text.replace("## Referência da API", "## Referência da API\n\n" + api_block, 1)
        else:
            text = text.rstrip() + "\n\n## Referência da API\n\n" + api_block + "\n"
        path.write_text(text, encoding="utf-8")


def build_navigation(modules: list[dict[str, Any]]) -> dict[str, Any]:
    nav = read_json(NAV_FILE, {})
    if not nav:
        nav = {
            "paginas": [
                {"arquivo": "introducao.md", "titulo": "Introdução", "slug": "introducao", "grupo": "Primeiros passos"},
                {"arquivo": "instalacao.md", "titulo": "Instalação", "slug": "instalacao", "grupo": "Primeiros passos"},
                {"arquivo": "primeiro_programa.md", "titulo": "Seu primeiro programa", "slug": "primeiro-programa", "grupo": "Primeiros passos"},
                {"arquivo": "projetos.md", "titulo": "Projetos e módulos", "slug": "projetos", "grupo": "Guias"},
                {"arquivo": "vscode.md", "titulo": "VS Code", "slug": "vscode", "grupo": "Guias"},
                {"arquivo": "testes.md", "titulo": "Testes", "slug": "testes", "grupo": "Guias"},
                {"arquivo": "repl_cli.md", "titulo": "REPL e CLI", "slug": "repl-cli", "grupo": "Referência"},
                {"arquivo": "exemplos.md", "titulo": "Exemplos oficiais", "slug": "exemplos", "grupo": "Referência"},
                {"arquivo": "livro.md", "titulo": "Livro Oficial", "slug": "livro", "grupo": "Referência"},
                {"arquivo": "release.md", "titulo": "Release atual", "slug": "release", "grupo": "Referência"},
            ]
        }
    regular = [p for p in nav.get("paginas", []) if not p.get("arquivo", "").startswith("modulos/")]
    primary_by_name = {m["nome"]: m for m in modules if m.get("destaque")}
    other_by_name = {m["nome"]: m for m in modules if not m.get("destaque")}
    primary_names = [name for name in PRIMARY_MODULE_ORDER if name in primary_by_name]
    primary_names += sorted(set(primary_by_name) - set(primary_names))
    module_pages = []
    for name in primary_names:
        m = primary_by_name[name]
        module_pages.append({"arquivo": f"modulos/{name}.md", "titulo": m["importacao"], "slug": f"modulo-{name}", "grupo": PRIMARY_GROUP})
    for name in sorted(other_by_name):
        m = other_by_name[name]
        module_pages.append({"arquivo": f"modulos/{name}.md", "titulo": m["importacao"], "slug": f"modulo-{name}", "grupo": OTHER_GROUP})
    nav["paginas"] = regular + module_pages
    write_json(NAV_FILE, nav)
    return nav


def render_docs(version: dict[str, Any], modules: list[dict[str, Any]]) -> None:
    nav = build_navigation(modules)
    render_docs_multipage(ROOT, version, modules, nav)


def generate_seo_files(url_base: str) -> None:
    """Gera sitemap.xml e robots.txt a partir da navegação atual."""
    base = url_base.rstrip("/")
    nav = read_json(NAV_FILE, {})
    paths = ["", "docs/"]
    for item in nav.get("paginas", []):
        paths.append("docs/" + source_to_public(item["arquivo"]))
    entries = "\n".join(
        f"  <url><loc>{html.escape(base + '/' + p)}</loc></url>"
        for p in paths
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!-- Gerado por tools/atualizar_docs.py. O domínio abaixo é um placeholder: '
        'gere novamente com --url-base=https://SEU-DOMINIO antes de publicar. -->\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "# Gerado por tools/atualizar_docs.py — ajuste o domínio via --url-base antes de publicar.\n"
        f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n",
        encoding="utf-8",
    )


def update_index_fallbacks(version: dict[str, Any]) -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    # asset paths from older starter package
    text = text.replace("assets/styles.css", "assets/css/styles.css").replace("assets/site.js", "assets/js/site.js")
    # Insere marcadores em pacotes antigos que ainda não os possuam.
    text = re.sub(r"Release estável\s+[0-9.]+", f'Release estável <span data-version-key="coral">{version.get("coral", "?")}</span>', text, count=1)
    text = re.sub(r"<strong>Runtime</strong>\s*[0-9.]+", f'<strong>Runtime</strong> <span data-version-key="coral">{version.get("coral", "?")}</span>', text, count=1)
    text = re.sub(r"<strong>VS Code</strong>\s*[0-9.]+", f'<strong>VS Code</strong> <span data-version-key="extensao_vscode">{version.get("extensao_vscode", "?")}</span>', text, count=1)
    text = re.sub(r"<strong>Livro Oficial</strong>\s*[0-9.]+", f'<strong>Livro Oficial</strong> <span data-version-key="livro">{version.get("livro", "?")}</span>', text, count=1)
    text = re.sub(r"Livro Oficial\s+[0-9.]+", f'Livro Oficial <span data-version-key="livro">{version.get("livro", "?")}</span>', text, count=1)
    text = re.sub(r"Coral Language\s+[0-9.]+\s+reúne", f'Coral Language <span data-version-key="extensao_vscode">{version.get("extensao_vscode", "?")}</span> reúne', text, count=1)
    text = re.sub(r'<span class="kicker">Coral\s+[0-9.]+</span>', f'<span class="kicker">Coral <span data-version-key="coral">{version.get("coral", "?")}</span></span>', text, count=1)
    text = re.sub(r"Na\s+[0-9.]+, o foco", f'Na <span data-version-key="coral">{version.get("coral", "?")}</span>, o foco', text, count=1)
    text = re.sub(r"Princípio da\s+[0-9.]+", f'Princípio da <span data-version-key="coral">{version.get("coral", "?")}</span>', text, count=1)
    text = re.sub(r"coral-\d+\.\d+\.\d+\.pyz", f'coral-{version.get("coral", "?")}.pyz', text)
    text = re.sub(r">Release\s+[0-9.]+<", f'>Release <span data-version-key="coral">{version.get("coral", "?")}</span><', text, count=1)

    # Atualiza também o fallback já marcado. Assim o HTML continua correto sem
    # JavaScript e o gerador permanece idempotente em releases sucessivas.
    for key, value in (
        ("coral", version.get("coral", "?")),
        ("extensao_vscode", version.get("extensao_vscode", "?")),
        ("livro", version.get("livro", "?")),
    ):
        text = re.sub(
            rf'(<span data-version-key="{re.escape(key)}">)[^<]*(</span>)',
            rf'\g<1>{value}\g<2>',
            text,
        )

    # Evita marcadores aninhados em pacotes muito antigos.
    text = re.sub(r'<span data-version-key="coral"><span data-version-key="coral">([^<]+)</span></span>', r'<span data-version-key="coral">\1</span>', text)
    path.write_text(text, encoding="utf-8")

def ensure_base_pages() -> None:
    pages = {
        "introducao.md": '''# Introdução\n\nCoral é uma linguagem com sintaxe corrente em português. A intenção é manter o programa legível sem transformar a linguagem em simples substituição textual: parser, AST, tipos, módulos e ferramentas continuam sendo partes reais da implementação.\n\n> Comece pequeno. Um único arquivo `.coral` funciona sem projeto. Quando precisar de módulos, testes e configuração, use `coral.toml`.\n''',
        "instalacao.md": '''# Instalação\n\nA distribuição oficial inclui runtime portátil, assistentes de instalação e a extensão Coral Language.\n\n## Linux\n\n```bash\nbash Instalacao/Coral_Setup.sh\npython Instalacao/Runtime/coral-<versao>.pyz --versao\n```\n\n## Windows\n\n```text\nInstalacao\\Coral_Setup.cmd\npython Instalacao\\Runtime\\coral-<versao>.pyz --versao\n```\n\nOs números de versão mostrados nesta página são atualizados pelo importador de releases.\n''',
        "primeiro_programa.md": '''# Seu primeiro programa\n\n```coral\nmostre "Olá, Coral!"\n\ndefina pontos como 10\nadicione 5 a pontos\n\nse pontos for maior ou igual a 15 então\n    mostre "Meta alcançada"\nsenão\n    mostre "Continue tentando"\nfim\n```\n\nPara executar diretamente, use o runtime portátil da release corrente.\n''',
        "projetos.md": '''# Projetos e módulos\n\nProjetos Coral usam `coral.toml` para declarar entrada, caminhos de módulos, testes e recursos. O LSP e o Project Explorer usam a mesma estrutura de projeto.\n\n## Formas naturais importadas\n\nFunções públicas podem declarar formas naturais. Quando importadas seletivamente, essas formas são reconhecidas pelo runtime e pelo editor.\n\n```coral\ncrie a função dobro com numero chamada como "dobre {numero}"\n    retorne numero vezes 2\nfim\n\nmostre dobre 21\n```\n''',
        "vscode.md": '''# VS Code\n\nA extensão Coral Language acompanha a linguagem com LSP, DAP/F5, IntelliSense contextual, diagnósticos, semantic tokens, Test Explorer, Project Explorer, Ambiente Coral e Biblioteca Coral.\n\n| Área | Comportamento |\n|---|---|\n| IntelliSense | Completion contextual, hover, definição, referências e rename |\n| Coloração | TextMate como fallback e semantic tokens como camada contextual |\n| Execução | Arquivo, projeto, REPL e debug integrados |\n| Projetos | `coral.toml`, multiroot e Project Explorer |\n| Testes | Integração com o runner e Test Explorer |\n''',
        "testes.md": '''# Testes\n\nA Coral separa o ciclo rápido das verificações lentas e históricas. Isso evita que a suíte cotidiana cresça indefinidamente e mantém os gates pesados no congelamento da release.\n\n> Testes que dependem de janela, áudio, entrada física ou ambiente gráfico ficam nas rotas de teste real da distribuição.\n''',
        "repl_cli.md": '''# REPL e CLI\n\nA lista abaixo é importada automaticamente do contrato gerado da release. O arquivo `docs/dados/cli.json` é a fonte mecânica desta seção.\n\n## Uso cotidiano\n\n```bash\npython coral-<versao>.pyz --repl\npython coral-<versao>.pyz --self-check\npython coral-<versao>.pyz --ambiente\n```\n''',
        "exemplos.md": '''# Exemplos oficiais\n\nA biblioteca de exemplos é organizada por assunto. Exemplos muito curtos ou redundantes são condensados e fixtures de aceitação ficam separadas dos exemplos pedagógicos.\n\nO inventário mecânico de arquivos `.coral` da release fica em `docs/dados/exemplos.json`.\n''',
        "livro.md": '''# Livro Oficial\n\nA edição do Livro é controlada separadamente da versão técnica do runtime. Os exemplos citados pelo Livro também são sincronizados na própria área do Livro sem substituir os caminhos canônicos da biblioteca geral.\n''',
        "release.md": '''# Release atual\n\nO changelog oficial importado da release fica em `docs/changelog/`. Quando uma nova release é importada, o gerador cria o arquivo correspondente e apresenta as diferenças mecânicas encontradas.\n''',
    }
    PAGINAS.mkdir(parents=True, exist_ok=True)
    for name, content in pages.items():
        path = PAGINAS / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")


def replace_auto_block(path: Path, name: str, body: str) -> None:
    start = f"<!-- AUTO:{name} -->"
    end = f"<!-- /AUTO:{name} -->"
    block = start + "\n\n" + body.strip() + "\n\n" + end
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if start in text and end in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")


def sync_mechanical_pages(version: dict[str, Any], cli: dict[str, Any], examples_data: dict[str, Any]) -> None:
    runtime = str(version.get("coral", "?"))
    ext = str(version.get("extensao_vscode", "?"))
    livro = str(version.get("livro", "?"))

    # Referências editoriais que apontam para o artefato corrente devem seguir
    # a fonte única de versão, sem exigir manutenção manual a cada release.
    for name in ("instalacao.md", "primeiro_programa.md", "repl_cli.md"):
        path = PAGINAS / name
        if not path.exists():
            continue
        page = path.read_text(encoding="utf-8")
        page = re.sub(
            r"coral-(?:\d+\.\d+\.\d+|<versao>)\.pyz",
            f"coral-{runtime}.pyz",
            page,
        )
        if name == "instalacao.md":
            page = re.sub(
                r"coral-language-(?:\d+\.\d+\.\d+|<versao>)\.vsix",
                f"coral-language-{ext}.vsix",
                page,
            )
        path.write_text(page, encoding="utf-8")

    # Frases editoriais padronizadas que descrevem a release corrente também
    # acompanham o runtime importado. Changelogs históricos ficam intocados.
    for path in sorted(MODULOS_DIR.glob("*.md")):
        page = path.read_text(encoding="utf-8")
        page = re.sub(
            r"(A documentação desta página descreve a superfície detectada na \*\*Coral )\d+\.\d+\.\d+(\*\*\.)",
            rf"\g<1>{runtime}\g<2>",
            page,
        )
        page = re.sub(
            r"(O exemplo abaixo foi validado com o runtime )\d+\.\d+\.\d+(:)",
            rf"\g<1>{runtime}\g<2>",
            page,
        )
        page = re.sub(
            r"(A release )\d+\.\d+\.\d+( usa `coral\.)",
            rf"\g<1>{runtime}\g<2>",
            page,
        )
        page = re.sub(
            r"(Na )\d+\.\d+\.\d+( a superfície pública é)",
            rf"\g<1>{runtime}\g<2>",
            page,
        )
        path.write_text(page, encoding="utf-8")

    vscode = PAGINAS / "vscode.md"
    if vscode.exists():
        replace_auto_block(vscode, "VERSAO", f"**Extensão corrente:** Coral Language `{ext}` para Coral `{runtime}`.")

    livro_page = PAGINAS / "livro.md"
    if livro_page.exists():
        replace_auto_block(livro_page, "EDICAO", f"**Edição editorial corrente:** `{livro}`.  \n**Runtime corrente:** `{runtime}`.")

    cli_lines = ["### Opções detectadas", "", ", ".join(f"`{x}`" for x in cli.get("opcoes", [])) or "Nenhuma opção detectada.", "", "### Subcomandos detectados", "", ", ".join(f"`{x}`" for x in cli.get("subcomandos", [])) or "Nenhum subcomando detectado."]
    replace_auto_block(PAGINAS / "repl_cli.md", "CLI", "\n".join(cli_lines))

    files = list(examples_data.get("arquivos", []))
    groups: dict[str, int] = {}
    for f in files:
        parts = f.split("/")
        group = parts[1] if len(parts) > 2 else "Raiz"
        groups[group] = groups.get(group, 0) + 1
    example_lines = [f"**Total detectado na release:** {len(files)} arquivos `.coral`.", "", "| Área | Arquivos |", "|---|---:|"]
    example_lines += [f"| {name} | {count} |" for name, count in sorted(groups.items())]
    replace_auto_block(PAGINAS / "exemplos.md", "EXEMPLOS", "\n".join(example_lines))

    changelog_path = CHANGELOG_DIR / f"{runtime}.md"
    if changelog_path.exists():
        change = changelog_path.read_text(encoding="utf-8").strip()
        # O título da release vira subtítulo dentro da página geral.
        change = re.sub(r"^#\s+", "## ", change, count=1)
        replace_auto_block(PAGINAS / "release.md", "CHANGELOG", change)

def write_review_report(diff: dict[str, Any]) -> None:
    path = DOCS / "REVISAO_PENDENTE.md"
    lines = [
        "# Revisão pendente da documentação",
        "",
        "Arquivo gerado automaticamente ao importar uma release. Use como checklist e mantenha o conteúdo pedagógico sob revisão humana.",
        "",
        f"Versão anterior: **{diff.get('versao_anterior') or 'sem snapshot'}**  ",
        f"Versão nova: **{diff.get('versao_nova')}**",
        "",
    ]
    labels = [
        ("Módulos novos", "modulos_novos"),
        ("Módulos removidos", "modulos_removidos"),
        ("Módulos com superfície alterada", "modulos_alterados"),
        ("Entradas novas de CLI", "cli_novo"),
        ("Entradas removidas de CLI", "cli_removido"),
        ("Exemplos novos", "exemplos_novos"),
        ("Exemplos removidos", "exemplos_removidos"),
    ]
    for label, key in labels:
        values = diff.get(key, [])
        lines += [f"## {label} ({len(values)})", ""]
        lines += [f"* `{x}`" for x in values] if values else ["Nenhuma alteração detectada."]
        lines.append("")
    lines += [
        "## Contrato sintático",
        "",
        "Alterado em relação ao snapshot anterior." if diff.get("sintaxe_alterada") else "Sem alteração detectada.",
        "",
        "## Checklist humano",
        "",
        "* [ ] Revisar páginas pedagógicas dos módulos novos ou alterados.",
        "* [ ] Confirmar que exemplos novos que merecem destaque aparecem no texto.",
        "* [ ] Revisar referências a itens removidos.",
        "* [ ] Abrir `index.html`, `docs/index.html` e páginas de amostra via servidor local.",
        "* [ ] Testar tema claro, escuro, busca, menu mobile e navegação por teclado.",
        "* [ ] Só depois fazer commit e push.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def import_and_update(zip_path: Path) -> dict[str, Any]:
    info = import_release(zip_path)
    new_snapshot = release_snapshot(info)
    old_snapshot = read_json(SNAPSHOT, {})
    diff = diff_release(old_snapshot, new_snapshot) if old_snapshot else {
        "versao_anterior": None, "versao_nova": info.runtime,
        "modulos_novos": [m["nome"] for m in info.modulos], "modulos_removidos": [], "modulos_alterados": [],
        "cli_novo": info.cli.get("opcoes", []) + info.cli.get("subcomandos", []), "cli_removido": [],
        "exemplos_novos": info.exemplos, "exemplos_removidos": [], "sintaxe_alterada": True,
    }

    version = {
        "coral": info.runtime,
        "extensao_vscode": info.extensao_vscode,
        "livro": info.livro,
        "estavel": True,
        "fonte_release": zip_path.name,
    }
    write_json(VERSION_FILE, version)
    write_json(MODULES_FILE, info.modulos)
    write_json(CLI_FILE, info.cli)
    write_json(EXAMPLES_FILE, {"total": len(info.exemplos), "arquivos": info.exemplos})
    write_json(SINTAXE_FILE, info.sintaxe)
    write_json(SNAPSHOT, new_snapshot)
    sync_module_pages(info.modulos)
    if info.changelog:
        CHANGELOG_DIR.mkdir(parents=True, exist_ok=True)
        (CHANGELOG_DIR / f"{info.runtime}.md").write_text(info.changelog, encoding="utf-8")
    write_review_report(diff)
    return diff


def print_diff(diff: dict[str, Any]) -> None:
    print("\nResumo da atualização")
    print("=" * 58)
    print(f"Versão: {diff.get('versao_anterior') or 'sem snapshot'} -> {diff.get('versao_nova')}")
    for label, key in [
        ("Módulos novos", "modulos_novos"),
        ("Módulos removidos", "modulos_removidos"),
        ("Módulos alterados", "modulos_alterados"),
        ("CLI nova", "cli_novo"),
        ("CLI removida", "cli_removido"),
        ("Exemplos novos", "exemplos_novos"),
        ("Exemplos removidos", "exemplos_removidos"),
    ]:
        values = diff.get(key, [])
        print(f"{label}: {len(values)}")
        for item in values[:12]:
            print(f"  • {item}")
        if len(values) > 12:
            print(f"  • ... e mais {len(values)-12}")
    print(f"Sintaxe alterada: {'sim' if diff.get('sintaxe_alterada') else 'não'}")
    print("\nRevisão manual recomendada:")
    if diff.get("modulos_novos"):
        print("  • Completar os guias pedagógicos dos módulos novos.")
    if diff.get("modulos_removidos") or diff.get("cli_removido"):
        print("  • Revisar links e texto que mencionem itens removidos.")
    if diff.get("exemplos_novos"):
        print("  • Escolher quais exemplos novos merecem destaque editorial.")
    print("  • Abrir o site localmente e revisar a navegação antes do git push.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Atualiza e regenera a documentação do site da Coral.")
    parser.add_argument("release", nargs="?", type=Path, help="ZIP oficial da nova release Coral")
    parser.add_argument("--somente-gerar", action="store_true", help="Não importa release; só regenera docs.html a partir dos dados e Markdown atuais")
    parser.add_argument("--url-base", default=SITE_URL_PADRAO, help="URL base do site usada no sitemap.xml e robots.txt (use o domínio real antes de publicar)")
    args = parser.parse_args()

    ensure_base_pages()
    diff = None
    if args.release and not args.somente_gerar:
        if not args.release.is_file():
            parser.error(f"release não encontrada: {args.release}")
        diff = import_and_update(args.release)

    version = read_json(VERSION_FILE, {"coral": "?", "extensao_vscode": "?", "livro": "?", "estavel": False})
    modules = read_json(MODULES_FILE, [])
    cli = read_json(CLI_FILE, {"opcoes": [], "subcomandos": []})
    examples_data = read_json(EXAMPLES_FILE, {"total": 0, "arquivos": []})
    sync_mechanical_pages(version, cli, examples_data)
    build_navigation(modules)
    render_docs(version, modules)
    update_index_fallbacks(version)
    generate_seo_files(args.url_base)

    print(f"Documentação regenerada: {ROOT / 'docs/index.html'}")
    print(f"Versão corrente: Coral {version.get('coral')} | VS Code {version.get('extensao_vscode')} | Livro {version.get('livro')}")
    if diff is not None:
        print_diff(diff)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
