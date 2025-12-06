.. meta::
  :description: Learn how Python's boolean data type, operators (and, or, not), and truthiness work in conditional statements to control program_ flow. Watch the tutorial!
  :keywords: Jacob Itegboje, python boolean tutorial for beginners, python boolean operators and or not, python if statement with boolean, python truthiness and falsiness explained, what is boolean in python with example, how to use bool() in python, python boolean return function, common python boolean mistakes, python boolean best practices

.. include:: ../../links.rst

.. _booleans: https://docs.python.org/3/library/functions.html#bool

#################################################################################
booleans
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/6r3QcYN0wxQ?si=cQaK63rwX3f9PGX6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

There are 2 booleans_ - True_ and False_

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``booleans`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh booleans

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 booleans

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_booleans.py:7: AssertionError

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_booleans.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestBooleans(unittest.TestCase):

*********************************************************************************
test_what_is_false
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

* I change ``test_failure`` to ``test_what_is_false`` to check if False_ is a child of bool_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

=================================================================================
GREEN: make it pass
=================================================================================

I change assertNotIsInstance_ to assertIsInstance_

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)

the test passes and I add a note

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1-2

  # NOTES
  # False is a boolean


  # Exceptions Encountered
  # AssertionError

----

*********************************************************************************
test_what_is_true
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================


I add another test

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)

      def test_what_is_true(self):
          self.assertNotIsInstance(True, bool)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

=================================================================================
GREEN: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the test passes

* I add another note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    # NOTES
    # True is a boolean
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

----

*********************************************************************************
REFACTOR: make it better
*********************************************************************************

* I add a failing line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(False)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add a note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertFalse(False)

  the test passes

* I move the line to the from the ``test_what_is_true`` to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)

* I add a note

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

* I add a failing line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add a note

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

    # NOTES
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertTrue(True)

  the test passes

* I move the line from ``test_what_is_false`` to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)

  then I add another note

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2


    # NOTES
    # True is true
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

I want to test the other Python_ basic data types_ to see if any of them are False_ or True_

* is :ref:`None` False_ or True_?
* is an integer_ False_ or True_?
* is a float_ False_ or True_?
* is a string_ False_ or True_?
* is a tuple_ False_ or True_?
* is a :ref:`list <lists>` False_ or True_?
* is a set_ False_ or True_?
* is a :ref:`dictionary <dictionaries>` False_ or True_?

----

*****************************************************************************************
is None False or True?
*****************************************************************************************

=================================================================================
RED: make it fail
=================================================================================


I add a line

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(None)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: None is not true

=================================================================================
GREEN: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 1

          self.assertFalse(None)

the test passes

=================================================================================
REFACTOR: make it better
=================================================================================

I move the line from ``test_what_is_true`` to ``test_what_is_false``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)

I add a note

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 5


  # NOTES
  # True is true
  # True is not false
  # True is a boolean
  # None is false
  # False is false
  # False is not true
  # False is a boolean


  # Exceptions Encountered
  # AssertionError

----

*********************************************************************************
is an integer False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================


I add a failing line to see if an integer_ is False_ or True_

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)
      self.assertFalse(False)
      self.assertFalse(None)
      self.assertFalse(-1)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: -1 is not false

=================================================================================
GREEN: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertTrue(-1)

the test passes

=================================================================================
REFACTOR: make it better
=================================================================================

* I move the line from ``test_what_is_false`` to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)

* I add a new failing line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertTrue(-1)
            self.assertTrue(0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 is not true

* I change the :ref:`method<functions>` to assertFalse_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertFalse(0)

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):

* I add another failing line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

            self.assertFalse(0)
            self.assertFalse(1)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 is not false

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7

            self.assertFalse(0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)

* I add notes

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2, 6

    # NOTES
    # positive and negative integers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

-----

*********************************************************************************
is a float False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a line to test if floats_ are True_ or False_ in ``test_what_is_false``

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2

            self.assertFalse(0)
            self.assertFalse(-0.1)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: -0.1 is not false

=================================================================================
GREEN: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(-0.1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)

=================================================================================
REFACTOR: make it better
=================================================================================

* I add another failing line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

            self.assertTrue(-0.1)
            self.assertTrue(0.0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.0 is not true

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertFalse(0.0)

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)

        def test_what_is_true(self):

* I add another line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertFalse(0.0)
            self.assertFalse(0.1)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)


  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.1 is not false

  when I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue(0.1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 9

            self.assertFalse(0.0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)


    # NOTES

* I add notes

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 7

    # NOTES
    # positive and negative floats are true
    # positive and negative integers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0.0 is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

* I make the new notes simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 5

    # NOTES
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

-----

*********************************************************************************
is a string False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a failing line to ``test_what_is_true`` to test if a string_ is False_ or True_

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 8

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue(str())


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '' is not true

the empty string_ is not True_

=================================================================================
GREEN: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 1

          self.assertFalse(str())

the test passes

=================================================================================
REFACTOR: make it better
=================================================================================

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertFalse(0.0)
            self.assertTrue(str())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

* I add a failing line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse('text')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'text' is not false

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertTrue('text')

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue('text')


    # NOTES

* I add notes

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2, 7

    # NOTES
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

----

*********************************************************************************
is a tuple False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a line to see if a tuple_ (anything in parentheses) is False_ or True_

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 9

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue('text')
          self.assertTrue(tuple())


  # NOTES

The terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: () is not true

the empty tuple_ is not True_

=================================================================================
GREEN: make it pass
=================================================================================

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

            self.assertFalse(tuple())

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())

=================================================================================
REFACTOR: make it better
=================================================================================

* I add another line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            self.assertTrue(tuple())
            self.assertFalse((1, 2, 3, 'n'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is not false

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertTrue((1, 2, 3, 'n'))

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 12

            self.assertFalse(str())
            self.assertFalse(tuple())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))


    # NOTES

* I add notes

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2, 8


    # NOTES
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

----

*********************************************************************************
is a list False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a line to test if a :ref:`list<lists>` (anything in square brackets (``[]``)) is False_ or True_

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 3

      self.assertTrue('text')
      self.assertTrue((1, 2, 3, 'n'))
      self.assertTrue(list())

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [] is not true

the empty :ref:`list<lists>` is not True_

=================================================================================
GREEN: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python

            self.assertFalse(list())

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

=================================================================================
REFACTOR: make it better
=================================================================================

* I add another line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertFalse(list())
            self.assertFalse([1, 2, 3, 'n'])

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is not false

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertTrue([1, 2, 3, 'n'])

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 13

            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])


    # NOTES

* I add notes

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2, 9

    # NOTES
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

-----

*********************************************************************************
is a set False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a line to test if a set_ is False_ or True_ in ``test_what_is_true``

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4

          self.assertTrue('text')
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue(set())


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: set() is not true

the empty set_ is not True_

=================================================================================
GREEN: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertFalse(set())

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())

        def test_what_is_true(self):

=================================================================================
REFACTOR: make it better
=================================================================================

* I add another line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

            self.assertFalse(set())
            self.assertFalse({1, 2, 3, 'n'})

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is not false

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertTrue({1, 2, 3, 'n'})

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 13

            self.assertFalse(set())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})


    # NOTES

* I add more notes

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2, 10

    # NOTES
    # a set with things is true
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty set is false
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

----

*********************************************************************************
is a dictionary False or True?
*********************************************************************************

=================================================================================
RED: make it fail
=================================================================================

I add a line to test if a :ref:`dictionary <dictionaries>` is False_ or True_ in ``test_what_is_true``

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 4

          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue(dict())


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {} is not true

the empty :ref:`dictionary <dictionaries>` is not True_

=================================================================================
GREEN: make it pass
=================================================================================

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            self.assertFalse(dict())

  the test passes

* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

=================================================================================
REFACTOR: make it better
=================================================================================

* I add another line to test if a :ref:`dictionary <dictionaries>` with things is also False_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())
            self.assertFalse({'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is not false

  I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

            self.assertTrue({'key': 'value'})

  the test passes

* I move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 24

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

* I add the last 2 notes

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2, 11

    # NOTES
    # a dictionary with things is true
    # a set with things is true
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty dictionary is false
    # the empty set is false
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions Encountered
    # AssertionError

----

*********************************************************************************
review
*********************************************************************************

From the tests I can see that in Python_

* a container with things is True_
* an empty container is False_
* positive and negative numbers are True_
* ``0`` is False_
* False_ is not True_
* True_ is not False_
* True_ and False_ are booleans_

Would you like to :ref:`test the truth table? <booleans: truth table>`

----

:ref:`data structures: booleans: tests`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->