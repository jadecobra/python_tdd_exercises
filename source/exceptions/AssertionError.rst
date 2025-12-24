.. meta::
  :description: Master Python's AssertionError for robust testing. Learn to use assert for debugging, handle exceptions, and see practical unittest examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python AssertionError example, how to handle AssertionError in Python, python unittest assert examples, python assert for debugging, python assert best practices, python custom AssertionError message, python testing with pytest and assert

.. include:: ../links.rst

.. _AssertionError: https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError

#################################################################################
AssertionError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
what is an assertion?
*********************************************************************************

I can use assertions_ when making a program_ to make sure something is :ref:`True<test_what_is_true>` before it continues. I can also use them to test how the program_ behaves, for example when it is given inputs.

Assertions_ can help catch things that break passing tests when I add new lines of code. They also help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations (tests and ideas) and reality (what happens when the program_ runs), tells me what to change to make them match. The closer my program_ is to reality, the better.

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_assertion_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about AssertionError
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`What is an assertion?<what is an assertion?>`
* :ref:`What causes AssertionError?<what causes AssertionError?>`
* :ref:`How can I test if something is NOT None?<how to test if something is NOT None>`
* :ref:`How can I test if something is None?<how to test if something is None>`
* :ref:`How can I test if something is False?<how to test if something is False>`
* :ref:`How can I test if something is NOT False?<how to test if something is True>`
* :ref:`How can I test if something is True?<how to test if something is True>`
* :ref:`How can I test if something is NOT True?<how to test if something is False>`
* :ref:`How can I test if 2 things are NOT Equal?<how to test if two things are NOT Equal>`
* :ref:`How can I test if 2 things are Equal?<how to test if two things are Equal>`

----

*********************************************************************************
start the project
*********************************************************************************

* I choose ``assertion_error`` as the name of this project
* I open a terminal_
* then I `make a directory`_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir assertion_error

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am now in the ``assertion_error`` folder_

  .. code-block:: shell

    .../pumping_python/assertion_error

* I `make a folder`_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/assertion_error

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/assertion_error.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item src/assertion_error.py`` instead of ``touch src/assertion_error.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/assertion_error.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/assertion_error

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I use touch_ to make an empty file_ in the ``tests`` folder_ to tell Python_ that it is a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_assertion_error.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/test_assertion_error.py`` instead of ``touch tests/test_assertion_error.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_assertion_error.py

  the terminal_ goes back to the command line

* I open ``test_assertion_error.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_ with

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_assertion_error.py

    ``test_assertion_error.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a `virtual environment`_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/assertion_error

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file for the `Python programs`_ my project needs

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to use the requirements file_ to install ``pytest-watch``

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloads and installs the `Python programs`_ that `pytest-watch`_ needs to run

* I use `pytest-watch`_ to run the test

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    ____________________ TestAssertionError.test_failure _____________________

    self = <tests.test_assertion_error.TestAssertionError testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_assertion_error.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_assertion_error.py::TestAssertionError::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_assertion_error.py:7`` to open it in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_what_is_an_assertion
*********************************************************************************

We know that the result of ``1 + 1`` is ``2``, but what if I said that ``'1' + '1'`` is ``'11'``, would you agree?

