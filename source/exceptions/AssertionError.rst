.. meta::
  :description: Master Python's AssertionError for robust testing. Learn to use assert for debugging, handle exceptions, and see practical unittest examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python AssertionError example, how to handle AssertionError in Python, python unittest assert examples, python assert for debugging, python assert best practices, python custom AssertionError message, python testing with pytest and assert

.. include:: ../links.rst

.. _assert: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
.. _assert statement: assert_
.. _assertion: assert_
.. _assertions: assert_
.. _assert statements: assert_
.. _variable: https://grokipedia.com/page/:ref:`variable<what is a variable?>`symbol
.. _variables: :ref:`variable<what is a variable?>`
.. _AssertionError: https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError

#################################################################################
what is an assertion?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

An :ref:`assertion<what is an assertion?>` or `assert statement`_ is a way for me to tell Python_, "DO NOT CONTINUE, if this statement is False", or said a different way "GO TO THE NEXT LINE, ONLY if this statement IS True".

I use assertions_ in testing when making a program_ to make sure something is :ref:`True<test_what_is_true>` about the program_ before I continue building or to test ideas and see if they work, without worrying about if I will remember the ideas later.

I use them to test how the program_ behaves, for example when it is given inputs. Assertions_ can help catch things that make tests that were passing before to start failing when I add new lines of code. They help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations (tests and ideas) and reality (what happens when the program_ runs), tells me what to change to make them match. The closer my program_ is to reality, the better.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

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
* :ref:`how can I test if something is NOT None?<how to test if something is NOT None>`
* :ref:`how can I test if something is None?<how to test if something is None>`
* :ref:`how can I test if something is False?<how to test if something is False>`
* :ref:`how can I test if something is NOT False?<how to test if something is True>`
* :ref:`how can I test if something is True?<how to test if something is True>`
* :ref:`how can I test if something is NOT True?<how to test if something is False>`
* :ref:`how can I test if 2 things are NOT Equal?<how to test if two things are NOT Equal>`
* :ref:`how can I test if 2 things are Equal?<how to test if two things are Equal>`

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

    Initialized project `assertion-error` at `.../pumping_python/assertion_error`

  then goes back to the command line

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I use rm_ to remove ``main.py`` because I do not use it in this project

  .. code-block:: shell
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I `make a directory`_ for the tests

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. DANGER:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

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

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_assertion_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_assertion_error.py

  the terminal_ goes back to the command line

* I open ``test_assertion_error.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_assertion_error.py

    `Visual Studio Code`_ opens ``test_assertion_error.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_assertion_error.py``

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

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

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

    * if your ``tests/__init__.py`` have 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
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
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
what is a variable?
*********************************************************************************

I can use a name for values when programming. This helps me avoid repetition when I have to change a value.

A variable_ is a name that is used for values that change. For example, in Mathematics_ we use ``x`` to represent any number.

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

  the test is still green

  - ``==`` is 2 equal signs - :kbd:`=+=` and means ``is equal`` which makes this statement read as ``reality is equal to my_expectation`` because

    - ``reality`` is the name or variable_ I have given to ``1 + 1``
    - ``my_expectation`` is the name or variable_ I have given to ``2``
    - in other words the statement is ``1 + 1 is equal to 2``

* I change ``my_expectation`` to make the statement :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 11
            reality == my_expectation

  the test is still green. Why?

* I want the test to fail when I write a statement that is NOT :ref:`True<test_what_is_true>`. I change it to an `assert statement`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 11
            assert reality == my_expectation

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 2 == 11

  because ``1 + 1 == 11`` is :ref:`False<test_what_is_false>`, ``2`` is NOT equal to ``11`` and I added assert_ before the statement, which tells the computer ``DO NOT CONTINUE, if 1 + 1 == 11 is False``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match ``reality`` and make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 3

      def test_what_is_an_assertion(self):
          reality = 1 + 1
          my_expectation = 2
          assert reality == my_expectation

the test passes because ``1 + 1 == 2`` is NOT :ref:`False<test_what_is_false>`, ``1 + 1 is equal to 2``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another statement

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6-8

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '2'
            reality == my_expectation


    # Exceptions seen
    # AssertionError

  the test is still green when the statement is not an assertion_

