#!/bin/bash
uv init car
cd car
mkdir src
mv src/car/__init__.py srccar.py
rm src/car
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestCar(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_car.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now