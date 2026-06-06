.. meta::
  :description: Step-by-step beginner Python TDD tutorial that teaches AssertionError by deliberately triggering it. See exactly why a bare `reality == my_expectation` line does not fail the test or raise an error (Python just evaluates it and continues), and how `assert` turns a false result into AssertionError. Understand the real error messages beginners hit: "AssertionError: True is not false", "unexpectedly identical: None", "AssertionError: 0 is not 0.0", "assert 0 != 0.0", and "AssertionError: 0 == 0.0". Master the difference between `=` (assignment) and `==` (equality), and especially `is` / `is not` (same object / identity) versus `==` / `!=` (value equality). Extensive practical examples testing None, True, False, 0 vs 0.0, strings, lists, dicts, sets and tuples using both the bare `assert` statement and unittest.TestCase methods (assertIs, assertIsNot, assertEqual, assertNotEqual). Full project setup with `uv init`, proper `tests/__init__.py` package, `uv add` for pytest + pytest-watcher, running via `uv run pytest-watcher . --now`, small git commits after every change, and the complete red-green-refactor cycle. Perfect for absolute beginners learning Python testing, None/True/False identity gotchas, why 0 == 0.0 is True but 0 is not 0.0, and how assertions actually control test outcomes.
  :keywords: Jacob Itegboje, Pumping Python, python assertionerror, AssertionError python, what causes AssertionError in python, python assert statement, assert statement python for beginners, how does assert work python, python assert tutorial, TDD for beginners python, red green refactor python, red green refactor cycle, uv pytest-watcher, pytest-watcher uv, uv run pytest-watcher . --now, python unittest beginners, difference between = and == python, assignment vs equality python, python is vs ==, object identity vs value equality python, python is not vs !=, is None vs == None python, python None identity, python is not None, assertIsNot None, unittest assertIs, assertIs vs is python, unexpectedly identical None, AssertionError unexpectedly identical, AssertionError True is not false, True is not false python, assert 0 is 0.0, 0 is not 0.0 python, why is 0 == 0.0 but 0 is not 0.0, 0 == 0.0 is True python, python 0 is not False, an integer is not False, python 0 is not True, testing None True False python, bare comparison does not fail test, reality == my_expectation still green, why doesn't == fail my python test, python assert makes test fail, python assert "DO NOT CONTINUE if false", setting up tests directory python, tests __init__.py python, python tests package structure, common python beginner AssertionError, AssertionError 0 == 0.0, assert 0 != 0.0, unittest assertEqual beginners, mixing assert and self.assertEqual, python tdd None, python singleton is, python falsy is not False, a list is not None, a dict is not False, python test driven development assert, how to cause AssertionError, python assertions expectations vs reality, what is an assertion python, common python test gotchas None True False, python 0 == 0.0 identity equality, python why does my test not fail when I write ==, python bare expression vs assert, python assert turns false into error, python tdd uv init, pytest-watcher with unittest, python None is not False, True is not None test, 0.0 is not False python, dictionary is not None, how to write failing test first TDD, common mistakes is vs equal python, AssertionError assert 11 == 2, E assert None is not None, python expectations vs reality testing, what is the same what is different python test

.. include:: ../../links.rst

.. _assert: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
.. _assert statement: assert_
.. _assertion: assert_
.. _assertions: assert_
.. _assert statements: assert_
.. _AssertionError: https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError
.. _unittest.TestCase.assertEqual: assertEqual_
.. _unittest.TestCase.assertNotEqual: assertNotEqual_
.. _assertEqual: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
.. _assertEqual method: assertEqual_
.. _assertNotEqual: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
.. _assertIs: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs
.. _assertIs method: assertIs_
.. _assertIsNot: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot
.. _assertIsNot method: assertIsNot_
.. _assertNotEqual method: assertNotEqual_

#################################################################################
what is an assertion?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

An :ref:`assertion<what is an assertion?>` or `assert statement`_ is a way for me to tell Python_, "DO NOT CONTINUE, if this statement is False", or said a different way "GO TO THE NEXT LINE, ONLY if this statement is True".

I use assertions_ in tests when making a program_ to make sure something is :ref:`True<test_what_is_true>` about the program_ before I continue building or to test ideas and see if they work, without worrying about if I will remember the ideas later.

I use them to test how the program_ behaves, for example when it is given inputs. Assertions_ can help catch things that make tests that were passing, start failing if I add new lines of code. They help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations (tests and ideas) and reality (what happens if the program_ runs), tells me what to change to make them match. The closer my program_ is to reality, the better.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about AssertionError
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is an assertion?<what is an assertion?>`
* :ref:`what is a variable?<what is a variable?>`
* :ref:`what causes AssertionError?<what causes AssertionError?>`
* :ref:`how can I test if something is NOT the same object as None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is the same object as None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is the same object as False?<test_assertion_error_w_false>`
* :ref:`how can I test if something is NOT the same object as False?<test_assertion_error_w_false>`
* :ref:`how can I test if something is the same object as True?<test_assertion_error_w_true>`
* :ref:`how can I test if something is NOT the same object as True?<test_assertion_error_w_true>`
* :ref:`how can I test if two things are not equal?<test_assertion_error_w_equality>`
* :ref:`how can I test if two things are equal?<test_assertion_error_w_equality>`
* :ref:`what is another way to test if something is the same object as None?<another way to test if something is the same object as None>`
* :ref:`what is another way to test if something is NOT the same object as None?<another way to test if something is NOT the same object as None>`
* :ref:`what is another way to test if something is the same object as False?<another way to test if something is the same object as False>`
* :ref:`what is another way to test if something is NOT the same object as False?<another way to test if something is NOT the same object as False>`
* :ref:`what is another way to test if something is the same object as True?<another way to test if something is the same object as True>`
* :ref:`what is another way to test if something is NOT the same object as True?<another way to test if something is NOT the same object as True>`
* :ref:`what is another way to test if two things are not equal?<another way to test if two things are not equal>`
* :ref:`what is another way to test if two things are equal?<another way to test if two things are equal>`
* :ref:`what is the difference between is and equal<test_assertion_error_w_is_vs_equal>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``assertion_error``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init assertion_error

  the terminal_ shows

  .. code-block:: shell

    Initialized project `assertion-error`
    at `.../pumping_python/assertion_error`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I `make a directory`_ for the tests

  .. code-block:: python
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

* I use the `mv program`_ to change the name of ``main.py`` to ``test_assertion_error.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_assertion_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_assertion_error.py

  the terminal_ goes back to the command line.

* I open ``test_assertion_error.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_


* I delete the text then add :ref:`the first failing test<test_failure>` to ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" > requirements.txt

  the terminal_ goes back to the command line.

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'setup project'

  the terminal_ shows

  .. code-block:: python

    [main (root-commit) a0b12c3] setup project
     8 files changed, 142 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .python-version
     create mode 100644 README.md
     create mode 100644 pyproject.toml
     create mode 100644 requirements.txt
     create mode 100644 tests/__init__.py
     create mode 100644 tests/test_assertion_error.py
     create mode 100644 uv.lock

  then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    ____________ TestAssertionError.test_failure _____________

    self = <tests.test_assertion_error.TestAssertionError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_assertion_error.py::TestAssertionError::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(False)


    # Exceptions seen
    # AssertionError

  the test passes.

