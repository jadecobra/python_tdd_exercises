#!/bin/bash
if [ -z "$1" ] ; then
    PROJECT_NAME="PROJECT_NAME"
else
    PROJECT_NAME=$1
fi

# Split on underscores and convert each word to Title Case,
# then join with no separator
IFS='_' read -r -a words <<< "$PROJECT_NAME"
IFS=''
CLASS_NAME="${words[*]^}"

uv init $PROJECT_NAME
cd $PROJECT_NAME
mkdir tests
touch tests/__init__.py

echo "import unittest


class Test$CLASS_NAME(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$PROJECT_NAME.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now