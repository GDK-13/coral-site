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


def _has_value_return(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """Indica se a função contém retorno explícito com valor.

    Funções aninhadas não contam para o comportamento da função pública.
    """
    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.found = False

        def visit_Return(self, item: ast.Return) -> None:  # noqa: N802
            if item.value is None:
                return
            if isinstance(item.value, ast.Constant) and item.value.value is None:
                return
            self.found = True

        def visit_FunctionDef(self, item: ast.FunctionDef) -> None:  # noqa: N802
            if item is node:
                for child in item.body:
                    self.visit(child)

        def visit_AsyncFunctionDef(self, item: ast.AsyncFunctionDef) -> None:  # noqa: N802
            if item is node:
                for child in item.body:
                    self.visit(child)

        def visit_Lambda(self, item: ast.Lambda) -> None:  # noqa: N802
            return

    visitor = Visitor()
    visitor.visit(node)
    return visitor.found

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


def _class_parameters(node: ast.ClassDef) -> list[dict[str, Any]]:
    init = next(
        (x for x in node.body if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef)) and x.name == "__init__"),
        None,
    )
    if init is not None:
        return _parameters(init.args, drop_receiver=True)
    decorators = _decorator_names(node)
    if any(name.endswith("dataclass") for name in decorators):
        result: list[dict[str, Any]] = []
        for field in _class_fields(node):
            result.append({
                "nome": field["nome"],
                "tipo": field["tipo"],
                "padrao": field["padrao"],
                "modo": "posicional",
            })
        return result
    return []


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
            "tem_retorno_valor": _has_value_return(node),
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
            "parametros": _class_parameters(node),
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


PARAMETER_MEANINGS = {
    "caminho": "Caminho do arquivo ou diretório usado pela operação.",
    "origem": "Origem usada pela operação.",
    "destino": "Destino que receberá o resultado da operação.",
    "texto": "Texto processado pela operação.",
    "conteudo": "Conteúdo processado ou armazenado.",
    "codificacao": "Codificação de texto usada na leitura ou escrita.",
    "valores": "Coleção de valores processada.",
    "valor": "Valor processado pela operação.",
    "linhas": "Linhas usadas para construir ou processar a estrutura.",
    "minimo": "Limite mínimo considerado pela operação.",
    "maximo": "Limite máximo considerado pela operação.",
    "inicio": "Valor inicial do intervalo ou processo.",
    "fim": "Valor final do intervalo ou processo.",
    "passo": "Incremento aplicado entre valores sucessivos.",
    "quantidade": "Quantidade de itens solicitada.",
    "semente": "Semente usada para tornar a sequência reproduzível.",
    "fonte": "Fonte explícita usada pela operação; quando omitida, vale o comportamento padrão do módulo.",
    "pesos": "Pesos associados aos valores usados na escolha.",
    "tipo": "Tipo solicitado para o resultado, quando o módulo oferece essa escolha.",
    "forma": "Forma ou dimensões da estrutura a criar.",
    "nome": "Nome usado para identificar o objeto criado ou consultado.",
    "largura": "Largura usada pela operação.",
    "altura": "Altura usada pela operação.",
    "x": "Coordenada horizontal.",
    "y": "Coordenada vertical.",
    "fps": "Quantidade alvo de quadros por segundo.",
    "backend": "Backend usado para executar a operação.",
    "mundo": "Mundo associado à operação.",
    "eventos": "Fonte ou conjunto de eventos associado à operação.",
    "relogio": "Relógio usado para controlar tempo ou atualização.",
    "tela_cheia": "Define se a janela deve usar tela cheia.",
    "chave": "Chave usada para localizar ou identificar um valor.",
    "padrao": "Valor usado quando não há resultado específico disponível.",
    "funcao": "Função fornecida para executar a operação.",
    "predicado": "Função ou condição usada para decidir quais valores atendem ao critério.",
    "separador": "Texto usado para separar partes do resultado.",
    "base": "Base usada pela conversão ou cálculo.",
    "precisao": "Precisão solicitada para o resultado.",
    "formato": "Formato usado para interpretar ou produzir o valor.",
    "dados": "Dados processados pela operação.",
    "objeto": "Objeto processado pela operação.",
    "estado": "Estado usado ou atualizado pela operação.",
    "motivo": "Texto que descreve o motivo associado à operação.",
}


