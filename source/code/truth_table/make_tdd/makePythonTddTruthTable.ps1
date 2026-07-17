uv init truth_table
cd truth_table
mkdir src
Move-Item "main.py" "src/truth_table.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestTruthTable(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_truth_table.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now