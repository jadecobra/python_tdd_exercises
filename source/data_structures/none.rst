.. meta::
  :description: Learn the difference between None and other Python data types. This guide explains how to check for None, and how it differs from 0 or an empty string.
  :keywords: Jacob Itegboje, python NoneType what is it, python None vs 0 vs empty string, how to check for None in python, python function returns None best practices, python None vs False, python NoneType error debugging, what is the use of None in python, python unit testing None

.. include:: ../links.rst

.. _None: https://docs.python.org/3/library/constants.html?highlight=none#None

#################################################################################
what is None?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/NKvM2yqyIrQ?si=rXBUptys2D9ns9d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

None_ is used when there is no value. It is like ``NULL`` in other languages or ``N/A`` in forms. It is the simplest :ref:`data structure<data structures>` in Python_

I use `assert methods`_ to compare None_ with the other Python_ :ref:`data structures` to see what it is and what it is not

*********************************************************************************
preview
*********************************************************************************

In :ref:`AssertionError<what causes AssertionError?>`, I used assertIsNone_ and assertIsNotNone_ to :ref:`test_assertion_error_w_none`, that experiment showed that

* :ref:`True<test_what_is_true>` is NOT None_ and NOT equal to None_
* :ref:`False<test_what_is_false>` is NOT None_ and NOT equal to None_
* None_ is None_ and equal to None_

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_none.py
  :language: python
  :linenos:

*********************************************************************************
questions about None
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is None?<test_what_is_none>`
* :ref:`Is None a boolean?<test_is_none_a_boolean>`
* :ref:`Is None an integer?<test_is_none_an_integer>`
* :ref:`Is None a float?<test_is_none_a_float>`
* :ref:`Is None a string?<test_is_none_a_string>`
* :ref:`Is None a tuple?<test_is_none_a_tuple>`
* :ref:`Is None a list?<test_is_none_a_list>`
* :ref:`Is None a set?<test_is_none_a_set>`
* :ref:`Is None a dictionary?<test_is_none_a_dictionary>`
* :ref:`how can I test if something is None?<how to test if something is None>`
* :ref:`how can I test if something is NOT None?<how to test if something is None>`
* :ref:`how can I test if something is an instance of a class?<how to test if something is an instance of a class>`
* :ref:`how can I test if something is NOT an instance of class<how to test if something is an instance of a class>`

----

*********************************************************************************
requirements
*********************************************************************************

* I name this project ``none``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir none

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd none

  the terminal_ shows I am in the ``none`` folder_

  .. code-block:: shell

    .../pumping_python/none

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/none

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/none.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/none.py`` instead of ``touch src/none.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/none.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/none

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

    touch tests/test_none.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_none.py`` instead of ``touch tests/test_none.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_none.py

  the terminal_ goes back to the command line

* I open ``test_none.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can use the terminal_ to open a file_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_. That means when I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_none.py

    `Visual Studio Code`_ opens ``test_none.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_none.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestNone(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_goes back to the command line

* I setup the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `none`

  then goes back to the command line

  .. code-block:: shell
    .../pumping_python/none (main)

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
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _________________________ TestNone.test_failure __________________________

    self = <tests.test_none.TestNone testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_none.py:7: AssertionError
    ========================= short test summary info ==========================
    FAILED tests/test_none.py::TestNone::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_none.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_none.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestNone(unittest.TestCase):

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
test_what_is_none
*********************************************************************************

We need a way to represent nothing or the absence of a value. In mathematics we use ``0`` to represent no quantity. In some languages or domains we use ``null``, in forms we use ``N/A`` when the options do not apply. In Python_ we use None_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_what_is_none``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    class TestNone(unittest.TestCase):

        def test_what_is_none(self):
            self.assertIsNotNone(None)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: unexpectedly None

  assertIsNotNone_ checks that what is in the parentheses is NOT None_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the assertIsNotNone_ to assertIsNone_, which checks if what it gets in parentheses is None_

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertIsNone(None)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I add a note

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1-2

  # NOTES
  # None is None


  # Exceptions seen
  # AssertionError

so far this is a repetition of :ref:`AssertionError<what causes AssertionError?>`

----

*********************************************************************************
test_is_none_a_boolean
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another failing test to see if None_ is a :ref:`boolean<what are booleans?>`

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 3-4

          self.assertIsNone(None)

      def test_is_none_a_boolean(self):
          self.assertIsNone(False)


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: False is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>` with the `assertIsNotNone method`_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertIsNotNone(False)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    # NOTES
    # False is NOT None
    # None is None

  Still a repetition of the lessons from :ref:`AssertionError<what causes AssertionError?>`

