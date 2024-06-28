#!/bin/bash
PROJECT_NAME=$1
mkdir --parents $PROJECT_NAME/tests
cd $PROJECT_NAME
touch $PROJECT_NAME.py tests/__init__.py

cat << DELIMITER > tests/test_$PROJECT_NAME.py
import unittest


class Test$PROJECT_NAME(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
DELIMITER

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
echo "pytest-watch" > requirements.txt
pip install --requirement requirements.txt
pytest-watch