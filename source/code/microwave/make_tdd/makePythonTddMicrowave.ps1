uv init microwave
cd microwave
mkdir src
Move-Item "main.py" "src/microwave.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestMicrowave(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_microwave.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now