VERB_DESCRIPTIONS = {
    "ler": "Lê",
    "escrever": "Escreve",
    "salvar": "Salva",
    "carregar": "Carrega",
    "abrir": "Abre",
    "fechar": "Fecha",
    "criar": "Cria",
    "remover": "Remove",
    "copiar": "Copia",
    "mover": "Move",
    "listar": "Lista",
    "converter": "Converte",
    "formatar": "Formata",
    "validar": "Valida",
    "normalizar": "Normaliza",
    "adicionar": "Adiciona",
    "definir": "Define",
    "registrar": "Registra",
    "cancelar": "Cancela",
    "executar": "Executa",
    "atualizar": "Atualiza",
    "renderizar": "Renderiza",
    "diagnosticar": "Produz informações de diagnóstico para",
    "observar": "Observa",
    "rastrear": "Rastreia",
    "reproduzir": "Reproduz",
    "embaralhar": "Embaralha",
    "escolher": "Escolhe",
    "renomear": "Renomeia",
    "resolver": "Resolve",
    "limpar": "Limpa",
    "avancar": "Avança",
    "pausar": "Pausa",
    "retomar": "Retoma",
    "reiniciar": "Reinicia",
    "encerrar": "Encerra",
    "iniciar": "Inicia",
    "parar": "Interrompe",
    "ligar": "Liga",
    "desligar": "Desliga",
    "seguir": "Passa a seguir",
    "usar": "Seleciona",
    "acionar": "Aciona",
    "emitir": "Emite",
    "enfileirar": "Enfileira",
    "processar": "Processa",
    "representar": "Cria uma representação de",
    "sincronizar": "Sincroniza",
    "girar": "Gira",
    "aumentar": "Aumenta",
    "diminuir": "Diminui",
    "configurar": "Configura",
    "restaurar": "Restaura",
    "adaptar": "Adapta",
    "tocar": "Executa",
    "intersectar": "Verifica a interseção de",
    "relacionar": "Relaciona",
    "guardar": "Armazena",
}


def _human_words(name: str) -> str:
    words = [w for w in re.split(r"_+", name.strip("_*")) if w]
    replacements = {
        "km2": "km²", "json": "JSON", "id": "identificador", "ids": "identificadores",
        "x": "x", "y": "y", "fps": "FPS", "api": "API", "numpy": "NumPy",
    }
    return " ".join(replacements.get(w, w) for w in words)


def _parameter_meaning(name: str) -> str:
    bare = name.lstrip("*")
    if bare in PARAMETER_MEANINGS:
        return PARAMETER_MEANINGS[bare]
    if bare.startswith("atributo_"):
        return f"Nome do atributo usado como {_human_words(bare.removeprefix('atributo_'))}."
    if bare.startswith("largura_"):
        return f"Largura de {_human_words(bare.removeprefix('largura_'))}."
    if bare.startswith("altura_"):
        return f"Altura de {_human_words(bare.removeprefix('altura_'))}."
    if bare.startswith("usar_") or bare.startswith("permitir_") or bare.startswith("incluir_"):
        return f"Controla se deve {_human_words(bare)}."
    if bare.startswith("eh_") or bare.startswith("is_"):
        return f"Indicador relacionado a {_human_words(bare)}."
    phrase = _human_words(bare)
    return f"Valor correspondente a {phrase}." if phrase else "Valor fornecido à operação."