* I add another failing :ref:`assertion<what is an assertion?>` for the other :ref:`boolean<what are booleans?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

            self.assertIsNotNone(False)
            self.assertIsNone(True)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not None

* I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertIsNotNone(True)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    # NOTES
    # True is NOT None
    # False is NOT None
    # None is None

  more repetition

---------------------------------------------------------------------------------
how to test if something is an instance of a class
---------------------------------------------------------------------------------

The `unittest.TestCase class`_ has 2 :ref:`methods<what is a function?>` I can use to test if an :ref:`object<what is a class?>` is a child/instance of a :ref:`class<what is a class?>` or not - assertIsInstance_ and assertNotIsInstance_

* I add the `assertNotIsInstance method`_ to test if :ref:`False<test_what_is_false>` is a :ref:`boolean<what are booleans?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertIsNotNone(True)
            self.assertNotIsInstance(False, bool)

  - assertNotIsInstance_ checks if the first item it is given is NOT a child/instance of the second item. It is like asking the question, "is False NOT a child of the bool class?" Okay, this is new
  - bool_ is the :ref:`class<what is a class?>` for :ref:`booleans<what are booleans?>`

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

  :ref:`False<test_what_is_false>` is a :ref:`boolean<what are booleans?>`

* I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>` with the `assertIsInstance method`_ which checks if the first item it is given is a child/instance of the second item. It is like asking the question ``is False a child of the bool class?``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertIsInstance(False, bool)

  the test passes

* I add a failing line for the other :ref:`boolean<what are booleans?>` with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

            self.assertIsInstance(False, bool)
            self.assertNotIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

  :ref:`True<test_what_is_true>` is a :ref:`boolean<what are booleans?>`

* I make the statement :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertIsInstance(True, bool)

  the test passes

* I add assertIsInstance_ to test if None_ is a child/instance of the bool_ :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            self.assertIsInstance(True, bool)
            self.assertIsInstance(None, bool)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'bool'>

  :ref:`None<what is None?>` is NOT a :ref:`boolean<what are booleans?>`

* I make the line :ref:`True<test_what_is_true>` with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)
            self.assertNotIsInstance(None, bool)


    # NOTES

  the test passes

* Since this is about None_, I change the last 2 notes I added

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    # NOTES
    # None is NOT a boolean
    # None is None

I know two new `assert methods`_

* assertIsInstance_ to see if something is an instance of a :ref:`class<what is a class?>`
* assertNotIsInstance_ to see if something is NOT an instance of a :ref:`class<what is a class?>`

.. CAUTION:: the naming of the `assert methods`_ can be confusing, there is

                  assertIsNotNone_

  where ``Not`` comes after ``Is`` and then there is

                  assertNotIsInstance_

  where ``Is`` comes after ``Not``. Maybe ``assertIsNotInstance`` would have been better, since ``assertNotIsNone`` does not sound better than ``assertIsNotNone``. Naming things is its own challenge

----

*********************************************************************************
test_is_none_an_integer
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if None_ is an integer_ (a whole number)

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, bool)

      def test_is_none_an_integer(self):
          self.assertIsNone(-1)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -1 is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 1

          self.assertIsNotNone(-1)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a new failing line with assertIsNone_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

            self.assertIsNotNone(-1)
            self.assertIsNone(0)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0 is not None

  I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertIsNotNone(0)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

            self.assertIsNotNone(0)
            self.assertIsNone(1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 1 is not None

  I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

            self.assertIsNotNone(1)

  the test passes

* I add a new failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

            self.assertIsNotNone(1)
            self.assertNotIsInstance(-1, int)

  int_ is the :ref:`class<what is a class?>` for integers_, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: -1 is an instance of <class 'int'>

  I use ``-1`` for all the integers_ (whole numbers) that are smaller than ``0``

* I make the line :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

            self.assertIsInstance(-1, int)

  the test passes

* I add another failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2

            self.assertIsInstance(-1, int)
            self.assertNotIsInstance(0, int)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0 is an instance of <class 'int'>

  ``0`` is an integer_

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

            self.assertIsInstance(0, int)

  the test passes

* I add another failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

            self.assertIsInstance(0, int)
            self.assertNotIsInstance(1, int)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 1 is an instance of <class 'int'>

  I use ``1`` for all the integers_ (whole numbers) that are bigger than ``0``

* I make the failing line :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

            self.assertIsInstance(1, int)

  the test passes

* I add one more failing line with to test if None_ is an integer_ with assertIsInstance_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2

            self.assertIsInstance(1, int)
            self.assertIsInstance(None, int)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'int'>

* I make the line :ref:`True<test_what_is_true>` with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 8

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertIsInstance(0, int)
            self.assertIsInstance(1, int)
            self.assertNotIsInstance(None, int)


    # NOTES

  the test passes

* I add a new note

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

    # NOTES
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_float
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if None_ is a float_ (floating point decimal number)

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, int)

      def test_is_none_a_float(self):
          self.assertIsNone(-0.1)


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -0.1 is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 1

          self.assertIsNotNone(-0.1)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line with assertIsNone_

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

            self.assertIsNotNone(-0.1)
            self.assertIsNone(0.0)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 is not None

  I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 1

            self.assertIsNotNone(0.0)

  the test passes

* I add a failing line with assertIsNone_

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

            self.assertIsNotNone(0.0)
            self.assertIsNone(0.1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.1 is not None

  I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            self.assertIsNotNone(0.1)

  the test passes

* time for instance tests. I add a failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2

            self.assertIsNotNone(0.1)
            self.assertNotIsInstance(-0.1, float)

  float_ is the :ref:`class<what is a class?>` for floating point numbers. The terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: -0.1 is an instance of <class 'float'>

  I use ``-0.1`` for all the floating point numbers that are smaller than ``0.0``

* I make the statement :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 1

            self.assertIsInstance(-0.1, float)

  the test passes

* I add the next instance test with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

            self.assertIsInstance(-0.1, float)
            self.assertNotIsInstance(0.0, float)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 is an instance of <class 'float'>

  ``0.0`` is a floating point number

* I make the statement :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1

            self.assertIsInstance(0.0, float)

  the test passes

* I add a failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

            self.assertIsInstance(0.0, float)
            self.assertNotIsInstance(0.1, float)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.1 is an instance of <class 'float'>

  I use ``0.1`` for all the floating point numbers that are bigger than ``0.0``

* I make the statement :ref:`True<test_what_is_true>` with assertIsInstance_

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1

            self.assertIsInstance(0.1, float)

  the test passes

* I add one more failing line with the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

            self.assertIsInstance(0.1, float)
            self.assertIsInstance(None, float)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'float'>

  I make the statement :ref:`True<test_what_is_true>` with the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 8

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)
            self.assertIsInstance(0.1, float)
            self.assertNotIsInstance(None, float)


    # NOTES

  the test passes

* I add a new note

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    # NOTES
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_string
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if None_ is a string_ (anything inside :ref:`quotes`)

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, float)

      def test_is_none_a_string(self):
          self.assertIsNone('')


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: '' is not None

the empty string_ (``''``) is NOT :ref:`None<what is None?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with assertIsNotNone_

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 1

          self.assertIsNotNone('')

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line with assertIsNone_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

            self.assertIsNotNone('')
            self.assertIsNone("text")

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'text' is not None

  I change the `assert method`_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

            self.assertIsNotNone("text")

  the test passes