I can use assertions_ to make the computer check if these statements are :ref:`True<test_what_is_true>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I change ``test_failure`` to ``test_what_is_an_assertion`` with the first statement

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestAssertionError(unittest.TestCase):

        def test_what_is_an_assertion(self):
            1 + 1 == 2


    # Exceptions seen
    # AssertionError

  ``==`` (:kbd:`=+=`)  is the symbol for ``is equal`` which makes this statement read as ``1 + 1 is equal to 2``. The terminal_ still shows green

* I change the statement to make it :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            1 + 1 == 11

  the terminal_ still shows green.

* I want the test to fail when I write a statement that is not :ref:`True<test_what_is_true>`. I change it to an `assert statement`_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            assert 1 + 1 == 11

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    E       assert (1 + 1) == 11

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          assert 1 + 1 == 2

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another statement

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            assert 1 + 1 == 2
            '1' + '1' == '2'


    # Exceptions seen

  the test is still green

* I add assert_ before the statement

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            assert 1 + 1 == 2
            assert '1' + '1' == '2'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 3-4

    E       AssertionError: assert '11' == '2'
    E
    E         - 2
    E         + 11

  - ``- 2`` shows my expectation - what I wrote as the result
  - ``+ 11`` shows reality - what the actual result is

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :emphasize-lines: 1
    :lineno-start: 8

            assert '1' + '1' == '11'

  the test passes

* It is important to note that these 2 statements are not the same

  - ``1 + 1 == 2`` checks if the result of :ref:`adding<test_addition>` two numbers is equal to the number on the right side of the ``==`` symbol
  - ``'1' + '1' == '11'`` checks if the result of "adding" 2 strings_ is equal to the string_ on the right side of the ``==`` symbol. A string_ is any characters inside :ref:`quotes`, for example

    * ``'single quotes'``
    * ``'''triple single quotes'''``
    * ``"double quotes"``
    * ``"""triple double quotes"""``

  I add another statement to show this

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

            assert '1' + '1' == '11'
            'I am' + ' a programmer' == '11'

  the test is still green

* I change the statement to an `assertion`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            assert 'I am' + ' a programmer' == '11'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 3-4

    E       AssertionError: assert 'I am a programmer' == '11'
    E
    E         - 11
    E         + I am a programmer

  - the ``- 11`` shows my expectation - what I wrote as the result
  - the ``+ I am a programmer`` shows reality - what the actual result is

* I make the assertion_ :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            assert 'I am' + ' a programmer' == 'I am a programmer'

  the test passes

---------------------------------------------------------------------------------
what causes AssertionError?
---------------------------------------------------------------------------------

AssertionError_ happens when the statement after assert_ is :ref:`False<test_what_is_false>`. It was in :ref:`how to make a python test driven development environment` with :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like this `assertion`_

.. code-block:: python

  assert True is False

I think of an `assert statement`_ as a command to the computer saying "DO NOT CONTINUE, UNLESS THIS STATEMENT IS TRUE". The statement above can be thought of as "DO NOT CONTINUE, UNLESS :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`". I expect this line to fail because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`. If it does not fail, then Python_ and I have a problem

----

*********************************************************************************
test_assertion_error_w_none
*********************************************************************************

:ref:`None` is used when there is no value, it is the simplest :ref:`data structure<data structures>` in Python_. I can use assertions_ to test if something is :ref:`None`.

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a new failing test

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

            assert 'I am' + ' a programmer' == 'I am a programmer'

        def test_assertion_error_w_none(self):
            assert None is not None


    # Exceptions seen

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert None is not None

  the `assert statement`_ is :ref:`False<test_what_is_false>`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the line to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 1

          assert None is None

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I can also make assertions_ with `assert methods`_ from the `unittest.TestCase class`_, they have more descriptive messages

---------------------------------------------------------------------------------
how to test if something is NOT None
---------------------------------------------------------------------------------

I add another failing line with the `assertIsNotNone method`_ which checks if the thing in parentheses (``()``) is NOT :ref:`None`

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 3

      def test_assertion_error_w_none(self):
          assert None is None
          self.assertIsNotNone(None)

the terminal_ shows :ref:`AssertionError` with a more descriptive message

.. code-block:: shell

  AssertionError: unexpectedly None

---------------------------------------------------------------------------------
how to test if something is None
---------------------------------------------------------------------------------

* I change the statement to use the `assertIsNone method`_ which checks if the thing in parentheses is :ref:`None`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

        def test_assertion_error_w_none(self):
            assert None is None
            self.assertIsNone(None)

  the test passes. I like the messages from the `assert methods`_ better

* I add a note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4-5

              self.assertIsNone(None)


    # NOTES
    # None is None


    # Exceptions seen
    # AssertionError

* I add a new :ref:`assertion<AssertionError>` to compare :ref:`None` with :ref:`False<test_what_is_false>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

            self.assertIsNone(None)

            assert False is None

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False is None

  I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            assert False is not None

  the test passes

* I add another assertion_ with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

            assert False is not None
            self.assertIsNone(False)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: False is not None

* I change assertIsNone_ to assertIsNotNone_ to make the assertion_ :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertIsNotNone(False)

  the test passes

* I add another note

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    # NOTES
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

* I add another :ref:`assertion<AssertionError>` to compare :ref:`None` with :ref:`True<test_what_is_true>`, another simple :ref:`data structure<data structures>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

            self.assertIsNotNone(False)

            assert True is None


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            assert True is not None

  the test passes

* I add a failing line with the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

            assert True is not None
            self.assertIsNone(True)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: True is not None

* I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

            assert True is not None
            self.assertIsNotNone(True)


    # NOTES

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2

    # NOTES
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

