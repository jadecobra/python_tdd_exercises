#!/bin/bash
uv init microwave
cd microwave
mkdir src
mv main.py src/microwave.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestMicrowave(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_microwave.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now