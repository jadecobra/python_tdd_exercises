Data Structures: Booleans
=========================

Let us take a look at Data Structures in python using Test Driven Development. This chapter covers ``booleans``

There are only two values that are boolean - ``True`` and ``False``. We will learn about booleans by comparing it with the data structures in python to figure what they are and what they are not

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment`
* `Data Structures <./DATA_STRUCTURES.rst>`_

----

What is False?
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test to ``test_data_structures.py`` called ``test_what_is_false``

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

the terminal updates to show an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* when we change all the ``self.assertTrue`` statements in ``test_what_is_false`` to ``self.assertFalse`` we are left with one failing test
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

* update ``self.assertNotIsInstance`` to ``self.assertIsInstance`` and all the tests pass
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

* we now know that in python

  * ``False`` is a ``boolean``
  * ``dict()`` is ``False`` which means an empty ``dictionary`` is ``False``
  * ``{}`` is ``False`` which means an empty ``set``/\ ``dictionary`` is ``False``
  * ``[]`` is ``False`` which means an empty ``list`` is ``False``
  * ``()`` is ``False`` which means an empty ``tuple`` is ``False``
  * ``""`` is ``False`` which means an empty ``string`` is ``False``
  * ``0`` is ``False``

we can sum this up as


* ``False`` is a ``boolean``
* empty things including ``0`` and :doc:`None </data structures: None>` are ``False``

What is True?
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

What if we try a similar series of failing tests for ``True`` by adding the following to ``test_data_structures.py``

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

the terminal updates to show an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* change all the ``self.assertFalse`` statements in ``test_what_is_true`` to ``self.assertTrue`` and we have one failing test left
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

* update ``self.assertNotIsInstance`` to ``self.assertIsInstance`` and all the tests pass
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

* we can sum up our current knowledge of python thus

  * any value except ``0``, empty objects and :doc:`None </data structures: None>` is ``True``
  * empty objects including ``0`` and :doc:`None </data structures: None>` are ``False``
  * ``True`` is a ``boolean``
  * ``False`` is a ``boolean``
  * :doc:`None </data structures: None>` is :doc:`None </data structures: None>`

HOORAY

You have built up your knowledge of python, you now know about booleans. Take a moment to celebrate