def _fallback_description(entry: dict[str, Any], module: dict[str, Any]) -> str:
    name = str(entry.get("nome", ""))
    kind = str(entry.get("tipo", "símbolo"))
    purpose = str((module.get("editorial_api") or {}).get(name, "")).strip()
    if purpose:
        text = purpose.rstrip(".")
        first_word = text.split(None, 1)[0].casefold() if text else ""
        looks_like_action = first_word.endswith(("ar", "er", "ir")) or first_word in {
            "obter", "ler", "gravar", "salvar", "carregar", "criar", "abrir", "fechar",
            "consultar", "detectar", "calcular", "medir", "sortear", "escolher", "selecionar",
            "reordenar", "converter", "interpretar", "gerar", "verificar", "comparar", "normalizar",
            "associar", "coordenar", "observar", "reconhecer", "persistir", "restaurar", "executar",
            "construir", "montar", "listar", "inspecionar", "agregar", "renderizar", "resolver",
        }
        if kind in {"classe", "protocolo", "exceção"} and not looks_like_action:
            prefix = "Representa" if kind != "protocolo" else "Define"
            return f"{prefix} {text}."
        if kind in {"função", "função assíncrona"} and looks_like_action:
            return text[0].upper() + text[1:] + "."
    if kind in {"classe", "protocolo", "exceção"}:
        label = _human_words(name)
        if kind == "exceção":
            return f"Representa a condição de erro {label}."
        if kind == "protocolo":
            return f"Define o contrato público de {label}."
        return f"Representa {label} na API de `{module.get('importacao', '')}`."
    if kind == "constante":
        return f"Expõe a constante pública `{name}`."
    if kind in {"alias", "símbolo"}:
        return f"Expõe `{name}` como parte da API pública do módulo."
    # Padrões de nomes usados em várias APIs Coral. São descrições de efeito,
    # não inferências de tipo.
    if name.startswith("quando_"):
        return f"Registra uma ação para quando ocorrer {_human_words(name.removeprefix('quando_'))}."
    if name.startswith("buscar_"):
        return f"Procura {_human_words(name.removeprefix('buscar_'))} e devolve o resultado quando encontrado."
    if name.startswith("exigir_"):
        return f"Obtém {_human_words(name.removeprefix('exigir_'))} e sinaliza falha quando ele não está disponível."
    if name.startswith("obter_"):
        return f"Obtém {_human_words(name.removeprefix('obter_'))}."
    if name.startswith("possui_"):
        return f"Indica se possui {_human_words(name.removeprefix('possui_'))}."
    if name.startswith("para_"):
        return f"Converte o valor para {_human_words(name.removeprefix('para_'))}."
    if name.startswith("de_"):
        return f"Interpreta ou reconstrói um valor a partir de {_human_words(name.removeprefix('de_'))}."
    if name.startswith("como_"):
        return f"Representa o valor como {_human_words(name.removeprefix('como_'))}."
    if name.startswith("desenhar_"):
        return f"Desenha {_human_words(name.removeprefix('desenhar_'))}."
    if name.startswith("alternar_"):
        return f"Alterna {_human_words(name.removeprefix('alternar_'))}."
    if name.startswith("definir_"):
        return f"Define {_human_words(name.removeprefix('definir_'))}."
    if name.startswith("configurar_"):
        return f"Configura {_human_words(name.removeprefix('configurar_'))}."
    if name.startswith("publicar_"):
        return f"Publica {_human_words(name.removeprefix('publicar_'))}."
    if name.startswith("programar_"):
        return f"Programa {_human_words(name.removeprefix('programar_'))}."
    if name.startswith("quadro_") or name.startswith("quadros_"):
        return f"Obtém {_human_words(name)}."
    if name in {"ativo", "aberta", "vivo", "terminou", "cancelado", "inicializado", "sucesso", "finalizada", "em_tela_cheia"}:
        return f"Indica o estado de {_human_words(name)}."
    if name in {"historico", "pendentes", "entidades", "relacoes", "mapas", "camadas", "direcoes", "estados", "eventos", "representacoes", "propriedades", "retornos", "combates_do_mundo", "portas_seriais", "dados_enviados", "variaveis_ambiente"}:
        return f"Obtém {_human_words(name)}."
    if name in {"maiusculas", "minusculas"}:
        return f"Converte o texto para {_human_words(name)}."
    if name == "comeca_com":
        return "Indica se o texto começa com o trecho informado."
    if name == "termina_com":
        return "Indica se o texto termina com o trecho informado."
    if name in {"mundo_para_tela", "tela_para_mundo", "celula_para_tela", "tela_para_celula"}:
        origem, destino = name.split("_para_", 1)
        return f"Converte coordenadas de {_human_words(origem)} para {_human_words(destino)}."
    if name.startswith("onda_"):
        return f"Calcula uma onda de {_human_words(name.removeprefix('onda_'))}."
    if name == "rgb":
        return "Cria uma cor a partir de componentes RGB."
    if name == "passo":
        return "Avança o estado controlado por um passo."
    if name in {"valor", "valor_anterior", "motivo", "pai", "relogio", "mundo", "atual", "total", "forma", "limites", "regiao", "retangulo", "imagem", "som", "spritesheet", "quadro_atual"}:
        return f"Obtém {_human_words(name)}."

    special = {
        "ler_texto": "Lê o conteúdo textual de um arquivo.",
        "escrever_texto": "Escreve texto em um arquivo, substituindo o conteúdo anterior.",
        "adicionar_texto": "Acrescenta texto ao final de um arquivo.",
        "ler_bytes": "Lê o conteúdo binário de um arquivo.",
        "escrever_bytes": "Escreve dados binários em um arquivo.",
        "listar": "Lista os itens do diretório indicado.",
        "listar_recursivo": "Lista o conteúdo de um diretório incluindo subdiretórios.",
        "existe": "Verifica se o caminho indicado existe.",
        "tamanho": "Obtém o tamanho do recurso indicado.",
        "metadados": "Obtém metadados do arquivo ou diretório indicado.",
        "para_json": "Converte um valor para texto JSON.",
        "de_json": "Interpreta texto JSON e devolve o valor correspondente.",
        "ler_json": "Lê e interpreta um documento JSON de arquivo.",
        "escrever_json": "Serializa um valor e grava o documento JSON em arquivo.",
        "normalizar_caminho": "Normaliza um caminho para uma representação consistente.",
        "juntar_caminho": "Combina partes de caminho sem concatenar separadores manualmente.",
        "caminho_portatil": "Reconstrói um caminho segundo o estilo solicitado.",
        "agora": "Obtém o instante civil atual.",
        "hoje": "Obtém a data civil atual.",
        "formatar": "Formata o valor usando a representação solicitada.",
        "analisar": "Interpreta o texto e produz o valor correspondente.",
        "para_iso": "Converte o valor temporal para representação ISO 8601.",
        "de_iso": "Interpreta uma representação ISO 8601.",
        "variavel_ambiente": "Lê uma variável de ambiente do processo atual.",
        "definir_variavel_ambiente": "Define uma variável de ambiente no processo atual.",
        "pasta_atual": "Obtém o diretório de trabalho atual.",
        "pasta_usuario": "Obtém o diretório pessoal do usuário.",
        "executar_comando": "Executa um programa externo com argumentos estruturados.",
        "rolar": "Realiza uma rolagem de dados a partir de uma expressão de RPG.",
        "criar_personagem": "Cria e registra um personagem no mundo informado.",
        "salvar_estado_rpg": "Persiste o estado de RPG no caminho informado.",
        "carregar_estado_rpg": "Carrega um mundo de RPG previamente persistido.",
        "criar_jogo": "Cria uma instância de jogo com janela, entrada e backend configuráveis.",
        "formas_colidem": "Verifica se duas formas transformadas estão em colisão.",
        "sprites_colidem": "Verifica se dois sprites estão em colisão.",
        "extensoes_para_dados": "Converte extensões persistentes registradas para dados portáteis.",
        "aplicar_extensoes_persistentes": "Aplica ao objeto as extensões persistentes presentes nos dados carregados.",
        "segundos": "Cria uma duração expressa em segundos.",
        "semanas": "Cria uma duração expressa em semanas.",
        "transposta": "Obtém a matriz transposta.",
        "multiplicar_matrizes": "Multiplica duas matrizes compatíveis.",
        "inversa": "Calcula a matriz inversa quando ela existe.",
        "autovalores": "Calcula os autovalores da matriz.",
        "estado_rpg": "Obtém o agregado de estado RPG associado ao mundo.",
        "arquivo_temporario": "Cria um arquivo temporário e retorna seu caminho.",
        "pasta_temporaria": "Cria uma pasta temporária e retorna seu caminho.",
        "nome": "Obtém o nome final do caminho.",
        "extensao": "Obtém a extensão do caminho.",
        "forma_espacial_sprite": "Converte a geometria de um sprite para uma forma espacial usada em consultas e colisões.",
        "posicao_espacial_sprite": "Obtém a posição espacial correspondente ao sprite.",
        "resumir": "Calcula um resumo criptográfico dos dados usando o algoritmo solicitado.",
        "autenticar": "Calcula um código de autenticação para os dados usando uma chave.",
        "gerar_bytes_seguros": "Gera bytes aleatórios adequados a usos criptográficos.",
        "gerar_token_seguro": "Gera um token textual aleatório adequado a usos criptográficos.",
        "comparar_com_seguranca": "Compara valores sensíveis usando uma comparação apropriada para material criptográfico.",
        "explicar_algoritmo": "Retorna uma explicação do algoritmo criptográfico solicitado.",
        "raiz": "Calcula uma raiz do valor informado.",
        "potencia": "Eleva um valor à potência informada.",
        "absoluto": "Calcula o valor absoluto.",
        "arredondar": "Arredonda o valor segundo a precisão solicitada.",
        "seno": "Calcula o seno do ângulo.",
        "cosseno": "Calcula o cosseno do ângulo.",
        "tangente": "Calcula a tangente do ângulo.",
        "piso": "Obtém o maior inteiro que não ultrapassa o valor.",
        "teto": "Obtém o menor inteiro que não é inferior ao valor.",
        "truncar": "Remove a parte fracionária do valor segundo a operação suportada pela release.",
        "log": "Calcula o logaritmo do valor na base informada.",
        "exp": "Calcula a função exponencial do valor.",
        "graus": "Converte um ângulo em radianos para graus.",
        "radianos": "Converte um ângulo em graus para radianos.",
        "finito": "Indica se o valor numérico é finito.",
        "mdc": "Calcula o máximo divisor comum.",
        "mmc": "Calcula o mínimo múltiplo comum.",
    }
    if name in special:
        return special[name]
    parts = [p for p in name.split("_") if p]
    if not parts:
        return f"Executa a operação pública `{name}`."
    first = parts[0]
    rest = _human_words("_".join(parts[1:]))
    if first in VERB_DESCRIPTIONS:
        verb = VERB_DESCRIPTIONS[first]
        return f"{verb} {rest or 'o valor solicitado'}."
    if name.startswith("eh_") or name.endswith("_disponivel") or name.startswith("tem_"):
        target = name.removeprefix("eh_").removesuffix("_disponivel").removeprefix("tem_")
        return f"Indica se {_human_words(target)} está disponível ou atende à condição esperada."
    if name in {"soma", "media", "mediana", "variancia", "desvio_padrao", "minimo", "maximo"}:
        labels = {
            "soma": "Calcula a soma dos valores.", "media": "Calcula a média dos valores.",
            "mediana": "Calcula a mediana dos valores.", "variancia": "Calcula a variância dos valores.",
            "desvio_padrao": "Calcula o desvio padrão dos valores.", "minimo": "Obtém o menor valor.",
            "maximo": "Obtém o maior valor.",
        }
        return labels[name]
    if name == "inteiro":
        return "Sorteia um número inteiro entre os limites informados."
    if name == "decimal":
        return "Sorteia um número decimal dentro do intervalo informado."
    if name == "fonte":
        return "Cria uma fonte de aleatoriedade, opcionalmente reproduzível por semente."
    if name == "amostra":
        return "Seleciona uma amostra de valores da coleção fornecida."
    if name == "escolha_ponderada":
        return "Escolhe um valor considerando os pesos fornecidos."
    if name == "vetor":
        return "Cria uma estrutura vetorial a partir dos valores fornecidos."
    if name == "matriz":
        return "Cria uma matriz a partir das linhas fornecidas."
    if name == "zeros":
        return "Cria uma estrutura numérica preenchida com zeros."
    if name == "uns":
        return "Cria uma estrutura numérica preenchida com uns."
    if name == "intervalo":
        return "Cria uma sequência numérica definida por início, fim e passo."
    if name == "espaco_linear":
        return "Cria valores igualmente espaçados entre dois limites."
    return f"Executa a operação `{name}` disponibilizada por `{module.get('importacao', '')}`."


