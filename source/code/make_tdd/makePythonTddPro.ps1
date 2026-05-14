$PROJECT_NAME=$args[0]
uv init $PROJECT_NAME
cd $PROJECT_NAME
mkdir src
Move-Item "main.py" "src/$PROJECT_NAME.py"
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($PROJECT_NAME)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$PROJECT_NAME.py" -Encoding UTF8

code src/$PROJECT_NAME.py
code tests/test_$PROJECT_NAME.py

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> Out-File requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now