$PROJECT_NAME=$args[0]
mkdir $PROJECT_NAME
cd $PROJECT_NAME
mkdir src tests
New-Item "src/$PROJECT_NAME.py"
New-Item tests/__init__.py

@"
import unittest


class Test$($PROJECT_NAME)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
"@ > "tests/test_$PROJECT_NAME.py"

python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
"pytest-watch" > requirements.txt
python -m pip install --requirement requirements.txt
pytest-watch