def _return_explanation(entry: dict[str, Any]) -> str:
    name = str(entry.get("nome", ""))
    declared = str(entry.get("retorno") or "não declarado")
    if entry.get("tipo") not in {"função", "função assíncrona"}:
        return ""
    known = {
        "inteiro": "Retorna o número inteiro sorteado.",
        "decimal": "Retorna o número decimal sorteado.",
        "escolher": "Retorna um dos valores fornecidos.",
        "amostra": "Retorna a amostra selecionada.",
        "escolha_ponderada": "Retorna o valor escolhido segundo os pesos.",
        "soma": "Retorna o resultado da soma.",
        "media": "Retorna a média calculada.",
        "mediana": "Retorna a mediana calculada.",
        "variancia": "Retorna a variância calculada.",
        "desvio_padrao": "Retorna o desvio padrão calculado.",
        "ler_texto": "Retorna o texto lido.",
        "ler_bytes": "Retorna os bytes lidos.",
        "fonte": "Retorna a fonte de aleatoriedade criada.",
        "vetor": "Retorna o vetor criado.",
        "matriz": "Retorna a matriz criada.",
        "zeros": "Retorna a estrutura preenchida com zeros.",
        "uns": "Retorna a estrutura preenchida com uns.",
        "intervalo": "Retorna a sequência numérica criada.",
        "espaco_linear": "Retorna a sequência de valores igualmente espaçados.",
    }
    if name in known:
        return known[name]
    if name.startswith(("eh_", "tem_")) or name.endswith(("_disponivel", "_existe")) or name in {"existe", "formas_colidem", "sprites_colidem"}:
        return "Retorna um valor lógico que indica o resultado da verificação."
    if entry.get("tem_retorno_valor") is False:
        return "Não produz um valor de retorno útil; o efeito ocorre no estado ou recurso alvo."
    if declared and declared != "não declarado":
        return f"Retorna um valor declarado como `{declared}`."
    return "Retorna o resultado produzido pela operação; o tipo não é declarado pela release."


