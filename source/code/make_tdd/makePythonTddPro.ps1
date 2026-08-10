param(
    [string]$PROJECT_NAME = "PROJECT_NAME"
)

# Split on underscores and convert each word to Title Case,
# then join with no separator
$CLASS_NAME = ($PROJECT_NAME -split '_') |
             ForEach-Object { (Get-Culture).TextInfo.ToTitleCase($_.ToLower()) } |
             Join-String -Separator ''

$PROJECT_NAME=$args[0]
uv init $PROJECT_NAME
cd $PROJECT_NAME
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($CLASS_NAME)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$PROJECT_NAME.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> Out-File requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now