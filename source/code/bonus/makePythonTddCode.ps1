$NAME_OF_THE_PROJECT=$args[0]
mkdir $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir src
New-Item "src/$NAME_OF_THE_PROJECT.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($NAME_OF_THE_PROJECT)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$NAME_OF_THE_PROJECT.py" -Encoding UTF8
code tests/test_$NAME_OF_THE_PROJECT.py

python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
"pytest-watcher" | Out-File requirements.txt -Encoding UTF8
python -m pip install --requirement requirements.txt
pytest-watcher