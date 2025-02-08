.. include:: ../../links.rst

#################################################################################
booleans: truth table
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with `if statements`_.

The following chapters are exercises on writing `if statements`_ in Python using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

There are two boolean values

* :ref:`True<test_what_is_true>`
* :ref:`False<test_what_is_false>`

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

.. toctree::
  :titlesonly:

  nullary and unary operations <truth_table/01_nullary_unary_operations>
  logical conjunction <truth_table/02_logical_conjunction>
  logical disjunction <truth_table/03_logical_disjunction>
  logical implication <truth_table/04_logical_implication>
  logical equality <truth_table/05_logical_equality>
  exclusive disjunction <truth_table/06_exclusive_disjunction>
  logical nand <truth_table/07_logical_nand>
  logical nor <truth_table/08_logical_nor>
  converse non-implication <truth_table/09_converse_non_implication>
  material non-implication <truth_table/10_material_non_implication>
  negate <truth_table/11_negate>
  project <truth_table/12_project>
  converse implication <truth_table/13_converse_implication>
  true lies <truth_table/14_true_lies>

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
