Data Structures: None
=====================

This chapter covers the null object ``(None)`` using Test Driven Development in python

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I How I setup a Test Driven Development Environment.md>`_
* `Data Structures <./DATA_STRUCTURES.md>`_

----

What is None?
-------------

``(None)`` is an object used to represent the absence of a value, let us explore it with tests

RED: make it fail
^^^^^^^^^^^^^^^^^

create a file named ``test_data_structures.py`` in the ``(tests)`` folder

.. code-block:: python

   import unittest


   class TestDataStructures(unittest.TestCase):

       def test_none_is_none(self):
           self.assertIsNotNone(None)

the terminal gives us an `AssertionError <./ASSERTION_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

change the ``(assert)`` statement in ``(test_none_is_none)`` to make it pass

.. code-block:: python

           self.assertIsNone(None)

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There are other python objects we can compare with ``(None)`` to learn more about what it is or is not

Is None a boolean?
------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to compare ``(None)`` with booleans

.. code-block:: python

       def test_is_none_a_boolean(self):
           self.assertIsNone(True)
           self.assertIsNone(False)

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``(test_is_none_a_boolean)`` to make the tests pass

.. code-block:: python

       def test_is_none_a_boolean(self):
           self.assertIsNotNone(True)
           self.assertIsNotNone(False)

we now know that


* ``(False)`` is not ``(None)``
* ``(True)`` is not ``(None)``
* ``(None)`` is ``(None)``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

booleans are represented by the keyword ``(bool)`` in python so we can do an instance test using another ``unittest.TestCase`` method that checks if an ``(object)`` is an instance of a `class <./CLASSES.md>`_


*
  ### RED: make it fail

    update ``(test_is_none_a_boolean)`` with ``self.assertIsInstance``

  .. code-block:: python

           def test_is_none_a_boolean(self):
               self.assertIsNotNone(True)
               self.assertIsNotNone(False)
               self.assertIsInstance(None, bool)

    we now see an `AssertionError <./ASSERTION_ERROR.md>`_ in the terminal because ``(None)`` is not an instance of a boolean

  .. code-block:: python

       AssertionError: None is not an instance of <class 'bool'>

*
  ### GREEN: make it pass

    update ``(test_is_none_a_boolean)`` to make the test pass

  .. code-block:: python

           def test_is_none_a_boolean(self):
               self.assertIsNotNone(True)
               self.assertIsNotNone(False)
               self.assertNotIsInstance(None, bool)

* We can summarize what we know about ``(None)`` so far as it is not a boolean and it is ``(None)``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What about other data types in python? Let us find out if ``(None)`` is equal to any ``(int)``\ , ``(float)``\ , ``(string)``\ , ``(tuple)``\ , ``(list)``\ , ``(set)`` or ``(dict)``

Is None an integer?
-------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to compare ``(None)`` with ``(int)``

.. code-block:: python

       def test_is_none_an_integer(self):
           self.assertIsNone(-1)
           self.assertIsNone(0)
           self.assertIsNone(1)

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

we update ``(test_is_none_an_integer)`` to make it pass

.. code-block:: python

           self.assertIsNotNone(-1)
           self.assertIsNotNone(0)
           self.assertIsNotNone(1)

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

integers are represented by the keyword ``(int)`` in python so we can do an instance test like we did above


*
  ### RED: make it fail

    add a new line to ``(test_is_none_an_integer)`` with ``self.assertIsInstance``

  .. code-block:: python

           def test_is_none_an_integer(self):
               self.assertIsNotNone(-1)
               self.assertIsNotNone(0)
               self.assertIsNotNone(1)
               self.assertIsInstance(None, int)

    an `AssertionError <./ASSERTION_ERROR.md>`_ is displayed in the terminal because ``(None)`` is not an instance of an integer

  .. code-block:: python

       AssertionError: None is not an instance of <class 'int'>

*
  ### GREEN: make it pass

    we update ``(test_is_none_an_integer)`` to make the test pass

  .. code-block:: python

           def test_is_none_an_integer(self):
               self.assertIsNotNone(-1)
               self.assertIsNotNone(0)
               self.assertIsNotNone(1)
               self.assertNotIsInstance(None, int)

* summarizing what we know about ``(None)`` so far as

  * ``(None)`` is not an integer
  * ``(None)`` is not a boolean
  * ``(None)`` is ``(None)``

Is None a string?
-----------------

let us add a test for ``(strings)``. A string is any characters that are enclosed by single, double or triple quotes e.g. ``'single quotes'``\ , ``"double quotes"``\ , ``'''triple single quotes'''``\ , ``"""triple double quotes"""``

RED: make it fail
^^^^^^^^^^^^^^^^^

we add a new failing test to ``test_data_structures.py`` to compare ``(None)`` with a ``(string)``

.. code-block:: python

       def test_is_none_a_string(self):
           self.assertIsNone('')
           self.assertIsNone("text")

