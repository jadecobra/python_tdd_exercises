#!/bin/bash
uv init traffic_light
cd traffic_light
touch src/traffic_light.py
rmdir src/traffic_light
mkdir tests
touch tests/__init__.py

echo "import unittest


class TestTrafficLight(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_traffic_light.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now