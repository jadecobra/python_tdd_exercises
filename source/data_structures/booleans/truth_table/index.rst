.. include:: ../../../links.rst

.. _truth_table:

#################################################################################
truth table
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=7_bVE9tCltIq1uBF&amp;list=PL5lANtH-CROCjQaiFJP0-XEjHfCiwgwt1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

Sometimes I want programs to make decisions based on inputs or conditions, and can make this happen with :ref:`if statement<if statements>`. For example, If I want to know if a person can vote, the conditions could be

* Is the person alive?
* Is the person old enough?

I can add these to a program so that when it gets information about the person, it can make a decision or return output of :ref:`True<test_what_is_true>` for "Yes, they can vote" or :ref:`False<test_what_is_false>` for "No, they can not vote"

The following are exercises on writing `conditional expressions`_ in Python_ using the `Truth Table`_ from Mathematics and the assertFalse_ and assertTrue_ :ref:`methods<what is a function?>` from :ref:`AssertionError<what causes AssertionError?>`, :ref:`None<what is None?>` and :ref:`booleans<what are booleans?>`.

All operations from the `Truth Table`_ always result in :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

Here are the tests I have at the end of the chapters

.. literalinclude:: ../../../code/tests/test_truth_table.py
  :language: python
  :linenos:

*********************************************************************************
questions about The Truth Table
*********************************************************************************

* :ref:`what is not?<test_logical_negation>`
* :ref:`what is and?<test_logical_conjunction>`
* :ref:`what is or?<test_logical_disjunction>`
* :ref:`what is an if statement<if statements>`
* :ref:`what is a conditional expression?<conditional expressions>`
* :ref:`what is a ternary operator?<conditional expressions>`
* What are the possible combinations of two inputs?

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``truth_table``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir truth_table

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

  the terminal_ shows I am in the ``truth_table`` folder_

  .. code-block:: shell

    .../pumping_python/truth_table

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/truth_table

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/truth_table.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/truth_table.py`` instead of ``touch src/truth_table.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/truth_table.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/truth_table

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_truth_table.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_truth_table.py`` instead of ``touch tests/test_truth_table.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_truth_table.py

  the terminal_ goes back to the command line

* I open ``test_truth_table.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can use the terminal_ to open a file_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_. That means when I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_truth_table.py

    `Visual Studio Code`_ opens ``test_truth_table.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestTruthTable(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest\npytest-watcher" > requirements.txt

  the terminal_ goes back to the command line

* I setup the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `truth_table`
    .../pumping_python/truth_table (main)

  I remove ``main.py`` from the project

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I install the Python packages listed in the requirements file

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now  .

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _____________________ TestTruthTable.test_failure ________________________

    self = <tests.test_truth_table.TestTruthTable testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_truth_table.py:7: AssertionError
    ========================= short test summary info ==========================
    FAILED tests/test_truth_table.py::TestTruthTable::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_truth_table.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

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

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I add an `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import unittest
    import src.truth_table

* :ref:`Click Here to continue to Nullary and Unary Operations<truth table: Nullary and Unary Operations>`

----

*********************************************************************************
truth table operations
*********************************************************************************

.. toctree::
  :titlesonly:

  Nullary and Unary<01_nullary_unary_operations>
  Binary Operations 1<02_binary_operations_1>
  Binary Operations 2<03_binary_operations_2>
  Binary Operations 3<04_binary_operations_3>
  Binary Operations 4<05_binary_operations_4>
  Truth Table Test<test_truth_table_tests>

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Continue in Nullary and Unary Operations?<truth table: Nullary and Unary Operations>`