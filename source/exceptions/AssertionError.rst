.. meta::
  :description: Learn what causes Python's AssertionError and how to use the assert statement in this beginner TDD tutorial. Master the Red-Green-Refactor cycle, pytest-watcher, the difference between = and ==, and how to test None, False, True, strings, lists, and dictionaries.
  :keywords: Jacob Itegboje, Python AssertionError, what causes AssertionError, assert statement Python, Python TDD tutorial, Test-Driven Development beginners, unittest assert examples, pytest-watcher setup, uv init python, difference between = and ==, Python is None vs is not None, testing False in Python, red green refactor cycle, test None type, testing lists and dictionaries python

.. include:: ../links.rst

.. _assert: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
.. _assert statement: assert_
.. _assertion: assert_
.. _assertions: assert_
.. _assert statements: assert_
.. _variable: https://grokipedia.com/page/:ref:`variable<what is a variable?>`symbol
.. _variables: :ref:`variable<what is a variable?>`
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

.. literalinclude:: ../code/tests/test_assertion_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about AssertionError
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is an assertion?<what is an assertion?>`
* :ref:`what is a variable?`
* :ref:`what causes AssertionError?<what causes AssertionError?>`
* :ref:`how can I test if something is NOT None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is False?<test_assertion_error_w_false>`
* :ref:`how can I test if something is NOT False?<test_assertion_error_w_true>`
* :ref:`how can I test if something is True?<test_assertion_error_w_true>`
* :ref:`how can I test if something is NOT True?<test_assertion_error_w_false>`
* :ref:`how can I test if 2 things are NOT Equal?<another way to test if two things are NOT Equal>`
* :ref:`how can I test if 2 things are Equal?<another way to test if two things are Equal>`

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

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_assertion_error.py

    `Visual Studio Code`_ opens ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

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

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line.

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

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

A variable_ is a name that is used for values that change. For example, in Mathematics_ we use ``x`` to represent any number.

I can use variables_ to remove repetition of values that change so that if I have to change a value, I only have to make the change in one place instead of many.


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

* I change ``test_failure`` to ``test_what_is_an_assertion`` then add variables_ with a statement

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

    - ``reality`` is the name or variable_ I gave to the result of ``1 + 1``
    - ``my_expectation`` is the name or variable_ I gave to ``2``
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

  because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'1' + '1' == '2'" is False``

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11-12
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

  because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'I am' + ' alive' == '11'" is False``

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

* I open a new terminal_ then change directories to ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_what_is_an_assertion'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
what is the difference between ``=`` and ``==``?
*********************************************************************************

----

* ``=`` is the symbol for assignment, pointing, defining references. It is how to give a name (:ref:`variable<what is a variable?>`) to an :ref:`object<what is a class?>` in Python_, for example

  .. code-block:: python

    project_name = 'assertion_error'

  is a way to tell Python_ that ``project_name`` is the name for the string_ ``'assertion_error'``. Python_ will substitute ``project_name`` with ``'assertion_error'`` anytime I use the name after the declaration, because I told it that ``project_name`` is a reference for that string_ (anything in :ref:`quotes`)

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

:ref:`None<what is None?>` is used when there is no value, it is the simplest :ref:`data structure<data structures>` in Python_. I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`None<what is None?>`, this is useful if I want to check what value I get from a process.

For example, if I have people fill a form and I want a test for when they leave something blank, I can use an :ref:`assertion<what is an assertion?>` to make sure that the value is :ref:`None<what is None?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new failing test to ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7-8

            reality = 'I am' + ' alive'
            # my_expectation = '11'
            my_expectation = 'I am alive'
            # reality == my_expectation
            assert reality == my_expectation

        def test_assertion_error_w_none(self):
            assert None is not None


    # Exceptions seen

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert None is not None

  because ``None is not None`` is :ref:`False<test_what_is_false>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 25
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
    :lineno-start: 25
    :emphasize-lines: 6-7

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None


    # NOTES
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add a new :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`False<test_what_is_false>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

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
    :lineno-start: 25
    :emphasize-lines: 4-5
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
    :lineno-start: 25
    :emphasize-lines: 9

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

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`True<test_what_is_true>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

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
    :lineno-start: 25
    :emphasize-lines: 6-7
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
    :lineno-start: 34
    :emphasize-lines: 2

    # NOTES
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for an integer_ (a whole number with no decimals)

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 8

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
    :lineno-start: 25
    :emphasize-lines: 8-9
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
    :lineno-start: 36
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
    :lineno-start: 25
    :emphasize-lines: 10

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
    :lineno-start: 25
    :emphasize-lines: 10-11
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
    :lineno-start: 38
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
    :lineno-start: 25
    :emphasize-lines: 12

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
    :lineno-start: 25
    :emphasize-lines: 12-13
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
    :lineno-start: 40
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
    :lineno-start: 25
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
    :lineno-start: 25
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
    :lineno-start: 25
    :emphasize-lines: 16

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
    :lineno-start: 25
    :emphasize-lines: 16-17
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
    :lineno-start: 44
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
    :lineno-start: 25
    :emphasize-lines: 18

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
    :lineno-start: 25
    :emphasize-lines: 18-19
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
    :lineno-start: 46
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
    :lineno-start: 25
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
    :lineno-start: 25
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
    :lineno-start: 48
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
    :emphasize-lines: 1

    git commit --all --message 'add test_assertion_error_w_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if something is NOT None
=================================================================================

----

I can also use `assert methods`_ from the `unittest.TestCase class`_ to test if something is :ref:`None<what is None?>` or not.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertIsNot method`_ which checks if the :ref:`object<what is a class?>` on the left is NOT the same as the :ref:`object<what is a class?>` on the right in the parentheses, in ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4
    :emphasize-text: Not

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            self.assertIsNot(None, None)

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
another way to test if something is None
=================================================================================

