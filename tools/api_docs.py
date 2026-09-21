from __future__ import annotations

import ast
import importlib.util
import re
import zipfile
from dataclasses import dataclass
from typing import Any


def _unparse(node: ast.AST | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def _summary(node: ast.AST) -> str:
    try:
        text = ast.get_docstring(node, clean=True) or ""
    except Exception:
        text = ""
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.split("\n\n", 1)[0]).strip()


def _full_doc(node: ast.AST) -> str:
    try:
        return (ast.get_docstring(node, clean=True) or "").strip()
    except Exception:
        return ""


def _name_of(expr: ast.AST | None) -> str:
    if expr is None:
        return ""
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.Attribute):
        left = _name_of(expr.value)
        return f"{left}.{expr.attr}" if left else expr.attr
    if isinstance(expr, ast.Call):
        return _name_of(expr.func)
    return _unparse(expr)


def _resolve_relative(current: str, is_package: bool, level: int, module: str | None) -> str | None:
    package = current if is_package else current.rsplit(".", 1)[0] if "." in current else current
    try:
        return importlib.util.resolve_name("." * level + (module or ""), package)
    except Exception:
        return None


@dataclass
class SourceModule:
    name: str
    source: str
    tree: ast.Module
    is_package: bool
    defs: dict[str, ast.AST]
    imports: dict[str, tuple[str | None, str | None]]
    stars: list[str]
    all_names: list[str] | None
    relpath: str


def _python_modules(zf: zipfile.ZipFile) -> dict[str, SourceModule]:
    raw: dict[str, tuple[str, str, bool]] = {}
    for name in zf.namelist():
        marker = "Projeto/coral/"
        pos = name.find(marker)
        if pos < 0 or not name.endswith(".py"):
            continue
        rel = name[pos + len("Projeto/"):]
        source = zf.read(name).decode("utf-8", errors="replace")
        if rel.endswith("/__init__.py"):
            dotted = rel[:-12].replace("/", ".")
            is_package = True
        else:
            dotted = rel[:-3].replace("/", ".")
            is_package = False
        raw[dotted] = (source, rel, is_package)

    modules: dict[str, SourceModule] = {}
    for dotted, (source, rel, is_package) in raw.items():
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        defs: dict[str, ast.AST] = {}
        imports: dict[str, tuple[str | None, str | None]] = {}
        stars: list[str] = []
        all_names: list[str] | None = None
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                defs[node.name] = node
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defs[target.id] = node
                        if target.id == "__all__":
                            try:
                                value = ast.literal_eval(node.value)
                                if isinstance(value, (list, tuple)):
                                    all_names = [str(x) for x in value]
                            except Exception:
                                pass
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                defs[node.target.id] = node
            elif isinstance(node, ast.ImportFrom):
                target_module = _resolve_relative(dotted, is_package, node.level, node.module)
                if any(alias.name == "*" for alias in node.names):
                    if target_module:
                        stars.append(target_module)
                else:
                    for alias in node.names:
                        imports[alias.asname or alias.name] = (target_module, alias.name)
        modules[dotted] = SourceModule(
            dotted, source, tree, is_package, defs, imports, stars, all_names, rel
        )
    return modules


def _resolve_symbol(
    modules: dict[str, SourceModule], module: str, symbol: str, visited: set[tuple[str, str]] | None = None
) -> tuple[str, ast.AST, SourceModule] | None:
    visited = visited or set()
    key = (module, symbol)
    if key in visited:
        return None
    visited.add(key)
    info = modules.get(module)
    if info is None:
        return None
    if symbol in info.defs:
        return module, info.defs[symbol], info
    if symbol in info.imports:
        target, original = info.imports[symbol]
        if target and original:
            found = _resolve_symbol(modules, target, original, visited)
            if found:
                return found
    for target in info.stars:
        star = modules.get(target)
        if star is None:
            continue
        if star.all_names is None or symbol in star.all_names or symbol in star.defs:
            found = _resolve_symbol(modules, target, symbol, visited)
            if found:
                return found
    prefix = module + "."
    for candidate, candidate_info in modules.items():
        if candidate.startswith(prefix) and symbol in candidate_info.defs:
            return candidate, candidate_info.defs[symbol], candidate_info
    if module.count(".") == 1:
        candidate = "coral.stdlib." + module.rsplit(".", 1)[-1]
        candidate_info = modules.get(candidate)
        if candidate_info and symbol in candidate_info.defs:
            return candidate, candidate_info.defs[symbol], candidate_info
    return None