* I add a failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

            self.assertIsNotNone("text")
            self.assertNotIsInstance('', str)

  str_ is the :ref:`class<what is a class?>` for strings_. The terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: '' is an instance of <class 'str'>

  because anything in :ref:`quotes` is a string_

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

            self.assertIsInstance('', str)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

            self.assertIsInstance('', str)
            self.assertNotIsInstance("text", str)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'text' is an instance of <class 'str'>

  because anything in :ref:`quotes` is a string_

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1

            self.assertIsInstance("text", str)

  A string_ is anything in single, double or triple :ref:`quotes`, for example

  - ``'single quotes'``
  - ``'''triple single quotes'''``
  - ``"double quotes"``
  - ``"""triple double quotes"""``

  see :ref:`quotes` for more

* I add another failing line with assertIsInstance_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

            self.assertIsInstance("text", str)
            self.assertIsInstance(None, str)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'str'>

  I change the `assert method`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertIsInstance('', str)
            self.assertIsInstance("text", str)
            self.assertNotIsInstance(None, str)


    # NOTES

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

    # NOTES
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_tuple
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see if None_ is a tuple_ (anything in parentheses (``()``)), pronounced ``two-pull``

.. code-block:: python
  :lineno-start: 39
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, str)

      def test_is_none_a_tuple(self):
          self.assertIsNone(())


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: () is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 1

          self.assertIsNotNone(())

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a failing :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

            self.assertIsNotNone(())
            self.assertIsNone((1, 2, 3, 'n'))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is not None

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1

            self.assertIsNotNone((1, 2, 3, 'n'))

  the test passes

