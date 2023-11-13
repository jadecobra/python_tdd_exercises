Data Structures: Booleans
=========================

Let us take a look at Data Structures in python using Test Driven Development. This chapter covers ``booleans``

There are only two values that are boolean - :doc:`True </data structures: booleans>` and :doc:`False </data structures: booleans>`. I will learn about booleans by comparing it with the data structures in python to figure what they are and what they are not

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


* when I change all the ``self.assertTrue`` statements in ``test_what_is_false`` to ``self.assertFalse`` I am left with one failing test
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

* I now know that in python

  * :doc:`False </data structures: booleans>` is a ``boolean``
  * ``dict()`` is :doc:`False </data structures: booleans>` which means an empty ``dictionary`` is :doc:`False </data structures: booleans>`
  * ``{}`` is :doc:`False </data structures: booleans>` which means an empty ``set``/\ ``dictionary`` is :doc:`False </data structures: booleans>`
  * ``[]`` is :doc:`False </data structures: booleans>` which means an empty ``list`` is :doc:`False </data structures: booleans>`
  * ``()`` is :doc:`False </data structures: booleans>` which means an empty ``tuple`` is :doc:`False </data structures: booleans>`
  * ``""`` is :doc:`False </data structures: booleans>` which means an empty ``string`` is :doc:`False </data structures: booleans>`
  * ``0`` is :doc:`False </data structures: booleans>`

I can sum this up as


* :doc:`False </data structures: booleans>` is a ``boolean``
* empty things including ``0`` and :doc:`None </data structures: None>` are :doc:`False </data structures: booleans>`

What is True?
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

What if I try a similar series of failing tests for :doc:`True </data structures: booleans>` by adding the following to ``test_data_structures.py``

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


* change all the ``self.assertFalse`` statements in ``test_what_is_true`` to ``self.assertTrue`` and I have one failing test left
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

* I can sum up the current knowledge of python thus

  * any value except ``0``, empty objects and :doc:`None </data structures: None>` is :doc:`True </data structures: booleans>`
  * empty objects including ``0`` and :doc:`None </data structures: None>` are :doc:`False </data structures: booleans>`
  * :doc:`True </data structures: booleans>` is a ``boolean``
  * :doc:`False </data structures: booleans>` is a ``boolean``
  * :doc:`None </data structures: None>` is :doc:`None </data structures: None>`

HOORAY

You have built up your knowledge of python, you now know about booleans. Take a moment to celebrate
