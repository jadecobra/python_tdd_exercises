uv init atm
cd atm
mkdir src
Move-Item "main.py" "src/atm.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestATM(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_atm.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now