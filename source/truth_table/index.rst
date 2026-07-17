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

Sometimes I want programs_ to choose what to do based on inputs or :ref:`conditions<if statements>`, and can make this happen with :ref:`if statements<if statements>`. For example

* If a person is younger than ``18``

  - the person cannot get a license.
  - the person cannot vote.

* If a person is ``18`` or older

  - and passes a test, the person can get a license.
  - and is a citizen, the person can vote.

These exercises cover writing :ref:`conditional expressions` in Python_ with the `Truth Table`_ from Mathematics_ and the :ref:`assertFalse<another way to test if something is grouped as False>` and :ref:`assertTrue methods<another way to test if something is grouped as True>`.

The operations in these chapters are fundamental to how the computer works. All operations from the `Truth Table`_ always return :ref:`False (which can be thought of as 0)<test_the_value_of_false>` or :ref:`True (which can be thought of as 1)<test_the_value_of_true>`.

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I open ``makePythonTdd.sh``

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``

* I name this project ``truth_table``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I change ``more_magic`` to ``truth_table`` in ``makePythonTdd.sh``

        .. literalinclude:: ../code/truth_table/make_tdd/makePythonTddTruthTable.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``truth_table`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I change ``more_magic`` to ``truth_table`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../code/truth_table/make_tdd/makePythonTddTruthTable.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4, 11, 19

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``truth_table`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    ______________ TestTruthTable.test_failure ________________

    self = <tests.test_truth_table.TestTruthTable testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_truth_table.py::TestTruthTable::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to open it
* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestTruthTable(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertFalse(False)


    # Exceptions seen

  the test passes.

* I close ``test_truth_table.py``

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I close ``makePythonTdd.sh``

  .. tab-item:: no WSL
    :sync: no_wsl

    * I close ``makePythonTdd.ps1``

* I open a new terminal_ then `change directory`_ to ``truth_table``

  .. code-block:: python
    :emphasize-lines: 1

    cd truth_table

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

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