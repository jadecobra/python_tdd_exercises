#!/bin/bash
uv init more_magic
cd more_magic
mkdir src
mv main.py src/more_magic.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestMoreMagic(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_more_magic.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now