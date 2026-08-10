param(
    [string]$ProjectName = "ProjectName"
)

# Split on underscores and convert each word to Title Case, then join with no separator
$ClassName = ($ProjectName -split '_') |
             ForEach-Object { (Get-Culture).TextInfo.ToTitleCase($_.ToLower()) } |
             Join-String -Separator ''

$ProjectName=$args[0]
uv init $ProjectName
cd $ProjectName
mkdir tests
New-Item tests/__init__.py

"import unittest


class Test$($ClassName)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions seen
# AssertionError
" | Out-File "tests/test_$ProjectName.py" -Encoding UTF8

"pytest" | Out-File requirements.txt -Encoding UTF8
"pytest-watcher" >> Out-File requirements.txt
uv add --requirement requirements.txt
uv run pytest-watcher . --now