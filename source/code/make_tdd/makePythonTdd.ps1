$PROJECT_NAME=$args[0]
mkdir $PROJECT_NAME
cd $PROJECT_NAME
mkdir src
mkdir tests
New-Item "src/$PROJECT_NAME.py"
New-Item tests/__init__.py

"import unittest


class Test$($PROJECT_NAME)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
" | Out-File "tests/test_$PROJECT_NAME.py" -Encoding UTF8

python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
"pytest-watch" | Out-File requirements.txt -Encoding UTF8
pip install --requirement requirements.txt
pytest-watch