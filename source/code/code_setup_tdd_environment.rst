
Automatically Setup a Test Driven Development Environment
==========================================================

* Here is the ``./setupPythonTdd.sh`` script from :doc:`/setup_tdd_environment`

  .. code-block:: shell
    :linenos:

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

* I use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x setupPythonTdd.sh

* I can now create a Test Driven Development environment on demand by giving a name for the ``{PROJECT_NAME}`` variable when the program is called. for example typing this command in the terminal in the folder where ``setupPythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./setupPythonTdd.sh calculator