import tempfile
import unittest
from pathlib import Path

from tools.check_chapter_rst import check_rst


def _write(dirpath: Path, name: str, text: str) -> Path:
    path = dirpath / name
    path.write_text(text)
    return path


class CheckChapterRstTest(unittest.TestCase):
    def test_emphasize_past_end_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "bad.rst",
                "\n".join(
                    [
                        ".. code-block:: python",
                        "  :emphasize-lines: 99",
                        "",
                        "  one",
                        "  two",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("outside 1..2" in item for item in errors))

    def test_missing_include_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "bad.rst",
                ".. literalinclude:: missing.py\n",
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("missing literalinclude" in item for item in errors))

    def test_blank_line_inside_window_counts(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "blank.rst",
                "\n".join(
                    [
                        ".. code-block:: python",
                        "  :emphasize-lines: 3",
                        "",
                        "  line1",
                        "",
                        "  line3",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertEqual(errors, [])

    def test_reversed_range_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "rev.rst",
                "\n".join(
                    [
                        ".. code-block:: python",
                        "  :emphasize-lines: 3-1",
                        "",
                        "  a",
                        "  b",
                        "  c",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("reversed" in item for item in errors))

    def test_option_line_missing_colon_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "colon.rst",
                "\n".join(
                    [
                        ".. code-block:: python",
                        "  :caption: terminal",
                        "  emphasize-lines: 1",
                        "",
                        "  cd elevator",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(
                any("option line must start with ':'" in item for item in errors)
            )
            self.assertFalse(any("outside" in item for item in errors))

    def test_lines_option_limits_include(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            _write(root, "sample.py", "a\nb\nc\nd\n")
            rst = _write(
                root,
                "ok.rst",
                "\n".join(
                    [
                        ".. literalinclude:: sample.py",
                        "  :lines: 2-3",
                        "  :emphasize-lines: 2",
                        "  :lineno-start: 2",
                        "",
                    ]
                ),
            )
            errors, notes = check_rst(rst)
            self.assertEqual(errors, [])
            self.assertIn("lineno-start 2", notes[0])

            bad = _write(
                root,
                "bad.rst",
                "\n".join(
                    [
                        ".. literalinclude:: sample.py",
                        "  :lines: 2-3",
                        "  :emphasize-lines: 3",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(bad)
            self.assertTrue(any("outside 1..2" in item for item in errors))

    def test_missing_code_block_language_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "no_lang.rst",
                "\n".join(
                    [
                        ".. code-block::",
                        "  :lineno-start: 1",
                        "",
                        "  x = 1",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("missing language argument" in item for item in errors))

    def test_empty_hyperlink_target_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "empty_target.rst",
                "\n".join(
                    [
                        ".. _pop method:",
                        ".. _insert: more_on_lists_",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("empty hyperlink target" in item for item in errors))

    def test_unclosed_role_backtick_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "unclosed_ref.rst",
                "* I change the expectation of the :ref:`assertion<what is an assertion?>\n",
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("unclosed role backtick" in item for item in errors))

    def test_double_backtick_role_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "double_backtick.rst",
                "* I change the expectation of the :ref:`assertion<what is an assertion?>``\n",
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("double backtick on role" in item for item in errors))

    def test_single_emphasize_blank_line_fails(self):
        with tempfile.TemporaryDirectory() as raw:
            rst = _write(
                Path(raw),
                "emp_blank.rst",
                "\n".join(
                    [
                        ".. code-block:: python",
                        "  :emphasize-lines: 2",
                        "",
                        "  line1",
                        "",
                        "  line3",
                        "",
                    ]
                ),
            )
            errors, _notes = check_rst(rst)
            self.assertTrue(any("highlights an empty/blank line" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