def _example_for(entry: dict[str, Any], module: dict[str, Any]) -> str:
    examples = module.get("editorial_examples") or {}
    return str(examples.get(entry.get("nome"), "")).strip()


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
            out += [f"#### `{entry['nome']}`", ""]
            description = (entry.get("descricao") or "").strip()
            if not description or description.startswith(("Símbolo público", "Constante pública", "Alias público")):
                description = _fallback_description(entry, module)
            out += [description, ""]

            example = _example_for(entry, module)
            if example:
                out += ["**Exemplo**", "", "```coral", example, "```", ""]

            params = entry.get("parametros") or []
            if params:
                out += ["**Parâmetros**", "", "| Parâmetro | Significado | Tipo | Padrão |", "|---|---|---|---|"]
                for param in params:
                    default = ("`" + _md_cell(param["padrao"]) + "`") if param.get("padrao") is not None else "obrigatório"
                    out.append(
                        f"| `{_md_cell(param['nome'])}` | {_md_cell(_parameter_meaning(param['nome']))} | "
                        f"`{_md_cell(param['tipo'])}` | {default} |"
                    )
                out.append("")

            if entry.get("tipo") in {"função", "função assíncrona"}:
                out += ["**Retorno**", "", _return_explanation(entry), ""]

            if entry.get("atributos"):
                out += ["**Atributos públicos**", "", "| Nome | Significado | Tipo | Padrão |", "|---|---|---|---|"]
                for field in entry["atributos"]:
                    default = f"`{_md_cell(field['padrao'])}`" if field.get("padrao") is not None else "obrigatório"
                    out.append(
                        f"| `{_md_cell(field['nome'])}` | {_md_cell(_parameter_meaning(field['nome']))} | "
                        f"`{_md_cell(field['tipo'])}` | {default} |"
                    )
                out.append("")

            if entry.get("metodos"):
                out += ["**Operações públicas da classe**", "", "| Nome | O que faz | Retorno |", "|---|---|---|"]
                for method in entry["metodos"]:
                    method_desc = (method.get("descricao") or "").strip()
                    if not method_desc:
                        method_desc = _fallback_description({"nome": method["nome"], "tipo": "função"}, module)
                    out.append(
                        f"| `{_md_cell(method['nome'])}` | {_md_cell(method_desc)} | `{_md_cell(method['retorno'])}` |"
                    )
                out.append("")

            # A informação de baixo nível permanece disponível sem dominar a leitura.
            out += [":::details Detalhes técnicos", "", f"**Assinatura:** `{_md_cell(sig)}`", ""]
            if entry.get("origem"):
                out += [f"**Origem da implementação:** `{entry['origem']}`", ""]
            if entry.get("arquivo"):
                out += [f"**Arquivo na release:** `{entry['arquivo']}`", ""]
            if params and any(param.get("modo") not in {"", "posicional"} for param in params):
                out += ["**Modo dos parâmetros**", "", "| Parâmetro | Modo |", "|---|---|"]
                for param in params:
                    out.append(f"| `{_md_cell(param['nome'])}` | {_md_cell(param.get('modo', ''))} |")
                out.append("")
            if entry.get("metodos"):
                out += ["**Assinaturas de métodos e propriedades**", "", "| Nome | Tipo | Assinatura |", "|---|---|---|"]
                for method in entry["metodos"]:
                    out.append(
                        f"| `{_md_cell(method['nome'])}` | {_md_cell(method['tipo'])} | `{_md_cell(method['assinatura'])}` |"
                    )
                out.append("")
            if entry.get("excecoes"):
                out += ["**Exceções diretamente observáveis no corpo:** " + ", ".join(f"`{name}`" for name in entry["excecoes"]), ""]
            if entry.get("valor"):
                out += [f"**Valor declarado:** `{entry['valor']}`", ""]
            out += [":::" , ""]
    return "\n".join(out).rstrip()
