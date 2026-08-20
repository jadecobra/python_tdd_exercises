$NAME_OF_THE_PROJECT="pro_magic"
uv init $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($NAME_OF_THE_PROJECT)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$NAME_OF_THE_PROJECT.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now