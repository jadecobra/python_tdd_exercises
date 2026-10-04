import unittest

from tools.check_light_code_contrast import check

_THEME = (
    ":root{--background:0 0% 100%;--foreground:222 47% 11%}"
    " .highlight{background-color:initial!important}"
)
_PYGMENTS = ".highlight { background: #f8f8f8; } .k { color: #008000 }"


class CheckLightCodeContrastTest(unittest.TestCase):
    def test_green_token_on_white_page_passes(self):
        self.assertEqual(check(_PYGMENTS, _THEME), [])

    def test_white_token_fails(self):
        pygments = ".highlight { background: #f8f8f8; } .k { color: #ffffff }"
        failures = check(pygments, _THEME)
        self.assertEqual(len(failures), 1)

    def test_dark_selector_and_dark_media_do_not_fail(self):
        pygments = (
            ".highlight { background: #f8f8f8; } .k { color: #008000 }"
            " .dark .k { color: #ffffff }"
            " @media (prefers-color-scheme: dark) { .err { color: #ffffff } }"
        )
        self.assertEqual(check(pygments, _THEME), [])

    def test_light_foreground_matching_background_fails(self):
        theme = (
            ":root{--background:0 0% 100%;--foreground:0 0% 100%}"
            " .highlight{background-color:initial!important}"
        )
        self.assertTrue(check(_PYGMENTS, theme))

    def test_grouped_pre_and_code_color_fails(self):
        theme = _THEME + " pre, code { color: #ffffff }"
        failures = check(_PYGMENTS, theme)
        self.assertEqual(len(failures), 2)

    def test_missing_background_fails(self):
        theme = ":root{--foreground:222 47% 11%} .highlight{background-color:initial!important}"
        self.assertEqual(check(_PYGMENTS, theme), ["missing light background"])


if __name__ == "__main__":
    unittest.main()
