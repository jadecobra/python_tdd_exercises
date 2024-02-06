.. include:: ../../links.rst

##################################
booleans
##################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/TGIZs2yHr4I?si=5f3ksQHQb9V2N6PP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The tests in this chapter go over `booleans <https://docs.python.org/3/library/functions.html#bool>`_ by comparing them with other data structures in Python to learn what they are and what they are not.

There are two `boolean <https://docs.python.org/3/library/functions.html#bool>`_ values - `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ and `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

****************
What is False?
****************

red: make it fail
==================

I create a file called ``test_booleans.py`` and add a failing test in ``test_what_is_false`` to check if `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`

.. code-block:: python

  import unittest


  class TestBooleans(unittest.TestCase):

      def test_what_is_false(self):
          self.assertNotIsInstance(False, bool)

the terminal shows an :ref:`AssertionError` because `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`

.. code-block:: python

  AssertionError: False is an instance of <class 'bool'>

The `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ :doc:`method </functions/functions>` checks that the first input given is NOT an instance of the :doc:`class </classes/classes>` given as the second input. It is like asking the question ``is False not an instance of bool?``

green: make it pass
====================

I change ``assertNotIsInstance`` to ``assertIsInstance`` to make the test pass

.. code-block:: python

  self.assertIsInstance(False, bool)

The `unittest.TestCase.assertIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance>`_ :doc:`method </functions/functions>` checks that the first input given is an instance of the :doc:`class </classes/classes>` given as the second input. It is like asking the question ``is False an instance of bool?``

From the tests I see that `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

refactor: make it better
=========================

* I add a failing line to ``test_what_is_false``

  .. code-block:: python

    self.assertTrue(False)

  the terminal shows an :ref:`AssertionError` because `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is not `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

  .. code-block:: python

    AssertionError: False is not true

  The `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :doc:`method </functions/functions>` checks if a given input is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

* When I change ``assertTrue`` to ``assertFalse`` to test if `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ the test passes

  .. code-block:: python

    self.assertFalse(False)

  The `unittest.TestCase.assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ :doc:`method </functions/functions>` checks if a given input is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

From these tests I see that

* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

****************
What is True?
****************

red: make it fail
==================

I add a :doc:`method </functions/functions>` called ``test_what_is_true`` with a failing line to to check if `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`

.. code-block:: python

    def test_what_is_true(self):
        self.assertNotIsInstance(True, bool)

the terminal shows an :ref:`AssertionError` because `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`

.. code-block:: python

    AssertionError: True is an instance of <class 'bool'>

green: make it pass
====================

I change ``assertNotIsInstance`` to ``assertIsInstance`` to make the test pass

.. code-block:: python

  self.assertIsInstance(True, bool)

refactor: make it better
=========================

* I add a failing line to ``test_what_is_true``

  .. code-block:: python

    self.assertFalse(True)

  the terminal shows an :ref:`AssertionError` because `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is not `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    AssertionError: True is not false

* When I change ``assertFalse`` to ``assertTrue`` to test if `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ the test passes

  .. code-block:: python

    self.assertTrue(True)

From the tests I see that

* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

I want to know if any of the other Python data types are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is an `integer <https://docs.python.org/3/library/functions.html#int>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a `float <https://docs.python.org/3/library/functions.html#float>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a :doc:`list </data_structures/lists/lists>` `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?
* is a :doc:`dictionary </data_structures/dictionaries>` `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_?

----

************************
is None False or True?
************************

red: make it fail
==================

I add a line to ``test_what_is_true`` to test if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(None)

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: None is not true

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(None)

and the terminal shows passing tests

refactor: make it better
=========================

I move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)

and the terminal still shows passing tests

From the tests I see that

* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

******************************
is an integer False or True?
******************************

red: make it fail
==================

I add a line to test if an `integer <https://docs.python.org/3/library/functions.html#int>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(-1)

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: -1 is not false

green: make it pass
====================

I change ``assertFalse`` to ``assertTrue``

.. code-block:: python

  self.assertTrue(-1)

and the terminal shows passing tests

refactor: make it better
=========================

* I move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 is not true

  I change ``assertTrue`` to ``assertFalse`` and the terminal shows passing tests

  .. code-block:: python

    self.assertFalse(0)
* I move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)

* I add one more line to test if positive `integers <https://docs.python.org/3/library/functions.html#int>`_ are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(1)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 is not false