I can use assertions_ to test if something is :ref:`None`

----

*********************************************************************************
test_assertion_error_w_false
*********************************************************************************

:ref:`False<test_what_is_false>` is a simple :ref:`data structures` , it is one of the two :ref:`boolean<booleans>` and is not :ref:`None`. I can use assertions_ to test if something is :ref:`False<test_what_is_false>` or not

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 3-4

          self.assertIsNotNone(True)

      def test_assertion_error_w_false(self):
          assert True is False


  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert True is False

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the `assertion`_ to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 1

          assert True is not False

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

There is an `assert method`_ to check if something is :ref:`False<test_what_is_false>`, it is the one from :ref:`the first failing test<test_failure>`

---------------------------------------------------------------------------------
how to test if something is False
---------------------------------------------------------------------------------

* I add a failing line with the `assertFalse method`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3

        def test_assertion_error_w_false(self):
            assert True is not False
            self.assertFalse(True)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: True is not false

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

            self.assertFalse(False)


    # NOTES

  the test passes

* I add notes

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-3

    # NOTES
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

I can use assertions_ to test if something is :ref:`False<test_what_is_false>` or :ref:`None`

----

*********************************************************************************
test_assertion_error_w_true
*********************************************************************************

:ref:`True<test_what_is_true>` is a simple :ref:`data structures`, it the other :ref:`boolean<booleans>` and is not :ref:`False<test_what_is_false>` or :ref:`None`. I can use assertions_ to test if something is :ref:`True<test_what_is_true>` or not

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 3-4

          self.assertFalse(False)

      def test_assertion_error_w_true(self):
          assert False is True


  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert False is True

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 1

          assert False is not True

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

There is an `assert method`_ to check if something is :ref:`True<test_what_is_true>`

---------------------------------------------------------------------------------
how to test if something is True
---------------------------------------------------------------------------------

* I add a failing assertion_ with the `assertTrue method`_

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

            assert False is not True
            self.assertTrue(False)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: False is not true

* I change the assertion_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 1

            self.assertTrue(True)


    # NOTES

  the test passes

* I add more notes

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

    # NOTES
    # True is True
    # False is not True
    # False is False
    # True is not False
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

I can use assertions_ to test if something is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` or :ref:`None`

All the assertions_ I have typed so far show that, :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None` are different. They give me a basic expectation of Python_ because I can compare things with them.

----

*********************************************************************************
test_assertion_error_w_equality
*********************************************************************************

I can use assertions_ to test if 2 things are equal, like I did with :ref:`test_what_is_an_assertion`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new failing test

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 3-4

          self.assertTrue(True)

      def test_assertion_error_w_equality(self):
          assert None != None


  # NOTES

the terminal_ shows AssertionError_

.. code-block:: python

  E    assert None != None

``!=`` (:kbd:`!+=`) is the symbol for ``NOT equal`` which makes this statement read as ``assert None is NOT equal to None`` or "DO NOT CONTINUE unless None is NOT equal to None"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the assertion_ to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 1

          assert None == None

the test passes.

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

---------------------------------------------------------------------------------
What is the difference between ``=`` and ``==``?
---------------------------------------------------------------------------------

* ``=`` is the symbol for assignment or pointing, it's how to give a name to something in Python_, for example

  .. code-block:: python

    project_name = 'assertion_error'

  any time I use ``project_name`` after writing that line, Python_ will replace it with ``assertion_error`` just like in :ref:`how to make a python test driven development environment` where I give a variable_ as the name of the project in :ref:`makePythonTdd.sh` or :ref:`makePythonTdd.ps1`

* ``==`` checks if the thing on the left of the symbol is equal to the thing on the right of the symbol

---------------------------------------------------------------------------------
how to test if two things are NOT Equal
---------------------------------------------------------------------------------

There are `assert methods`_ to check if 2 things are equal or not.

* I add assertNotEqual_ which checks if the 2 things in the parentheses are NOT equal

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

        def test_assertion_error_w_equality(self):
            assert None == None
            self.assertNotEqual(None, None)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: None == None

---------------------------------------------------------------------------------
how to test if two things are Equal
---------------------------------------------------------------------------------

* I change assertNotEqual_ to assertEqual_ which checks if the 2 things in the parentheses are equal

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1

            self.assertEqual(None, None)

  the test passes

* I add to the notes

  .. code-block:: python
    :lineno-start: 34
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

