.. include:: ../../links.rst

#################################################################################
booleans: truth table
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with `if statements`_.

These are exercises on writing `conditional expressions`_ in Python using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

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

Here are the tests

* :ref:`test_logical_true`
* :ref:`test_logical_false`
* :ref:`test_logical_identity`
* :ref:`test_logical_negation_aka_not`
* :ref:`test_logical_conjunction`
* :ref:`test_logical_disjunction`
* :ref:`test_logical_implication`
* :ref:`test_logical_equality_or_logical_biconditional`
* :ref:`test_exclusive_disjunction`
* :ref:`test_logical_nand`
* :ref:`test_logical_nor`
* :ref:`test_converse_non_implication`
* :ref:`test_material_non_implication`
* :ref:`test_negate`
* :ref:`test_project`
* :ref:`test_converse_implication`
* :ref:`test_true_lies`

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
