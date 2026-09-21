from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


_DEFAULT_INICIO = r"[A-Za-z_ªºÀ-ÖØ-öø-ÿ]"
_DEFAULT_CONT = r"[A-Za-z0-9_ªºÀ-ÖØ-öø-ÿ]"
_NATURAL_COMMENT_PREFIXES = ("comentário:", "observação:")


@dataclass(frozen=True)
class CoralSyntax:
    release: str
    esquema: str
    lexemas: frozenset[str]
    inicio_ident: str = _DEFAULT_INICIO
    continuacao_ident: str = _DEFAULT_CONT
    decimal: str = "."
    aspas: tuple[str, ...] = ('"', "'")

    @classmethod
    def from_mapping(cls, data: dict) -> "CoralSyntax":
        lexemas = frozenset(str(x).casefold() for x in data.get("lexemas", []) if str(x).strip())
        aspas = tuple(str(x) for x in data.get("aspas", ['"', "'"]) if str(x) in {'"', "'"})
        return cls(
            release=str(data.get("release", "desconhecida")),
            esquema=str(data.get("esquema", "desconhecida")),
            lexemas=lexemas,
            inicio_ident=str(data.get("identificador_inicio", _DEFAULT_INICIO)),
            continuacao_ident=str(data.get("identificador_continuacao", _DEFAULT_CONT)),
            decimal=str(data.get("decimal", ".")) or ".",
            aspas=aspas or ('"', "'"),
        )


@dataclass(frozen=True)
class Token:
    kind: str
    text: str


def carregar_sintaxe_coral(path: str | Path) -> CoralSyntax:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return CoralSyntax.from_mapping(data)


def eh_bloco_coral(language: str | None) -> bool:
    lang = (language or "").strip().casefold()
    return lang == "coral" or lang.startswith("coral-")


def _append(tokens: list[Token], kind: str, text: str) -> None:
    if not text:
        return
    if tokens and tokens[-1].kind == kind:
        prev = tokens[-1]
        tokens[-1] = Token(kind, prev.text + text)
    else:
        tokens.append(Token(kind, text))


def _segmentos_primarios(raw: str, syntax: CoralSyntax) -> list[Token]:
    """Separa texto comum, strings e comentários sem sobreposição.

    A lógica acompanha o contrato lexical da Coral: aspas simples/duplas,
    barra invertida como escape e # como comentário apenas fora de strings.
    Linhas naturais ``comentário:`` e ``observação:`` também são reconhecidas
    no início lógico da linha.
    """
    tokens: list[Token] = []
    n = len(raw)
    i = 0
    text_start = 0
    logical_line_start = True
    quote_set = set(syntax.aspas)

    def flush(end: int) -> None:
        nonlocal text_start
        if end > text_start:
            _append(tokens, "text", raw[text_start:end])
        text_start = end

    while i < n:
        if logical_line_start:
            j = i
            while j < n and raw[j] in " \t\r":
                j += 1
            folded = raw[j:].casefold()
            marker = next((m for m in _NATURAL_COMMENT_PREFIXES if folded.startswith(m)), None)
            if marker is not None:
                flush(j)
                end = raw.find("\n", j)
                if end == -1:
                    end = n
                _append(tokens, "comment", raw[j:end])
                i = end
                text_start = i
                logical_line_start = False
                continue

        ch = raw[i]
        if ch in quote_set:
            flush(i)
            quote = ch
            j = i + 1
            escaped = False
            while j < n:
                cur = raw[j]
                if escaped:
                    escaped = False
                    j += 1
                    continue
                if cur == "\\":
                    escaped = True
                    j += 1
                    continue
                if cur == quote:
                    j += 1
                    break
                j += 1
            _append(tokens, "str", raw[i:j])
            i = j
            text_start = i
            logical_line_start = False
            continue

        if ch == "#":
            flush(i)
            end = raw.find("\n", i)
            if end == -1:
                end = n
            _append(tokens, "comment", raw[i:end])
            i = end
            text_start = i
            logical_line_start = False
            continue

        if ch == "\n":
            logical_line_start = True
        elif logical_line_start and ch in " \t\r":
            pass
        else:
            logical_line_start = False
        i += 1

    flush(n)
    return tokens


def _scanner_helpers(syntax: CoralSyntax):
    start_re = re.compile(rf"^(?:{syntax.inicio_ident})$")
    cont_re = re.compile(rf"^(?:{syntax.continuacao_ident})$")
    ident = rf"(?:{syntax.inicio_ident})(?:{syntax.continuacao_ident})*"
    module_re = re.compile(rf"coral\.{ident}(?:\.{ident})*", re.IGNORECASE)
    return start_re, cont_re, module_re


def _tokenize_text(text: str, syntax: CoralSyntax) -> list[Token]:
    tokens: list[Token] = []
    start_re, cont_re, module_re = _scanner_helpers(syntax)
    n = len(text)
    i = 0
    plain_start = 0

    def flush_plain(end: int) -> None:
        nonlocal plain_start
        if end > plain_start:
            _append(tokens, "text", text[plain_start:end])
        plain_start = end

    while i < n:
        # Caminhos coral.IDENT(.IDENT)* têm precedência sobre identificadores.
        if text[i:i + 6].casefold() == "coral.":
            match = module_re.match(text, i)
            if match:
                flush_plain(i)
                _append(tokens, "mod", match.group(0))
                i = match.end()
                plain_start = i
                continue

        ch = text[i]

        # Literais numéricos Coral usam apenas dígitos ASCII e ponto decimal.
        if "0" <= ch <= "9":
            flush_plain(i)
            j = i + 1
            while j < n and "0" <= text[j] <= "9":
                j += 1
            if j < n and text[j] == syntax.decimal:
                j += 1
                while j < n and "0" <= text[j] <= "9":
                    j += 1
            _append(tokens, "num", text[i:j])
            i = j
            plain_start = i
            continue

        if start_re.fullmatch(ch):
            flush_plain(i)
            j = i + 1
            while j < n and cont_re.fullmatch(text[j]):
                j += 1
            word = text[i:j]
            folded = word.casefold()
            if folded in syntax.lexemas:
                kind = "key"
            elif j < n and text[j] == "(":
                kind = "fn"
            else:
                kind = "text"
            _append(tokens, kind, word)
            i = j
            plain_start = i
            continue

        i += 1

    flush_plain(n)
    return tokens


def tokenize_coral(raw: str, syntax: CoralSyntax) -> Iterator[tuple[str, str]]:
    """Tokeniza Coral para documentação, sem inferência semântica.

    A primeira fase protege strings e comentários. A segunda reconhece apenas
    módulos, números, lexemas sintáticos e chamadas tradicionais com parênteses.
    """
    for segment in _segmentos_primarios(raw, syntax):
        if segment.kind != "text":
            yield segment.kind, segment.text
            continue
        for token in _tokenize_text(segment.text, syntax):
            yield token.kind, token.text


def highlight_coral(raw: str, syntax: CoralSyntax) -> str:
    out: list[str] = []
    for kind, text in tokenize_coral(raw, syntax):
        escaped = html.escape(text)
        if kind == "text":
            out.append(escaped)
        else:
            out.append(f'<span class="code-{kind}">{escaped}</span>')
    return "".join(out)


def token_list(raw: str, syntax: CoralSyntax) -> list[tuple[str, str]]:
    """Helper estável para testes e ferramentas de diagnóstico."""
    return list(tokenize_coral(raw, syntax))


__all__ = [
    "CoralSyntax",
    "Token",
    "carregar_sintaxe_coral",
    "eh_bloco_coral",
    "highlight_coral",
    "token_list",
    "tokenize_coral",
]
