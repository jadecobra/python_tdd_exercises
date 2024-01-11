
#############################################################
Automatically Create a Test Driven Development Environment
#############################################################

* Here is the ``./createPythonTdd.sh`` script from :doc:`/how_to/create_tdd_environment`

  .. code-block:: shell

    PROJECT_NAME=$1
    mkdir -p $PROJECT_NAME/tests
    cd $PROJECT_NAME
    touch $PROJECT_NAME.py
    touch tests/__init__.py

    cat << DELIMITER > tests/test_$PROJECT_NAME.py
    import unittest


    class Test$PROJECT_NAME(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)
    DELIMITER

    echo "pytest-watch" > requirements.txt

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install --requirement requirements.txt
    pytest-watch

* use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x createPythonTdd.sh

* give a name for the ``$PROJECT_NAME`` variable when the program is called to setup a Test Driven Development on demand. for example typing this command in the terminal in the folder where ``createPythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./createPythonTdd.sh calculator

* Here is the ``./createPythonTdd.ps1`` script from :doc:`/how_to/create_tdd_environment`

  .. code-block:: shell

    $projectName=$args[0]
    mkdir -p $projectName/tests
    Set-Location $projectName

    New-Item "$projectName.py"
    New-Item tests/__init__.py
    $testSetup = @"
    import unittest

    class Test$($projectName)(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(False)
    "@
    $testSetup |  Out-File $("tests/test_$($projectName).py") -Encoding UTF8

    python -m venv .venv
    .venv/scripts/activate
    pip install --upgrade pip
    pip install pytest-watch
    pytest-watch