def _actual_exports(modules: dict[str, SourceModule], module: str, fallback: list[str]) -> list[str]:
    info = modules.get(module)
    if not info:
        return fallback
    if info.all_names:
        return list(info.all_names)
    if len(info.stars) == 1:
        star = modules.get(info.stars[0])
        if star and star.all_names:
            return list(star.all_names)
    return fallback


def _parameters(args: ast.arguments, drop_receiver: bool = False) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    positional = list(args.posonlyargs) + list(args.args)
    defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    for index, (arg, default) in enumerate(zip(positional, defaults)):
        if drop_receiver and index == 0 and arg.arg in {"self", "cls"}:
            continue
        result.append({
            "nome": arg.arg,
            "tipo": _unparse(arg.annotation) or "não declarado",
            "padrao": _unparse(default) if default is not None else None,
            "modo": "posicional",
        })
    if args.vararg:
        result.append({
            "nome": "*" + args.vararg.arg,
            "tipo": _unparse(args.vararg.annotation) or "não declarado",
            "padrao": None,
            "modo": "variádico",
        })
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        result.append({
            "nome": arg.arg,
            "tipo": _unparse(arg.annotation) or "não declarado",
            "padrao": _unparse(default) if default is not None else None,
            "modo": "nomeado",
        })
    if args.kwarg:
        result.append({
            "nome": "**" + args.kwarg.arg,
            "tipo": _unparse(args.kwarg.annotation) or "não declarado",
            "padrao": None,
            "modo": "variádico nomeado",
        })
    return result


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef, *, name: str | None = None, drop_receiver: bool = False) -> str:
    parts: list[str] = []
    positional = list(node.args.posonlyargs) + list(node.args.args)
    defaults = [None] * (len(positional) - len(node.args.defaults)) + list(node.args.defaults)
    posonly_count = len(node.args.posonlyargs)
    emitted_positional = 0
    for index, (arg, default) in enumerate(zip(positional, defaults)):
        if drop_receiver and index == 0 and arg.arg in {"self", "cls"}:
            continue
        item = arg.arg
        if arg.annotation:
            item += f": {_unparse(arg.annotation)}"
        if default is not None:
            item += f" = {_unparse(default)}"
        parts.append(item)
        emitted_positional += 1
        if posonly_count and index == posonly_count - 1:
            parts.append("/")
    if node.args.vararg:
        item = "*" + node.args.vararg.arg
        if node.args.vararg.annotation:
            item += f": {_unparse(node.args.vararg.annotation)}"
        parts.append(item)
    elif node.args.kwonlyargs:
        parts.append("*")
    for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
        item = arg.arg
        if arg.annotation:
            item += f": {_unparse(arg.annotation)}"
        if default is not None:
            item += f" = {_unparse(default)}"
        parts.append(item)
    if node.args.kwarg:
        item = "**" + node.args.kwarg.arg
        if node.args.kwarg.annotation:
            item += f": {_unparse(node.args.kwarg.annotation)}"
        parts.append(item)
    prefix = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
    text = f"{prefix}{name or node.name}({', '.join(parts)})"
    retorno = _unparse(node.returns)
    if retorno:
        text += f" -> {retorno}"
    return text


def _raise_names(node: ast.AST) -> list[str]:
    names: list[str] = []
    for item in ast.walk(node):
        if isinstance(item, ast.Raise) and item.exc is not None:
            name = _name_of(item.exc)
            if name and name not in names:
                names.append(name)
    return names[:12]


def _decorator_names(node: ast.AST) -> set[str]:
    return {_name_of(x) for x in getattr(node, "decorator_list", [])}


def _class_fields(node: ast.ClassDef) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for item in node.body:
        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name) and not item.target.id.startswith("_"):
            fields.append({
                "nome": item.target.id,
                "tipo": _unparse(item.annotation) or "não declarado",
                "padrao": _unparse(item.value) if item.value is not None else None,
            })
    return fields


