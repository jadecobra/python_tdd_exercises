Data Structures: Lists
======================

Let us explore ``lists/arrays`` in python using Test Driven Development

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I How I setup a Test Driven Development Environment.rst>`_
* `Data Structures <./DATA_STRUCTURES.rst>`_

----

A ``list`` is an object that holds elements. It is a container like ``tuples`` and ``sets``.


* Lists are represented with ``[]``
* They can also be created with the ``list`` keyword
* They are mutable which means they can be changed after creation by calling some operation on them

Create a list
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

create a file named ``test_lists.py`` in the ``tests`` folder with the following code

.. code-block:: python

   import unittest


   class TestLists(unittest.TestCase):

       def test_creating_a_list_with_the_list_keyword(self):
           self.assertEqual(list(0, 1, 2, 3), [])

the terminal shows a `TypeError <./TYPE_ERROR.rst>`_ and we add it to our list of exceptions encountered

.. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # TypeError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* Looking at the error we see that the ``list`` keyword expects one argument but we gave it four, so we are violating the signature for creating lists. How can we pass in values correctly to this object?
* We check out the `documentation <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ and see that list takes in an ``iterable``. An iterable is an object that we can loop over
* update the left input of the ``self.assertEqual`` by putting the values in an iterable, we will use a tuple for this example by placing parentheses around the values
  .. code-block:: python

           def test_creating_a_list_with_the_list_keyword(self):
               self.assertEqual(list((0, 1, 2, 3)), [])
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_
  .. code-block:: python

       >       self.assertEqual(list((0, 1, 2, 3)), [])
       E       AssertionError: Lists differ: [0, 1, 2, 3] != []
       E
       E       First list contains 4 additional elements.
       E       First extra element 0:
       E       1
       E
       E       - [0, 1, 2, 3]
       E       + []

* change the right side to match the values on the left from the terminal
  .. code-block:: python

           def test_creating_a_list_with_the_list_keyword(self):
               self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])
    the test passes

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* we now know we can create a list with the ``list`` keyword but our passing test also shows we can create a list with ``[]`` which uses less characters, let us test this out
  .. code-block:: python

           def test_creating_a_list_with_square_brackets(self):
               self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

How to add items to a list
--------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

let us add a test to ``TestLists`` in ``test_lists.py`` to learn about updating an existing list using the ``append`` method

.. code-block:: python

       def test_adding_an_item_to_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           a_list.append(4)
           self.assertEqual(a_list, [0, 1, 2, 3])

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_ because after we call ``a_list.append(5)``\ , the values in ``a_list`` change

.. code-block:: python

   >       self.assertEqual(a_list, [0, 1, 2, 3])
   E       AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]
   E
   E       First list contains 1 additional elements.
   E       First extra element 4:
   E       4
   E
   E       - [0, 1, 2, 3, 4]
   E       ?            ---
   E
   E       + [0, 1, 2, 3]

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the values on the right side of the ``assertEqual`` statement to make it match the expectation

.. code-block:: python

       def test_adding_an_item_to_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           a_list.append(4)
           self.assertEqual(a_list, [0, 1, 2, 3, 4])

the terminal updates to show passing tests, we started with a list that contained 4 elements then added an element using the ``append`` method, and confirmed that the element we added is now part of the list

Remove an item from a list
--------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

since we know how to add an item to a ``list`` let us add a test for removing an item from a list using the ``remove`` method

.. code-block:: python

       def test_removing_any_item_from_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           a_list.remove(2)
           self.assertEqual(a_list, [0, 1, 2, 3])

the terminal updates to show a difference after we call ``a_list.remove(2)``\ , because the operation removes an element from ``a_list``

.. code-block:: python

   >       self.assertEqual(a_list, [0, 1, 2, 3])
   E       AssertionError: Lists differ: [0, 1, 3] != [0, 1, 2, 3]
   E
   E       First differing element 2:
   E       3
   E       2
   E
   E       Second list contains 1 additional elements.
   E       First extra element 3:
   E       3
   E
   E       - [0, 1, 3]
   E       + [0, 1, 2, 3]
   E       ?

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the test to make the values on the right to match the expected values and we are green again with passing tests

.. code-block:: python

       def test_removing_any_item_from_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           a_list.remove(2)
           self.assertEqual(a_list, [0, 1, 3])

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if there was more than one element, how does python decide which to remove when we call ``.remove(element)`` on a list? There is a way to find out


* add a failing test
  .. code-block:: python

           def test_removing_an_item_from_a_list_when_multiple_exist(self):
               a_list = [0, 2, 1, 2, 3, 2]
               self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
               a_list.remove(2)
               self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_
* update the values on the right to match the expectation
  .. code-block:: python

       def test_remove_an_item_from_a_list_when_multiple_exist(self):
           a_list = [0, 2, 1, 2, 3, 2]
           self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
           a_list.remove(2)
           self.assertEqual(a_list, [0, 1, 2, 3, 2])
    the tests pass, show us from our experiment that the ``remove`` function removes the first occurrence of an item from a list

Remove the last item in a list
------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test to ``TestLists`` in ``test_lists.py``

.. code-block:: python

       def test_removing_the_last_item_of_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           last_item = a_list.pop()
           self.assertEqual(last_item, 0)
           self.assertEqual(a_list, [0, 1, 2, 3])


* we define ``a list`` with 4 elements and confirm the values, then call the ``pop`` method
* we check the value that gets popped and check the list to see what values remain after calling ``pop``

