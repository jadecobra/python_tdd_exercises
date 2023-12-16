
##################################
Data Structures: Booleans: False
##################################

The tests in this chapter go over `booleans <https://docs.python.org/3/library/functions.html#bool>`_ by comparing them with other data structures in Python to learn what they are and what they are not.

There are two `boolean <https://docs.python.org/3/library/functions.html#bool>`_ values - `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_ and `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

****************
What is False?
****************

RED: make it fail
==================

I create a failing test in ``test_booleans.py`` called ``test_what_is_false`` to find out what is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  import unittest


  class TestBooleans(unittest.TestCase):

      def test_what_is_false(self):
          self.assertTrue(False)

the terminal shows an :doc:`/exceptions/AssertionError` because `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is not `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

  AssertionError: False is not true

GREEN: make it pass
====================

When I change ``assertTrue`` to ``assertFalse`` to test if `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ the test passes

.. code-block:: python

  self.assertFalse(False)

The `unittest.TestCase.assertFalse <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse>`_ :doc:`method </functions/functions>` checks if a given input is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

From this test I see that `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_


REFACTOR: make it better
=========================

I want to know if any of the other Python data types are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

* is `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is an `integer <https://docs.python.org/3/library/functions.html#int>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a `float <https://docs.python.org/3/library/functions.html#float>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a :doc:`list </data_structures/lists>` `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?
* is a :doc:`dictionary </data_structures/dictionaries>` `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_?

----

********************
is False a Boolean?
********************

RED: make it fail
==================

I add a line to confirm that `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is an instance of the `boolean <https://docs.python.org/3/library/functions.html#bool>`_ :doc:`class </classes/classes>`

.. code-block:: python

    def test_what_is_false(self):
        self.assertNotIsInstance(False, bool)
        self.assertFalse(False)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: False is an instance of <class 'bool'>

The `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ :doc:`method </functions/functions>` checks that the first input given is NOT an instance of the :doc:`class </classes/classes>` given as the second input. It is like asking the question ``is False not an instance of bool?``


GREEN: make it pass
====================

I change ``assertNotIsInstance`` to ``assertIsInstance`` to make the test pass

.. code-block:: python

  self.assertIsInstance(False, bool)

The `unittest.TestCase.assertIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance>`_ :doc:`method </functions/functions>` checks that the first input given is an instance of the :doc:`class </classes/classes>` given as the second input. It is like asking the question ``is False an instance of bool?``

From the tests I see that

* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

****************
is None False?
****************

RED: make it fail
==================

I add a line to test if `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertTrue(None)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: None is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(None)

and the terminal shows passing tests.

From the tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

**********************
is an integer False?
**********************

RED: make it fail
==================

I add a line to test if an `integer <https://docs.python.org/3/library/functions.html#int>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertTrue(0)

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: 0 is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(0)

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add 2 more lines to test if positive and negative `integers <https://docs.python.org/3/library/functions.html#int>`_ are also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(-1)
        self.assertFalse(1)

the terminal shows an :doc:`/exceptions/AssertionError` for both, showing that negative and positive `integers <https://docs.python.org/3/library/functions.html#int>`_ are not `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_. I remove the lines to return to passing tests

.. code-block:: python

  AssertionError: 1 is not false

From the tests I see that

* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

**********************
is a float False?
**********************

RED: make it fail
==================

I add a line to test if a `float <https://docs.python.org/3/library/functions.html#float>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertTrue(0.0)


the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: 0.0 is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(0.0)

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add 2 more lines to test if positive and negative `floats <https://docs.python.org/3/library/functions.html#float>`_ are also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse(-1.2)
        self.assertFalse(2.3)

the terminal shows an :doc:`/exceptions/AssertionError` for both, showing that negative and positive `floats <https://docs.python.org/3/library/functions.html#float>`_ are not `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_. I delete the lines to return to passing tests

.. code-block:: python

  AssertionError: -1.2 is not false

From the tests I see that

* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

**********************
is a string False?
**********************

RED: make it fail
==================

I add a line to test if an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertTrue("")

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: '' is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse("")

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add a line to test if a `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ with characters is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  self.assertFalse('text')

the terminal shows an :doc:`/exceptions/AssertionError` and I remove the line to return to passing tests

.. code-block:: python

  AssertionError: 'text' is not false


From the tests I see that

* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

**********************
is a tuple False?
**********************

RED: make it fail
==================

I add a line to test if an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse("")
        self.assertTrue(())

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: () is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(())

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add a line to test if a `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ with objects is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  self.assertFalse((1, 2, 3, "n"))

the terminal shows an :doc:`/exceptions/AssertionError` and I remove the line to return to passing tests

.. code-block:: python

  AssertionError: (1, 2, 3, 'n') is not false


From the tests I see that

* an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

**********************
is a list False?
**********************

RED: make it fail
==================

I add a line to test if an empty :doc:`list </data_structures/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertTrue([])

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: [] is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse([])

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add a line to test if a :doc:`list </data_structures/lists>`  with objects is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  self.assertFalse([1, 2, 3, "n"])

the terminal shows an :doc:`/exceptions/AssertionError` and I remove the line to return to passing tests

.. code-block:: python

  AssertionError: [1, 2, 3, 'n'] is not false

From the tests I see that

* an empty :doc:`list </data_structures/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

-----

**********************
is a set False?
**********************

RED: make it fail
==================

I add a line to test if an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertTrue(set())

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: set() is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse(set())

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add a line to test if a `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_  with objects is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  self.assertFalse({1, 2, 3, "n"})

the terminal shows an :doc:`/exceptions/AssertionError` and I remove the line to return to passing tests

.. code-block:: python

  AssertionError: {1, 2, 3, 'n'} is not false

From the tests I see that

* an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty :doc:`list </data_structures/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

----

**********************
is a dictionary False?
**********************

RED: make it fail
==================

I add a line to test if an empty :doc:`dictionary </data_structures/dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

    def test_what_is_false(self):
        self.assertIsInstance(False, bool)
        self.assertFalse(False)
        self.assertFalse(None)
        self.assertFalse(0)
        self.assertFalse(0.0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse(set())
        self.assertTrue({})

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: {} is not true

GREEN: make it pass
====================

I change ``assertTrue`` to ``assertFalse``

.. code-block:: python

  self.assertFalse({})

and the terminal shows passing tests.

REFACTOR: make it better
=========================

I add a line to test if a :doc:`dictionary </data_structures/dictionaries>` with objects is also `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

.. code-block:: python

  self.assertFalse({'key': 'value'})

the terminal shows an :doc:`/exceptions/AssertionError` and I remove the line to return to passing tests

.. code-block:: python

  AssertionError: {'key': 'value'} is not false

From the tests I see that


* an empty :doc:`dictionary </data_structures/dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty :doc:`list </data_structures/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0.0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `floats <https://docs.python.org/3/library/functions.html#float>`_ are not
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ and other `integers <https://docs.python.org/3/library/functions.html#int>`_ are not
* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

I can sum this up as

* empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None </data_structures/none>` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_

:doc:`/code/booleans`