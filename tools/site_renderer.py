from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

from syntax_highlight import CoralSyntax, carregar_sintaxe_coral, eh_bloco_coral, highlight_coral

PRIMARY_MODULE_ORDER = [
    "numerico", "sistema", "laboratorio", "hardware",
    "mundo", "regras", "rpg", "jogos",
]
PRIMARY_GROUP = "Módulos principais"
OTHER_GROUP = "Outros módulos"

# Rótulos textuais de callout exigidos pela identidade visual (§11).
CALLOUT_VARIANTS = {
    "nota": "nota",
    "aviso": "aviso",
    "dica": "dica",
    "atenção": "aviso",
    "atencao": "aviso",
}
OUTPUT_LANGS = {"saida", "saída", "output", "terminal", "resultado"}


def slugify(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-zA-Z0-9]+", "-", norm).strip("-").lower() or "secao"


def inline_markup(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def split_table_row(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|") and not text.endswith(r"\|"):
        text = text[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for ch in text:
        if escaped:
            if ch == "|":
                current.append("|")
            else:
                current.append("\\")
                current.append(ch)
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def markdown_to_html(md: str, syntax: CoralSyntax | None = None) -> tuple[str, list[dict[str, Any]]]:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    toc: list[dict[str, Any]] = []
    i = 0
    list_type: str | None = None
    first_h1_skipped = False
    used_ids: dict[str, int] = {}

    def unique_id(title: str) -> str:
        base = slugify(title)
        count = used_ids.get(base, 0) + 1
        used_ids[base] = count
        return base if count == 1 else f"{base}-{count}"

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("<!--"):
            i += 1
            continue

        if stripped.startswith(":::resultado"):
            close_list()
            title = stripped[len(":::resultado"):].strip() or "Resultado esperado"
            i += 1
            inner: list[str] = []
            while i < len(lines) and lines[i].strip() != ":::":
                inner.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            inner_html, _ = markdown_to_html("\n".join(inner), syntax)
            out.append(
                '<details class="expected-result">'
                f'<summary>{html.escape(title)}</summary>'
                f'<div class="expected-result-body">{inner_html}</div>'
                '</details>'
            )
            continue

        if stripped.startswith(":::aprender") or stripped.startswith(":::referencia"):
            close_list()
            learn = stripped.startswith(":::aprender")
            label = "docs-mode-learn-only" if learn else "docs-mode-reference-only"
            i += 1
            inner: list[str] = []
            while i < len(lines) and lines[i].strip() != ":::":
                inner.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            inner_html, _ = markdown_to_html("\n".join(inner), syntax)
            out.append(f'<div class="{label}">{inner_html}</div>')
            continue

        if stripped.startswith(":::details"):
            close_list()
            title = stripped[len(":::details"):].strip() or "Detalhes"
            i += 1
            inner: list[str] = []
            while i < len(lines) and lines[i].strip() != ":::":
                inner.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            inner_html, _ = markdown_to_html("\n".join(inner), syntax)
            out.append(
                '<details class="api-tech-details">'
                f'<summary>{html.escape(title)}</summary>'
                f'<div class="api-tech-body">{inner_html}</div>'
                '</details>'
            )
            continue

        if stripped.startswith("```"):
            close_list()
            lang = stripped[3:].strip()
            i += 1
            code_lines: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            raw_code = "\n".join(code_lines)
            code = highlight_coral(raw_code, syntax) if syntax is not None and eh_bloco_coral(lang) else html.escape(raw_code)
            if lang.lower() in OUTPUT_LANGS:
                out.append('<div class="output-block"><div class="output-label">Saída</div>'
                           f'<div class="output-body">{code}</div></div>')
                continue
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append('<div class="code-card"><div class="code-frame"><div class="ring-stripe" aria-hidden="true"></div>'
                       f'<pre><code{cls}>{code}</code></pre></div></div>')
            continue

        if not stripped:
            close_list()
            i += 1
            continue

        if line.startswith("# "):
            close_list()
            if first_h1_skipped:
                title = line[2:].strip()
                ident = unique_id(title)
                out.append(f'<h2 id="{ident}" data-searchable>{inline_markup(title)}</h2>')
                toc.append({"level": 2, "id": ident, "title": title})
            first_h1_skipped = True
            i += 1
            continue

        heading_match = re.match(r"^(##|###|####)\s+(.+?)\s*$", line)
        if heading_match:
            close_list()
            marks, title = heading_match.groups()
            level = len(marks)
            # Remove a markdown code wrapper only for slug generation.
            plain_title = re.sub(r"`([^`]+)`", r"\1", title)
            ident = unique_id(plain_title)
            out.append(f'<h{level} id="{ident}" data-searchable>{inline_markup(title)}</h{level}>')
            if level in (2, 3):
                toc.append({"level": level, "id": ident, "title": plain_title})
            i += 1
            continue

        if stripped.startswith("> "):
            close_list()
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            body = " ".join(quote_lines)
            variant = None
            label = ""
            lowered = body.lower()
            for prefix, name in CALLOUT_VARIANTS.items():
                if lowered.startswith(prefix + ":"):
                    variant = name
                    label = body[: len(prefix)].capitalize()
                    body = body[len(prefix) + 1 :].strip()
                    break
            if variant:
                out.append(f'<div class="callout variant-{variant}"><div class="ring-stripe" aria-hidden="true"></div>'
                           f'<div class="callout-body"><span class="callout-label">{html.escape(label)}</span>'
                           f'<p class="callout-text" data-searchable>{inline_markup(body)}</p></div></div>')
            else:
                out.append('<div class="callout"><div class="ring-stripe" aria-hidden="true"></div>'
                           f'<div class="callout-body"><p data-searchable>{inline_markup(body)}</p></div></div>')
            continue

        if re.match(r"^[-*]\s+", line):
            if list_type != "ul":
                close_list(); list_type = "ul"; out.append("<ul>")
            content = re.sub(r"^[-*]\s+", "", line)
            out.append(f'<li data-searchable>{inline_markup(content)}</li>')
            i += 1
            continue

        if re.match(r"^\d+\.\s+", line):
            if list_type != "ol":
                close_list(); list_type = "ol"; out.append("<ol>")
            content = re.sub(r"^\d+\.\s+", "", line)
            out.append(f'<li data-searchable>{inline_markup(content)}</li>')
            i += 1
            continue

        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[i + 1]):
            close_list()
            headers = split_table_row(line)
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip() and "|" in lines[i]:
                rows.append(split_table_row(lines[i]))
                i += 1
            parts = ['<div class="table-wrap"><table><thead><tr>']
            parts.extend(f"<th>{inline_markup(cell)}</th>" for cell in headers)
            parts.append("</tr></thead><tbody>")
            for row in rows:
                if len(row) < len(headers):
                    row += [""] * (len(headers) - len(row))
                parts.append("<tr>" + "".join(f'<td data-searchable>{inline_markup(cell)}</td>' for cell in row[:len(headers)]) + "</tr>")
            parts.append("</tbody></table></div>")
            out.extend(parts)
            continue

        # Plain paragraph: merge adjacent ordinary lines.
        close_list()
        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            s = nxt.strip()
            if not s or s.startswith(("#", "> ", "```", "<!--")) or re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+\.\s+", nxt):
                break
            if "|" in nxt and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[i + 1]):
                break
            paragraph.append(s)
            i += 1
        out.append(f'<p data-searchable>{inline_markup(" ".join(paragraph))}</p>')

    close_list()
    return "\n".join(out), toc


def page_title(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def page_description(md: str, fallback: str) -> str:
    in_auto = False
    for raw in md.splitlines():
        line = raw.strip()
        if line.startswith("<!-- AUTO:"):
            in_auto = True
            continue
        if line.startswith("<!-- /AUTO:"):
            in_auto = False
            continue
        if in_auto or not line or line.startswith(("#", "```", "|", "<!--")):
            continue
        if line.startswith(("* ", "- ", "> ")):
            continue
        text = re.sub(r"`([^`]+)`", r"\1", line)
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
        return text[:260]
    return fallback


def source_to_public(arquivo: str) -> str:
    p = Path(arquivo)
    if p.name == "introducao.md":
        return "index.html"
    return str(p.with_suffix(".html")).replace("\\", "/")


def _plain_text(line: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", line)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    return text.strip()


def extract_search_sections(md: str, max_chars: int = 6000) -> list[dict[str, Any]]:
    """Extrai seções (h2/h3) com texto plano para o índice de busca global.

    O conteúdo antes do primeiro h2 vira uma seção de introdução sem âncora;
    blocos de código são mantidos (nomes de funções são pesquisáveis), apenas
    com as cercas removidas.
    """
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] = {"id": "", "titulo": "", "lines": []}
    in_code = False
    for line in md.replace("\r\n", "\n").split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        heading = re.match(r"^(#{2,3})\s+(.+?)\s*$", stripped)
        if heading and not in_code:
            if current["lines"] or current["titulo"]:
                sections.append(current)
            titulo = _plain_text(heading.group(2))
            current = {"id": slugify(titulo), "titulo": titulo, "lines": []}
            continue
        if stripped.startswith("# ") or stripped.startswith("<!--"):
            continue
        if stripped.startswith("> "):
            current["lines"].append(_plain_text(stripped[2:]))
            continue
        current["lines"].append(_plain_text(line))
    if current["lines"] or current["titulo"]:
        sections.append(current)
    out: list[dict[str, Any]] = []
    for sec in sections:
        text = re.sub(r"\s+", " ", " ".join(l for l in sec["lines"] if l)).strip()
        if not text and not sec["titulo"]:
            continue
        out.append({"id": sec["id"], "titulo": sec["titulo"], "texto": text[:max_chars]})
    return out


def href_between(current_public: str, target_public: str) -> str:
    current_dir = Path(current_public).parent
    # pathlib relpath without importing os manually inside call sites.
    import os
    rel = os.path.relpath(Path(target_public), current_dir if str(current_dir) != "." else Path("."))
    return rel.replace("\\", "/")


def _module_sort_key(item: dict[str, Any], module_meta: dict[str, dict[str, Any]]) -> tuple[int, str]:
    name = Path(item["arquivo"]).stem
    meta = module_meta.get(name, {})
    if meta.get("destaque"):
        try:
            return (PRIMARY_MODULE_ORDER.index(name), name)
        except ValueError:
            return (len(PRIMARY_MODULE_ORDER), name)
    return (999, name)


def build_sidebar(nav: dict[str, Any], modules: list[dict[str, Any]], current_item: dict[str, Any], current_public: str) -> str:
    module_meta = {m["nome"]: m for m in modules}
    regular_groups: dict[str, list[dict[str, Any]]] = {}
    primary: list[dict[str, Any]] = []
    others: list[dict[str, Any]] = []

    for item in nav.get("paginas", []):
        arquivo = item.get("arquivo", "")
        if arquivo.startswith("modulos/"):
            name = Path(arquivo).stem
            (primary if module_meta.get(name, {}).get("destaque") else others).append(item)
        else:
            regular_groups.setdefault(item.get("grupo", "Documentação"), []).append(item)

    primary.sort(key=lambda x: _module_sort_key(x, module_meta))
    others.sort(key=lambda x: x.get("titulo", ""))

    out: list[str] = []
    for group, items in regular_groups.items():
        out.append(f"<h4>{html.escape(group)}</h4><ul>")
        for item in items:
            target = source_to_public(item["arquivo"])
            href = href_between(current_public, target)
            active = item["arquivo"] == current_item["arquivo"]
            attrs = ' class="active" aria-current="page"' if active else ""
            out.append(f'<li><a{attrs} href="{html.escape(href)}">{html.escape(item["titulo"])}</a></li>')
        out.append("</ul>")

    current_file = current_item.get("arquivo", "")
    current_name = Path(current_file).stem if current_file.startswith("modulos/") else None
    current_is_primary = bool(current_name and module_meta.get(current_name, {}).get("destaque"))
    current_is_other = bool(current_name and not current_is_primary)

    def details(title: str, items: list[dict[str, Any]], open_it: bool, css: str) -> None:
        open_attr = " open" if open_it else ""
        out.append(f'<details class="docs-nav-group {css}"{open_attr}><summary>{html.escape(title)}</summary><ul>')
        for item in items:
            target = source_to_public(item["arquivo"])
            href = href_between(current_public, target)
            active = item["arquivo"] == current_file
            attrs = ' class="active" aria-current="page"' if active else ""
            label = html.escape(item["titulo"])
            out.append(f'<li><a{attrs} href="{html.escape(href)}"><code>{label}</code></a></li>')
        out.append("</ul></details>")

    details(PRIMARY_GROUP, primary, (not current_is_other), "docs-nav-primary")
    details(OTHER_GROUP, others, current_is_other, "docs-nav-secondary")
    return "\n".join(out)


def build_toc(toc: list[dict[str, Any]]) -> str:
    if not toc:
        return '<li class="toc-empty">Esta página não possui subseções.</li>'
    return "\n".join(
        f'<li class="toc-level-{item["level"]}"><a href="#{html.escape(item["id"])}" data-toc-link>{html.escape(item["title"])}</a></li>'
        for item in toc
    )


def build_prev_next(items: list[dict[str, Any]], current_index: int, current_public: str) -> str:
    links = []
    if current_index > 0:
        prev = items[current_index - 1]
        href = href_between(current_public, source_to_public(prev["arquivo"]))
        links.append(f'<a class="docs-page-nav-link" href="{html.escape(href)}"><span>Anterior</span><strong>{html.escape(prev["titulo"])}</strong></a>')
    else:
        links.append("<span></span>")
    if current_index + 1 < len(items):
        nxt = items[current_index + 1]
        href = href_between(current_public, source_to_public(nxt["arquivo"]))
        links.append(f'<a class="docs-page-nav-link next" href="{html.escape(href)}"><span>Próxima</span><strong>{html.escape(nxt["titulo"])}</strong></a>')
    else:
        links.append("<span></span>")
    return '<nav class="docs-page-nav" aria-label="Páginas relacionadas">' + "".join(links) + "</nav>"


def _section_text(md: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(md)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s+", md[start:], re.MULTILINE)
    end = start + nxt.start() if nxt else len(md)
    return md[start:end].strip()


def _first_plain_paragraph(section: str) -> str:
    lines = section.splitlines()
    paragraph: list[str] = []
    in_code = False
    for raw in lines:
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            if paragraph:
                break
            continue
        if in_code or not stripped or stripped.startswith(("#", "<!--", "|", ":::", "- ", "* ")):
            if paragraph:
                break
            continue
        paragraph.append(stripped)
    return " ".join(paragraph).strip()


def _not_use_text(section: str) -> str:
    text = re.sub(r"\s+", " ", section)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    candidates = re.split(r"(?<=[.!?])\s+", text)
    for sentence in candidates:
        clean = sentence.strip()
        low = clean.lower()
        if (
            low.startswith(("evite ", "não use ", "nao use ", "se você só ", "se voce so "))
            or " prefira " in low
            or " pode operar sem " in low
            or " podem operar sem " in low
        ):
            return clean
    return ""


def _first_coral_example(md: str) -> str:
    preferred = _section_text(md, "Começando") or _section_text(md, "Começando sem janela") or md
    match = re.search(r"```coral\s*\n(.*?)\n```", preferred, re.DOTALL | re.IGNORECASE)
    if not match and preferred is not md:
        match = re.search(r"```coral\s*\n(.*?)\n```", md, re.DOTALL | re.IGNORECASE)
    if not match:
        return ""
    code = match.group(1).strip()
    lines = code.splitlines()
    if len(lines) > 12:
        code = "\n".join(lines[:12]).rstrip() + "\n# …"
    return code


def build_module_quick_summary(
    md: str,
    meta: dict[str, Any],
    module_name: str,
    all_modules: list[dict[str, Any]],
    current_public: str,
    syntax: CoralSyntax,
) -> str:
    finalidade = str(meta.get("finalidade") or f"recursos públicos de coral.{module_name}").strip()
    when_section = _section_text(md, "Quando usar")
    when_paragraph = _first_plain_paragraph(when_section)
    when_parts = re.split(r"(?<=[.!?])\s+", when_paragraph, maxsplit=1) if when_paragraph else []
    when = when_parts[0] if when_parts else ""
    not_use = _not_use_text(when_section)
    if not not_use:
        ecosystem = _section_text(md, "Papel no ecossistema")
        not_use = _not_use_text(ecosystem)
    if not not_use:
        not_use = "Quando a necessidade for mais específica e outro módulo do ecossistema expressar melhor a intenção do programa."

    module_names = {m.get("nome") for m in all_modules}
    mentioned = []
    for name in re.findall(r"`?coral\.([a-z_]+)`?", md):
        if name != module_name and name in module_names and name not in mentioned:
            mentioned.append(name)
        if len(mentioned) >= 5:
            break
    related = []
    for name in mentioned:
        target = f"modulos/{name}.html"
        href = href_between(current_public, target)
        related.append(f'<a href="{html.escape(href)}"><code>coral.{html.escape(name)}</code></a>')
    related_html = ", ".join(related) if related else "Consulte a navegação lateral para módulos relacionados."

    example = _first_coral_example(md)
    if example:
        rendered = highlight_coral(example, syntax)
        example_html = (
            '<div class="quick-summary-example">'
            '<div class="quick-summary-label">Exemplo mínimo</div>'
            '<div class="code-card"><div class="code-frame"><div class="ring-stripe" aria-hidden="true"></div>'
            f'<pre><code class="language-coral">{rendered}</code></pre></div></div>'
            '</div>'
        )
    else:
        example_html = '<p class="quick-summary-empty">Este módulo não possui um exemplo mínimo curto na documentação atual.</p>'

    return (
        '<section class="module-quick-summary" aria-labelledby="resumo-rapido-modulo">'
        '<div class="module-quick-summary-head">'
        '<span class="module-quick-summary-kicker">Resumo rápido</span>'
        '<h2 id="resumo-rapido-modulo">Antes de mergulhar</h2>'
        '</div>'
        '<div class="module-quick-grid">'
        '<div class="module-quick-item"><strong>Serve para</strong>'
        f'<p>{inline_markup(finalidade.rstrip("."))}.</p></div>'
        '<div class="module-quick-item"><strong>Use quando</strong>'
        f'<p>{inline_markup(when or finalidade)}</p></div>'
        '<div class="module-quick-item"><strong>Talvez você não precise dele quando</strong>'
        f'<p>{inline_markup(not_use)}</p></div>'
        '<div class="module-quick-item"><strong>Relaciona se com</strong>'
        f'<p>{related_html}</p></div>'
        '</div>'
        f'{example_html}'
        '</section>'
    )


def render_docs(root: Path, version: dict[str, Any], modules: list[dict[str, Any]], nav: dict[str, Any]) -> list[Path]:
    docs_source = root / "docs" / "paginas"
    docs_public = root / "docs"
    template = (root / "templates" / "docs.html").read_text(encoding="utf-8")
    module_meta = {m["nome"]: m for m in modules}
    syntax_path = root / "docs" / "dados" / "sintaxe.json"
    if not syntax_path.exists():
        raise RuntimeError(f"contrato de realce ausente: {syntax_path}")
    syntax = carregar_sintaxe_coral(syntax_path)

    items = [p for p in nav.get("paginas", []) if (docs_source / p["arquivo"]).exists()]
    outputs: list[Path] = []
    search_entries: list[dict[str, Any]] = []

    for idx, item in enumerate(items):
        source = docs_source / item["arquivo"]
        md = source.read_text(encoding="utf-8")
        title = page_title(md, item.get("titulo", "Documentação"))
        body, toc = markdown_to_html(md, syntax)
        public_rel = source_to_public(item["arquivo"])
        output = docs_public / public_rel
        output.parent.mkdir(parents=True, exist_ok=True)

        # Entrada do índice de busca global (grupo/descrição calculados abaixo).
        search_entries.append({
            "titulo": title,
            "apelido": item.get("titulo", "") if item.get("titulo", "") and item.get("titulo", "") != title else "",
            "url": public_rel,
            "ordem": idx,
            "secoes": extract_search_sections(md),
        })

        is_module = item["arquivo"].startswith("modulos/")
        module_name = Path(item["arquivo"]).stem if is_module else ""
        meta = module_meta.get(module_name, {})
        group = PRIMARY_GROUP if meta.get("destaque") else OTHER_GROUP if is_module else item.get("grupo", "Documentação")
        fallback_desc = str(meta.get("finalidade") or f"Referência de {title} na Coral.")
        description = page_description(md, fallback_desc)
        search_entries[-1]["grupo"] = group
        search_entries[-1]["descricao"] = description

        depth = len(Path(public_rel).parent.parts)
        site_root = "../" * (depth + 1)  # docs root is one level below site root
        # public_rel lives relative to docs/. index.html => ../ ; modulos/x.html => ../../
        if public_rel == "index.html":
            site_root = "../"
        elif public_rel.startswith("modulos/"):
            site_root = "../../"
        else:
            site_root = "../"

        sidebar = build_sidebar(nav, modules, item, public_rel)
        docs_home = href_between(public_rel, "index.html")
        home_href = site_root + "index.html"
        toc_visible = [entry for entry in toc if entry["level"] == 2] if is_module else toc
        quick_summary = build_module_quick_summary(md, meta, module_name, modules, public_rel, syntax) if is_module else ""
        out = template
        replacements = {
            "{{SITE_ROOT}}": site_root,
            "{{PAGE_DESCRIPTION}}": html.escape(description, quote=True),
            "{{PAGE_TITLE}}": html.escape(title),
            "{{HOME_HREF}}": html.escape(home_href),
            "{{DOCS_HOME_HREF}}": html.escape(docs_home),
            "{{RUNTIME_VERSION}}": html.escape(str(version.get("coral", "?"))),
            "{{EXTENSION_VERSION}}": html.escape(str(version.get("extensao_vscode", "?"))),
            "{{BOOK_EDITION}}": html.escape(str(version.get("livro", "?"))),
            "{{NAVIGATION}}": sidebar,
            "{{PAGE_GROUP}}": html.escape(group),
            "{{MODULE_QUICK_SUMMARY}}": quick_summary,
            "{{CONTENT}}": body,
            "{{TOC}}": build_toc(toc_visible),
            "{{PREV_NEXT}}": build_prev_next(items, idx, public_rel),
        }
        for key, value in replacements.items():
            out = out.replace(key, value)
        output.write_text(out, encoding="utf-8")
        outputs.append(output)

    redirect = root / "docs.html"
    redirect.write_text(
        '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=docs/">'
        '<link rel="canonical" href="docs/"><title>Documentação Coral</title></head>'
        '<body><p><a href="docs/">Abrir a documentação da Coral</a></p></body></html>\n',
        encoding="utf-8",
    )
    outputs.append(redirect)

    # Índice estático da busca global da documentação.
    # Duas formas: JSON (ferramentas) e JS (window.CORAL_INDICE_BUSCA).
    # O formato JS é carregado via <script defer>, que funciona inclusive em
    # file:// (o fetch() falha nesses contextos por política CORS).
    dados_dir = docs_public / "dados"
    dados_dir.mkdir(parents=True, exist_ok=True)
    index_payload = json.dumps({"paginas": search_entries}, ensure_ascii=False, separators=(",", ":"))
    index_path = dados_dir / "indice_busca.json"
    index_path.write_text(index_payload, encoding="utf-8")
    outputs.append(index_path)
    index_js_path = dados_dir / "indice_busca.js"
    index_js_path.write_text(
        "/* Gerado por tools/site_renderer.py — índice da busca global da documentação.\n"
        "   Carregado via <script defer> para funcionar também em file://. */\n"
        "window.CORAL_INDICE_BUSCA = " + index_payload + ";\n",
        encoding="utf-8",
    )
    outputs.append(index_js_path)
    return outputs
