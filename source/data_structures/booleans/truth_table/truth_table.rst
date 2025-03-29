.. include:: ../../links.rst

#################################################################################
booleans: truth table
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with `if statements`_.

These are exercises on writing `conditional expressions`_ in Python using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ from Mathematics

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``truth_table`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh truth_table

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 truth_table

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* I add an `import statement`_

  .. code-block:: python

    import unittest
    import src.truth_table

*********************************************************************************
Operations
*********************************************************************************

.. toctree::
  :maxdepth: 2
  :titlesonly:

  truth_table/01_nullary_unary_operations
  truth_table/02_binary_operations_i
  truth_table/03_binary_operations_ii
  truth_table/04_binary_operations_iii
  truth_table/05_binary_operations_iv

----

*********************************************************************************
how to run automated tests if you exit
*********************************************************************************

.. code-block:: shell

  cd truth_table
  source .venv/bin/activate
  pytest-watch

*********************************************************************************
how to run automated tests on Windows_ without WSL if you exit
*********************************************************************************

.. warning:: This is for Windows_ without `Windows Subsystem Linux`_

.. code-block:: shell

  cd truth_table
  .venv/scripts/activate.ps1
  pytest-watch

----

:doc:`/code/code_truth_table`