* I add assert_ before the statement to make it an assertion_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '2'
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

  because when I added assert_ before the statement it became a command to Python_ - ``DO NOT CONTINUE if "'1' + '1' == '2'" is False``

  - ``- 2`` shows my expectation - what I wrote as the result, which is what is missing from the actual result
  - ``+ 11`` shows reality - what the actual result is, , which is what is missing from my expectation

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7
    :emphasize-text: 11

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation


    # Exceptions seen

  the test passes because the statement is now :ref:`True<test_what_is_true>`

  .. NOTE::

    * these 2 statements are not the same

      - ``1 + 1 == 2`` checks if the result of :ref:`adding<test_addition>` two numbers is equal to the number on the right side of the ``==`` symbol
      - ``'1' + '1' == '11'`` checks if the result of "adding" 2 strings_ is equal to the string_ on the right side of the ``==`` symbol. A string_ is anything inside :ref:`quotes`

* I add another statement to show the difference between the statements

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10-12

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = '11'
            reality == my_expectation


    # Exceptions seen

  the test is still green because ``reality == my_expectation`` is just a statement. Python_ does not care whether it is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`. The statement follows Python_ rules.

* I change the statement to an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 12
    :emphasize-text: assert

        def test_what_is_an_assertion(self):
            reality = 1 + 1
            my_expectation = 2
            assert reality == my_expectation

            reality = '1' + '1'
            my_expectation = '11'
            assert reality == my_expectation

            reality = 'I am' + ' alive'
            my_expectation = '11'
            assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3-4

    E       AssertionError: assert 'I am alive' == '11'
    E
    E         - 11
    E         + I am alive

  because when I added assert_ before the statement it became a command to Python_ - ``DO NOT CONTINUE if "'I am' + ' alive' == '11'" is False``

  - the ``- 11`` shows my expectation - what I wrote as the result, which is what is missing from the actual result
  - the ``+ I am alive`` shows reality - what the actual result is, which is what is missing from my expectation

  .. attention:: If your result is different, check that you added a space before ``alive``, it should be ``' alive'`` not ``'alive'``. There is a space before the phrase.

* I change ``my_expectation`` to match ``reality`` and make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 11

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

  the test passes

----

*********************************************************************************
what causes AssertionError?
*********************************************************************************

AssertionError_ happens when the statement after assert_ is :ref:`False<test_what_is_false>`. It was in :ref:`how to make a python test driven development environment` with :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like this :ref:`assertion<what is an assertion?>`

.. code-block:: python

  assert True is False

With these statements, I tell Python_ - "DO NOT CONTINUE, if :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`", or said a different way "GO TO THE NEXT LINE, ONLY if :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`". I expect this line to fail because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`, they at least have different spellings. If it does not fail, then Python_ and I have a problem.

----

*********************************************************************************
test_assertion_error_w_none
*********************************************************************************

:ref:`None<what is None?>` is used when there is no value, it is the simplest :ref:`data structure<data structures>` in Python_. I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`None<what is None?>`, this is useful when I want to check what value I am getting from some process or user input.

For example, if I have people fill a form and I want a test for when they leave a value blank, I can use an :ref:`assertion<what is an assertion?>` to make sure that the process returns :ref:`None<what is None?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new failing test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 14-15

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
  :lineno-start: 19
  :emphasize-lines: 2
  :emphasize-text: is

      def test_assertion_error_w_none(self):
          assert None is None

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I can also make :ref:`assertions<what is an assertion?>` with `assert methods`_ from the `unittest.TestCase class`_, they have clearer messages

----

---------------------------------------------------------------------------------
how to test if something is NOT None
---------------------------------------------------------------------------------

----

I add a failing line with the `assertIsNotNone method`_ which checks if the thing in parentheses - ``( )``, is NOT :ref:`None<what is None?>`

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 3
  :emphasize-text: Not

      def test_assertion_error_w_none(self):
          assert None is None
          self.assertIsNotNone(None)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` with a clearer message

.. code-block:: python

  E       AssertionError: unexpectedly None

because :ref:`None<what is None?>` is ...

----

---------------------------------------------------------------------------------
how to test if something is None
---------------------------------------------------------------------------------

----

