.. meta::
  :description: Learn the difference between None and other Python data types. This guide explains how to check for None, and how it differs from 0 or an empty string.
  :keywords: Jacob Itegboje, python NoneType what is it, python None vs 0 vs empty string, how to check for None in python, python function returns None best practices, python None vs False, python NoneType error debugging, what is the use of None in python, python unit testing None

.. include:: ../links.rst

.. _None: https://docs.python.org/3/library/constants.html?highlight=none#None

#################################################################################
None
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/NKvM2yqyIrQ?si=rXBUptys2D9ns9d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

None_ is used when there is no value

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``none`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh none

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 none

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python
    :emphasize-lines: 1

    E       AssertionError: True is not false

    tests/test_none.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_none.py:7`` to open it in the editor
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to make the statement :ref:`True<test_what_is_true>` the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4

    class TestNone(unittest.TestCase):

*********************************************************************************
test_what_is_none
*********************************************************************************

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_what_is_none``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    class TestNone(unittest.TestCase):

        def test_what_is_none(self):
            self.assertIsNotNone(None)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: unexpectedly None

  assertIsNotNone_ checks that what it gets in parentheses is NOT None_

green: make it pass
#################################################################################

* I change the :ref:`assertion<AssertionError>` to assertIsNone_, which checks if what it gets in parentheses is None_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

        def test_what_is_none(self):
            self.assertIsNone(None)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1-2

    # NOTES
    # None is None


    # Exceptions Encountered
    # AssertionError

----

*********************************************************************************
test_is_none_a_boolean
*********************************************************************************

red: make it fail
#################################################################################

I add another failing test to see if None_ is a :ref:`boolean<booleans>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-5

      def test_what_is_none(self):
          self.assertIsNone(None)

      def test_is_none_a_boolean(self):
          self.assertIsNone(False)

  # NOTES
  ...

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not None

green: make it pass
#################################################################################

I add a note

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2

  # NOTES
  # False is NOT None
  # None is None

then I change the :ref:`assertion<AssertionError>`

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 2

      def test_is_none_a_boolean(self):
          self.assertIsNotNone(False)

the test passes

refactor: make it better
#################################################################################

* I add another failing line for the other :ref:`boolean<booleans>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNone(True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not None

* I add a note

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    # NOTES
    # True is NOT None
    # False is NOT None
    # None is None

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)

  the test passes

* The `unittest.TestCase`_ :ref:`class<classes>` has 2 :ref:`methods<functions>` I can use to test if an :ref:`object<classes>` is a child of a :ref:`class<classes>` or not, I use them to test if :ref:`None` is a :ref:`boolean<booleans>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertNotIsInstance(False, bool)

  I use the assertNotIsInstance_ :ref:`method<functions>` to test if :ref:`False<test_what_is_false>` is NOT a child of the :ref:`bool<booleans>` :ref:`class<classes>`. The terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

  :ref:`False<test_what_is_false>` is a :ref:`boolean<booleans>`. I change the :ref:`assertion<AssertionError>` to assertIsInstance_ to show that :ref:`False<test_what_is_false>` is a child of the bool_ :ref:`class<classes>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)

  the test passes

* I use assertNotIsInstance_ with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertNotIsInstance(True, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

  :ref:`True<test_what_is_true>` is a :ref:`boolean<booleans>`

* I use the assertIsInstance_ :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)

  the test passes

* I add another :ref:`assertion<AssertionError>` to test if None_ is a child of the :ref:`boolean<booleans>` :ref:`class<classes>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)
            self.assertIsInstance(None, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'bool'>

  :ref:`None` is NOT a :ref:`boolean<booleans>`

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)
            self.assertNotIsInstance(None, bool)

  the test passes

