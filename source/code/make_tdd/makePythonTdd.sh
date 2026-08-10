#!/bin/bash
PROJECT_NAME=$1
uv init $PROJECT_NAME
cd $PROJECT_NAME
mkdir tests
touch tests/__init__.py

echo "import unittest


class Test$PROJECT_NAME(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$PROJECT_NAME.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now