* I add a failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertNotIsInstance((), tuple)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: () is an instance of <class 'tuple'>

  because anything in parentheses (``()``) in Python_ is a tuple_

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 1

            self.assertIsInstance((), tuple)

  the test passes

* I add another failing line

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

            self.assertIsInstance((), tuple)
            self.assertNotIsInstance((1, 2, 3, 'n'), tuple)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is an instance of <class 'tuple'>

  because anything in parentheses (``()``) in Python_ is a tuple_

* I change the `assert method`_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 1

            self.assertIsInstance((1, 2, 3, 'n'), tuple)

  the test passes

* I add one more instance test

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

            self.assertIsInstance((1, 2, 3, 'n'), tuple)
            self.assertIsInstance(None, tuple)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'tuple'>

  I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsInstance((), tuple)
            self.assertIsInstance((1, 2, 3, 'n'), tuple)
            self.assertNotIsInstance(None, tuple)


    # NOTES

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    # NOTES
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

  it looks like None_ is None_ and not anything else

----

*********************************************************************************
test_is_none_a_list
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to see if None_ is a :ref:`list<lists>` (anything in square brackets (``[]``))

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, tuple)

      def test_is_none_a_list(self):
          self.assertIsNone([])


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: [] is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 1

          self.assertIsNotNone([])

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

            self.assertIsNotNone([])
            self.assertIsNone([1, 2, 3, 'n'])

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is not None

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 1

            self.assertIsNotNone([1, 2, 3, 'n'])

  the test passes

* I add a failing instance test

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2

            self.assertIsNotNone([1, 2, 3, 'n'])
            self.assertNotIsInstance([], list)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [] is an instance of <class 'list'>

  because anything in square brackets (``[]``) in Python_ is a :ref:`list<lists>`

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 1

            self.assertIsInstance([], list)

  the test passes

* I add another failing line with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

            self.assertIsInstance([], list)
            self.assertNotIsInstance([1, 2, 3, 'n'], list)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is an instance of <class 'list'>

  because anything in square brackets (``[]``) in Python_ is a :ref:`list<lists>`

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 1

        self.assertIsInstance([1, 2, 3, 'n'], list)

  the test passes

* I add one more failing line with the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertIsInstance(None, list)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'list'>

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 6

        def test_is_none_a_list(self):
            self.assertIsNotNone([])
            self.assertIsNotNone([1, 2, 3, 'n'])
            self.assertIsInstance([], list)
            self.assertIsInstance([1, 2, 3, 'n'], list)
            self.assertNotIsInstance(None, list)


    # NOTES

  the test passes

* I add a new note

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

    # NOTES
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_set
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I want to see if None_ is a set_

