#!/bin/bash
if [ -z "$1" ] ; then
    NAME_OF_THE_PROJECT="NAME_OF_THE_PROJECT"
else
    NAME_OF_THE_PROJECT=$1
fi

# Split on underscores and convert each word to Title Case,
# then join with no separator
IFS='_' read -r -a words <<< "$NAME_OF_THE_PROJECT"
IFS=''
CLASS_NAME="${words[*]^}"

uv init $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir tests
touch tests/__init__.py

echo "import unittest


class Test$CLASS_NAME(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$NAME_OF_THE_PROJECT.py

echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now