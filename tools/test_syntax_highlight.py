from __future__ import annotations

import html as html_lib
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from site_renderer import markdown_to_html  # noqa: E402
from syntax_highlight import carregar_sintaxe_coral, highlight_coral, token_list  # noqa: E402


class CodeTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_code = False
        self.code: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "code":
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == "code":
            self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.code.append(data)


def recovered_code(fragment: str) -> str:
    parser = CodeTextParser()
    parser.feed(f"<code>{fragment}</code>")
    return "".join(parser.code)


class SyntaxHighlightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.syntax = carregar_sintaxe_coral(ROOT / "docs" / "dados" / "sintaxe.json")

    def tokens(self, raw: str):
        return token_list(raw, self.syntax)

    def test_strings_escapes_and_comment(self):
        raw = 'mostre "Ele disse \\"oi\\""\nmostre \'# ainda é string\'\nmostre "# ainda é string" # agora é comentário'
        tokens = self.tokens(raw)
        strings = [text for kind, text in tokens if kind == "str"]
        comments = [text for kind, text in tokens if kind == "comment"]
        self.assertEqual(strings, ['"Ele disse \\"oi\\""', "'# ainda é string'", '"# ainda é string"'])
        self.assertEqual(comments, ["# agora é comentário"])

    def test_natural_comment_line(self):
        raw = "  comentário: exemplo pedagógico\nmostre 1"
        tokens = self.tokens(raw)
        self.assertIn(("comment", "comentário: exemplo pedagógico"), tokens)

    def test_decimal_and_comma(self):
        tokens = self.tokens("defina x como 12.5\nsoma(1, 2)")
        nums = [text for kind, text in tokens if kind == "num"]
        self.assertEqual(nums, ["12.5", "1", "2"])
        self.assertNotIn("1, 2", nums)

    def test_keyword_boundary_and_function(self):
        tokens = self.tokens("definidor()\ndefina valor como 1")
        self.assertIn(("fn", "definidor"), tokens)
        self.assertIn(("key", "defina"), tokens)
        self.assertNotIn(("key", "defini"), tokens)

    def test_casefold_without_accent_fabrication(self):
        tokens = self.tokens("SE verdadeiro ENTÃO\nsenão\nsenao")
        self.assertIn(("key", "SE"), tokens)
        self.assertIn(("key", "ENTÃO"), tokens)
        self.assertIn(("key", "senão"), tokens)
        self.assertNotIn(("key", "senao"), tokens)

    def test_module_path(self):
        tokens = self.tokens("coral.regras.eventos")
        self.assertEqual(tokens, [("mod", "coral.regras.eventos")])

    def test_natural_call_not_invented(self):
        tokens = self.tokens("defina resultado como dobre 21")
        self.assertIn(("key", "defina"), tokens)
        self.assertIn(("num", "21"), tokens)
        self.assertNotIn(("fn", "dobre"), tokens)

    def test_html_safety_and_text_fidelity(self):
        raw = 'se x < 10 então\n    mostre "a & b"\nfim'
        fragment = highlight_coral(raw, self.syntax)
        self.assertIn("&lt;", fragment)
        self.assertIn("&amp;", fragment)
        self.assertEqual(recovered_code(fragment), raw)

    def test_only_coral_fences_receive_highlight(self):
        md = '''# Exemplo\n\n```coral\ndefina x como 1\n```\n\n```coral-natural\nmostre "ok"\n```\n\n```bash\necho coral.jogos 12.5\n```\n\n```text\ndefina x como 1\n```\n\n```json\n{"coral": 1}\n```\n'''
        rendered, _ = markdown_to_html(md, self.syntax)
        blocks = re.findall(r'<code(?: class="language-([^"]+)")?>(.*?)</code>', rendered, re.S)
        self.assertEqual(len(blocks), 5)
        for lang, body in blocks:
            has_tokens = bool(re.search(r'class="code-(?:key|str|num|mod|fn|comment)"', body))
            if lang == "coral" or lang.startswith("coral-"):
                self.assertTrue(has_tokens, lang)
            else:
                self.assertFalse(has_tokens, lang)

    def test_highlight_preserves_raw_text(self):
        fixtures = [
            'mostre "Olá"',
            "mostre 'Olá'",
            'mostre "Ele disse \\"oi\\""',
            'mostre "# texto" # comentário',
            'coral.regras.eventos',
            'soma(1, 2)',
            'se x < 10 então\n    mostre "a & b"\nfim',
        ]
        for raw in fixtures:
            with self.subTest(raw=raw):
                self.assertEqual(recovered_code(highlight_coral(raw, self.syntax)), raw)


if __name__ == "__main__":
    unittest.main(verbosity=2)
