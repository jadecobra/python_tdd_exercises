#!/bin/bash
NAME_OF_THE_PROJECT=$1
mkdir $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir src
touch src/$NAME_OF_THE_PROJECT.py
mkdir tests
touch tests/__init__.py

echo "import unittest


class Test$NAME_OF_THE_PROJECT(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$NAME_OF_THE_PROJECT.py
code tests/test_$NAME_OF_THE_PROJECT.py

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
echo "pytest-watcher" > requirements.txt
python3 -m pip install --requirement requirements.txt
pytest-watcher