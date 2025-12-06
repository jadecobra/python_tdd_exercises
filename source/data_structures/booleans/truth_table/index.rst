.. include:: ../../../links.rst

.. _truth_table:

#################################################################################
booleans: truth table
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=7_bVE9tCltIq1uBF&amp;list=PL5lANtH-CROCjQaiFJP0-XEjHfCiwgwt1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with `if statements`_.

These are exercises on writing `conditional expressions`_ in Python_ using the `Truth Table`_ from Mathematics

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``truth_table`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh truth_table

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 truth_table

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError

* I hold ``ctrl`` (Windows/Linux) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass
* I add an `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import unittest
    import src.truth_table

* then I continue in :ref:`truth table: Nullary and Unary Operations`

----

*********************************************************************************
truth table operations
*********************************************************************************

.. toctree::
  :maxdepth: 2
  :titlesonly:

  01_nullary_unary_operations
  02_binary_operations_1
  03_binary_operations_2
  04_binary_operations_3
  05_binary_operations_4
  test_truth_table_tests

----

*********************************************************************************
how to run automated tests after you exit the tests
*********************************************************************************

.. code-block:: shell

  cd truth_table
  source .venv/bin/activate
  pytest-watch

*********************************************************************************
how to run automated tests on Windows_ without WSL after you exit the tests
*********************************************************************************

.. warning:: This is for Windows_ without `Windows Subsystem Linux`_

.. code-block:: shell

  cd truth_table
  .venv/scripts/activate.ps1
  pytest-watch

----

:ref:`truth table: tests and solutions`