----

* I change the `assertIsNot method`_ to the `assertIs method`_ which checks if the :ref:`object<what is a class?>` on the left is the same as the :ref:`object<what is a class?>` on the right in the parentheses

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5

        def test_assertion_error_w_none(self):
            # assert None is not None
            assert None is None
            # self.assertIsNot(None, None)
            self.assertIs(None, None)

            # assert False is None

  the test passes because :ref:`None<what is None?>` is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`

* I use the `assertIs method`_ to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 25
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False is not None

  compare this error message with the one for ``assert False is None``

  .. code-block:: python

    E    assert False is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3-4

            # assert False is None
            assert False is not None
            # self.assertIs(False, None)
            self.assertIsNot(False, None)

            # assert True is None

  the test passes.

* I use assertIs_ to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 25
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: True is not None

  compare this error message with the one for ``assert True is None``

  .. code-block:: python

    E    assert True is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-4

            # assert True is None
            assert True is not None
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None

  the test passes.

* I use assertIs_ to compare an integer_ (a whole number with no decimals) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 8

            # assert True is None
            assert True is not None
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None
            assert 0 is not None
            self.assertIs(0, None)

            # assert 0.0 is None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

  compare this error message with the one for ``assert 0 is None``

  .. code-block:: python

    E    assert 0 is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-4

            # assert 0 is None
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            # assert 0.0 is None

  the test passes.

* I use assertIs_ to compare a float_ (binary floating point decimal number) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 24

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
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            # assert 0.0 is None
            assert 0.0 is not None
            self.assertIs(0.0, None)

            # assert 'a string' is None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0.0 is not None

  compare this error message with the one for ``assert 0.0 is None``

  .. code-block:: python

    E    assert 0.0 is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4

            # assert 0.0 is None
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            # assert 'a string' is None

  the test passes.

* I use assertIs_ to compare a string_ (anything in :ref:`quotes`) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 8

            # assert 0.0 is None
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            # assert 'a string' is None
            assert 'a string' is not None
            self.assertIs('a string', None)

            # assert (1, 2, 3, 'n') is None

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

  the test passes.

* I use assertIs_ to compare a tuple_ (anything in parentheses ``( )`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8

            # assert 'a string' is None
            assert 'a string' is not None
            # self.assertIs('a string', None)
            self.assertIsNot('a string', None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            self.assertIs((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: (1, 2, 3, 'n') is not None

  compare this error message with the one for ``assert (1, 2, 3, 'n') is None``

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-4

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            self.assertIsNot((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None

  the test passes.

* I use assertIs_ to compare a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 8

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            self.assertIsNot((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            self.assertIs([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: [1, 2, 3, 'n'] is not None

  compare this error message with the one for ``assert [1, 2, 3, 'n'] is None``

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3-4

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None

  the test passes.

* I use assertIs_ to compare a set_ (anything in curly braces ``{ }`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 8

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            self.assertIs({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {1, 2, 3, 'n'} is not None

  compare this error message with the one for ``assert {1, 2, 3, 'n'} is None``

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is None

* I change assertIs_ to assertIsNot_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 3-4

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            self.assertIsNot({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None

  the test passes.

* I use assertIs_ to compare a a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 8

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            self.assertIsNot({1, 2, 3, 'n'}, None)

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
    :lineno-start: 25
    :emphasize-lines: 49-50

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
            # self.assertIs(True, None)
            self.assertIsNot(True, None)

            # assert 0 is None
            assert 0 is not None
            # self.assertIs(0, None)
            self.assertIsNot(0, None)

            # assert 0.0 is None
            assert 0.0 is not None
            # self.assertIs(0.0, None)
            self.assertIsNot(0.0, None)

            # assert 'a string' is None
            assert 'a string' is not None
            # self.assertIs('a string', None)
            self.assertIsNot('a string', None)

            # assert (1, 2, 3, 'n') is None
            assert (1, 2, 3, 'n') is not None
            # self.assertIs((1, 2, 3, 'n'), None)
            self.assertIsNot((1, 2, 3, 'n'), None)

            # assert [1, 2, 3, 'n'] is None
            assert [1, 2, 3, 'n'] is not None
            # self.assertIs([1, 2, 3, 'n'], None)
            self.assertIsNot([1, 2, 3, 'n'], None)

            # assert {1, 2, 3, 'n'} is None
            assert {1, 2, 3, 'n'} is not None
            # self.assertIs({1, 2, 3, 'n'}, None)
            self.assertIsNot({1, 2, 3, 'n'}, None)

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None
            # self.assertIs({'key': 'value'}, None)
            self.assertIsNot({'key': 'value'}, None)


    # NOTES

  the test passes.

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

:ref:`False<test_what_is_false>` is one of the two :ref:`booleans<what are booleans?>` and is NOT :ref:`None<what is None?>` and :ref:`test_assertion_error_w_none` shows that :ref:`False<test_what_is_false>` is NOT :ref:`None<what is None?>`. :ref:`is None False?<is None False or True?>`

I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`False<test_what_is_false>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new test

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 6-7

            # assert {'key': 'value'} is None
            assert {'key': 'value'} is not None
            # self.assertIs({'key': 'value'}, None)
            self.assertIsNot({'key': 'value'}, None)

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
  :lineno-start: 76
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
    :lineno-start: 81
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
    :lineno-start: 76
    :emphasize-lines: 3

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
    :lineno-start: 76
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 36
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

* I add an `assert statement`_ to see if :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
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

* I add an `assert statement`_ to see if an integer_ (a whole number with no decimals) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 38
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

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 6

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 6
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 39
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

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 7

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 7
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False


    # NOTES

  the test passes.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 40
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

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 8

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 8
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 41
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

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 9

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 9
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is not False


    # NOTES

  the test passes.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 42
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

* I add an `assert statement`_ to see if a set_ is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 10

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is not False
            assert {1, 2, 3, 'n'} is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 10
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is not False
            assert {1, 2, 3, 'n'} is not False


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 43
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

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 11

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is not False
            assert {1, 2, 3, 'n'} is not False
            assert {'key': 'value'} is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 11
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False
            assert True is not False
            assert 0 is not False
            assert 0.0 is not False
            assert 'a string' is not False
            assert (1, 2, 3, 'n') is not False
            assert [1, 2, 3, 'n'] is not False
            assert {1, 2, 3, 'n'} is not False
            assert {'key': 'value'} is not False


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 44
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
    :emphasize-lines: 1

    git commit --all --message 'add test_assertion_error_w_false'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is False or NOT<test_assertion_error_w_false>`

----

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

:ref:`True<test_what_is_true>` is the other :ref:`boolean<what are booleans?>` and is NOT :ref:`None<what is None?>`. I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`True<test_what_is_true>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` to see if :ref:`None<what is None?>` is :ref:`True<test_what_is_true>`, in ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-4

            assert {'key': 'value'} is not False

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
  :lineno-start: 43
  :emphasize-lines: 2
  :emphasize-text: not

        def test_assertion_error_w_true(self):
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
    :lineno-start: 47
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

* I add an `assert statement`_ to see if :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 48
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
    :lineno-start: 43
    :emphasize-lines: 4

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is not True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is not True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
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

* I add an `assert statement`_ to see if an integer_ (a whole number with no decimals) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 50
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

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 51
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

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True


    # NOTES

  the test passes.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 52
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

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 53
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

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert [1, 2, 3, 'n'] is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is not True


    # NOTES

  the test passes.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 54
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

* I add an `assert statement`_ to see if a set_ is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is not True
            assert {1, 2, 3, 'n'} is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is not True
            assert {1, 2, 3, 'n'} is not True


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 55
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

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 11

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is not True
            assert {1, 2, 3, 'n'} is not True
            assert {'key': 'value'} is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 11
    :emphasize-text: not

        def test_assertion_error_w_true(self):
            assert None is not True
            assert False is not True
            assert True is True
            assert 0 is not True
            assert 0.0 is not True
            assert 'a string' is not True
            assert (1, 2, 3, 'n') is not True
            assert [1, 2, 3, 'n'] is not True
            assert {1, 2, 3, 'n'} is not True
            assert {'key': 'value'} is not True


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 56
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
    :emphasize-lines: 1

    git commit --all --message 'add test_assertion_error_w_true'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is True or NOT<test_assertion_error_w_true>`

----

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

All the :ref:`assertions<what is an assertion?>` I have typed so far show that :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different. They give me a basic expectation of Python_ because I can compare things with them.

I can use :ref:`assertions<what is an assertion?>` to test if 2 things are equal, like I did in :ref:`test_what_is_an_assertion`

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
    :lineno-start: 53
    :emphasize-lines: 3-4

            assert {'key': 'value'} is not True

        def test_assertion_error_w_equality(self):
            assert None != None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert None != None

  because ``None is NOT equal to None`` is :ref:`False<test_what_is_false>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

.. note::

  ``==`` is :kbd:`=+=` on the keyboard and is the symbol for ``is equal``

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 2

        def test_assertion_error_w_equality(self):
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
    :lineno-start: 59
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
    :lineno-start: 55
    :emphasize-lines: 3

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False == None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None


    # NOTES

  the test passes.

* I add to the ``False is not None`` and ``None is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 60
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
    :lineno-start: 55
    :emphasize-lines: 4

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False == True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert False == True

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True


    # NOTES

  the test passes.

* I add to the ``False is not True`` and ``True is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 61
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
    :lineno-start: 55
    :emphasize-lines: 5

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False != False


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False != False

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 5

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False == False


    # NOTES

  the test passes.

* I add to the ``False is False`` note

  .. code-block:: python
    :lineno-start: 62
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
    :lineno-start: 55
    :emphasize-lines: 6

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False == False
            assert True == None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False == False
            assert True != None


    # NOTES

  the test passes.

* I add to the ``True is not None`` and ``None is not True`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 69
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
    :lineno-start: 55
    :emphasize-lines: 7

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False == False
            assert True != None
            assert True != True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True != True

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 7

        def test_assertion_error_w_equality(self):
            assert None == None
            assert False != None
            assert False != True
            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the test passes.

* I add to the ``True is True`` note

  .. code-block:: python
    :lineno-start: 52
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

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_assertion_error_w_equality'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
another way to test if two things are NOT Equal
=================================================================================

----

I can also use `assert methods`_ from the `unittest.TestCase class`_ to test if 2 things are equal or not.

* I go back to the terminal_ where the tests are running

* I add an :ref:`assertion<what is an assertion?>` with the `assertNotEqual method`_ which checks if the 2 things in the parentheses are NOT equal, in ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3
    :emphasize-text: Not

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertNotEqual(None, None)

            assert False != None
            assert False != True
            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: None == None

  because :ref:`None<what is None?>` is equal to :ref:`None<what is None?>`, they are the same :ref:`object<what is a class?>`. Compare this error message with the one for ``assert None != None``

  .. code-block:: python

    E    assert None != None

  which do you like better?

  .. admonition:: these two statements check the same thing

    .. code-block:: python

      assert None != None
      self.assertNotEqual(None, None)

    they are asking the same question: ``is None NOT equal to None?`` or giving Python_ the command ``DO NOT CONTINUE if "None is NOT Equal to None" is False``

----

=================================================================================
another way to test if two things are Equal
=================================================================================

----

* I change the `assertNotEqual method`_ to the `assertEqual method`_ which checks if the 2 things in the parentheses are equal

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            assert False != True
            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the test passes because :ref:`None<what is None?>` is equal to :ref:`None<what is None?>`

* I use assertEqual_ to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertEqual(False, None)

            assert False != True
            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False != None

  compare this error message with the one for ``assert False == None``

  .. code-block:: python

    E    assert False == None

* I change assertEqual_ to assertNotEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert False != True
            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the test passes.

* I use assertEqual_ to compare :ref:`False<test_what_is_false>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert False != True
            self.assertEqual(False, True)

            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False != True

  compare this error message with the one for ``assert False == True``

  .. code-block:: python

    E    assert False == True

* I change assertEqual_ to assertNotEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert False != True
            self.assertNotEqual(False, True)

            assert False == False
            assert True != None
            assert True == True


    # NOTES

  the test passes.

* I use assertNotEqual_ to compare :ref:`False<test_what_is_false>` with itself

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 12

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert False != True
            self.assertNotEqual(False, True)

            assert False == False
            self.assertNotEqual(False, False)

            assert True != None
            assert True == True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: False == False

  compare this error message with the one for ``assert False != False``

  .. code-block:: python

    E    assert False != False

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 12

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
            assert True == True


    # NOTES

  the test passes.

* I use assertEqual_ to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 15

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
            self.assertEqual(True, None)

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
    :lineno-start: 55
    :emphasize-lines: 15

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


    # NOTES

  the test passes.

* I use assertNotEqual_ to compare :ref:`True<test_what_is_true>` with itself

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 18

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
    :lineno-start: 55
    :emphasize-lines: 18

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

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add assert methods'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

* I go back to the terminal_ where the tests are running

* I use the `assertNotEqual method`_ in :ref:`test_what_is_an_assertion`, in ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-7
    :emphasize-text: not

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertNotEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation

        def test_assertion_error_w_none(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 2 == 2

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation

        def test_assertion_error_w_none(self):

  the test passes.

* I add a call to assertNotEqual_ for the next assertion_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 12-14

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertNotEqual(
                reality, my_expectation
            )

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation

        def test_assertion_error_w_none(self):

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       AssertionError: '11' == '11'

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 12

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation

        def test_assertion_error_w_none(self):

  the test passes.

* I add a call to  assertNotEqual_ for the last :ref:`assertion<what is an assertion?>` in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 19-21

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertNotEqual(
                reality, my_expectation
            )

        def test_assertion_error_w_none(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'I am alive' == 'I am alive'

  it shows what the :ref:`True<test_what_is_true>` statement is

* I change assertNotEqual_ to assertEqual_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 19

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

            reality = 'I am' + ' alive'
            my_expectation = 'I am alive'
            assert reality == my_expectation
            self.assertEqual(
                reality, my_expectation
            )

        def test_assertion_error_w_none(self):

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add assertEqual'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if 2 things are equal<test_assertion_error_w_equality>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``assertion_error.py`` in the :ref:`editor<2 editors>`
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

* :ref:`NOT None<test_assertion_error_w_none>`
* :ref:`None<test_assertion_error_w_none>`
* :ref:`False or NOT False<test_assertion_error_w_none>`
* :ref:`True or NOT True<test_assertion_error_w_none>`

and to test if 2 things are

* :ref:`NOT Equal<test_assertion_error_w_equality>` with assertNotEqual_
* :ref:`Equal<test_assertion_error_w_equality>` with assertEqual_

The tests show that :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different.

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
* :ref:`how to raise AssertionError<what causes AssertionError?>`

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