* I change the last 2 notes I added

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    # NOTES
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_an_integer
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if None_ is an integer_ (a whole number)

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, bool)

      def test_is_none_an_integer(self):
          self.assertIsNone(-1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not None

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 2

      def test_is_none_an_integer(self):
          self.assertIsNotNone(-1)

the test passes

refactor: make it better
#################################################################################

* I add a new line

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNone(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNone(1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)

  the test passes

* I add assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertNotIsInstance(-1, int)

  int_ is the :ref:`class<classes>` for integers_, the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: -1 is an instance of <class 'int'>

  ``-1`` is an integer_ for the positive integers_

* I use assertIsInstance_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)

  the test passes

* I add another instance test

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertNotIsInstance(0, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 is an instance of <class 'int'>

  ``0`` is an integer_

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertIsInstance(0, int)

  the test passes

* I add another failing line

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertIsInstance(0, int)
            self.assertNotIsInstance(1, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 is an instance of <class 'int'>

  ``1`` is for the positive integers_

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertIsInstance(0, int)
            self.assertIsInstance(1, int)

  the test passes

* one more instance test

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
            self.assertIsInstance(None, int)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'int'>

* I use assertNotIsInstance_

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

  the test passes

* I add a new note

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    # NOTES
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

----

*********************************************************************************
test_is_none_a_float
*********************************************************************************

red: make it fail
#################################################################################

I add a test to see if None_ is a float_ (floating point decimal number)

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, int)

      def test_is_none_a_float(self):
          self.assertIsNone(-0.1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -0.1 is not None

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 2

      def test_is_none_a_float(self):
          self.assertIsNotNone(-0.1)

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNone(0.0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.0 is not None

  when I change the :ref:`assertion<AssertionError>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)

  the test passes

* I add another assertion

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNone(0.1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.1 is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)

  the test passes

* time for instance tests

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertNotIsInstance(-0.1, float)

  float_ is the :ref:`class<classes>` for floating point numbers. The terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: -0.1 is an instance of <class 'float'>

  ``-0.1`` is for the negative floating point numbers. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)

  the test passes

* I add the next instance test

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertNotIsInstance(0.0, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.0 is an instance of <class 'float'>

  ``0.0`` is a floating point number. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)

  the test passes

* I add another instance test

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)
            self.assertNotIsInstance(0.1, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.1 is an instance of <class 'float'>

  ``0.1`` is for the positive floating point numbers. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)
            self.assertIsInstance(0.1, float)

  the test passes

* I add one more line

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
            self.assertIsInstance(None, float)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'float'>

  I change the :ref:`assertion<AssertionError>`

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
    ...

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

red: make it fail
#################################################################################

I add a test to see if None_ is a string_ (any thing in quotes)

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 3-4

          self.assertNotIsInstance(None, float)

      def test_is_none_a_string(self):
          self.assertIsNone('')


  # NOTES
  ...

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not None

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>`

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 2

      def test_is_none_a_string(self):
          self.assertIsNotNone('')

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNone("text")

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is not None

  I change the :ref:`assertion<AssertionError>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")

  the test passes

* I add an :ref:`assertion<AssertionError>` for an instance test

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertNotIsInstance('', str)

  str_ is the :ref:`class<classes>` for strings_. The terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '' is an instance of <class 'str'>

  ``''`` is the empty string_

* I change the assert_ :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertIsInstance('', str)

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertIsInstance('', str)
            self.assertNotIsInstance("text", str)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'text' is an instance of <class 'str'>

  ``'text'`` is a string_

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertIsInstance('', str)
            self.assertIsInstance("text", str)

  A string_ is anything in single, double or triple quotes, for example

  - ``'single quotes'``
  - ``'''triple single quotes'''``
  - ``"double quotes"``
  - ``"""triple double quotes"""``

  see :ref:`quotes` for more

* I add another instance test

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("text")
            self.assertIsInstance('', str)
            self.assertIsInstance("text", str)
            self.assertIsInstance(None, str)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'str'>

  I change the :ref:`assertion<AssertionError>`

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
    ...

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

red: make it fail
#################################################################################

I add a test to see if None_ is a tuple_ (anything in parentheses ``()``)

.. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-4

          self.assertNotIsInstance(None, str)

      def test_is_none_a_tuple(self):
          self.assertIsNone(())

  # NOTES
  ...

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not None

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>`

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 2

      def test_is_none_a_tuple(self):
          self.assertIsNotNone(())

the test passes

refactor: make it better
#################################################################################

* I add an :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNone((1, 2, 3, 'n'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))

  the test passes

* I add an instance test

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 4

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertNotIsInstance((), tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: () is an instance of <class 'tuple'>

  ``()`` is the empty tuple_

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 4

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsInstance((), tuple)

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsInstance((), tuple)
            self.assertNotIsInstance((1, 2, 3, 'n'), tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is an instance of <class 'tuple'>

  ``(1, 2, 3, 'n')`` is a tuple_

* I change the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsInstance((), tuple)
            self.assertIsInstance((1, 2, 3, 'n'), tuple)

  the test passes

* I add one more instance test

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((1, 2, 3, 'n'))
            self.assertIsInstance((), tuple)
            self.assertIsInstance((1, 2, 3, 'n'), tuple)
            self.assertIsInstance(None, tuple)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'tuple'>

  I change the :ref:`assertion<AssertionError>`

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
    ...

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

red: make it fail
#################################################################################

I add a new test for :ref:`lists`

.. code-block:: python

  def test_is_none_a_tuple(self):
      ...
      self.assertNotIsInstance(None, tuple)

  def test_is_none_a_list(self):
      self.assertIsNone([])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not None

green: make it pass
#################################################################################

when I change the :ref:`assertion<AssertionError>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python

  def test_is_none_a_list(self):
      self.assertIsNotNone([])

the test passes

refactor: make it better
#################################################################################

* I add another failing line

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNone([1, 2, 3, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])

  the test passes

* I add an instance test

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertNotIsInstance([], list)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [] is an instance of <class 'list'>

  ``[]`` is the empty :ref:`list <lists>`. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)

  the test passes

* then I add another instance test

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertNotIsInstance([1, 2, 3, 'n'], list)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is an instance of <class 'list'>

  ``[1, 2, 3, 'n']`` is a :ref:`list <lists>`. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)

  the test passes

* I add one more line

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertIsInstance(None, list)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'list'>

  I change the line to make the test pass

  .. code-block:: python

    def test_is_none_a_list(self):
        self.assertIsNotNone([])
        self.assertIsNotNone([1, 2, 3, 'n'])
        self.assertIsInstance([], list)
        self.assertIsInstance([1, 2, 3, 'n'], list)
        self.assertNotIsInstance(None, list)

  then add a new note

  .. code-block:: python

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

red: make it fail
#################################################################################

I want to see if None_ is a set_

.. code-block:: python

  def test_is_none_a_list(self):
      ...
      self.assertNotIsInstance(None, list)

  def test_is_none_a_set(self):
      self.assertIsNone(set())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not None

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python

  def test_is_none_a_set(self):
      self.assertIsNotNone(set())

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNone({1, 2, 3, 'n'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not None

  I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})

  the test passes

* then I add an instance test

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertNotIsInstance({1, 2, 3, 'n'}, set)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is an instance of <class 'set'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)

* then add another instance test

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)
        self.assertIsInstance(None, set)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'set'>

  I change the :ref:`assertion<AssertionError>` to make it pass

  .. code-block:: python

    def test_is_none_a_set(self):
        self.assertIsNotNone(set())
        self.assertIsNotNone({1, 2, 3, 'n'})
        self.assertIsInstance({1, 2, 3, 'n'}, set)
        self.assertNotIsInstance(None, set)

  then add a note

  .. code-block:: python

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

red: make it fail
#################################################################################

One last test to see if None_ is a :ref:`dictionary<dictionaries>`

.. code-block:: python

  def test_is_none_a_set(self):
      ...
      self.assertNotIsInstance(None, set)

  def test_is_none_a_dictionary(self):
      self.assertIsNone(dict())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not None

wait a minute! Python_ uses ``{}`` for sets_, it also uses them for :ref:`dictionaries` with a difference.

green: make it pass
#################################################################################

I change the :ref:`assertion<AssertionError>`

.. code-block:: python

  def test_is_none_a_dictionary(self):
      self.assertIsNotNone(dict())

the test passes

refactor: make it better
#################################################################################

* then I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNone({'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not None

  when I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})

  the test passes

* I add an instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertNotIsInstance({}, dict)

  :ref:`dict<dictionaries>` is the :ref:`class<classes>` for :ref:`dictionaries`, the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {} is an instance of <class 'dict'>

  ``{}`` is the empty :ref:`dictionary<dictionaries>`. I change the :ref:`assertion<AssertionError>` to make it pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)

* then I add another instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertNotIsInstance({'key': 'value'}, dict)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is an instance of <class 'dict'>

  ``{'key': 'value'}`` is a :ref:`dictionary<dictionaries>` with ``:`` separating the key on the left from the value on the right, I can add more key-value pairs separating them with commas, that is the difference between :ref:`dictionaries` and sets_. I change the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)

  the test passes

* time for the last instance test

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)
        self.assertIsInstance(None, dict)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'dict'>

  I make the test pass

  .. code-block:: python

    def test_is_none_a_dictionary(self):
        self.assertIsNotNone(dict())
        self.assertIsNotNone({'key': 'value'})
        self.assertIsInstance({}, dict)
        self.assertIsInstance({'key': 'value'}, dict)
        self.assertNotIsInstance(None, dict)

  then I add the last note

  .. code-block:: python

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
review
*********************************************************************************

I ran tests to show what None_ is and what it is not

Would you like to :ref:`test what is True and False?<booleans>`

----

:ref:`data structures: None: tests`