----

*********************************************************************************
what is a variable?
*********************************************************************************

A variable is a name that is used for values that change. For example, in Mathematics_ we use ``x`` to represent any number.

I can use variables to remove repetition of values that change so that if I have to change a value, I only have to make the change in one place instead of many.


----

*********************************************************************************
test_what_is_an_assertion
*********************************************************************************

We know that the result of ``1 + 1`` is ``2``. What if I said that ``'1' + '1'`` is ``'11'``, would you agree?

I can use :ref:`assertions<what is an assertion?>` to make the computer check if these statements are :ref:`True<test_what_is_true>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_what_is_an_assertion`` then add :ref:`variables<what is a variable?>` with a statement

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            reality == my_expectation


    # Exceptions seen
    # AssertionError

  the test is still green.

  - ``==`` is 2 equal signs - :kbd:`=+=` and means ``is equal`` which makes this statement read as ``reality is equal to my_expectation`` because

    - ``reality`` is the name or :ref:`variable<what is a variable?>` I gave to the result of ``1 + 1``
    - ``my_expectation`` is the name or :ref:`variable<what is a variable?>` I gave to ``2``
    - in other words the statement is ``1 + 1 is equal to 2``

* I change ``my_expectation`` to make the statement :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            # my_expectation = 2
            my_expectation = 11
            reality == my_expectation

  why is the test still green?

* I want the test to fail if I write a statement that is NOT :ref:`True<test_what_is_true>`. I change it to an `assert statement`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            # my_expectation = 2
            my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 2 == 11

  because ``1 + 1 == 11`` is :ref:`False<test_what_is_false>`. ``2`` is NOT equal to ``11`` and I added assert_ before the statement, which tells the computer ``DO NOT CONTINUE, if "1 + 1 == 11" is False``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` back, to match ``reality`` and make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 3-4

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

the test passes because ``1 + 1 == 2`` is NOT :ref:`False<test_what_is_false>`, ``1 + 1 is equal to 2``.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another statement

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8-10

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '2'
            reality == my_expectation


    # Exceptions seen

  the test is still green because the statement is not an assertion_

* I add assert_ before the statement to make it an assertion_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10-11
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '2'
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3-4
    :emphasize-text: 2 11

    E       AssertionError: assert '11' == '2'
    E
    E         - 2
    E         + 11

  - because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'1' + '1' == '2'" is False``
  - ``- 2`` shows what is missing from ``reality``
  - ``+ 11`` shows the actual value of ``reality``

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9-10
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            # my_expectation = '2'
            my_expectation = '11'
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

  the test passes because the statement is now :ref:`True<test_what_is_true>`, ``'1' + '1'`` is equal to ``'11'``

* These 2 statements are NOT the same

  - ``1 + 1 == 2`` checks if the result of :ref:`adding<test_addition>` two numbers is equal to the number on the right side of the ``==`` symbol
  - ``'1' + '1' == '11'`` checks if the result of "adding" 2 strings_ is equal to the string_ on the right side of the ``==`` symbol. A string_ is anything inside :ref:`quotes`

  I add another statement to show why ``'1' + '1' == '11'``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 14-16

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            # my_expectation = '2'
            my_expectation = '11'
            # reality == my_expectation
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = '11'
            reality == my_expectation


    # Exceptions seen

  the test is still green because ``reality == my_expectation`` is just a statement. Python_ does not care whether it is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` and the statement follows Python_ rules.

* I change the statement to an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 16-17
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            # my_expectation = '2'
            my_expectation = '11'
            # reality == my_expectation
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = '11'
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3-4

    E       AssertionError: assert 'I am alive' == '11'
    E
    E         - 11
    E         + I am alive

  - because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'I am' + ' alive' == '11'" is False``
  - ``- 11`` shows what is missing from ``reality``
  - ``+ I am alive`` shows the actual value of ``reality``

  .. attention:: If your result is different, check that you added a space before ``alive``, it should be ``' alive'`` not ``'alive'``.

* I change ``my_expectation`` to match ``reality`` and make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 15-16

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            # my_expectation = 11
            # reality == my_expectation
            assert reality == my_expectation

            reality = '1' + '1'
            # my_expectation = '2'
            my_expectation = '11'
            # reality == my_expectation
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            # my_expectation = '11'
            my_expectation = 'I am alive'
            # reality == my_expectation
            assert reality == my_expectation


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation


    # Exceptions seen

* I open a new terminal_ then change directories to ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_what_is_an_assertion'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
what is the difference between ``=`` and ``==``?
*********************************************************************************

----

* ``=`` is the symbol for assignment, pointing, defining references. It is how to give a name (:ref:`variable<what is a variable?>`) to an :ref:`object<what is a class?>` in Python_, for example

  .. code-block:: python

    project_name = 'assertion_error'

  is a way to tell Python_ that ``project_name`` is the name for the string_ ``'assertion_error'``. Python_ will substitute ``project_name`` with ``'assertion_error'`` anytime I use the name after the declaration, because I told it that ``project_name`` is a reference for that string_ (anything in :ref:`quotes`).

* ``==`` is used to check if the thing on the left of ``==`` is equal to the thing on the right of ``==``, for example

  .. code-block:: python

    assert 'thing on the left' == 'thing on the right'

  .. code-block:: python

    if 'thing on the left' == 'thing on the right':
        return 'magic'

----

*********************************************************************************
what causes AssertionError?
*********************************************************************************

AssertionError_ happens if the statement after assert_ is :ref:`False<test_what_is_false>`. It was in :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like this :ref:`assertion<what is an assertion?>`

.. code-block:: python

  assert True == False

With these statements, I tell Python_ - "DO NOT CONTINUE, if :ref:`True<test_what_is_true>` is equal to :ref:`False<test_what_is_false>`", or said a different way "GO TO THE NEXT LINE, ONLY if :ref:`True<test_what_is_true>` is equal to :ref:`False<test_what_is_false>`".

----

*********************************************************************************
test_assertion_error_w_none
*********************************************************************************

:ref:`None<what is None?>` is used when there is no value. I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`, this is useful if I want to check what value I get from a process.