* I use the `assertIsNone method`_ which checks if the thing in parentheses is :ref:`None<what is None?>`, to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

  the test passes. I like the messages from the `assert methods`_ better

  .. code-block:: python

    E       AssertionError: unexpectedly None

  vs

  .. code-block:: python

    E       assert None is not None

  which do you like better?

* I add comments with what I learned from the experiments in the test

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6-7

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)


    # NOTES
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add a new :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`False<test_what_is_false>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1
    :emphasize-text: not

            assert False is not None

  the test passes

* I add another :ref:`assertion<what is an assertion?>` with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNone(False)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: False is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1
    :emphasize-text: Not

            self.assertIsNotNone(False)

  the test passes

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6

            assert False is not None
            self.assertIsNotNone(False)


    # NOTES
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`True<test_what_is_true>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is None


    # NOTES

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1
    :emphasize-text: not

            assert True is not None

  the test passes

* I add a failing line with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

            assert True is not None
            self.assertIsNone(True)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       AssertionError: True is not None

* I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 9

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)


    # NOTES

  the test passes

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6

            assert True is not None
            self.assertIsNotNone(True)


    # NOTES
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for an integer_ (a whole number with no decimals)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 11

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            assert 0 is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

            assert 0 is not None

  the test passes

* I add a statement with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

            assert 0 is not None
            self.assertIsNone(0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0 is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 12
    :emphasize-text: Not

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            assert 0 is not None
            self.assertIsNotNone(0)


      # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 11

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert 0 is not None
            self.assertIsNotNone(0)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-5

            an_integer = 0
            # assert 0 is not None
            assert an_integer is not None
            # self.assertIsNotNone(0)
            self.assertIsNotNone(an_integer)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)


    # NOTES

  I can change the value of the integer_ in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

    # NOTES
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a float_ (binary floating point decimal numbers)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 15

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            assert 0.0 is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 0.0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

            assert 0.0 is not None

  the test passes

* I add a statement for floats_ with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

            assert 0.0 is not None
            self.assertIsNone(0.0)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 0.0 is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2
    :emphasize-text: Not

            assert 0.0 is not None
            self.assertIsNotNone(0.0)


    # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert 0.0 is not None
            self.assertIsNotNone(0.0)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.0``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-5

            a_float = 0.0
            # assert 0.0 is not None
            assert a_float is not None
            # self.assertIsNotNone(0.0)
            self.assertIsNotNone(a_float)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)


    # NOTES

  I can change the value of the float_ in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

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
    :lineno-start: 33
    :emphasize-lines: 5

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            assert 'a string' is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert 'a string' is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

            assert 'a string' is not None

  the test passes

* I add a statement for strings_ with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

            assert 'a string' is not None
            self.assertIsNone('a string')


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: 'a string' is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2
    :emphasize-text: Not

            assert 'a string' is not None
            self.assertIsNotNone('a string')


    # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'a string'``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert 'a string' is not None
            self.assertIsNotNone('a string')


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'a string'``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-5

            a_string = 'a string'
            # assert 'a string' is not None
            assert a_string is not None
            # self.assertIsNotNone('a string')
            self.assertIsNotNone(a_string)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)


    # NOTES

  I can change the value of the string_ in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

    # NOTES
    # a string not None
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
    :lineno-start: 37
    :emphasize-lines: 5

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            assert (1, 2, 3, 'n') is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert (1, 2, 3, 'n') is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 1

            assert (1, 2, 3, 'n') is not None

  the test passes

* I add a statement for tuples_ with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

            assert (1, 2, 3, 'n') is not None
            self.assertIsNone((1, 2, 3, 'n'))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: (1, 2, 3, 'n') is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2
    :emphasize-text: Not

            assert (1, 2, 3, 'n') is not None
            self.assertIsNotNone((1, 2, 3, 'n'))


    # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``(1, 2, 3, 'n')``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            a_tuple = (1, 2, 3, 'n')
            assert (1, 2, 3, 'n') is not None
            self.assertIsNotNone((1, 2, 3, 'n'))


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``(1, 2, 3, 'n')``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-5

            a_tuple = (1, 2, 3, 'n')
            # assert (1, 2, 3, 'n') is not None
            assert a_tuple is not None
            # self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsNotNone(a_tuple)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)


    # NOTES

  I can change the value of the tuple_ in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 46
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
    :lineno-start: 41
    :emphasize-lines: 5

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)

            assert [1, 2, 3, 'n'] is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block::

    E       AssertionError: assert [1, 2, 3, 'n'] is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

            assert [1, 2, 3, 'n'] is not None

  the test passes

