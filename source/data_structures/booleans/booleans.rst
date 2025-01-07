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

The tests in this chapter go over booleans_ by comparing them with other data structures in Python to learn what they are and what they are not.

There are two boolean_ values - True_ and False_

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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_booleans.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_what_is_false`` to check if False_ is an instance of the boolean_ :ref:`class <classes>`

  .. code-block:: python

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is an instance of <class 'bool'>

  The `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ :ref:`method<functions>` checks that the first input given is NOT an instance of the :ref:`class <classes>` given as the second input. It is like asking the question ``is False not an instance of bool?``

green: make it pass
#################################################################################

I change assertNotIsInstance_ to assertIsInstance_ to make the test pass

.. code-block:: python

  self.assertIsInstance(False, bool)

The `unittest.TestCase.assertIsInstance`_ :ref:`method<functions>` checks that the first input given is an instance of the :ref:`class <classes>` given as the second input. It is like asking the question ``is False an instance of bool?``. The test shows that False_ is a boolean_

refactor: make it better
#################################################################################

* I add a failing line to ``test_what_is_false``

  .. code-block:: python

    self.assertTrue(False)

  the terminal shows :ref:`AssertionError` because False_ is not True_

  .. code-block:: python

    AssertionError: False is not true

  The `unittest.TestCase.assertTrue` :ref:`method<functions>` checks if a given input is True_

* When I change assertTrue_ to assertFalse_ to test if False_ is False_ the test passes

  .. code-block:: python

    self.assertFalse(False)

  The `unittest.TestCase.assertFalse`_ :ref:`method<functions>` checks if a given input is False_

From these tests I see that

* False_ is False_
* False_ is a boolean_

----

*********************************************************************************
test_what_is_true
*********************************************************************************

red: make it fail
#################################################################################


I add a :ref:`method<functions>` called ``test_what_is_true`` with a failing line to to check if True_ is an instance of the boolean_ :ref:`class <classes>`

.. code-block:: python

    def test_what_is_true(self):
        self.assertNotIsInstance(True, bool)

the terminal shows :ref:`AssertionError` because True_ is an instance of the boolean_ :ref:`class <classes>`

.. code-block:: python

    AssertionError: True is an instance of <class 'bool'>

green: make it pass
#################################################################################

I make ``assertNotIsInstance`` to ``assertIsInstance`` to make the test pass

.. code-block:: python

  self.assertIsInstance(True, bool)

refactor: make it better
#################################################################################

* I add a failing line to ``test_what_is_true``

  .. code-block:: python

    self.assertFalse(True)

  the terminal shows :ref:`AssertionError` because True_ is not False_

  .. code-block:: python

    AssertionError: True is not false

* When I change assertFalse_ to assertTrue_ to test if True_ is True_ the test passes

  .. code-block:: python

    self.assertTrue(True)

From the tests I see that

* True_ is True_
* True_ is a boolean_
* False_ is False_
* False_ is a boolean_

I want to know if any of the other Python data types are False_ or True_

* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ False_ or True_?
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


I add a line to ``test_what_is_true`` to test if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_ or True_

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

I change assertTrue_ to assertFalse_

.. code-block:: python

  self.assertFalse(None)

and the terminal shows passing tests

refactor: make it better
#################################################################################

I move the line to the ``test_what_is_false`` :ref:`method<functions>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)

and the terminal still shows passing tests

From the tests I see that

* True_ is True_
* True_ is a boolean_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
* False_ is False_
* False_ is a boolean_

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

* I add one more line to test if positive :ref:`integers<int>`_ are False_ or True_

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

* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertFalse(-1.2)
        self.assertFalse(2.3)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -1.2 is not false

* I change assertFalse_ to assertTrue_ for both of them and the terminal shows passing tests

  .. code-block:: python

    self.assertTrue(-1.2)
    self.assertTrue(2.3)

* I move the lines to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block::python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-1.2)
        self.assertTrue(2.3)

From the tests I see that

* Positive and Negative floats_ are True_
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
        self.assertTrue('text')

  the terminal shows passing tests

From the tests I see that

* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
        self.assertTrue('text')
        self.assertTrue((1, 2, 3, 'n'))

From the tests I see that

* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* an empty tuple_ is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
        self.assertTrue('text')
        self.assertTrue((1, 2, 3, 'n'))
        self.assertTrue([])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not true

:doc:`lists </data_structures/lists/lists>` are represented with ``[]`` in Python

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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
        self.assertTrue('text')
        self.assertTrue((1, 2, 3, 'n'))
        self.assertTrue([1, 2, 3, 'n'])

  the terminal shows passing tests

From the tests I see that

* a :ref:`list <lists>` with things is True_
* a tuple_ with things is True_
* a string_ with things is True_
* Positive and Negative floats_ are True_
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* an empty set_ is False_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
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
* Positive and Negative :ref:`integers<int>`_ are True_
* True_ is True_
* True_ is a boolean_
* an empty :ref:`dictionary <dictionaries>` is False_
* an empty set_ is False_
* an empty :ref:`list <lists>` is False_
* an empty string_ is False_
* ``0.0`` is False_
* ``0`` is False_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is False_
* False_ is False_
* False_ is a boolean_

I can sum this up as

* all objects_ that have things are True_
* empty objects_ including ``0`` and :ref:`None` are False_
* False_ is a boolean_

Would you like to :doc:`test the truth table<truth_table>`?

----

:doc:`/code/code_booleans`