For example, if I have people fill a form and I want a test for when they leave something blank, I can use an :ref:`assertion<what is an assertion?>` to make sure that the value is :ref:`None<what is None?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new failing test to ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation

        def test_assertion_error_w_none(self):
            assert None is not None


    # Exceptions seen

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert None is not None

  because ``None is not None`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 2-3
  :emphasize-text: is

      def test_assertion_error_w_none(self):
          # assert None is not None
          assert None is None


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note with what I learned from the experiment

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6-7

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None


    # NOTES
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add a new :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`False<test_what_is_false>`.

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            assert False is None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None


    # NOTES
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`True<test_what_is_true>`.

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            assert True is None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8-9
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    # NOTES
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for an integer_ (a whole number without decimals)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 11

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            assert 0 is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 11-12
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    # NOTES
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a float_ (binary floating point decimal number)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 14

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            assert 0.0 is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 14-15
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

    # NOTES
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a string_ (anything in :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 17

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            assert 'a string' is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 17-18
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None


    # NOTES

  the test passes.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2

    # NOTES
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a tuple_ (anything in parentheses ``( )`` separated by a comma)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 20

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            assert (1, 2, 3, 'n') is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 20-21
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

    # NOTES
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 23

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            assert [1, 2, 3, 'n'] is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 23-24
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None


    # NOTES

  the test passes.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    # NOTES
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a set_ (anything in curly braces ``{ }`` separated by a comma)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 26

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

            assert {1, 2, 3, 'n'} is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 26-27
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    # NOTES
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 29

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

            assert {'key': 'value'} is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 29-30
    :emphasize-text: not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None

            # assert False is None
            assert False is not None

            # assert True is None
            assert True is not None

            # assert 0 is None
            assert 0 is not None

            # assert 0.0 is None
            assert 0.0 is not None

            # assert 'a string' is None
            assert 'a string' is not None

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if something is NOT the same object as None
=================================================================================

----

I can also use `assert methods`_ from the `unittest.TestCase class`_ to test if something is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>` or NOT.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertIsNot method`_ which checks if the :ref:`object<what is a class?>` in the parentheses on the left is NOT the same as the :ref:`object<what is a class?>` in the parentheses on the right

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4
    :emphasize-text: Not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            self.assertIsNot(None, None)

            # assert False is None
            assert False is not None

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: unexpectedly identical: None

  because :ref:`None<what is None?>` is :ref:`None<what is None?>`, they are the same :ref:`object<what is a class?>`. Compare this error message with the one for ``assert None is not None``

  .. code-block:: python

    E       assert None is not None

  which do you like better?

  .. admonition:: these two statements check the same thing

    .. code-block:: python

      assert None is not None
      self.assertIsNot(None, None)

    they are asking the same question: ``is None the same object as None?`` or giving Python_ the command ``DO NOT CONTINUE if "None is NOT the same object as None" is False``

----

=================================================================================
another way to test if something is the same object as None
=================================================================================

----

* I change the `assertIsNot method`_ to the `assertIs method`_ which checks if the :ref:`object<what is a class?>` in parentheses on the left is the same as the :ref:`object<what is a class?>` in parentheses on the right

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            # assert False is None
            assert False is not None

  the test passes because :ref:`None<what is None?>` is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`.

* I use the `assertIs method`_ to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 9

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            # assert False is None
            assert False is not None
            self.assertIs(False, None)

            # assert True is None
            assert True is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False is not None

  compare this error message with the one for ``assert False is None``

  .. code-block:: python

    E    assert False is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-4

            # assert False is None
            assert False is not None
            # self.assertIs(False, None)
            self.assertIsNot(False, None)

            # assert True is None
            assert True is not None

  the test passes.

* I use assertIs_ to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 14

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            # assert False is None
            assert False is not None
            # self.assertIs(False, None)
            self.assertIsNot(False, None)

            # assert True is None
            assert True is not None
            self.assertIs(True, None)

            # assert 0 is None
            assert 0 is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True is not None

  compare this error message with the one for ``assert True is None``

  .. code-block:: python

    E    assert True is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3-4

            # assert True is None
            assert True is not None
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None
            assert 0 is not None

  the test passes.

* I use assertIs_ to compare an integer_ (a whole number without decimals) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8

            # assert True is None
            assert True is not None
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None
            assert 0 is not None
            self.assertIs(0, None)

            # assert 0.0 is None
            assert 0.0 is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

  compare this error message with the one for ``assert 0 is None``

  .. code-block:: python

    E    assert 0 is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3-4

            # assert 0 is None
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            # assert 0.0 is None
            assert 0.0 is not None

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 1

            an_integer = 0
            # assert 0 is None
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            # assert 0.0 is None
            assert 0.0 is not None

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2-3, 5, 7

            an_integer = 0
            assert an_integer is not None
            self.assertIsNot(an_integer, None)
            # assert 0 is None
            # assert 0 is not None
            # self.assertIs(0, None)
            # self.assertIsNot(0, None)

            # assert 0.0 is None
            assert 0.0 is not None

  the test is still green.

* I use assertIs_ to compare a float_ (binary floating point decimal number) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

            # assert 0.0 is None
            assert 0.0 is not None
            self.assertIs(0.0, None)

            # assert 'a string' is None
            assert 'a string' is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0.0 is not None

  compare this error message with the one for ``assert 0.0 is None``

  .. code-block:: python

    E    assert 0.0 is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-4

            # assert 0.0 is None
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            # assert 'a string' is None
            assert 'a string' is not None

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1

            a_float = 0.0
            # assert 0.0 is None
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            # assert 0.0 is None
            assert 0.0 is not None

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-3, 5, 7

            a_float = 0.0
            assert a_float is not None
            self.assertIsNot(a_float, None)
            # assert 0.0 is None
            # assert 0.0 is not None
            # self.assertIs(0.0, None)
            # self.assertIsNot(0.0, None)

            # assert 'a string' is None
            assert 'a string' is not None

  the test is still green.

* I use assertIs_ to compare a string_ (anything in :ref:`quotes`) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3

            # assert 'a string' is None
            assert 'a string' is not None
            self.assertIs('a string', None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'a string' is not None

  compare this error message with the one for ``assert 'a string' is None``

  .. code-block:: python

    E       AssertionError: assert 'a string' is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3-4

            # assert 'a string' is None
            assert 'a string' is not None
            # self.assertIs('a string', None)
            self.assertIsNot('a string', None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 1

            a_string = 'a string'
            # assert 'a string' is None
            assert 'a string' is not None
            # self.assertIs('a string', None)
            self.assertIsNot('a string', None)

            # assert 'a string' is None
            assert 'a string' is not None

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3, 5, 7

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNot(a_string, None)
            # assert 'a string' is None
            # assert 'a string' is not None
            # self.assertIs('a string', None)
            # self.assertIsNot('a string', None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

  the test is still green.

* I use assertIs_ to compare a tuple_ (anything in parentheses ``( )`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            self.assertIs((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: (1, 2, 3, 'n') is not None

  compare this error message with the one for ``assert (1, 2, 3, 'n') is None``

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3-4

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            self.assertIsNot((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 1

            a_tuple = (1, 2, 3, 'n')
            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            self.assertIsNot((1, 2, 3, 'n'), None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-3, 5, 7

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)
            # assert (1, 2, 3, 'n') is None
            # assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            # self.assertIsNot((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None

  the test is still green.

* I use assertIs_ to compare a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            self.assertIs([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: [1, 2, 3, 'n'] is not None

  compare this error message with the one for ``assert [1, 2, 3, 'n'] is None``

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3-4

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

            a_list = [1, 2, 3, 'n']
            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3, 5, 7

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)
            # assert [1, 2, 3, 'n'] is None
            # assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            # self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None

  the test is still green.

* I use assertIs_ to compare a set_ (anything in curly braces ``{ }`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            self.assertIs({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {1, 2, 3, 'n'} is not None

  compare this error message with the one for ``assert {1, 2, 3, 'n'} is None``

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3-4

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            self.assertIsNot({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 1

            a_set = {1, 2, 3, 'n'}
            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            self.assertIsNot({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-3, 5, 7

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)
            # assert {1, 2, 3, 'n'} is None
            # assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            # self.assertIsNot({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None


    # NOTES

  the test is still green.

* I use assertIs_ to compare a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None
            self.assertIs({'key': 'value'}, None)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not None

  compare this error message with the one for ``assert {'key': 'value'} is None``

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3-4

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None
            # self.assertIs({'key': 'value'}, None)
            self.assertIsNot({'key': 'value'}, None)


    # NOTES

  the test passes.

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3-4

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False
            # self.assertIs({'key': 'value'}, False)
            self.assertIsNot({'key': 'value'}, False)


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{'key': 'value'}`` from the test

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 1

            a_dictionary = {'key': 'value'}
            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None
            # self.assertIs({'key': 'value'}, None)
            self.assertIsNot({'key': 'value'}, None)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{'key': 'value'}`` from the test

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-3, 5, 7

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)
            # assert {'key': 'value'} is None
            # assert {'key': 'value'} is not None
            # self.assertIs({'key': 'value'}, None)
            # self.assertIsNot({'key': 'value'}, None)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIs(None, None)

            assert False is not None
            self.assertIsNot(False, None)

            assert True is not None
            self.assertIsNot(True, None)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNot(an_integer, None)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNot(a_float, None)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNot(a_string, None)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNot(a_tuple, None)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNot(a_list, None)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNot(a_set, None)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test_assertion_error_w_none with assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is None<what is None?>`

----

*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

:ref:`False<test_what_is_false>` is one of the two :ref:`booleans<what are booleans?>` and :ref:`test_assertion_error_w_none` shows that :ref:`False<test_what_is_false>` is NOT :ref:`None<what is None?>`. :ref:`is None False?<is None False or True?>`

I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new test

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5-6

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNot(a_dictionary, None)

        def test_assertion_error_w_false(self):
            assert None is False


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert None is False

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-3
  :emphasize-text: not

      def test_assertion_error_w_false(self):
          # assert None is False
          assert None is not False


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 11

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is not False
    # None is None

----

* I add a failing `assert statement`_ about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 5

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            assert False is not False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is not False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 5-6

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 10

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if :ref:`True<test_what_is_true>` is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            assert True is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-9
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 9

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if an integer_ (a whole number without decimals) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 11

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            assert 0 is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 11-12
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 8

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 14

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            assert 0.0 is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 14-15
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 7

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 17

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            assert 'a string' is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 17-18
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False


    # NOTES

  the test passes.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 6

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 20

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            assert (1, 2, 3, 'n') is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 20-21
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 5

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 23

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            assert [1, 2, 3, 'n'] is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 23-24
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False


    # NOTES

  the test passes.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a set_ (anything in curly braces ``{ }`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 26

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

            assert {1, 2, 3, 'n'} is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 26-27
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3

    # NOTES
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

-----

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 29

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

            assert {'key': 'value'} is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 29-30
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False

            # assert False is not False
            assert False is False

            # assert True is False
            assert True is not False

            # assert 0 is False
            assert 0 is not False

            # assert 0.0 is False
            assert 0.0 is not False

            # assert 'a string' is False
            assert 'a string' is not False

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_false'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if something is the same object as False
=================================================================================

----

I can also use the assertIs_ and assertIsNot_  :ref:`methods<what is a method?>` from the `unittest.TestCase class`_ to test if something is the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>` or not.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertIs method`_ (it checks if the two :ref:`objects<what is a class?>` in parentheses are the same)

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4
    :emphasize-text: Not

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False
            self.assertIs(None, False)

            # assert False is not False
            assert False is False

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: None is not False

  because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`. Compare this error message with the one for ``assert None is False``

  .. code-block:: python

    E       assert None is False

  which do you like better?

----

=================================================================================
another way to test if something is NOT the same object as False
=================================================================================

----

* I change the `assertIs method`_ to the `assertIsNot method`_ which checks if the two :ref:`objects<what is a class?>` in parentheses are NOT the same

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4-5

        def test_assertion_error_w_false(self):
            # assert None is False
            assert None is not False
            # self.assertIs(None, False)
            self.assertIsNot(None, False)

            # assert False is not False
            assert False is False

  the test passes because :ref:`None<what is None?>` is NOT the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I use the `assertIsNot method`_ to compare :ref:`False<test_what_is_false>` with itself

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

            # assert False is not False
            assert False is False
            self.assertIsNot(False, False)

            # assert True is False
            assert True is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: unexpectedly identical: False

  compare this error message with the one for ``assert False is not False``

  .. code-block:: python

    E    assert False is not False

* I change assertIsNot_ to assertIs_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-4

            # assert False is not False
            assert False is False
            # self.assertIsNot(False, False)
            self.assertIs(False, False)

            # assert True is False
            assert True is not False

  the test passes.

* I use assertIs_ to compare :ref:`True<test_what_is_true>` with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3

            # assert True is False
            assert True is not False
            self.assertIs(True, False)

            # assert 0 is False
            assert 0 is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True is not False

  compare this error message with the one for ``assert True is False``

  .. code-block:: python

    E    assert True is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-4

            # assert True is False
            assert True is not False
            # self.assertIs(True, False)
            self.assertIsNot(True, False)

            # assert 0 is False
            assert 0 is not False

  the test passes.

* I use assertIs_ to compare an integer_ (a whole number without decimals) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3

            # assert 0 is False
            assert 0 is not False
            self.assertIs(0, False)

            # assert 0.0 is False
            assert 0.0 is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not False

  compare this error message with the one for ``assert 0 is False``

  .. code-block:: python

    E    assert 0 is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3-4

            # assert 0 is False
            assert 0 is not False
            # self.assertIs(0, False)
            self.assertIsNot(0, False)

            # assert 0.0 is False
            assert 0.0 is not False

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 1

            an_integer = 0
            # assert 0 is False
            assert 0 is not False
            # self.assertIs(0, False)
            self.assertIsNot(0, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-3, 5, 7

            an_integer = 0
            assert an_integer is not False
            self.assertIsNot(an_integer, False)
            # assert 0 is False
            # assert 0 is not False
            # self.assertIs(0, False)
            # self.assertIsNot(0, False)

            # assert 0.0 is False
            assert 0.0 is not False
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

  the test is still green.

* I use assertIs_ to compare a float_ (binary floating point decimal number) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3

            # assert 0.0 is False
            assert 0.0 is not False
            self.assertIs(0.0, False)

            # assert 'a string' is False
            assert 'a string' is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0.0 is not False

  compare this error message with the one for ``assert 0.0 is False``

  .. code-block:: python

    E    assert 0.0 is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3-4

            # assert 0.0 is False
            assert 0.0 is not False
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

            # assert 'a string' is False
            assert 'a string' is not False

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 1

            a_float = 0.0
            # assert 0.0 is False
            assert 0.0 is not False
            # self.assertIs(0.0, False)
            self.assertIsNot(0.0, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-3, 5, 7

            a_float = 0.0
            assert a_float is not False
            self.assertIsNot(a_float, False)
            # assert 0.0 is False
            # assert 0.0 is not False
            # self.assertIs(0.0, False)
            # self.assertIsNot(0.0, False)

            # assert 'a string' is False
            assert 'a string' is not False

  the test is still green.

* I use assertIs_ to compare a string_ (anything in :ref:`quotes`) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 3

            # assert 'a string' is False
            assert 'a string' is not False
            self.assertIs('a string', False)

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'a string' is not False

  compare this error message with the one for ``assert 'a string' is False``

  .. code-block:: python

    E       AssertionError: assert 'a string' is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 3-4

            # assert 'a string' is False
            assert 'a string' is not False
            # self.assertIs('a string', False)
            self.assertIsNot('a string', False)

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 1

            a_string = 'a string'
            # assert 'a string' is False
            assert 'a string' is not False
            # self.assertIs('a string', False)
            self.assertIsNot('a string', False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3, 5, 7

            a_string = 'a string'
            assert a_string is not False
            self.assertIsNot(a_string, False)
            # assert 'a string' is False
            # assert 'a string' is not False
            # self.assertIs('a string', None)
            # self.assertIsNot('a string', None)

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False

  the test is still green.

* I use assertIs_ to compare a tuple_ (anything in parentheses ``( )`` separated by a comma) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 3

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False
            self.assertIs((1, 2, 3, 'n'), False)

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: (1, 2, 3, 'n') is not False

  compare this error message with the one for ``assert (1, 2, 3, 'n') is False``

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 3-4

            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False
            # self.assertIs((1, 2, 3, 'n'), False)
            self.assertIsNot((1, 2, 3, 'n'), False)

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 1

            a_tuple = (1, 2, 3, 'n')
            # assert (1, 2, 3, 'n') is False
            assert (1, 2, 3, 'n') is not False
            # self.assertIs((1, 2, 3, 'n'), False)
            self.assertIsNot((1, 2, 3, 'n'), False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 2-3, 5, 7

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)
            # assert (1, 2, 3, 'n') is False
            # assert (1, 2, 3, 'n') is not False
            # self.assertIs((1, 2, 3, 'n'), False)
            # self.assertIsNot((1, 2, 3, 'n'), False)

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False

  the test is still green.

* I use assertIs_ to compare a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False
            self.assertIs([1, 2, 3, 'n'], False)

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: [1, 2, 3, 'n'] is not False

  compare this error message with the one for ``assert [1, 2, 3, 'n'] is False``

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3-4

            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False
            # self.assertIs([1, 2, 3, 'n'], False)
            self.assertIsNot([1, 2, 3, 'n'], False)

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 1

            a_list = [1, 2, 3, 'n']
            # assert [1, 2, 3, 'n'] is False
            assert [1, 2, 3, 'n'] is not False
            # self.assertIs([1, 2, 3, 'n'], False)
            self.assertIsNot([1, 2, 3, 'n'], False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 2-3, 5, 7

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)
            # assert [1, 2, 3, 'n'] is False
            # assert [1, 2, 3, 'n'] is not False
            # self.assertIs([1, 2, 3, 'n'], False)
            # self.assertIsNot([1, 2, 3, 'n'], False)

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

  the test is still green.

* I use assertIs_ to compare a set_ (anything in curly braces ``{ }`` separated by a comma) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 3

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False
            self.assertIs({1, 2, 3, 'n'}, False)

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {1, 2, 3, 'n'} is not False

  compare this error message with the one for ``assert {1, 2, 3, 'n'} is False``

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 3-4

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False
            # self.assertIs({1, 2, 3, 'n'}, False)
            self.assertIsNot({1, 2, 3, 'n'}, False)

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 1

            a_set = {1, 2, 3, 'n'}
            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False
            # self.assertIs({1, 2, 3, 'n'}, False)
            self.assertIsNot({1, 2, 3, 'n'}, False)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2-3, 5, 7

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)
            # assert {1, 2, 3, 'n'} is False
            # assert {1, 2, 3, 'n'} is not False
            # self.assertIs({1, 2, 3, 'n'}, False)
            # self.assertIsNot({1, 2, 3, 'n'}, False)

            # assert {1, 2, 3, 'n'} is False
            assert {1, 2, 3, 'n'} is not False

  the test is still green.

* I use assertIs_ to compare a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) with :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 3

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False
            self.assertIs({'key': 'value'}, False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not False

  compare this error message with the one for ``assert {'key': 'value'} is False``

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is False

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 3-4

            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False
            # self.assertIs({'key': 'value'}, False)
            self.assertIsNot({'key': 'value'}, False)


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{'key': 'value'}`` from the test

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 1

            a_dictionary = {'key': 'value'}
            # assert {'key': 'value'} is False
            assert {'key': 'value'} is not False
            # self.assertIs({'key': 'value'}, False)
            self.assertIsNot({'key': 'value'}, False)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{'key': 'value'}`` from the test

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 2-3, 5, 7

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)
            # assert {'key': 'value'} is False
            # assert {'key': 'value'} is not False
            # self.assertIs({'key': 'value'}, False)
            # self.assertIsNot({'key': 'value'}, False)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 57

        def test_assertion_error_w_false(self):
            assert None is not False
            self.assertIsNot(None, False)

            assert False is False
            self.assertIs(False, False)

            assert True is not False
            self.assertIsNot(True, False)

            an_integer = 0
            assert an_integer is not False
            self.assertIsNot(an_integer, False)

            a_float = 0.0
            assert a_float is not False
            self.assertIsNot(a_float, False)

            a_string = 'a string'
            assert a_string is not False
            self.assertIsNot(a_string, False)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not False
            self.assertIsNot(a_tuple, False)

            a_list = [1, 2, 3, 'n']
            assert a_list is not False
            self.assertIsNot(a_list, False)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not False
            self.assertIsNot(a_set, False)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test_assertion_error_w_false with assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is the same object as False or NOT<test_assertion_error_w_false>`.

----

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

:ref:`True<test_what_is_true>` is the other :ref:`boolean<what are booleans?>` and is NOT :ref:`None<what is None?>`. I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` to see if :ref:`None<what is None?>` is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 5-6

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not False
            self.assertIsNot(a_dictionary, False)

        def test_assertion_error_w_true(self):
            assert None is True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert None is True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 95
  :emphasize-lines: 2-3
  :emphasize-text: not

      def test_assertion_error_w_true(self):
          # assert None is True
          assert None is not True


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 20

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if :ref:`False<test_what_is_false>` is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 5

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            assert False is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 5-6
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 18

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ about :ref:`True<test_what_is_true>`, that will fail

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 8

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            assert True is not True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is not True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 8-9

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 16

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if an integer_ (a whole number without decimals) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 11

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            assert 0 is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 11-12
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 14

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 14

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            assert 0.0 is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 14-15
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 12

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 17

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            assert 'a string' is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 17-18
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True


    # NOTES

  the test passes.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 10

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 20

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            assert (1, 2, 3, 'n') is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 20-21
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 8

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 23

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            assert [1, 2, 3, 'n'] is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 23-24
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True


    # NOTES

  the test passes.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 6

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a set_ (anything in curly braces ``{ }`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 26

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

            assert {1, 2, 3, 'n'} is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 26-27
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 4

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

-----

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 29

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

            assert {'key': 'value'} is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 29-30
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True

            # assert False is True
            assert False is not True

            # assert True is not True
            assert True is True

            # assert 0 is True
            assert 0 is not True

            # assert 0.0 is True
            assert 0.0 is not True

            # assert 'a string' is True
            assert 'a string' is not True

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_true'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if something is the same object as True
=================================================================================

----

I can also use the assertIs_ and assertIsNot_  :ref:`methods<what is a method?>` from the `unittest.TestCase class`_ to test if something is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>` or not.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertIs method`_ (it checks if the two :ref:`objects<what is a class?>` in parentheses are the same)

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 4
    :emphasize-text: Not

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True
            self.assertIs(None, True)

            # assert False is True
            assert False is not True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: None is not True

  because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`. Compare this error message with the one for ``assert None is True``

  .. code-block:: python

    E       assert None is True

----

=================================================================================
another way to test if something is NOT the same object as True
=================================================================================

----

* I change the `assertIs method`_ to the `assertIsNot method`_ which checks if the two :ref:`objects<what is a class?>` in parentheses are NOT the same :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 4-5

        def test_assertion_error_w_true(self):
            # assert None is True
            assert None is not True
            # self.assertIs(None, True)
            self.assertIsNot(None, True)

            # assert False is True
            assert False is not True

  the test passes because :ref:`None<what is None?>` is NOT the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I use the `assertIs method`_ to compare :ref:`False<test_what_is_false>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3

            # assert False is True
            assert False is not True
            self.assertIs(False, True)

            # assert True is not True
            assert True is True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False is not True

  compare this error message with the one for ``assert False is True``

  .. code-block:: python

    E    assert False is True

* I change assertIsNot_ to assertIs_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3-4

            # assert False is True
            assert False is not True
            # self.assertIs(False, True)
            self.assertIsNot(False, True)

            # assert True is not True
            assert True is True

  the test passes.

* I use assertIsNot_ to compare :ref:`True<test_what_is_true>` with itself

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3

            # assert True is not True
            assert True is True
            self.assertIsNot(True, True)

            # assert 0 is True
            assert 0 is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: unexpectedly identical: True

  compare this error message with the one for ``assert True is not True``

  .. code-block:: python

    E    assert True is not True

* I change assertIsNot_ to assertIs_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3-4

            # assert True is not True
            assert True is True
            # self.assertIsNot(True, True)
            self.assertIs(True, True)

            # assert 0 is True
            assert 0 is not True

  the test passes.

* I use assertIs_ to compare an integer_ (a whole number without decimals) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

            # assert 0 is True
            assert 0 is not True
            self.assertIs(0, True)

            # assert 0.0 is True
            assert 0.0 is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not True

  compare this error message with the one for ``assert 0 is True``

  .. code-block:: python

    E    assert 0 is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3-4

            # assert 0 is True
            assert 0 is not True
            # self.assertIs(0, True)
            self.assertIsNot(0, True)

            # assert 0.0 is True
            assert 0.0 is not True

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 1

            an_integer = 0
            # assert 0 is True
            assert 0 is not True
            # self.assertIs(0, True)
            self.assertNot(0, True)

            # assert 0.0 is True
            assert 0.0 is not True

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0`` from the test

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2-3, 5, 7

            an_integer = 0
            assert an_integer is not True
            self.assertIsNot(an_integer, True)
            # assert 0 is True
            # assert 0 is not True
            # self.assertIs(0, True)
            # self.assertIsNot(0, True)

            # assert 0.0 is True
            assert 0.0 is not True

  the test is still green.

* I use assertIs_ to compare a float_ (binary floating point decimal number) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3

            # assert 0.0 is True
            assert 0.0 is not True
            self.assertIs(0.0, True)

            # assert 'a string' is True
            assert 'a string' is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0.0 is not True

  compare this error message with the one for ``assert 0.0 is True``

  .. code-block:: python

    E    assert 0.0 is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3-4

            # assert 0.0 is True
            assert 0.0 is not True
            # self.assertIs(0.0, True)
            self.assertIsNot(0.0, True)

            # assert 'a string' is True
            assert 'a string' is not True

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 1

            a_float = 0.0
            # assert 0.0 is True
            assert 0.0 is not True
            # self.assertIs(0.0, True)
            self.assertNot(0.0, True)

            # assert 'a string' is True
            assert 'a string' is not True

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0`` from the test

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 2-3, 5, 7

            a_float = 0.0
            assert a_float is not True
            self.assertIsNot(a_float, True)
            # assert 0.0 is True
            # assert 0.0 is not True
            # self.assertIs(0.0, True)
            # self.assertIsNot(0.0, True)

            # assert 'a string' is True
            assert 'a string' is not True

  the test is still green.

* I use assertIs_ to compare a string_ (anything in :ref:`quotes`) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 3

            # assert 'a string' is True
            assert 'a string' is not True
            self.assertIs('a string', True)

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'a string' is not True

  compare this error message with the one for ``assert 'a string' is True``

  .. code-block:: python

    E       AssertionError: assert 'a string' is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 3-4

            # assert 'a string' is True
            assert 'a string' is not True
            # self.assertIs('a string', True)
            self.assertIsNot('a string', True)

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 1

            a_string = 'a string'
            # assert 'a string' is True
            assert 'a string' is not True
            # self.assertIs('a string', True)
            self.assertNot('a string', True)

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'a string'`` from the test

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 2-3, 5, 7

            a_string = 'a string'
            assert a_string is not True
            self.assertIsNot(a_string, True)
            # assert 'a string' is True
            # assert 'a string' is not True
            # self.assertIs('a string', True)
            # self.assertIsNot('a string', True)

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True

  the test is still green.

* I use assertIs_ to compare a tuple_ (anything in parentheses ``( )`` separated by a comma) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 3

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True
            self.assertIs((1, 2, 3, 'n'), True)

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: (1, 2, 3, 'n') is not True

  compare this error message with the one for ``assert (1, 2, 3, 'n') is True``

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 3-4

            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True
            # self.assertIs((1, 2, 3, 'n'), True)
            self.assertIsNot((1, 2, 3, 'n'), True)

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 1

            a_tuple = (1, 2, 3, 'n')
            # assert (1, 2, 3, 'n') is True
            assert (1, 2, 3, 'n') is not True
            # self.assertIs((1, 2, 3, 'n'), True)
            self.assertNot((1, 2, 3, 'n'), True)

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``(1, 2, 3, 'n')`` from the test

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 2-3, 5, 7

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)
            # assert (1, 2, 3, 'n') is True
            # assert (1, 2, 3, 'n') is not True
            # self.assertIs((1, 2, 3, 'n'), True)
            # self.assertIsNot((1, 2, 3, 'n'), True)

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True

  the test is still green.

* I use assertIs_ to compare a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True
            self.assertIs([1, 2, 3, 'n'], True)

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: [1, 2, 3, 'n'] is not True

  compare this error message with the one for ``assert [1, 2, 3, 'n'] is True``

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3-4

            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True
            # self.assertIs([1, 2, 3, 'n'], True)
            self.assertIsNot([1, 2, 3, 'n'], True)

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 1

            a_list = [1, 2, 3, 'n']
            # assert [1, 2, 3, 'n'] is True
            assert [1, 2, 3, 'n'] is not True
            # self.assertIs([1, 2, 3, 'n'], True)
            self.assertNot([1, 2, 3, 'n'], True)

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[1, 2, 3, 'n']`` from the test

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 2-3, 5, 7

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)
            # assert [1, 2, 3, 'n'] is True
            # assert [1, 2, 3, 'n'] is not True
            # self.assertIs([1, 2, 3, 'n'], True)
            # self.assertIsNot([1, 2, 3, 'n'], True)

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True

  the test is still green.

* I use assertIs_ to compare a set_ (anything in curly braces ``{ }`` separated by a comma) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True
            self.assertIs({1, 2, 3, 'n'}, True)

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {1, 2, 3, 'n'} is not True

  compare this error message with the one for ``assert {1, 2, 3, 'n'} is True``

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3-4

            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True
            # self.assertIs({1, 2, 3, 'n'}, True)
            self.assertIsNot({1, 2, 3, 'n'}, True)

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 1

            a_set = {1, 2, 3, 'n'}
            # assert {1, 2, 3, 'n'} is True
            assert {1, 2, 3, 'n'} is not True
            # self.assertIs({1, 2, 3, 'n'}, True)
            self.assertNot({1, 2, 3, 'n'}, True)

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 2-3, 5, 7

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)
            # assert {1, 2, 3, 'n'} is True
            # assert {1, 2, 3, 'n'} is not True
            # self.assertIs({1, 2, 3, 'n'}, True)
            # self.assertIsNot({1, 2, 3, 'n'}, True)

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True


    # NOTES

  the test is still green.

* I use assertIs_ to compare a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 3

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True
            self.assertIs({'key': 'value'}, True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not True

  compare this error message with the one for ``assert {'key': 'value'} is True``

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is True

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 3-4

            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True
            # self.assertIs({'key': 'value'}, True)
            self.assertIsNot({'key': 'value'}, True)


    # NOTES

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 1

            a_dictionary = {'key': 'value'}
            # assert {'key': 'value'} is True
            assert {'key': 'value'} is not True
            # self.assertIs({'key': 'value'}, True)
            self.assertIsNot({'key': 'value'}, True)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{1, 2, 3, 'n'}`` from the test

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 2-3, 5, 7

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)
            # assert {'key': 'value'} is True
            # assert {'key': 'value'} is not True
            # self.assertIs({'key': 'value'}, True)
            # self.assertIsNot({'key': 'value'}, True)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 95

        def test_assertion_error_w_true(self):
            assert None is not True
            self.assertIsNot(None, True)

            assert False is not True
            self.assertIsNot(False, True)

            assert True is True
            self.assertIs(True, True)

            an_integer = 0
            assert an_integer is not True
            self.assertIsNot(an_integer, True)

            a_float = 0.0
            assert a_float is not True
            self.assertIsNot(a_float, True)

            a_string = 'a string'
            assert a_string is not True
            self.assertIsNot(a_string, True)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not True
            self.assertIsNot(a_tuple, True)

            a_list = [1, 2, 3, 'n']
            assert a_list is not True
            self.assertIsNot(a_list, True)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not True
            self.assertIsNot(a_set, True)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test_assertion_error_w_true with assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is the same object as True or NOT<test_assertion_error_w_true>`.

----

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

All the :ref:`assertions<what is an assertion?>` I have typed so far show that :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different. They give me a basic expectation of Python_ because I can compare things with them.

I can also use :ref:`assertions<what is an assertion?>` to test if 2 things are equal, like I did in :ref:`test_what_is_an_assertion`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----


* I go back to the terminal_ where the tests are running

* I add a new test with an :ref:`assertion<what is an assertion?>` to see if :ref:`None<what is None?>` is NOT equal to :ref:`None<what is None?>`, in ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. note::

    ``!=`` is :kbd:`!+=` on the keyboard and is the symbol for ``NOT equal``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 5-6

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not True
            self.assertIsNot(a_dictionary, True)

        def test_assertion_error_w_equality(self):
            assert None != None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert None != None

  because the statement ``None is NOT equal to None``, is :ref:`False<test_what_is_false>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

.. note::

  ``==`` is :kbd:`=+=` on the keyboard and is the symbol for ``is equal``

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 133
  :emphasize-lines: 2-3

      def test_assertion_error_w_equality(self):
          # assert None != None
          assert None == None


  # NOTES

the test passes because ``None is equal to None`` is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add to the ``None is None`` note

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 31

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 5

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            assert False == None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 5-6

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None


    # NOTES

  the test passes.

* I add to the ``False is not None`` and ``None is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 28, 30

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 8

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            assert False == True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert False == True

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 8-9

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True


    # NOTES

  the test passes.

* I add to the ``False is not True`` and ``True is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 24, 26

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None
    # False is not True and NOT equal to True
    # False is False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with itself

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 11

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            assert False != False


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False != False

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 11-12

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            # assert False != False
            assert False == False


    # NOTES

  the test passes.

* I add to the ``False is False`` note

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 27

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

----

* I add a new failing :ref:`assertion<what is an assertion?>` to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 14

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            # assert False != False
            assert False == False

            assert True == None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 14-15

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            # assert False != False
            assert False == False

            # assert True == None
            assert True != None


    # NOTES

  the test passes.

* I add to the ``True is not None`` and ``None is not True`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 25, 29

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None and NOT equal to None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True and NOT equal to True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`True<test_what_is_true>` with itself

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 17

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            # assert False != False
            assert False == False

            # assert True == None
            assert True != None

            assert True != True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True != True

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 17-18

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None

            # assert False == None
            assert False != None

            # assert False == True
            assert False != True

            # assert False != False
            assert False == False

            # assert True == None
            assert True != None

            # assert True != True
            assert True == True


    # NOTES

  the test passes.

* I add to the ``True is True`` note

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 23

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True and equal to True
    # True is not False and NOT equal to False
    # True is not None and NOT equal to None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True and NOT equal to True
    # None is not False and NOT equal to False
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_equality'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if two things are not equal
=================================================================================

----

I can also use `assert methods`_ from the `unittest.TestCase class`_ to test if 2 things are equal or not.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertNotEqual method`_ which checks if the 2 things in the parentheses are NOT equal

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 4
    :emphasize-text: Not

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None
            self.assertNotEqual(None, None)

            # assert False == None
            assert False != None

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: None == None

  because :ref:`None<what is None?>` is equal to :ref:`None<what is None?>`, they are exactly the same :ref:`object<what is a class?>`. Compare this error message with the one for ``assert None != None``

  .. code-block:: python

    E    assert None != None

  which do you like better?

  .. admonition:: these two statements check the same thing

    .. code-block:: python

      assert None != None
      self.assertNotEqual(None, None)

    they are asking the same question: ``is None NOT equal to None?`` or giving Python_ the command ``DO NOT CONTINUE if "None is not equal to None" is False``

----

=================================================================================
another way to test if two things are equal
=================================================================================

----

* I change the `assertNotEqual method`_ to the `assertEqual method`_ which checks if the 2 things in the parentheses are equal

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 4-5

        def test_assertion_error_w_equality(self):
            # assert None != None
            assert None == None
            # self.assertNotEqual(None, None)
            self.assertEqual(None, None)

            # assert False == None
            assert False != None

  the test passes because :ref:`None<what is None?>` is equal to :ref:`None<what is None?>`.

* I use assertEqual_ to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 3

            # assert False == None
            assert False != None
            self.assertEqual(False, None)

            # assert False == True
            assert False != True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False != None

  compare this error message with the one for ``assert False == None``

  .. code-block:: python

    E    assert False == None

* I change assertEqual_ to assertNotEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 3-4

            # assert False == None
            assert False != None
            # self.assertEqual(False, None)
            self.assertNotEqual(False, None)

            # assert False == True
            assert False != True

  the test passes.

* I use assertEqual_ to compare :ref:`False<test_what_is_false>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 3

            # assert False == True
            assert False != True
            self.assertEqual(False, True)

            # assert False != False
            assert False == False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False != True

  compare this error message with the one for ``assert False == True``

  .. code-block:: python

    E    assert False == True

* I change assertEqual_ to assertNotEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 3-4

            # assert False == True
            assert False != True
            # self.assertEqual(False, True)
            self.assertNotEqual(False, True)

            # assert False != False
            assert False == False

  the test passes.

* I use assertNotEqual_ to compare :ref:`False<test_what_is_false>` with itself

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 3

            # assert False != False
            assert False == False
            self.assertNotEqual(False, False)

            # assert True == None
            assert True != None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False == False

  compare this error message with the one for ``assert False != False``

  .. code-block:: python

    E    assert False != False

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 3-4

            # assert False != False
            assert False == False
            # self.assertNotEqual(False, False)
            self.assertEqual(False, False)

            # assert True == None
            assert True != None

  the test passes.

* I use assertEqual_ to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 3

            # assert True == None
            assert True != None
            self.assertEqual(True, None)

            # assert True != True
            assert True == True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True != None

  compare this error message with the one for ``assert True == None``

  .. code-block:: python

    E    assert True == None

* I change assertEqual_ to assertNotEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 3-4

            # assert True == None
            assert True != None
            # self.assertEqual(True, None)
            self.assertNotEqual(True, None)

            # assert True != True
            assert True == True


    # NOTES

  the test passes.

* I use assertNotEqual_ to compare :ref:`True<test_what_is_true>` with itself

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 3

            # assert True != True
            assert True == True
            self.assertNotEqual(True, True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True == True

  compare this error message with the one for ``assert True != True``

  .. code-block:: python

    E    assert True != True

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 3-4

            # assert True != True
            assert True == True
            # self.assertNotEqual(True, True)
            self.assertEqual(True, True)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 133

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert False != True
            self.assertNotEqual(False, True)

            assert False == False
            self.assertEqual(False, False)

            assert True != None
            self.assertNotEqual(True, None)

            assert True == True
            self.assertEqual(True, True)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test_assertion_error_w_equality with assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

* I go back to the terminal_ where the tests are running

* I use the `assertNotEqual method`_ in the first :ref:`assertion<what is an assertion?>` of :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5
    :emphasize-text: not

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 2 == 2

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

  the test passes.

* I add a call to assertNotEqual_ for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       AssertionError: '11' == '11'

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11-12

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

  the test passes.

* I add a call to  assertNotEqual_ for the last :ref:`assertion<what is an assertion?>` in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 17

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'I am alive' == 'I am alive'

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            # self.assertNotEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_assertion_error_w_none(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test_what_is_an_assertion with assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if 2 things are equal<test_assertion_error_w_equality>`.

----

*********************************************************************************
test_assertion_error_w_is_vs_equal
*********************************************************************************

Some of the tests I have written use ``is`` and some use ``==``, if they mean the same thing, why do I use different symbols? What is the difference between ``is`` and ``==``?

In Python_ they do not mean the same thing

* ``x is y`` states that ``x`` is the same exact :ref:`object<what is a class?>` as ``y``
* ``x is not y`` states that ``x`` is NOT the same exact :ref:`object<what is a class?>` as ``y``
* ``x == y`` states that ``x`` is equal to ``y`` according to a rule or instruction programmed in Python_
* ``x != y`` states that ``x`` is NOT equal to ``y`` according to a rule or instruction programmed in Python_

This means that things can be equal without being the same exact :ref:`object<what is a class?>`. For example, an integer_ (a whole number without decimals) can be equal to a float_ (binary floating point decimal numbers) and they are NOT the same :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to show this

.. code-block:: python
  :lineno-start: 152
  :emphasize-lines: 4-5

          assert True == True
          self.assertEqual(True, True)

      def test_assertion_error_w_is_vs_equal(self):
          assert 0 is 0.0


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

.. code-block:: python

  E       assert 0 is 0.0

because an integer_ is NOT a float_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 155
  :emphasize-lines: 2-3

      def test_assertion_error_w_is_vs_equal(self):
          # assert 0 is 0.0
          assert 0 is not 0.0


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 5

        def test_assertion_error_w_is_vs_equal(self):
            # assert 0 is 0.0
            assert 0 is not 0.0

            assert 0 != 0.0


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 != 0.0

  because the two quantities are equal.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 5-6

        def test_assertion_error_w_is_vs_equal(self):
            # assert 0 is 0.0
            assert 0 is not 0.0

            # assert 0 != 0.0
            assert 0 == 0.0


    # NOTES

  the test passes.

* I add assertIs_ for the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 4

        def test_assertion_error_w_is_vs_equal(self):
            # assert 0 is 0.0
            assert 0 is not 0.0
            self.assertIs(0, 0.0)

            # assert 0 != 0.0
            assert 0 == 0.0


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0 is not 0.0

* I change assertIs_ to assertIsNot_

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 4-5

        def test_assertion_error_w_is_vs_equal(self):
            # assert 0 is 0.0
            assert 0 is not 0.0
            # self.assertIs(0, 0.0)
            self.assertIsNot(0, 0.0)

            # assert 0 != 0.0
            assert 0 == 0.0


    # NOTES

  the test passes.

* I add the `assertNotEqual method`_ for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 3

            # assert 0 != 0.0
            assert 0 == 0.0
            self.assertNotEqual(0, 0.0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0 == 0.0

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 3-4

            # assert 0 != 0.0
            assert 0 == 0.0
            # self.assertNotEqual(0, 0.0)
            self.assertEqual(0, 0.0)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 155

        def test_assertion_error_w_is_vs_equal(self):
            assert 0 is not 0.0
            self.assertIsNot(0, 0.0)

            assert 0 == 0.0
            self.assertEqual(0, 0.0)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_is_vs_equal'

  the terminal_ shows a summary of the changes then goes back to the command line.

The tests show that an integer_ can be ``EQUAL`` to a float_ but an integer_ ``IS`` NOT a float_.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_assertion_error.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I can use `assert statements`_ and `assert methods`_ to test if something is

* :ref:`None or NOT None<test_assertion_error_w_none>`
* :ref:`False or NOT False<test_assertion_error_w_false>`
* :ref:`True or NOT True<test_assertion_error_w_true>`

and to test if two things are

* :ref:`not equal<test_assertion_error_w_equality>` with assertNotEqual_
* :ref:`equal<test_assertion_error_w_equality>` with assertEqual_

The tests show that

* :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different
* ``is`` and ``==`` are different

:ref:`How many questions can you answer about AssertionError?<questions about AssertionError>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AssertionError: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

Congratulations! You now know

* :ref:`how to make a Python test driven development environment any time you want<how to make a Python test driven development environment>` and
* :ref:`what causes AssertionError?`

:ref:`Would you like to test functions?<what is a function?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->