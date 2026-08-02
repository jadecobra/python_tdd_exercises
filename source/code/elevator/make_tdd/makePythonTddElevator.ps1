uv init elevator
cd elevator
New-Item "src/elevator.py"
Remove-Item "src/elevator"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestElevator(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_elevator.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now