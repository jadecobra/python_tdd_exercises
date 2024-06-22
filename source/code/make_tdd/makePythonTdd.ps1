$projectName=$args[0]
mkdir -p $projectName/tests
Set-Location $projectName
New-Item "$projectName.py"
New-Item tests/__init__.py

$testCode = @"
import unittest


class Test$($projectName)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
"@
$testCode |  Out-File "tests/test_$projectName.py"

"pytest-watch" | Out-File requirements.txt
python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
python -m pip install --requirement requirements.txt
pytest-watch