* When I change ``assertFalse`` to ``assertTrue`` the test passes

  .. code-block:: python

    self.assertTrue(1)

* I move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

  .. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)

  the terminal still shows passing tests

From the tests I see that

* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

******************************
is a float False  or True?
******************************

red: make it fail
==================

I add a line to test if a `float <https://docs.python.org/3/library/functions.html#float>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(0.0)

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0.0 is not true

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(0.0)

and the terminal shows passing tests

refactor: make it better
=========================

* I move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)

* I add 2 more lines to test if positive and negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertFalse(0)
          self.assertFalse(0.0)
          self.assertFalse(-1.2)
          self.assertFalse(2.3)

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: -1.2 is not false

* I change ``assertFalse`` to ``assertTrue`` for both of them and the terminal shows passing tests

  .. code-block:: python

    self.assertTrue(-1.2)
    self.assertTrue(2.3)

* I move the lines to the ``test_what_is_true`` :doc:`method </functions/functions>`

  .. code-block::python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-1.2)
        self.assertTrue(2.3)

From the tests I see that

* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

******************************
is a string False or True?
******************************

red: make it fail
==================

I add a line to test if a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

    def test_what_is_true(self):
        self.assertIsInstance(True, bool)
        self.assertTrue(True)
        self.assertTrue(-1)
        self.assertTrue(1)
        self.assertTrue(-1.2)
        self.assertTrue(2.3)
        self.assertTrue('')

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: '' is not true

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse('')

and the terminal shows passing tests

refactor: make it better
=========================

* I move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

  .. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse('')
* I add a line to test if a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with characters is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    self.assertFalse('text')

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'text' is not false

* I change ``assertFalse`` to ``assertTrue`` and move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

* a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

******************************
is a tuple False or True?
******************************

red: make it fail
==================

I add a line to test if a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

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

The terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: () is not true

`tuples <https://docs.python.org/3/library/stdtypes.html#tuples>`_ are represented with ``()`` in Python

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse`` and move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

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
=========================

* I add a line to test if a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with things is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    self.assertFalse((1, 2, 3, 'n'))

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (1, 2, 3, 'n') is not false

* I change ``assertFalse`` to ``assertTrue`` and move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

* a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

******************************
is a list False or True?
******************************

red: make it fail
==================

I add a line to test if a :doc:`list </data_structures/lists/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] is not true

:doc:`lists </data_structures/lists/lists>` are represented with ``[]`` in Python

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse`` and move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

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
=========================

* I add a line to test if a :doc:`list </data_structures/lists/lists>`  with things is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    self.assertFalse([1, 2, 3, 'n'])

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [1, 2, 3, 'n'] is not false
* I change ``assertFalse`` to ``assertTrue`` and move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

* a :doc:`list </data_structures/lists/lists>` with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* an empty :doc:`list </data_structures/lists/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

******************************
is a set False or True?
******************************

red: make it fail
==================

I add a line to test if a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: set() is not true

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse`` and move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

.. code-block:: python

  self.assertFalse(set())

the terminal shows passing tests

refactor: make it better
=========================

* I add a line to test if a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_  with things is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    self.assertFalse({1, 2, 3, 'n'})

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {1, 2, 3, 'n'} is not false

* I change ``assertFalse`` to ``assertTrue`` and move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

* a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a :doc:`list </data_structures/lists/lists>` with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty :doc:`list </data_structures/lists/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

********************************
is a dictionary False or True?
********************************

red: make it fail
==================

I add a line to test if a :doc:`dictionary </data_structures/dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ or `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: {} is not true

green: make it pass
====================

I change ``assertTrue`` to ``assertFalse`` and move the line to the ``test_what_is_false`` :doc:`method </functions/functions>`

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
=========================

* I add a line to test if a :doc:`dictionary </data_structures/dictionaries>` with things is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

  .. code-block:: python

    self.assertFalse({'key': 'value'})

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not false

* I change ``assertFalse`` to ``assertTrue`` and move the line to the ``test_what_is_true`` :doc:`method </functions/functions>`

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

* a :doc:`dictionary </data_structures/dictionaries>` with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a :doc:`list </data_structures/lists/lists>` with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with things is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* Positive and Negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* an empty :doc:`dictionary </data_structures/dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty :doc:`list </data_structures/lists/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

I can sum this up as

* all `objects <https://docs.python.org/3/glossary.html#term-object>`_ that contain things are `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_
* empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :ref:`None` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

:doc:`/code/code_booleans`
