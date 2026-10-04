import unittest

from tools.rescope_pygments_dark import rescope

_SHEET = """\
.highlight { background: #f8f8f8; }
.highlight .k { color: #008000 }
.highlight .n { color: inherit }
@media (prefers-color-scheme: dark) {
.highlight { background: #272822; color: #F8F8F2 }
.highlight .hll { background-color: #49483e }
.highlight .n { color: #F8F8F2 }
.highlight .k { color: #66D9EF }
}
"""


class RescopePygmentsDarkTest(unittest.TestCase):
    def test_dark_media_block_follows_html_dark(self):
        rewritten = rescope(_SHEET)
        self.assertNotIn("prefers-color-scheme", rewritten)
        self.assertIn(".highlight .k { color: #008000 }", rewritten)
        flat = rewritten.replace("\n", " ")
        self.assertIn("html.dark .highlight { color: #F8F8F2 }", flat)
        self.assertNotIn("#272822", rewritten)
        self.assertNotIn("#49483e", rewritten)
        self.assertIn("html.dark .highlight .n { color: #F8F8F2 }", rewritten)
        self.assertIn("html.dark .highlight .k { color: #66D9EF }", rewritten)

    def test_sheet_without_dark_block_is_unchanged(self):
        light = ".highlight .k { color: #008000 }\n"
        self.assertEqual(rescope(light), light)


if __name__ == "__main__":
    unittest.main()
