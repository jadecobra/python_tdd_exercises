#!/bin/bash
if [ -z "$1" ] ; then
    PROJECT_NAME="PROJECT_NAME"
else
    PROJECT_NAME=$1
fi

IFS='_' read -r -a words <<< "$PROJECT_NAME"
IFS=''
CLASS_NAME="${words[*]^}"

mkdir -p $PROJECT_NAME/{src,tests}
cd $PROJECT_NAME
touch src/$PROJECT_NAME.py tests/__init__.py

echo "import unittest


class Test$CLASS_NAME(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" > tests/test_$PROJECT_NAME.py

code src/$PROJECT_NAME.py
code tests/test_$PROJECT_NAME.py

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
echo "pytest-watch" > requirements.txt
python3 -m pip install --requirement requirements.txt
pytest-watch