* I add a statement for :ref:`lists<what is a list?>` with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

            assert [1, 2, 3, 'n'] is not None
            self.assertIsNone([1, 2, 3, 'n'])


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: [1, 2, 3, 'n'] is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2
    :emphasize-text: Not

            assert [1, 2, 3, 'n'] is not None
            self.assertIsNotNone([1, 2, 3, 'n'])


    # NOTES


  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``[1, 2, 3, 'n']``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)

            a_list = [1, 2, 3, 'n']
            assert [1, 2, 3, 'n'] is not None
            self.assertIsNotNone([1, 2, 3, 'n'])


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[1, 2, 3, 'n']``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-5

            a_list = [1, 2, 3, 'n']
            # assert [1, 2, 3, 'n'] is not None
            assert a_list is not None
            # self.assertIsNotNone([1, 2, 3, 'n'])
            self.assertIsNotNone(a_list)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNotNone(a_list)


    # NOTES

  I can change the value of the :ref:`list<what is a list?>` in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

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

* I add an `assert statement`_ for a set (anything in curly braces ``{ }`` separated by a comma)

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNotNone(a_list)

            assert {1, 2, 3, 'n'} is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {1, 2, 3, 'n'} is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1

            assert {1, 2, 3, 'n'} is not None

  the test passes