the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_ for the test that checks the value of the item that is popped

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update the value to match the actual value popped
  .. code-block:: python

       def test_removing_the_last_item_of_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           last_item = a_list.pop()
           self.assertEqual(last_item, 3)
           self.assertEqual(a_list, [0, 1, 2, 3])
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_ for the values of ``a_list`` after the last item is popped
* update the values in the ``self.assertEqual`` to make the tests pass
  .. code-block:: python

       def test_removing_the_last_item_of_a_list(self):
           a_list = [0, 1, 2, 3]
           self.assertEqual(a_list, [0, 1, 2, 3])
           last_item = a_list.pop()
           self.assertEqual(last_item, 3)
           self.assertEqual(a_list, [0, 1, 2])

Get a specific item in a list aka Indexing
------------------------------------------

To view an item in a list we provide the position as an index in ``[]`` to the list. ``python`` uses zero-based indexing which means the position of elements starts at 0

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test

.. code-block:: python

       def test_getting_items_in_a_list(self):
           a_list = ['first', 'second', 'third', 'fourth']
           self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
           self.assertEqual(a_list[0], '')
           self.assertEqual(a_list[2], '')
           self.assertEqual(a_list[1], '')
           self.assertEqual(a_list[3], '')
           self.assertEqual(a_list[4], '')
           self.assertEqual(a_list[-1], '')
           self.assertEqual(a_list[-3], '')
           self.assertEqual(a_list[-2], '')
           self.assertEqual(a_list[-4], '')

the terminal output an `AssertionError <./ASSERTION_ERROR.rst>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update the value on the right for the failing test
  .. code-block:: python

       def test_getting_items_in_a_list(self):
           a_list = ['first', 'second', 'third', 'fourth']
           self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
           self.assertEqual(a_list[0], 'first')
           self.assertEqual(a_list[2], '')
           self.assertEqual(a_list[1], '')
           self.assertEqual(a_list[3], '')
           self.assertEqual(a_list[4], '')
           self.assertEqual(a_list[-1], '')
           self.assertEqual(a_list[-3], '')
           self.assertEqual(a_list[-2], '')
           self.assertEqual(a_list[-4], '')
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_ for the next test
* update the value
  .. code-block:: python

       def test_getting_items_in_a_list(self):
           a_list = ['first', 'second', 'third', 'fourth']
           self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
           self.assertEqual(a_list[0], 'first')
           self.assertEqual(a_list[2], 'third')
           self.assertEqual(a_list[1], '')
           self.assertEqual(a_list[3], '')
           self.assertEqual(a_list[-1], '')
           self.assertEqual(a_list[-3], '')
           self.assertEqual(a_list[-2], '')
           self.assertEqual(a_list[-4], '')
    the terminal shows a failure for the next test
* modify each failing line till all the tests pass

IndexError
----------

An ``IndexError`` is raised when we try to get an item from a list but use an index that is greater than the number of items in the list

RED: make it fail
^^^^^^^^^^^^^^^^^

let us add a failing test to illustrate this

.. code-block:: python

       def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
           a_list = ['a', 'b', 'c', 'd']
           self.assertEqual(a_list[5], 'd')

the terminal updates to show an `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add ``IndexError`` to the running list of exceptions encountered
  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # TypeError

* add a ``self.assertRaises`` to confirm that the ``IndexError`` gets raised. You can read more about ``self.assertRaises`` in `Exception Handling <./05_EXCEPTION_HANDLING.rst>`_
  .. code-block:: python

       def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
           a_list = ['a', 'b', 'c', 'd']
           with self.assertRaises(IndexError):
               a_list[5]
    the test passes

View the attributes and methods of a list
-----------------------------------------

In `Classes <./CLASSES.rst>`_ we cover how to view the ``attributes`` and ``methods`` of an object. let us do the same for ``lists``

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test

.. code-block:: python

       def test_attributes_and_methods_of_a_list(self):
           self.maxDiff = None
           self.assertEqual(
               dir(list),
               []
           )


* the terminal updates to show an `AssertionError <./ASSERTION_ERROR.rst>`_
* ``maxDiff`` is an attribute of the ``unittest.TestCase`` class that sets the maximum amount of characters to show in the comparison between the two objects that is displayed in the terminal. When it is set to ``None`` there is no limit to the number of characters

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the test with the expected values

.. code-block:: python

       def test_attributes_and_methods_of_a_list(self):
           self.maxDiff = None
           self.assertEqual(
               dir(list),
               [
                   '__add__',
                   '__class__',
                   '__class_getitem__',
                   '__contains__',
                   '__delattr__',
                   '__delitem__',
                   '__dir__',
                   '__doc__',
                   '__eq__',
                   '__format__',
                   '__ge__',
                   '__getattribute__',
                   '__getitem__',
                   '__gt__',
                   '__hash__',
                   '__iadd__',
                   '__imul__',
                   '__init__',
                   '__init_subclass__',
                   '__iter__',
                   '__le__',
                   '__len__',
                   '__lt__',
                   '__mul__',
                   '__ne__',
                   '__new__',
                   '__reduce__',
                   '__reduce_ex__',
                   '__repr__',
                   '__reversed__',
                   '__rmul__',
                   '__setattr__',
                   '__setitem__',
                   '__sizeof__',
                   '__str__',
                   '__subclasshook__',
                   'append',
                   'clear',
                   'copy',
                   'count',
                   'extend',
                   'index',
                   'insert',
                   'pop',
                   'remove',
                   'reverse',
                   'sort'
               ]
           )

all our tests are passing again

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There are more methods listed than what we have reviewed. Based on their names, we can make a guess as to what they do, and we know some from our tests above


* append - adds an item to the list
* clear
* copy
* count
* extend
* index
* insert
* pop - removes the last item in the list
* remove - removes the first occurrence of a given item in the list
* reverse
* sort

You can add tests for these methods to find out what they do. Do you want to `read more about lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_
