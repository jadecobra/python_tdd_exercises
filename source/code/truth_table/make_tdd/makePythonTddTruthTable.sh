#!/bin/bash
uv init truth_table
cd truth_table
mkdir src
mv main.py src/truth_table.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestTruthTable(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_truth_table.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now