def _class_signature(node: ast.ClassDef) -> str:
    init = next((x for x in node.body if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef)) and x.name == "__init__"), None)
    if init:
        sig = _signature(init, name=node.name, drop_receiver=True)
        return sig.replace("async " + node.name, node.name, 1)
    decorators = _decorator_names(node)
    if any(name.endswith("dataclass") for name in decorators):
        fields = _class_fields(node)
        parts = []
        for field in fields:
            value = field["nome"]
            if field["tipo"] != "não declarado":
                value += f": {field['tipo']}"
            if field["padrao"] is not None:
                value += f" = {field['padrao']}"
            parts.append(value)
        return f"{node.name}({', '.join(parts)})"
    return f"{node.name}(...)"


def _class_methods(node: ast.ClassDef) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in node.body:
        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) or item.name.startswith("_"):
            continue
        decorators = _decorator_names(item)
        kind = "propriedade" if "property" in decorators else "método"
        result.append({
            "nome": item.name,
            "tipo": kind,
            "assinatura": _signature(item, drop_receiver=True),
            "retorno": _unparse(item.returns) or "não declarado",
            "descricao": _summary(item),
        })
    return result


def _kind_for_class(node: ast.ClassDef) -> str:
    bases = {_name_of(x) for x in node.bases}
    if any(name.endswith(("Error", "Exception", "ErroCoral", "ErroOperacaoCoral", "ErroDependenciaCoral")) for name in bases) or node.name.startswith(("Erro", "Dependencia")):
        return "exceção"
    if "Protocol" in bases:
        return "protocolo"
    return "classe"


def _assignment_info(symbol: str, node: ast.Assign | ast.AnnAssign, module_name: str, relpath: str) -> dict[str, Any]:
    value = node.value if isinstance(node, (ast.Assign, ast.AnnAssign)) else None
    annotation = _unparse(node.annotation) if isinstance(node, ast.AnnAssign) else ""
    value_text = _unparse(value)
    kind = "constante" if symbol.isupper() else "alias"
    return {
        "nome": symbol,
        "tipo": kind,
        "assinatura": f"{symbol}: {annotation}" if annotation else symbol,
        "retorno": annotation or "não declarado",
        "descricao": "Constante pública do módulo." if kind == "constante" else "Alias público de tipo ou valor.",
        "valor": value_text[:240] if value_text else "",
        "origem": module_name,
        "arquivo": relpath,
        "parametros": [],
        "excecoes": [],
        "metodos": [],
        "atributos": [],
    }


def _symbol_info(modules: dict[str, SourceModule], public_module: str, symbol: str) -> dict[str, Any]:
    resolved = _resolve_symbol(modules, public_module, symbol)
    if not resolved:
        return {
            "nome": symbol, "tipo": "símbolo", "assinatura": symbol,
            "retorno": "não declarado", "descricao": "Símbolo público da release.",
            "origem": public_module, "arquivo": "", "parametros": [], "excecoes": [],
            "metodos": [], "atributos": [],
        }
    origin, node, source_module = resolved
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return {
            "nome": symbol,
            "tipo": "função assíncrona" if isinstance(node, ast.AsyncFunctionDef) else "função",
            "assinatura": _signature(node, name=symbol),
            "retorno": _unparse(node.returns) or "não declarado",
            "descricao": _summary(node),
            "documentacao": _full_doc(node),
            "origem": origin,
            "arquivo": source_module.relpath,
            "parametros": _parameters(node.args),
            "excecoes": _raise_names(node),
            "metodos": [],
            "atributos": [],
        }
    if isinstance(node, ast.ClassDef):
        kind = _kind_for_class(node)
        return {
            "nome": symbol,
            "tipo": kind,
            "assinatura": _class_signature(node),
            "retorno": symbol,
            "descricao": _summary(node),
            "documentacao": _full_doc(node),
            "origem": origin,
            "arquivo": source_module.relpath,
            "parametros": [],
            "excecoes": [],
            "metodos": _class_methods(node),
            "atributos": _class_fields(node),
            "bases": [_name_of(x) for x in node.bases],
        }
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        return _assignment_info(symbol, node, origin, source_module.relpath)
    return {
        "nome": symbol, "tipo": "símbolo", "assinatura": symbol,
        "retorno": "não declarado", "descricao": "Símbolo público da release.",
        "origem": origin, "arquivo": source_module.relpath, "parametros": [], "excecoes": [],
        "metodos": [], "atributos": [],
    }


