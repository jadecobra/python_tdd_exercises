.. meta::
  :description: Learn how Python's boolean data type, operators (and, or, not), and truthiness work in conditional statements to control program flow. Watch the tutorial!
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
test_what_is_false
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``booleans`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh booleans

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 booleans

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_booleans.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_booleans.py:7`` to open it in the editor
* then I change ``True`` to ``False`` to make the test pass
* and I change ``test_failure`` to ``test_what_is_false`` to check if False_ is an instance of bool_

  .. code-block:: python

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

green: make it pass
#################################################################################

I change assertNotIsInstance_ to assertIsInstance_

.. code-block:: python

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)

the test passes and I add a note

.. code-block:: python

  # NOTES
  # False is a boolean


  # Exceptions Encountered
  # AssertionError

----

*********************************************************************************
test_what_is_true
*********************************************************************************

red: make it fail
#################################################################################


I add another test

.. code-block:: python

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)

  def test_what_is_true(self):
      self.assertNotIsInstance(True, bool)

the terminal shows :ref:`AssertionError`

.. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)

the test passes and I add another note

.. code-block:: python

  # NOTES
  # True is a boolean
  # False is a boolean

----

*********************************************************************************
refactor: make it better
*********************************************************************************

* I add a failing line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(False)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add a note

  .. code-block:: python

    # NOTES
    # True is a boolean
    # False is not true
    # False is a boolean

  when I change assertTrue_ to assertFalse_

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertFalse(False)

  the test passes and I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)

  then I add a note

  .. code-block:: python

    # NOTES
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean

* I add a failing line to ``test_what_is_false``

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(True)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add a note

  .. code-block:: python

    # NOTES
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean

  then change assertFalse_ to assertTrue_

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertTrue(True)

  the test passes and I move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)

  then I add another note

  .. code-block:: python

    # NOTES
    # True is true
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean

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

red: make it fail
#################################################################################


I add a line

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)
      self.assertTrue(True)
      self.assertTrue(None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not true

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertFalse(None)

the terminal shows passing tests

refactor: make it better
#################################################################################

I move the line to ``test_what_is_false``

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)

then add a note

.. code-block:: python

  # NOTES
  # True is true
  # True is not false
  # True is a boolean
  # None is false
  # False is false
  # False is not true
  # False is a boolean

----

*********************************************************************************
is an integer False or True?
*********************************************************************************

red: make it fail
#################################################################################


I add another line

.. code-block:: python

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)
      self.assertFalse(False)
      self.assertFalse(None)
      self.assertFalse(-1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not false

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertTrue(-1)

the test passes

refactor: make it better
#################################################################################

* then I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_true(self):
        ...
        self.assertTrue(-1)

* I add a new line

  .. code-block:: python

    def test_what_is_true(self):
        ...
        self.assertTrue(-1)
        self.assertTrue(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not true

  I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertFalse(0)

  the test passes and I move the line to ``test_what_is_false``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0)

* I add one more line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0)
        self.assertFalse(1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not false

  when I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue(1)

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0)

    def test_what_is_true(self):
        ...
        self.assertTrue(-1)
        self.assertTrue(1)

  then I add notes

  .. code-block:: python

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

-----

*********************************************************************************
is a float False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test

.. code-block:: python

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)
      self.assertFalse(False)
      self.assertFalse(None)
      self.assertFalse(0)
      self.assertFalse(-0.1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: -0.1 is not false

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertTrue(-0.1)

the test passes and I move the line to ``test_what_is_true``

.. code-block:: python

  def test_what_is_true(self):
      ...
      self.assertTrue(-0.1)

refactor: make it better
#################################################################################

* I add a line

  .. code-block:: python

    def test_what_is_true(self):
        ...
        self.assertTrue(-0.1)
        self.assertTrue(0.0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.0 is not true

  I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertFalse(0.0)

  the test passes.and I move the line to ``test_what_is_false``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0.0)

* I add another line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0.0)
        self.assertFalse(0.1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.1 is not false

  when I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue(0.1)

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(0.0)

    def test_what_is_true(self):
        ...
        self.assertTrue(-0.1)
        self.assertTrue(0.1)

  then I add notes

  .. code-block:: python

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

  I can make the new notes simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python

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

-----

*********************************************************************************
is a string False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)
      self.assertTrue(True)
      self.assertTrue(-1)
      self.assertTrue(1)
      self.assertTrue(-0.1)
      self.assertTrue(0.1)
      self.assertTrue(str())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not true

the empty string_ is not True_

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertFalse(str())

the test passes

refactor: make it better
#################################################################################

* I move the line to ``test_what_is_false``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(str())

* then I add another line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(str())
        self.assertFalse('text')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is not false

  I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue('text')

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(str())

    def test_what_is_true(self):
        ...
        self.assertTrue('text')

  I add notes

  .. code-block:: python

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

----

*********************************************************************************
is a tuple False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to see

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)
      self.assertTrue(True)
      self.assertTrue(-1)
      self.assertTrue(1)
      self.assertTrue(-0.1)
      self.assertTrue(0.1)
      self.assertTrue('text')
      self.assertTrue(tuple())

The terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not true

the empty tuple_ is not True_

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertTrue(tuple())

the test passes and I move the line to ``test_what_is_false``

.. code-block:: python

  def test_what_is_false(self):
      ...
      self.assertFalse(tuple())

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(tuple())
        self.assertFalse((1, 2, 3, 'n'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not false

  I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue((1, 2, 3, 'n'))

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(tuple())

    def test_what_is_true(self):
        ...
        self.assertTrue((1, 2, 3, 'n'))

  then I add notes

  .. code-block:: python

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

red: make it fail
#################################################################################

I add a line

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)
      self.assertTrue(True)
      self.assertTrue(-0.1)
      self.assertTrue(1)
      self.assertTrue(-0.1)
      self.assertTrue(0.1)
      self.assertTrue('text')
      self.assertTrue((1, 2, 3, 'n'))
      self.assertTrue(list())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not true

the empty :ref:`list<lists>` is not True_

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertFalse(list())

the test passes, then I move the line to ``test_what_is_false``

.. code-block:: python

  def test_what_is_false(self):
      ...
      self.assertFalse(list())

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(list())
        self.assertFalse([1, 2, 3, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not false

* I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue([1, 2, 3, 'n'])

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(list())

    def test_what_is_true(self):
        ...
        self.assertTrue([1, 2, 3, 'n'])

  then add notes

  .. code-block:: python

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

-----

*********************************************************************************
is a set False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)
      self.assertTrue(True)
      self.assertTrue(-0.1)
      self.assertTrue(0.1)
      self.assertTrue(-1)
      self.assertTrue(1)
      self.assertTrue('text')
      self.assertTrue((1, 2, 3, 'n'))
      self.assertTrue([1, 2, 3, 'n'])
      self.assertTrue(set())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not true

the empty set_ is not True_

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  self.assertFalse(set())

the test passes and I move the line to ``test_what_is_false``

.. code-block:: python

  def test_what_is_false(self):
      ...
      self.assertFalse(set())

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(set())
        self.assertFalse({1, 2, 3, 'n'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not false

  I change the :ref:`method<functions>`

  .. code-block:: python

    self.assertTrue({1, 2, 3, 'n'})

  the test passes and I move the line to ``test_what_is_true``

  .. code-block:: python

    def test_what_is_false(self):
        ...
        self.assertFalse(set())

    def test_what_is_true(self):
        ...
        self.assertTrue({1, 2, 3, 'n'})

  I add more notes

  .. code-block:: python

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

----

*********************************************************************************
is a dictionary False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test if a :ref:`dictionary <dictionaries>` is False_ or True_

.. code-block:: python

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
      self.assertTrue(dict())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not true

the empty :ref:`dictionary <dictionaries>` is not True_

green: make it pass
#################################################################################

when I change assertTrue_ to assertFalse_

.. code-block:: python

  self.assertFalse(dict())

the test passes and I move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

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

refactor: make it better
#################################################################################

* I add another line to test if a :ref:`dictionary <dictionaries>` with things is also False_

  .. code-block:: python

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
        self.assertFalse({'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not false

  I change assertFalse_ to assertTrue_

  .. code-block:: python

    self.assertTrue({'key': 'value'})

  the test passes and I move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python

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

  then I add the last 2 notes

  .. code-block:: python

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

----

*********************************************************************************
review
*********************************************************************************

From the tests I can see that

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