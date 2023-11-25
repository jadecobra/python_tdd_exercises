
Data Structures: Booleans
=========================

The tests in this chapter cover ``booleans`` by comparing them with other data structures in python to learn what they are and what they are not. There are only two boolean values - ``True`` and ``False``

Prerequisites
-------------


* :doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>`
* :doc:`Data Structures </data structures>`

----

What is False?
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a failing test in ``test_data_structures.py`` called ``test_what_is_false``

.. code-block:: python

  def test_what_is_false(self):
   self.assertTrue(None)
   self.assertTrue(False)
   self.assertTrue(0)
   self.assertTrue("")
   self.assertTrue(())
   self.assertTrue([])
   self.assertTrue({})
   self.assertTrue(dict())
   self.assertNotIsInstance(False, bool)

the ``assertTrue`` method checks if a given input is ``True``, the terminal shows an :doc:`AssertionError` indicating that the given input is not ``True``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* when I change the ``self.assertTrue`` statements in ``test_what_is_false`` to ``self.assertFalse`` I am left with one failing test

  .. code-block:: python

  def test_what_is_false(self):
    self.assertFalse(None)
    self.assertFalse(False)
    self.assertFalse(0)
    self.assertFalse("")
    self.assertFalse(())
    self.assertFalse([])
    self.assertFalse({})
    self.assertFalse(dict())
    self.assertNotIsInstance(False, bool)

  the ``assertNotIsInstance`` method checks that the first input given is not an instance of the :doc:`class <classes>` given as the second input in other words, it is asking the question ``if False not an instance of bool``

* When I change ``self.assertNotIsInstance`` to ``self.assertIsInstance`` the final test passes

  .. code-block:: python

  def test_what_is_false(self):
    self.assertFalse(None)
    self.assertFalse(False)
    self.assertFalse(0)
    self.assertFalse("")
    self.assertFalse(())
    self.assertFalse([])
    self.assertFalse({})
    self.assertFalse(dict())
    self.assertIsInstance(False, bool)

I can say that in python

* ``False`` is a ``boolean``
* ``dict()`` is ``False`` which means an empty :doc:`dictionary <data_structures_dictionaries>` is ``False``
* ``{}`` is ``False`` which means an empty ``set``/\ ``dictionary`` is ``False``
* ``[]`` is ``False`` which means an empty :doc:`list <data_structures_lists>` is ``False``
* ``()`` is ``False`` which means an empty ``tuple`` is ``False``
* ``""`` is ``False`` which means an empty ``string`` is ``False``
* ``0`` is ``False``

I can sum this up as


* ``False`` is a ``boolean``
* empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None <data_structures_none>` are ``False``

What is True?
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try a similar series of failing tests for ``True`` by adding the following to ``test_data_structures.py``

.. code-block:: python

  def test_what_is_true(self):
   self.assertFalse(True)
   self.assertFalse(1)
   self.assertFalse(-1)
   self.assertFalse("text")
   self.assertFalse((1, 2, 3, "n"))
   self.assertFalse([1, 2, 3, 'n'])
   self.assertFalse({1, 2, 3, "n"})
   self.assertFalse({
     "a": 1,
     "b": 2,
     "c":  3,
     "n": "n"
   })
   self.assertNotIsInstance(True, bool)

the terminal shows an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* When I change all the ``self.assertFalse`` statements to ``self.assertTrue`` in ``test_what_is_true`` I am left with a failing test for the ``assertNotIsInstance`` statement

  .. code-block:: python

  def test_what_is_true(self):
    self.assertTrue(True)
    self.assertTrue(1)
    self.assertTrue(-1)
    self.assertTrue("text")
    self.assertTrue((1, 2, 3, "n"))
    self.assertTrue([1, 2, 3, 'n'])
    self.assertTrue({1, 2, 3, "n"})
    self.assertTrue({
      "a": 1,
      "b": 2,
      "c":  3,
      "n": "n"
    })
    self.assertNotIsInstance(True, bool)

* I change ``self.assertNotIsInstance`` to ``self.assertIsInstance`` and all the tests pass, confirming that ``True`` is an instance of the ``boolean`` object

  .. code-block:: python

  def test_what_is_true(self):
    self.assertTrue(True)
    self.assertTrue(1)
    self.assertTrue(-1)
    self.assertTrue("text")
    self.assertTrue((1, 2, 3, "n"))
    self.assertTrue([1, 2, 3, 'n'])
    self.assertTrue({1, 2, 3, "n"})
    self.assertTrue({
      "a": 1,
      "b": 2,
      "c":  3,
      "n": "n"
    })
    self.assertIsInstance(True, bool)

* I can sum up my current knowledge of python as

  - any value except ``0``, empty objects and :doc:`None <data_structures_none>` are ``True``
  - empty `objects <https://docs.python.org/3/glossary.html#term-object>`_ including ``0`` and :doc:`None <data_structures_none>` are ``False``
  - ``True`` is a ``boolean``
  - ``False`` is a ``boolean``
  - :doc:`None <data_structures_none>` is :doc:`None <data_structures_none>`
