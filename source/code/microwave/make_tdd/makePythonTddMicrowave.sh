#!/bin/bash
uv init atm
cd atm
mkdir src
mv main.py src/atm.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestATM(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_atm.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now