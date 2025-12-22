#!/bin/bash
mkdir more_magic
cd more_magic
mkdir src
touch src/more_magic.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestMoreMagic(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_more_magic.py

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
echo "pytest-watch" > requirements.txt
python3 -m pip install --requirement requirements.txt
pytest-watch