.. include:: ../links.rst

.. _ModuleNotFoundError:

#################################################################################
ModuleNotFoundError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

Programming allows us to gain from solutions to problems that we or other people come up with, in the form of modules or packages, that can be imported to be used.

A Python :ref:`module<ModuleNotFoundError>` is a file that ends in ``.py``. The ``ModuleNotFoundError`` is raised when Python cannot find a module that is in an `import statement`_.

*********************************************************************************
test_module_not_found_error
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``module_not_found_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh module_not_found_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 module_not_found_error

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_module_not_found_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_module_not_found_error.py:7`` with the mouse to open it in the editor, then change ``test_failure`` to ``test_module_not_found_error``

  .. code-block:: python

  import unittest


  class TestModuleNotFoundError(unittest.TestCase):

      def test_module_not_found_error(self):
          import src.module_00

  and the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_00'

  - ``ModuleNotFoundError`` is raised when an `import statement`_ fails because python cannot find a module/package with the name, in this case ``module_00`` does not exist
  - ``import module_00`` is the line of code that caused the failure

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

  If you want more information about imports you can read `The Import Statement <https://docs.python.org/3/reference/simple_stmts.html#import>`_

green: make it pass
#################################################################################

* I rename ``module_not_found_error.py`` in the ``src`` folder to ``module_00.py`` and the terminal shows a passing test
* then I add another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01

  which gives me

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_01'

* When I add ``module_01.py`` to the ``src`` folder, the terminal shows a passing test
* I continue with another `import statement`

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02

  and get

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_02'

* I add ``module_02.py`` to the ``src`` folder, and the terminal shows green again
* after another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02
        import src.module_03

  the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_03'

* I add the file to the ``src`` folder and the test passes

----

*********************************************************************************
review
*********************************************************************************

You can keep going and do this as a drill up to ``src.module_99`` if you want and you would have done this exercise 100 times, which would make you very familiar with it. I ran a test for the :ref:`ModuleNotFoundError` and Python modules. Would you like to test the :ref:`AssertionError`?

----

:doc:`/code/code_exception_handling`