.. code-block:: python
  :lineno-start: 53
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, list)

      def test_is_none_a_set(self):
          self.assertIsNone(set())

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: set() is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 56
  :emphasize-lines: 1

              self.assertIsNotNone(set())

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2

            self.assertIsNotNone(set())
            self.assertIsNone({1, 2, 3, 'n'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is not None

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1

            self.assertIsNotNone({1, 2, 3, 'n'})

  the test passes

* I add an instance test

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

            self.assertIsNotNone({1, 2, 3, 'n'})
            self.assertNotIsInstance({1, 2, 3, 'n'}, set)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is an instance of <class 'set'>

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 1

            self.assertIsInstance({1, 2, 3, 'n'}, set)

  the test passes

* I add another instance test

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

            self.assertIsInstance({1, 2, 3, 'n'}, set)
            self.assertIsInstance(None, set)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'set'>

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 5

        def test_is_none_a_set(self):
            self.assertIsNotNone(set())
            self.assertIsNotNone({1, 2, 3, 'n'})
            self.assertIsInstance({1, 2, 3, 'n'}, set)
            self.assertNotIsInstance(None, set)


    # NOTES

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2

    # NOTES
    # None is NOT a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_dictionary
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

One last test to see if None_ is a :ref:`dictionary<dictionaries>`

.. code-block:: python
  :lineno-start: 59
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, set)

      def test_is_none_a_dictionary(self):
          self.assertIsNone(dict())


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: {} is not None

wait a minute! Python_ uses ``{}`` for sets_. It also uses them for :ref:`dictionaries` with a difference.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 1

          self.assertIsNotNone(dict())

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2

            self.assertIsNotNone(dict())
            self.assertIsNone({'key': 'value'})

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is not None

  I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 1

            self.assertIsNotNone({'key': 'value'})

  the test passes

* I add a failing instance test

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

            self.assertIsNotNone({'key': 'value'})
            self.assertNotIsInstance({}, dict)

  :ref:`dict<dictionaries>` is the :ref:`class<what is a class?>` for :ref:`dictionaries`, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {} is an instance of <class 'dict'>

  ``{}`` is the empty :ref:`dictionary<dictionaries>`

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 1

            self.assertIsInstance({}, dict)

  the test passes

* I add another instance test

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2

            self.assertIsInstance({}, dict)
            self.assertNotIsInstance({'key': 'value'}, dict)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is an instance of <class 'dict'>

  ``{'key': 'value'}`` is a :ref:`dictionary<dictionaries>` with ``:`` separating the :ref:`key<test_keys_of_a_dictionary>` on the left from the :ref:`value<test_values_of_a_dictionary>` on the right.

  I can add more :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` separating them with commas.

  sets_ do NOT have key-value pairs.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 1

            self.assertIsInstance({'key': 'value'}, dict)

  the test passes

* I add the last failing instance test with assertIsInstance_

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2

            self.assertIsInstance({'key': 'value'}, dict)
            self.assertIsInstance(None, dict)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'dict'>

  I make the statement :ref:`True<test_what_is_true>` with assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 6

        def test_is_none_a_dictionary(self):
            self.assertIsNotNone(dict())
            self.assertIsNotNone({'key': 'value'})
            self.assertIsInstance({}, dict)
            self.assertIsInstance({'key': 'value'}, dict)
            self.assertNotIsInstance(None, dict)


    # NOTES

  the test passes

* I add the last note

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    # NOTES
    # None is NOT a dictionary
    # None is NOt a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/none

* I `change directory`_ to the parent of ``none``

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

I used `assert methods`_ to test what None_ is and what it is NOT. I used 2 that were in :ref:`AssertionError<what causes AssertionError?>`

* assertIsNone_ - which tests if the thing in parentheses is None_
* assertIsNotNone_ - which tests if the thing in parentheses is not None_

and 2 new `assert methods`_

* assertIsInstance_ which checks if something is an instance of a given :ref:`class<what is a class?>`
* assertNotIsInstance_ which checks if something is NOT an instance of a given :ref:`class<what is a class?>`

I also showed the basic Python_ :ref:`data structures`

* None_ - the simplest
* integers_ - whole numbers, negative and positive
* floats_ - floating point decimal numbers
* strings_ - anything inside :ref:`quotes`
* :ref:`booleans<what are booleans?>` - :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>`
* tuples_ - anything in parentheses (``()``) separated by commas
* :ref:`lists` - anything in square brackets (``[]``) separated by commas
* sets_ - anything in curly braces (``{}``) separated by commas but NOT :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`
* :ref:`dictionaries` - :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces (``{}``)

:ref:`How many questions can you answer after going through this chapter?<questions about None>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: None: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

so far you have covered

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>` and
* :ref:`what is None and NOT None and learned new assert methods<what is None?>`

:ref:`Would you like to test what is True and False in Python?<what are booleans?>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->