and the terminal gives us an `AssertionError <./ASSERTION_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``(test_is_none_a_string)`` to make it pass

.. code-block:: python

       def test_is_none_a_string(self):
           self.assertIsNotNone('')
           self.assertIsNotNone("text")

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

``(strings)`` are represented by the ``(str)`` class keyword in python, we will add a test to check if ``(None)`` is an instance of the ``(string)`` class


*
  ### RED: make it fail

    update ``(test_is_none_a_string)`` and the terminal updates to show a failing test

  .. code-block:: python

           def test_is_none_a_string(self):
               self.assertIsNotNone('')
               self.assertIsNotNone("text")
               self.assertIsInstance(None, str)

*
  ### GREEN: make it pass
    change the failing line in the test to make it pass

  .. code-block:: python

           def test_is_none_a_string(self):
               self.assertIsNotNone('')
               self.assertIsNotNone("text")
               self.assertNotIsInstance(None, str)

* Our knowledge of ``(None)`` has grown to

  * ``(None)`` is not a string
  * ``(None)`` is not an integer
  * ``(None)`` is not a boolean
  * ``(None)`` is ``(None)``

Is None a tuple?
----------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a new test to ``test_data_structures.py``

.. code-block:: python

       def test_is_none_a_tuple(self):
           self.assertIsNone(())
           self.assertIsNone((1, 2, 3, 'n'))
           self.assertIsInstance(None, tuple)

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_

.. code-block:: python

   AssertionError: () is not None


* ``()`` is how ``(tuples)`` are represented in python
* Do you want to `read more about tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* modify the first line in\ ``(test_is_none_a_tuple)`` to make it pass
  .. code-block:: python

           def test_is_none_a_tuple(self):
               self.assertIsNotNone(())
    and the terminal displays an `AssertionError <./ASSERTION_ERROR.md>`_ for the second line
  .. code-block:: python

       AssertionError: (1, 2, 3, 'n') is not None
    because the ``(tuple)`` that contains the four elements ``1, 2, 3, 'n'`` is not ``(None)``
* update the failing line in ``(test_is_none_a_tuple)``
  .. code-block:: python

           def test_is_none_a_tuple(self):
               self.assertIsNotNone(())
               self.assertIsNotNone((1, 2, 3, 'n'))
    the terminal now shows another `AssertionError <./ASSERTION_ERROR.md>`_ for the next line in our test but with a different message
  .. code-block:: python

       AssertionError: None is not an instance of <class 'tuple'>

* change the failing line in the test to make it pass
  .. code-block:: python

           def test_is_none_a_tuple(self):
               self.assertIsNotNone(())
               self.assertIsNotNone((1, 2, 3, 'n'))
               self.assertNotIsInstance(None, tuple)

* we now know that in python

  * ``(None)`` is not a ``(tuple)``
  * ``(None)`` is not a ``(string)``
  * ``(None)`` is not an ``(integer)``
  * ``(None)`` is not a ``(boolean)``
  * ``(None)`` is ``(None)``

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Based on what we have seen so far, it is safe to assume that ``(None)`` is only ``(None)`` and is not any other data structure, let us find out if this assumption is false.

Is None a list(array)?
----------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

we add a new test to our series of tests

.. code-block:: python

       def test_is_none_a_list(self):
           self.assertIsNone([])
           self.assertIsNone([1, 2, 3, "n"])
           self.assertIsInstance(None, list)

the terminal shows an `AssertionError <./ASSERTION_ERROR.md>`_

.. code-block:: python

   AssertionError: [] is not None


* ``[]`` is how `lists <./LISTS.md>`_ are represented in python
* what is the difference between a ``(list)`` and a ``(tuple)`` other than ``[]`` vs ``()``\ ?
* Do you want to `read more about lists <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#list>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

We've done this dance a few times now so we can update ``(test_is_none_a_list)`` to make it pass. With the passing tests our knowledge of ``(None)`` is updated to


* ``(None)`` is not a ``(list)``
* ``(None)`` is not a ``(tuple)``
* ``(None)`` is not a ``(string)``
* ``(None)`` is not an ``(integer)``
* ``(None)`` is not a ``(boolean)``
* ``(None)`` is ``(None)``

Is None a set?
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

following the same pattern from earlier, we add a new failing test, this time for sets

.. code-block:: python

       def test_is_none_a_set(self):
           self.assertIsNone({})
           self.assertIsNone({1, 2, 3, "n"})
           self.assertIsInstance(None, set)

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_

.. code-block:: python

   AssertionError: {} is not None


* ``{}`` is how ``(sets)`` are represented in python
* Do you want to `read more about sets <https://docs.python.org/3/tutorial/datastructures.html?highlight=sets#sets>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the tests to make them pass and we can update our knowledge of ``(None)`` to state that


* ``(None)`` is not a ``(set)``
* ``(None)`` is not a ``(list)``
* ``(None)`` is not a ``(tuple)``
* ``(None)`` is not a ``(string)``
* ``(None)`` is not an ``(integer)``
* ``(None)`` is not a ``(boolean)``
* ``(None)`` is ``(None)``

Is None a dictionary?
---------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

let us add a new test

.. code-block:: python

       def test_is_none_a_dictionary(self):
           self.assertIsNone(dict())
           self.assertIsNone({
               "a": 1,
               "b": 2,
               "c":  3,
               "n": "n"
           })
           self.assertIsInstance(None, dict)

the terminal displays an `AssertionError <./ASSERTION_ERROR.md>`_

.. code-block:: python

   AssertionError: {} is not None


* ``dict()`` is how we create an empty ``(dictionary)``
* ``{}`` is how `dictionaries <./DICTIONARIES.md>`_ are represented in python. Wait a minute, sets are also represented with ``{}``\ , the difference is that dictionaries contain key/value pairs
* Do you want to `read more about dictionaries <https://docs.python.org/3/tutorial/datastructures.html?highlight=sets#dictionaries>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the tests to make them pass and we can update our knowledge of ``(None)`` to state that


* ``(None)`` is not a ``(dictionary)``
* ``(None)`` is not a ``(set)``
* ``(None)`` is not a ``(list)``
* ``(None)`` is not a ``(tuple)``
* ``(None)`` is not a ``(string)``
* ``(None)`` is not an ``(integer)``
* ``(None)`` is not a ``(boolean)``
* ``(None)`` is ``(None)``
