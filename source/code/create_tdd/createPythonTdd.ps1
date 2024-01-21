$projectName=$args[0]
mkdir -p $projectName/tests
Set-Location $projectName

New-Item "$projectName.py"
New-Item tests/__init__.py

$testSetup = @"
import unittest


class Test$($projectName)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)
"@
$testSetup |  Out-File $("tests/test_$($projectName).py") -Encoding UTF8

python -m venv .venv
.venv/scripts/activate
python -m pip install --upgrade pip
python -m pip install pytest-watch
pytest-watch