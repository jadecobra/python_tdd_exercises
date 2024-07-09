$projectName=$args[0]
mkdir $projectName
cd $projectName
mkdir src tests
New-Item "src/$projectName.py"
New-Item tests/__init__.py

@"
import unittest


class Test$($projectName)(unittest.TestCase):

    def test_failure(self):
        self.assertFalse(True)


# Exceptions Encountered
# AssertionError
"@ > "tests/test_$projectName.py"

python -m venv .venv
.venv/scripts/activate.ps1
python -m pip install --upgrade pip
Write-Output pytest-watch > requirements.txt
python -m pip install --requirement requirements.txt
pytest-watch