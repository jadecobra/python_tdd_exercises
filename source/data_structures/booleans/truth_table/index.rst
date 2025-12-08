.. include:: ../../../links.rst

.. _truth_table:

#################################################################################
booleans: truth table
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=7_bVE9tCltIq1uBF&amp;list=PL5lANtH-CROCjQaiFJP0-XEjHfCiwgwt1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with `if statements`_. For example, If I want to know if a person can vote, the conditions could be

* Is the person alive?
* Is the person old enough?

I can add these to a program so that when it gets information about the person, it can make a decision or return output of :ref:`True<test_what_is_true>` for "Yes, they can vote" or :ref:`False<test_what_is_false>` for "No, they can not vote"

The following are exercises on writing `conditional expressions`_ in Python_ using the `Truth Table`_ from Mathematics and the assertFalse_ and assertTrue_ :ref:`methods<functions>` from :ref:`AssertionError`, :ref:`None` and :ref:`booleans`.

All operations from the `Truth Table`_ always result in :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of the chapters

.. literalinclude:: ../../../code/tests/test_truth_table.py
  :language: python
  :linenos:

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``truth_table`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh truth_table

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 truth_table

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change assertFalse_ to assertTrue_ to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertTrue(True)

* I add an `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import unittest
    import src.truth_table

* I click on :ref:`truth table: Nullary and Unary Operations` to continue to the :ref:`next chapter<truth table: Nullary and Unary Operations>`

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

* Make sure you are in the ``pumping_python`` folder_, then `change directory` to ``truth_table``

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

* Activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

* Run the automated tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

*********************************************************************************
how to run automated tests on Windows_ without WSL after you exit the tests
*********************************************************************************

.. warning:: This is ONLY for Windows_ without `Windows Subsystem for Linux`_, if you have MacOS_ or successfully installed `Windows Subsystem for Linux`_ on a Windows_ computer, skip this part

* Make sure you are in the ``pumping_python`` folder_, then `change directory` to ``truth_table``

  .. code-block:: PowerShell
    :emphasize-lines: 1

    cd truth_table

* Activate the `virtual environment`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    .venv/scripts/activate.ps1

* Run the automated tests

  .. code-block:: PowerShell
    :emphasize-lines: 1

    pytest-watch

----

:ref:`Click here for the tests and solutions from the Truth Table chapters<truth table: tests and solutions>`
