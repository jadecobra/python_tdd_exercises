.. meta::
  :description: Truth Table in Python for absolute beginners using Test Driven Development. Start the truth_table project manually with uv init, mkdir src/tests, tests/__init__.py, pytest-watcher, and the first failing test_failure (self.assertFalse(True) → AssertionError True is not false). Preview the full test suite for Nullary Operations (logical_true, logical_false — no inputs, always True/False), Unary Operations (logical_identity returns input, logical_negation/NOT returns opposite via not keyword), and all 16 Binary Operations (contradiction, AND/logical_conjunction, OR/logical_disjunction, NAND, NOR, XOR/exclusive_disjunction, material implication, project_first/second, negate_first/second, tautology, and more). Reuses assertTrue and assertFalse from the booleans chapter; builds conditional logic and if-statement foundations; every truth-table operation returns only True or False (1 or 0). Continue through Nullary and Unary Operations, Binary Operations 1–4, optional examples (BO5), the blank-file test_truth_table_tests challenge, and real-world projects. Red-Green-Refactor with AttributeError module has no attribute, TypeError takes N positional arguments, AssertionError None is not true. Part of Jacob Itegboje Pumping Python TDD series.
  :keywords: Jacob Itegboje, Pumping Python, truth table python, python truth table tutorial, uv init truth_table, pytest-watcher, test_failure assertFalse, AssertionError True is not false, AssertionError None is not true, AttributeError module has no attribute logical_true, TypeError takes 0 positional arguments but 1 was given, assertTrue assertFalse booleans chapter, logical_true logical_false nullary operations, logical_identity logical_negation not keyword, logical_conjunction AND, logical_disjunction OR, logical_nand logical_nor XOR exclusive_disjunction, material implication python, 16 binary operations truth table, conditional expressions if statements python, TDD red green refactor truth table, python boolean logic beginners, truth table always returns True or False, test_nullary_unary.py test_binary.py, test_truth_table_tests challenge, beginner programming logic gates

.. include:: ../links.rst

.. _truth_table:

#################################################################################
truth table
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=7_bVE9tCltIq1uBF&amp;list=PL5lANtH-CROCjQaiFJP0-XEjHfCiwgwt1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Sometimes I want programs_ to choose what to do based on inputs or :ref:`conditions<if statements>`, and can make this happen with :ref:`if statements<if statements>`. For example, If I want to know if a person can vote, the inputs could be

* Is the person alive?
* Is the person old enough?
* Is the person a citizen?

I can add these to a program so that when it gets information about the person it returns  :ref:`True<test_what_is_true>` for "Yes, they can vote" or :ref:`False<test_what_is_false>` for "No, they can NOT vote".

These are exercises on writing :ref:`conditional expressions` in Python_ with the `Truth Table`_ from Mathematics_ and the :ref:`assertFalse<another way to test if something is grouped as False>` and :ref:`assertTrue methods<another way to test if something is grouped as True>` from :ref:`booleans<what are booleans?>`.

The operations in these chapters are fundamental to how the computer works. All operations from the `Truth Table`_ always return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` which can also be thought of as ``1`` or ``0``.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapters

.. literalinclude:: ../code/truth_table/tests/test_nullary_unary.py
  :language: python
  :linenos:

.. literalinclude:: ../code/truth_table/tests/test_binary.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``truth_table``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init truth_table

  the terminal_ shows

  .. code-block:: shell

    Initialized project `truth_table`
    at `.../pumping_python/truth_table`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

  the terminal_ shows I am in the ``truth_table`` folder_

  .. code-block:: shell

    .../pumping_python/truth_table

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``truth_table.py`` and move it to the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py src/truth_table.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py src/truth_table.py

  the terminal_ goes back to the command line.

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_truth_table.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_truth_table.py

  the terminal_ goes back to the command line.

* I open ``test_truth_table.py``

* I add :ref:`the first failing test<test_failure>` to ``test_truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestTruthTable(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line.

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line.

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed `pytest-watcher`_ and its dependencies.

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    _____________ TestTruthTable.test_failure ________________

    self = <tests.test_truth_table.TestTruthTable testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_truth_table.py::TestTruthTable::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`.

  .. admonition:: if the terminal_ does not show the same error, then check if

    * your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestTruthTable(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.truth_table
    import unittest

* :ref:`Click Here to continue to Nullary and Unary Operations<truth table: Nullary and Unary Operations>`

----

*********************************************************************************
truth table operations
*********************************************************************************

.. toctree::
  :titlesonly:

  Nullary and Unary<nullary_unary_operations>
  Binary Operations<binary_operations/index>
  Truth Table Test<test_truth_table_tests>
  Truth Table Projects<projects/index>

:ref:`Do you want to see all the CODE for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Nullary and Unary Operations<truth table: Nullary and Unary Operations>`