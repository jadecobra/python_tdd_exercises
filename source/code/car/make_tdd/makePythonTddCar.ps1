uv init car
cd car
mkdir src
Move-Item "src/car/__init__.py"  "src/car.py"
Remove-Item "src/car"
mkdir tests
New-Item tests/__init__.py

"import unittest


class TestCar(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_car.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now