def enrich_modules_from_zip(zf: zipfile.ZipFile, modules_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sources = _python_modules(zf)
    enriched: list[dict[str, Any]] = []
    for module in modules_data:
        item = dict(module)
        import_name = str(item.get("importacao", f"coral.{item['nome']}"))
        fallback = list(item.get("operacoes", []))
        public_names = _actual_exports(sources, import_name, fallback)
        if not public_names:
            public_names = fallback
        item["operacoes"] = public_names
        item["api"] = [_symbol_info(sources, import_name, name) for name in public_names]
        info = sources.get(import_name)
        if info:
            item["doc_modulo"] = (ast.get_docstring(info.tree, clean=True) or "").strip()
        enriched.append(item)
    return enriched


def _md_cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def render_api_markdown(module: dict[str, Any]) -> str:
    api = list(module.get("api", []))
    if not api:
        return "A release não forneceu metadados estruturados para esta superfície."
    groups = [
        ("Funções", {"função", "função assíncrona"}),
        ("Classes e protocolos", {"classe", "protocolo"}),
        ("Exceções", {"exceção"}),
        ("Constantes e aliases", {"constante", "alias", "símbolo"}),
    ]
    out: list[str] = []
    for title, kinds in groups:
        entries = [entry for entry in api if entry.get("tipo") in kinds]
        if not entries:
            continue
        out += [f"### {title}", ""]
        for entry in entries:
            sig = entry.get("assinatura") or entry["nome"]
            out += [f"#### `{sig}`", ""]
            description = (entry.get("descricao") or "").strip()
            if description:
                out += [description, ""]
            else:
                out += [f"Entrada pública `{entry['nome']}` da superfície `{module['importacao']}`.", ""]
            if entry.get("origem") and entry.get("origem") != module.get("importacao"):
                out += [f"**Implementação:** `{entry['origem']}`", ""]
            params = entry.get("parametros") or []
            if params:
                out += ["**Parâmetros**", "", "| Nome | Tipo | Padrão | Modo |", "|---|---|---|---|"]
                for param in params:
                    out.append(
                        f"| `{_md_cell(param['nome'])}` | `{_md_cell(param['tipo'])}` | "
                        f"{('`' + _md_cell(param['padrao']) + '`') if param.get('padrao') is not None else 'obrigatório'} | "
                        f"{_md_cell(param.get('modo', ''))} |"
                    )
                out.append("")
            if entry.get("retorno") and entry.get("tipo") in {"função", "função assíncrona"}:
                out += [f"**Retorno:** `{entry['retorno']}`", ""]
            if entry.get("atributos"):
                out += ["**Atributos declarados**", "", "| Nome | Tipo | Padrão |", "|---|---|---|"]
                for field in entry["atributos"]:
                    default = f"`{_md_cell(field['padrao'])}`" if field.get("padrao") is not None else "obrigatório"
                    out.append(f"| `{_md_cell(field['nome'])}` | `{_md_cell(field['tipo'])}` | {default} |")
                out.append("")
            if entry.get("metodos"):
                out += ["**Métodos e propriedades públicas**", "", "| Nome | Tipo | Assinatura | Retorno | Descrição |", "|---|---|---|---|---|"]
                for method in entry["metodos"]:
                    out.append(
                        f"| `{_md_cell(method['nome'])}` | {_md_cell(method['tipo'])} | "
                        f"`{_md_cell(method['assinatura'])}` | `{_md_cell(method['retorno'])}` | "
                        f"{_md_cell(method.get('descricao') or 'Sem docstring própria na release.')} |"
                    )
                out.append("")
            if entry.get("excecoes"):
                out += ["**Exceções observáveis no corpo:** " + ", ".join(f"`{name}`" for name in entry["excecoes"]), ""]
            if entry.get("valor"):
                out += [f"**Valor declarado:** `{entry['valor']}`", ""]
    return "\n".join(out).rstrip()
