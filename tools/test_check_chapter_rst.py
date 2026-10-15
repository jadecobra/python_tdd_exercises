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


if __name__ == "__main__":
    unittest.main()
