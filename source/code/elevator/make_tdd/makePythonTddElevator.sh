#!/bin/bash
uv init elevator
cd elevator
mkdir src
mv src/elevator/__init__.py srcelevator.py
rm src/elevator
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestElevator(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_elevator.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now