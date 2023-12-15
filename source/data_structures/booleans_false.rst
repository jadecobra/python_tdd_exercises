
##########################
Data Structures: Booleans
##########################

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

****************
is None False?
****************

* I add a failing line to ``test_what_is_false``

  .. code-block:: python

      def test_what_is_false(self):
          self.assertFalse(False)
          self.assertTrue(None)

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: None is not true

* I change ``assertTrue`` to ``assertFalse``

  .. code-block:: python

    self.assertTrue(None)

  and the terminal shows passing tests.

From the tests I see that

* `None <https://docs.python.org/3/library/constants.html?highlight=none#None>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

**********************
is an integer False?
**********************

**********************
is a string False?
**********************

**********************
is a tuple False?
**********************

**********************
is a list False?
**********************

**********************
is a set False?
**********************

**********************
is a dictionary False?
**********************

    self.assertTrue(False)
    self.assertTrue(0)
    self.assertTrue("")
    self.assertTrue(())
    self.assertTrue([])
    self.assertTrue(set())
    self.assertTrue(dict())
    self.assertNotIsInstance(False, bool)

The `unittest.TestCase.assertTrue <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue>`_ :doc:`method </functions/functions>` checks if a given input is `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

The terminal shows an :doc:`/exceptions/AssertionError` indicating that the given input is not `True <https://docs.python.org/3/library/constants.html?highlight=true#True>`_

.. code-block:: python

  >       self.assertTrue(None)
  E       AssertionError: None is not true


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the ``self.assertTrue`` statements in ``test_what_is_false`` to ``self.assertFalse`` and there is one failing test left

  .. code-block:: python

    def test_what_is_false(self):
        self.assertFalse(None)
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse(set())
        self.assertFalse(dict())
        self.assertNotIsInstance(False, bool)

  - the `unittest.TestCase.assertNotIsInstance <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance>`_ :doc:`method </functions/functions>` checks that the first input given is not an instance of the :doc:`class </classes/classes>` given as the second input.
  - it is like asking the question ``is False not an instance of bool?``

* the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    >       self.assertNotIsInstance(False, bool)
    E       AssertionError: False is an instance of <class 'bool'>

* When I change ``self.assertNotIsInstance`` to ``self.assertIsInstance`` the last test passes

  .. code-block:: python

    def test_what_is_false(self):
        self.assertFalse(None)
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse("")
        self.assertFalse(())
        self.assertFalse([])
        self.assertFalse(set())
        self.assertFalse(dict())
        self.assertIsInstance(False, bool)

----

From the tests I can see that in Python

* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* ``dict()`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty :doc:`dictionary </data_structures/dictionaries>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``set()`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_/\ :doc:`dictionary </data_structures/dictionaries>`  is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``[]`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty :doc:`list </data_structures/lists>` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``()`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `tuple <https://docs.python.org/3/library/stdtypes.html#tuples>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``""`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ which means an empty `string <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_ is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_
* ``0`` is `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

I can sum this up as

* `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_ is a `boolean <https://docs.python.org/3/library/functions.html#bool>`_
* empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None </data_structures/none>` are `False <https://docs.python.org/3/library/constants.html?highlight=true#False>`_

:doc:`/code/booleans`