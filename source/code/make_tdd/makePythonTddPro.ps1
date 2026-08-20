param(
    [string]$NAME_OF_THE_PROJECT = "NAME_OF_THE_PROJECT"
)

# Split on underscores and convert each word to Title Case,
# then join with no separator
$CLASS_NAME = ($NAME_OF_THE_PROJECT -split '_') |
             ForEach-Object { (Get-Culture).TextInfo.ToTitleCase($_.ToLower()) } |
             Join-String -Separator ''

$NAME_OF_THE_PROJECT=$args[0]
uv init $NAME_OF_THE_PROJECT
cd $NAME_OF_THE_PROJECT
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($CLASS_NAME)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$NAME_OF_THE_PROJECT.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> Out-File requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now