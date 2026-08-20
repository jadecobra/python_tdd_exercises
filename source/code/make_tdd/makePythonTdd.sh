#!/bin/bash
NAME_OF_THE_PROJECT=$1
uv init $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir tests
touch tests/__init__.py

echo "import unittest


class Test$NAME_OF_THE_PROJECT(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$NAME_OF_THE_PROJECT.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now