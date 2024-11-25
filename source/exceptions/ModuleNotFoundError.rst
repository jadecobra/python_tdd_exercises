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

A Python Module is a file that ends in ``.py`` or a directory that has an ``__init__.py``. This exercise will help you remember how to solve the ``ModuleNotFoundError`` and what a Python module is.

The ``ModuleNotFoundError`` is raised when Python tries to import a module that does not exist or it cannot find the module from an `import statement`_.

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
* I repeat this pattern until ``module_99.py``

  .. code-block:: python

    def test_module_not_found_error(self):
        import src.module_0
        import src.module_1
        import src.module_2
        import src.module_3
        import src.module_4
        import src.module_5
        import src.module_6
        import src.module_7
        import src.module_8
        import src.module_9
        import src.module_10
        import src.module_11
        import src.module_12
        import src.module_13
        import src.module_14
        import src.module_15
        import src.module_16
        import src.module_17
        import src.module_18
        import src.module_19
        import src.module_20
        import src.module_21
        import src.module_22
        import src.module_23
        import src.module_24
        import src.module_25
        import src.module_26
        import src.module_27
        import src.module_28
        import src.module_29
        import src.module_30
        import src.module_34
        import src.module_32
        import src.module_33
        import src.module_34
        import src.module_35
        import src.module_36
        import src.module_37
        import src.module_38
        import src.module_39
        import src.module_40
        import src.module_41
        import src.module_42
        import src.module_43
        import src.module_44
        import src.module_45
        import src.module_46
        import src.module_47
        import src.module_48
        import src.module_49
        import src.module_50
        import src.module_51
        import src.module_52
        import src.module_53
        import src.module_54
        import src.module_55
        import src.module_56
        import src.module_57
        import src.module_58
        import src.module_59
        import src.module_60
        import src.module_61
        import src.module_62
        import src.module_63
        import src.module_64
        import src.module_65
        import src.module_66
        import src.module_67
        import src.module_68
        import src.module_69
        import src.module_70
        import src.module_71
        import src.module_72
        import src.module_73
        import src.module_74
        import src.module_75
        import src.module_76
        import src.module_77
        import src.module_78
        import src.module_79
        import src.module_80
        import src.module_81
        import src.module_82
        import src.module_83
        import src.module_84
        import src.module_85
        import src.module_86
        import src.module_87
        import src.module_88
        import src.module_89
        import src.module_90
        import src.module_91
        import src.module_92
        import src.module_93
        import src.module_94
        import src.module_95
        import src.module_96
        import src.module_97
        import src.module_98
        import src.module_99

  and make the ``.py`` files to make the test pass

----

*********************************************************************************
review
*********************************************************************************

I ran a test for the :ref:`ModuleNotFoundError` and Python modules

----

:doc:`/code/code_exception_handling`