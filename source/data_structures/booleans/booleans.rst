.. include:: ../../links.rst

#################################################################################
booleans
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/TGIZs2yHr4I?si=5f3ksQHQb9V2N6PP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

There are two booleans_ - True_ and False_

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
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_what_is_false`` to check if False_ is an instance of the boolean_ :ref:`class <classes>`

  .. code-block:: python

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

  False_ is a boolean_

green: make it pass
#################################################################################

I change assertNotIsInstance_ to assertIsInstance_ to make the test pass

.. code-block:: python

  def test_what_is_false(self):
      self.assertIsInstance(False, bool)

these :ref:`methods<functions>` were introduced in the :ref:`AssertionError` chapter. I add a note

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

True_ is a boolean_

green: make it pass
#################################################################################

I change the :ref:`method<functions>`

.. code-block:: python

  def test_what_is_true(self):
      self.assertIsInstance(True, bool)

the test passes and I add a note

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

  because False_ is not True_. I add a note

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

  I add another note

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

  because True_ is not False_. I add a note

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

  and the test passes, I move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)

  then add another note

  .. code-block:: python

    # NOTES
    # True is true
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean

I want to know if any of the other Python data types are False_ or True_

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


I add a line to ``test_what_is_true`` to test if :ref:`None` is False_ or True_

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

I change the :ref:`method`

.. code-block:: python

  self.assertFalse(None)

and the terminal shows passing tests

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


I add a line to test if an integer_ is False_ or True_

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

I make assertFalse_ to assertTrue_

.. code-block:: python

  self.assertTrue(-1)

and the terminal shows passing tests

refactor: make it better
#################################################################################


* I move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)

  the terminal shows tests are still passing
* I add a new line with a test for ``0``

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not true

  I change assertTrue_ to assertFalse_ and the terminal shows passing tests

  .. code-block:: python

    self.assertFalse(0)
* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)

* I add one more line to test if positive integers_ are False_ or True_

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not false

* When I change assertFalse_ to assertTrue_ the test passes

  .. code-block:: python

    self.assertTrue(1)

* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)

  the terminal still shows passing tests

From the tests I see that

* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

-----

*********************************************************************************
is a float False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test if a float_ is False_ or True_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(0.0)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0.0 is not true

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_

.. code-block:: python

  self.assertFalse(0.0)

and the terminal shows passing tests

refactor: make it better
#################################################################################


* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)

* I add 2 more lines to test if positive and negative floats_ are also False_

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse(-0.1)
        self.assertFalse(0.1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -0.1 is not false

* I change assertFalse_ to assertTrue_ for both of them and the terminal shows passing tests

  .. code-block:: python

    self.assertTrue(-0.1)
    self.assertTrue(0.1)

* I move the lines to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block::python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-0.1)
        self.assertTrue(0.1)

From the tests I see that

* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

-----

*********************************************************************************
is a string False or True?
*********************************************************************************

red: make it fail
#################################################################################


I add a line to test if a string_ is False_ or True_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-0.1)
        self.assertTrue(0.1)
        self.assertTrue('')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not true

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_

.. code-block:: python

  self.assertFalse('')

and the terminal shows passing tests

refactor: make it better
#################################################################################

* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse('')

* I add a line to test if a string_ with characters is also False_

  .. code-block:: python

    self.assertFalse('text')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is not false

* I change assertFalse_ to assertTrue_ and move the line to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-0.1)
        self.assertTrue(0.1)
        self.assertTrue('text')

  the terminal shows passing tests

From the tests I see that

* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

----

*********************************************************************************
is a tuple False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test if a tuple_ is False_ or True_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-0.1)
        self.assertTrue(0.1)
        self.assertTrue('text')
        self.assertTrue(())

The terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not true

tuples_ are represented with ``()`` in Python

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_ and move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse('')
        self.assertFalse(())

the terminal shows passing tests

refactor: make it better
#################################################################################


* I add a line to test if a tuple_ with things is also False_

  .. code-block:: python

    self.assertFalse((1, 2, 3, 'n'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not false

* I change assertFalse_ to assertTrue_ and move the line to the ``test_what_is_true`` :ref:`method<functions>`

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

From the tests I see that

* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* an empty tuple_ is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

----

*********************************************************************************
is a list False or True?
*********************************************************************************

red: make it fail
#################################################################################

I add a line to test if a :ref:`list <lists>` is False_ or True_

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
        self.assertTrue([])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not true

:ref:`lists` are represented with ``[]`` in Python

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_ and move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse('')
        self.assertFalse(())
        self.assertFalse([])

and the terminal shows passing tests

refactor: make it better
#################################################################################

* I add a line to test if a :ref:`list <lists>`  with things is also False_

  .. code-block:: python

    self.assertFalse([1, 2, 3, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not false
* I change assertFalse_ to assertTrue_ and move the line to the ``test_what_is_true`` :ref:`method<functions>`

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

  the terminal shows passing tests

From the tests I see that

* a :ref:`list <lists>` with things is True_
* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

-----

*********************************************************************************
is a set False or True?
*********************************************************************************

red: make it fail
#################################################################################


I add a line to test if a set_ is False_ or True_

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
        self.assertTrue(set())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not true

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_ and move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

  self.assertFalse(set())

the terminal shows passing tests

refactor: make it better
#################################################################################


* I add a line to test if a set_ with things is also False_

  .. code-block:: python

    self.assertFalse({1, 2, 3, 'n'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not false

* I change assertFalse_ to assertTrue_ and move the line to the ``test_what_is_true`` :ref:`method<functions>`

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

From the tests I see that

* a set_ with things is True_
* a :ref:`list <lists>` with things is True_
* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is True_
* True_ is a boolean_
* an empty set_ is False_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is False_
* False_ is a boolean_

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
        self.assertTrue({})

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not true

green: make it pass
#################################################################################

I change assertTrue_ to assertFalse_ and move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse('')
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse(set())
        self.assertFalse({})

the terminal shows passing tests

refactor: make it better
#################################################################################

* I add a line to test if a :ref:`dictionary <dictionaries>` with things is also False_

  .. code-block:: python

    self.assertFalse({'key': 'value'})

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not false

* I change assertFalse_ to assertTrue_ and move the line to the ``test_what_is_true`` :ref:`method<functions>`

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
        self.assertTrue({'key': 'value'})

  the terminal shows all tests pass

From the tests I see that

* a :ref:`dictionary <dictionaries>` with things is True_
* a set_ with things is True_
* a :ref:`list <lists>` with things is True_
* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative integers_ are True_
* True_ is not_ False_
* True_ is True_
* True_ is a boolean_
* an empty :ref:`dictionary <dictionaries>` is False_
* an empty set_ is False_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* :ref:`None` is False_
* False_ is not True_
* False_ is False_
* False_ is a boolean_

I can sum this up as

* all objects_ that have things are True_
* empty objects_ including ``0`` and :ref:`None` are False_
* False_ is a boolean_

Would you like to :doc:`test the truth table<truth_table>`?

----

:doc:`/code/code_booleans`