* I add a new failing assertion_ to compare :ref:`False<test_what_is_false>` with :ref:`None`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

            self.assertEqual(None, None)

            assert False == None


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

            assert False != None

  the test passes

* I add a failing assertion_ with the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

            assert False != None
            self.assertEqual(False, None)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: False != None

* I make the statement :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1

            self.assertNotEqual(False, None)

  the test passes

* I add to the notes

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
    :lineno-start: 33
    :emphasize-lines: 4

            assert False != None
            self.assertNotEqual(False, None)

            assert True == None

    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True == None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            assert True != None

  the test passes

* I add a failing assertion_ with assertEqual_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

            assert True != None
            self.assertEqual(True, None)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: True != None

* I make the assertion_ :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

            self.assertNotEqual(True, None)

  the test passes

* I add a note

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
    :lineno-start: 36
    :emphasize-lines: 4

            assert True != None
            self.assertNotEqual(True, None)

            assert True == False


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True == False

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 1

            assert True != False

  the test passes

* I add a failing assertion_ with assertEqual_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2

            assert True != False
            self.assertEqual(True, False)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: True != False

* I change the `assert method`_ to assertNotEqual_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1

            self.assertNotEqual(True, False)

  the test passes

* I add a note

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
    :lineno-start: 40
    :emphasize-lines: 3

            self.assertNotEqual(True, False)

            assert False != False


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False != False

* I make the assertion_ :ref:`True<test_what_is_true>`

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

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: False == False

* I change assertNotEqual_ to assertEqual_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1

            self.assertEqual(False, False)

  the test passes

* I add a note

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

* I add a failing `assert statement`_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

            self.assertEqual(False, False)

            assert False == True


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert False == True

* I change the assertion_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

            assert False != True

  the test passes

* I add another failing line with the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

            assert False != True
            self.assertEqual(False, True)

  the terminal_ shows AssertionError_

  .. code-block:: shell

    AssertionError: False != True

* I make the statement :ref:`True<test_what_is_true>` with assertNotEqual_

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 1

            self.assertNotEqual(False, True)

  the test passes

* I add another note

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

* time for the last `assert statements`_

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

            self.assertNotEqual(False, True)

            assert True != True


    # NOTES

  the terminal_ shows AssertionError_

  .. code-block:: python

    E    assert True != True

* I make the assertion_ :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 1

              assert True == True

  the test passes

* I add a failing line with the `assertNotEqual method`_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

              assert True == True
              self.assertNotEqual(True, True)

  the terminal_ shows AssertionError_

  .. code-block:: shell

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

* I add a note for the last statement

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

* I add calls to the `assertEqual method`_ in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    class TestAssertionError(unittest.TestCase):

        def test_what_is_an_assertion(self):
            assert 1 + 1 == 2
            self.assertEqual(1+1, 3)

            assert '1' + '1' == '11'
            assert 'I am' + ' a programmer' == 'I am a programmer'

        def test_assertion_error_w_none(self):

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 2 != 3

* I change the expectation in the call to the `assertEqual method`_ to make the assertion_ :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1

            self.assertEqual(1+1, 2)

  the test passes

* I add assertEqual_ for the next assertion_

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4-5

            self.assertEqual(1+1, 2)

            assert '1' + '1' == '11'
            self.assertEqual('1'+'1', '2')

            assert 'I am' + ' a programmer' == 'I am a programmer'

  the terminal_ shows

  .. code-block:: shell

    AssertionError: '11' != '2'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertEqual('1'+'1', '11')

  the test passes

* I add assertEqual_ for the last assertion_ in :ref:`test_what_is_an_assertion`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-5

            self.assertEqual('1'+'1', '11')

            assert 'I am' + ' a programmer' == 'I am a programmer'
            self.assertEqual('I am'+' a programmer', '11')

        def test_assertion_error_w_none(self):

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I am a programmer' != '11'

* I make the expectation match reality

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertEqual('I am'+' a programmer', 'I am a programmer')

  the test passes

I can use assertions_ to test if 2 things are equal

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I had open in the :ref:`editor(s)<2 editors>`
* I exit the tests in the terminal_ with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/assertion_error

* I `change directory`_ to the parent of ``assertion_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

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

*********************************************************************************
what is next?
*********************************************************************************

Congratulations! You now know

* :ref:`how to make a test driven development environment any time you want<how to make a test driven development environment>` and
* :ref:`how to raise AssertionError with assert methods<AssertionError>`

:ref:`Would you like to test functions?<functions>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->