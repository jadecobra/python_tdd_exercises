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

Programming allows us to gain from solutions to problems that we or other people come up with, in the form of packages and modules, they have to be imported to be used.

A Python :ref:`module<ModuleNotFoundError>` is a file that ends in ``.py``, a package is a directory that has an ``__init__.py``. The ``ModuleNotFoundError`` is raised when Python tries to import a module that does not exist or it cannot find the module from an `import statement`_.

This exercise will help you remember how to solve the ``ModuleNotFoundError`` and what a Python module is.

*********************************************************************************
requirements
*********************************************************************************


:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

----

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

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_module_not_found_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_module_not_found_error.py:7`` with the mouse to open it in the editor, then change ``test_failure`` to ``test_module_not_found_error``

  .. code-block:: python

  import unittest


  class TestModuleNotFoundError(unittest.TestCase):

      def test_module_not_found_error(self):
          import src.module_0

  and the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_0'

  - ``ModuleNotFoundError`` is raised when an `import statement`_ fails because python cannot find a module/package with the given name, in this case ``module_0`` does not exist
  - ``import module_0`` is the line of code that caused the failure

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

  If you want more information about imports you can read `The Import Statement <https://docs.python.org/3/reference/simple_stmts.html#import>`_

green: make it pass
#################################################################################

* I make ``module_0.py`` in the ``src`` folder and the terminal shows a passing test
* then add another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_0
        import src.module_1

  which gives me

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module_1'

* When I add ``module_1.py`` to the ``src`` folder, the terminal shows a passing test
* I continue with another `import statement`

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_0
        import src.module_1
        import src.module_2

  and get

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_2'

* I add ``module_2.py`` to the ``src`` folder, and the terminal shows green again
* after another `import statement`_

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_0
        import src.module_1
        import src.module_2
        import src.module_3

  the terminal shows

  .. code-block:: python

    ModuleNotFoundError: No module called 'src.module_3'

* I add ``module_3.py`` to the ``src`` folder and the test passes

----

*********************************************************************************
review
*********************************************************************************

I ran a test for the :ref:`ModuleNotFoundError` and Python modules

----

:doc:`/code/code_exception_handling`