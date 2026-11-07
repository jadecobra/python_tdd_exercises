"""Tests for autosectionlabel-aware reference validator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

# check_refs will be imported once created:
from tools.check_refs import build_target_catalog, check_refs, validate_file


class TestCheckRefs(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source_dir = self.root / "source"
        self.source_dir.mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_explicit_target_detection(self) -> None:
        doc = self.source_dir / "targets.rst"
        doc.write_text(
            ".. _explicit_target:\n"
            ".. _`spaced explicit target`:\n"
            "\n"
            "Heading\n"
            "=======\n"
        )
        catalog = build_target_catalog(self.source_dir)
        self.assertIn("explicit_target", catalog)
        self.assertIn("spaced explicit target", catalog)

    def test_heading_detection_underline(self) -> None:
        doc = self.source_dir / "heading1.rst"
        doc.write_text(
            "Introduction to Testing\n"
            "=======================\n"
            "\n"
            "Subsection Details\n"
            "------------------\n"
        )
        catalog = build_target_catalog(self.source_dir)
        self.assertIn("introduction to testing", catalog)
        self.assertIn("subsection details", catalog)

    def test_heading_detection_overline(self) -> None:
        doc = self.source_dir / "part.rst"
        doc.write_text(
            "========\n"
            "Top Part\n"
            "========\n"
        )
        catalog = build_target_catalog(self.source_dir)
        self.assertIn("top part", catalog)

    def test_heading_strips_inline_code_and_markup(self) -> None:
        doc = self.source_dir / "markup.rst"
        doc.write_text(
            "The ``assert_equal`` Method\n"
            "---------------------------\n"
        )
        catalog = build_target_catalog(self.source_dir)
        self.assertIn("the assert_equal method", catalog)

    def test_valid_simple_and_custom_title_refs(self) -> None:
        doc = self.source_dir / "valid.rst"
        doc.write_text(
            "Section Title\n"
            "=============\n"
            "\n"
            "See :ref:`Section Title`.\n"
            "See :ref:`custom link text <Section Title>`.\n"
        )
        catalog = build_target_catalog(self.source_dir)
        errors = check_refs(doc, catalog)
        self.assertEqual(errors, [])

    def test_broken_ref_reports_error_with_line_number(self) -> None:
        doc = self.source_dir / "broken.rst"
        doc.write_text(
            "Overview\n"
            "========\n"
            "\n"
            "Line 4 has :ref:`non_existent_target`.\n"
            "Line 5 has :ref:`bad text <another_bad_target>`.\n"
        )
        catalog = build_target_catalog(self.source_dir)
        errors = check_refs(doc, catalog)
        self.assertEqual(len(errors), 2)
        self.assertIn("broken.rst:4", errors[0])
        self.assertIn("non_existent_target", errors[0])
        self.assertIn("broken.rst:5", errors[1])
        self.assertIn("another_bad_target", errors[1])

    def test_validate_file_helper(self) -> None:
        doc = self.source_dir / "doc.rst"
        doc.write_text(
            "Heading\n"
            "=======\n"
            "\n"
            ":ref:`Heading`\n"
        )
        catalog = build_target_catalog(self.source_dir)
        errors = validate_file(doc, catalog)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