* I add a statement for sets_ with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

            assert {1, 2, 3, 'n'} is not None
            self.assertIsNone({1, 2, 3, 'n'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {'n', 1, 2, 3} is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2
    :emphasize-text: Not

            assert {1, 2, 3, 'n'} is not None
            self.assertIsNotNone({1, 2, 3, 'n'})


    # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{1, 2, 3, 'n'}``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNotNone(a_list)

            a_set = {1, 2, 3, 'n'}
            assert {1, 2, 3, 'n'} is not None
            self.assertIsNotNone({1, 2, 3, 'n'})


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{1, 2, 3, 'n'}``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-5

            a_set = {1, 2, 3, 'n'}
            # assert {1, 2, 3, 'n'} is not None
            assert a_set is not None
            # self.assertIsNotNone({1, 2, 3, 'n'})
            self.assertIsNotNone(a_set)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNotNone(a_list)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNotNone(a_set)


    # NOTES

  I can change the value of the set_ in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 56
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
    :lineno-start: 49
    :emphasize-lines: 5

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNotNone(a_set)

            assert {'key': 'value'} is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert {'key': 'value'} is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 1

            assert {'key': 'value'} is not None

  the test passes

* I add a statement for :ref:`dictionaries<what is a dictionary?>` with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

            assert {'key': 'value'} is not None
            self.assertIsNone({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: {'key': 'value'} is not None

* I change assertIsNone_ to assertIsNotNone_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2
    :emphasize-text: Not

            assert {'key': 'value'} is not None
            self.assertIsNotNone({'key': 'value'})


    # NOTES

  the test passes

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``{'key': 'value'}``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 5

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNotNone(a_set)

            a_dictionary = {'key': 'value'}
            assert {'key': 'value'} is not None
            self.assertIsNotNone({'key': 'value'})


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{'key': 'value'}``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2-5

            a_dictionary = {'key': 'value'}
            # assert {'key': 'value'} is not None
            assert a_dictionary is not None
            # self.assertIsNotNone({'key': 'value'})
            self.assertIsNotNone(a_dictionary)


    # NOTES

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

            assert False is not None
            self.assertIsNotNone(False)

            assert True is not None
            self.assertIsNotNone(True)

            an_integer = 0
            assert an_integer is not None
            self.assertIsNotNone(an_integer)

            a_float = 0.0
            assert a_float is not None
            self.assertIsNotNone(a_float)

            a_string = 'a string'
            assert a_string is not None
            self.assertIsNotNone(a_string)

            a_tuple = (1, 2, 3, 'n')
            assert a_tuple is not None
            self.assertIsNotNone(a_tuple)

            a_list = [1, 2, 3, 'n']
            assert a_list is not None
            self.assertIsNotNone(a_list)

            a_set = {1, 2, 3, 'n'}
            assert a_set is not None
            self.assertIsNotNone(a_set)

            a_dictionary = {'key': 'value'}
            assert a_dictionary is not None
            self.assertIsNotNone(a_dictionary)


    # NOTES

  I can change the value of the :ref:`dictionary<what is a dictionary?>` in one place with no need to change the other lines because of the :ref:`variable<what is a variable?>`

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

:ref:`I can use assertions to test if something is None<what is None?>`

----

*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

:ref:`False<test_what_is_false>` is a simple :ref:`data type<data structures>`, it is one of the two :ref:`booleans<what are booleans?>` and is NOT :ref:`None<what is None?>`. I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`False<test_what_is_false>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 53
  :emphasize-lines: 5-6

          a_dictionary = {'key': 'value'}
          assert a_dictionary is not None
          self.assertIsNotNone(a_dictionary)

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
  :emphasize-lines: 2
  :emphasize-text: not

      def test_assertion_error_w_false(self):
          assert None is not False


  # NOTES

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10

    # NOTES
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I add an `assert statement`_ that will fail about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is not False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is not False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert False is False


    # NOTES

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 9

    # NOTES
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I add an `assert statement`_ to see if :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert None is not False
            assert True is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True is False

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3
    :emphasize-text: not

        def test_assertion_error_w_false(self):
            assert None is not False
            assert True is not False


    # NOTES

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 8

    # NOTES
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string not None
    # a float is not None
    # an integer is not None
    # True is not False
    # True is not None
    # False is not None
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError






----

----

----

----

There is an `assert method`_ to check if something is :ref:`False<test_what_is_false>`, it is the one from :ref:`the first failing test<test_failure>`

----

---------------------------------------------------------------------------------
how to test if something is False
---------------------------------------------------------------------------------

----

* I add a failing line with the `assertFalse method`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert True is not False
            self.assertFalse(True)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: True is not false

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I add comments

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 7-8

        def test_assertion_error_w_false(self):
            assert True is not False
            self.assertFalse(False)


    # NOTES
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen

:ref:`I can use assertions to test if something is False or NOT<test_assertion_error_w_false>`

----

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

:ref:`True<test_what_is_true>` is a simple :ref:`data type<data structures>`, it is the other :ref:`boolean<what are booleans?>` and is NOT :ref:`False<test_what_is_false>` or :ref:`None<what is None?>`. I can use :ref:`assertions<what is an assertion?>` to test if something is :ref:`True<test_what_is_true>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-6

      def test_assertion_error_w_false(self):
          assert True is not False
          self.assertFalse(False)

      def test_assertion_error_w_true(self):
          assert False is True


  # NOTES

the terminal_ is my friend, and shows AssertionError_

.. code-block:: python

  E    assert False is True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 1
  :emphasize-text: not

          assert False is not True

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

There is an `assert method`_ to check if something is :ref:`True<test_what_is_true>`

----

---------------------------------------------------------------------------------
how to test if something is True
---------------------------------------------------------------------------------

----

* I add a failing :ref:`assertion<what is an assertion?>` with the `assertTrue method`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

        def test_assertion_error_w_true(self):
            assert False is not True
            self.assertTrue(False)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: False is not true

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

        def test_assertion_error_w_true(self):
            assert False is not True
            self.assertTrue(True)


    # NOTES

  the test passes

* I add more comments

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7-8

        def test_assertion_error_w_true(self):
            assert False is not True
            self.assertTrue(True)


    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None

:ref:`I can use assertions to test if something is True or NOT<test_assertion_error_w_true>`

All the :ref:`assertions<what is an assertion?>` I have typed so far show that, :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different. They give me a basic expectation of Python_ because I can compare things with them.

----

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

I can use :ref:`assertions<what is an assertion?>` to test if 2 things are equal, like I did with :ref:`test_what_is_an_assertion`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

.. NOTE::

  ``!=`` is :kbd:`!+=` on the keyboard and is the symbol for ``NOT equal``

I add a new test with a failing :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-8

        def test_assertion_error_w_true(self):
            assert False is not True
            self.assertTrue(True)

        def test_assertion_error_w_equality(self):
            reality = None
            my_expectation = None
            assert reality != my_expectation


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

.. NOTE::

  ``==`` is :kbd:`=+=` on the keyboard and is the symbol for ``is equal``

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 3

      def test_assertion_error_w_equality(self):
          reality = None
          my_expectation = None
          assert reality == my_expectation

the test passes because ``None is equal to None`` is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

---------------------------------------------------------------------------------
what is the difference between ``=`` and ``==``?
---------------------------------------------------------------------------------

----

* ``=`` is the symbol for assignment or pointing, it's how to give a name (:ref:`variable<what is a variable?>`) to something in Python_, for example

  .. code-block:: python

    project_name = 'assertion_error'

  any time I use ``project_name`` after writing that line, Python_ will replace it with ``assertion_error``

* ``==`` checks if the thing on the left of ``==`` is equal to the thing on the right of ``==``, for example

  .. code-block:: python

    'thing on the left' == 'thing on the right'

----

---------------------------------------------------------------------------------
how to test if two things are NOT Equal
---------------------------------------------------------------------------------

----

There are `assert methods`_ to check if 2 things are equal or not.

* I add assertNotEqual_ which checks if the 2 things in the parentheses are NOT equal

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5
    :emphasize-text: Not

        def test_assertion_error_w_equality(self):
            reality = None
            my_expectation = None
            assert reality == my_expectation
            self.assertNotEqual(reality, my_expectation)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: None == None

----

---------------------------------------------------------------------------------
how to test if two things are Equal
---------------------------------------------------------------------------------

-----

* I change assertNotEqual_ to assertEqual_ which checks if the 2 things in the parentheses are equal

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5
    :emphasize-text: Equal

        def test_assertion_error_w_equality(self):
            reality = None
            my_expectation = None
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)


    # NOTES

  the test passes

* I add to the ``None is None`` comment

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* I add a new failing :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False == None

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

            assert False != None

  the test passes

* I add a failing :ref:`assertion<what is an assertion?>` with the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertEqual(False, None)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: False != None

* I make the statement :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6
    :emphasize-text: Not

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)


    # NOTES

  the test passes

* I add to the ``False is not None`` comment

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 7

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* I add the next failing assertion_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert True == None

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            assert True != None

  the test passes

* I add a failing :ref:`assertion<what is an assertion?>` with assertEqual_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 9

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert True != None
            self.assertEqual(True, None)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: True != None

* I make the statement :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5
    :emphasize-text: Not

            assert False != None
            self.assertNotEqual(False, None)

            assert True != None
            self.assertNotEqual(True, None)


    # NOTES

  the test passes

* I add to the ``True is not None`` comment

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 6

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* I add another failing assertion_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 11

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert True != None
            self.assertNotEqual(True, None)

            assert True == False

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True == False

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 1

            assert True != False

  the test passes

* I add a failing :ref:`assertion<what is an assertion?>` with assertEqual_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 12

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert True != None
            self.assertNotEqual(True, None)

            assert True != False
            self.assertEqual(True, False)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: True != False

* I change the `assert method`_ to assertNotEqual_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 5
    :emphasize-text: Not

            assert True != None
            self.assertNotEqual(True, None)

            assert True != False
            self.assertNotEqual(True, False)


    # NOTES

  the test passes

* I add to the ``True is not False`` comment

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* on to the next failing assertion_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 7

            assert True != None
            self.assertNotEqual(True, None)

            assert True != False
            self.assertNotEqual(True, False)

            assert False != False


    # NOTES
    # True is True
    # False is not True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False != False

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

            assert False == False

  the test passes

* I add another failing `assert statement`_ with assertNotEqual_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

            assert False == False
            self.assertNotEqual(False, False)

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: False == False

* I change assertNotEqual_ to assertEqual_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5

            assert True != False
            self.assertNotEqual(True, False)

            assert False == False
            self.assertEqual(False, False)


    # NOTES
    # True is True
    # False is not True

  the test passes

* I add to the ``False is False`` comment

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4

    # NOTES
    # True is True
    # False is not True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

----

* I add a failing `assert statement`_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7

            assert True != False
            self.assertNotEqual(True, False)

            assert False == False
            self.assertEqual(False, False)

            assert False == True


    # NOTES
    # True is True
    # False is not True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert False == True

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

            assert False != True

  the test passes

* I add another failing line with the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 5

            assert False == False
            self.assertEqual(False, False)

            assert False != True
            self.assertEqual(False, True)


    # NOTES
    # True is True
    # False is not True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: False != True

* I make the statement :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2
    :emphasize-text: Not

            assert False != True
            self.assertNotEqual(False, True)


    # NOTES

  the test passes

* I add to the ``False is not True`` comment

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines:  3

    # NOTES
    # True is True
    # False is not True and not equal to True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

----

* time for the last `assert statements`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4

            assert False != True
            self.assertNotEqual(False, True)

            assert True != True


    # NOTES
    # True is True
    # False is not True and not equal to True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E    assert True != True

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 1

              assert True == True

  the test passes

* I add a failing line with the `assertNotEqual method`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5

            assert False != True
            self.assertNotEqual(False, True)

            assert True == True
            self.assertNotEqual(True, True)


    # NOTES
    # True is True
    # False is not True and not equal to True

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    AssertionError: True == True

* I change the `assertNotEqual method`_ to the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 21

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertEqual(None, None)

            assert False != None
            self.assertNotEqual(False, None)

            assert True != None
            self.assertNotEqual(True, None)

            assert True != False
            self.assertNotEqual(True, False)

            assert False == False
            self.assertEqual(False, False)

            assert False != True
            self.assertNotEqual(False, True)

            assert True == True
            self.assertEqual(True, True)


    # NOTES

  the test passes

* I add to the ``True is True`` comment

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

    # NOTES
    # True is True and equal to True
    # False is not True and not equal to True
    # False is False and equal to False
    # True is not False and not equal to False
    # True is not None and not equal to None
    # False is not None and not equal to None
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

----

* I add calls to the `assertEqual method`_ in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5

    class TestAssertionError(unittest.TestCase):

        def test_what_is_an_assertion(self):
            assert 1 + 1 == 2
            self.assertEqual(1+1, 3)

            assert '1' + '1' == '11'
            assert 'I am' + ' alive' == 'I am alive'

        def test_assertion_error_w_none(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 3

* I change the expectation in the call to the `assertEqual method`_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1
    :emphasize-text: 2

            self.assertEqual(1+1, 2)

  the test passes

* I add assertEqual_ for the next assertion_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def test_what_is_an_assertion(self):
            assert 1 + 1 == 2
            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            self.assertEqual('1'+'1', '2')

            assert 'I am' + ' alive' == 'I am alive'

  the terminal_ is my friend, and shows

  .. code-block:: python

    AssertionError: '11' != '2'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1
    :emphasize-text: 11

            self.assertEqual('1'+'1', '11')

  the test passes

* I add assertEqual_ for the last :ref:`assertion<what is an assertion?>` in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_what_is_an_assertion(self):
            assert 1 + 1 == 2
            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            self.assertEqual('1'+'1', '11')

            assert 'I am' + ' alive' == 'I am alive'
            self.assertEqual('I am'+' alive', '11')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'I am alive' != '11'

* I make my expectation match reality

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_what_is_an_assertion(self):
            assert 1 + 1 == 2
            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            self.assertEqual('1'+'1', '11')

            assert 'I am' + ' alive' == 'I am alive'
            self.assertEqual('I am'+' alive', 'I am alive')

        def test_assertion_error_w_none(self):

  the test passes

:ref:`I can use assertions to test if 2 things are equal<test_assertion_error_w_equality>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``assertion_error.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

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

* :ref:`NOT None<test_assertion_error_w_none>` with assertIsNotNone_
* :ref:`None<test_assertion_error_w_none>` with assertIsNone_
* :ref:`False or NOT False<test_assertion_error_w_none>` with assertFalse_
* :ref:`True or NOT True<test_assertion_error_w_none>` with assertTrue_

and to test if 2 things are

* :ref:`NOT Equal<test_assertion_error_w_equality>` with assertNotEqual_
* :ref:`Equal<test_assertion_error_w_equality>` with assertEqual_

for a total of 6 `assert methods`_ I can use when testing

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
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`

:ref:`Would you like to test functions?<what is a function?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->