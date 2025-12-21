mkdir more_magic
cd more_magic
mkdir src
New-Item "src/more_magic.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestMoreMagic(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
" | Out-File "tests/test_more_magic.py" -Encoding UTF8

python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
"pytest-watch" | Out-File requirements.txt -Encoding UTF8
python -m pip install --requirement requirements.txt
pytest-watch