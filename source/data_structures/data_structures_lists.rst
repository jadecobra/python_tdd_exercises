
Data Structures: Lists
======================

A `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is an object that holds elements. It is a container like `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_ and `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_.


* Lists are represented with ``[]``
* They can also be created with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor
* They can contain any `object <https://docs.python.org/3/glossary.html#term-object>`_
* They are mutable which means they can be changed after creation by calling some operation on them


How create a list
-----------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_lists.py`` in the ``tests`` folder with the following code

.. code-block:: python

  import unittest


  class TestLists(unittest.TestCase):

      def test_creating_a_list_with_the_list_keyword(self):
          self.assertEqual(list(0, 1, 2, 3), [])

the terminal shows a :doc:`TypeError` and I add it to the list of exceptions encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # TypeError

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* Looking at the error I see that the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor expects one argument but four are given in the test, so I am violating the signature for creating lists. How can I pass in values correctly to this object?
* I check out the `documentation <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ and see that `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ takes in an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_. An `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ is an object that I can loop over
* I change the left input of the ``self.assertEqual`` by putting the values in an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_, I will use a `tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_ for this example by placing parentheses around the values

  .. code-block:: python

    def test_creating_a_list_with_the_list_keyword(self):
        self.assertEqual(list((0, 1, 2, 3)), [])

  the terminal shows an :doc:`/AssertionError`

  .. code-block:: python

    >    self.assertEqual(list((0, 1, 2, 3)), [])
    E    AssertionError: Lists differ: [0, 1, 2, 3] != []
    E
    E    First list contains 4 additional elements.
    E    First extra element 0:
    E    1
    E
    E    - [0, 1, 2, 3]
    E    + []

* When I change the right side to match the values on the left from the terminal

  .. code-block:: python

    def test_creating_a_list_with_the_list_keyword(self):
        self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

  the test passes

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I can create a list with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor but the passing test also shows I can create a list with ``[]`` which uses less characters, let me add a test for it

  .. code-block:: python

    def test_creating_a_list_with_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

----

How to add an item to a list
-----------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestLists`` in ``test_lists.py`` to test adding items to an existing list with the ``append`` method

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows an :doc:`/AssertionError` because after I call ``a_list.append(5)``, the values in ``a_list`` change

  .. code-block:: python

    >    self.assertEqual(a_list, [0, 1, 2, 3])
    E    AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]
    E
    E    First list contains 1 additional elements.
    E    First extra element 4:
    E    4
    E
    E    - [0, 1, 2, 3, 4]
    E    ?      ---
    E
    E    + [0, 1, 2, 3]

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the values on the right side of the `unittest.TestCase.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ statement to make it match the expectation

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

the terminal shows passing tests. I started with a list that contained 4 elements then added an element using the ``append`` method, and confirmed that the element I added is now part of the list

----

How to remove an item from a list
---------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

Since I know how to add an item to a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ I want to add a test for removing an item from a list using the ``remove`` method

.. code-block:: python

    def test_removing_any_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows a difference after I call ``a_list.remove(2)``, because the operation removes an element from ``a_list``

.. code-block:: python

  >    self.assertEqual(a_list, [0, 1, 2, 3])
  E    AssertionError: Lists differ: [0, 1, 3] != [0, 1, 2, 3]
  E
  E    First differing element 2:
  E    3
  E    2
  E
  E    Second list contains 1 additional elements.
  E    First extra element 3:
  E    3
  E
  E    - [0, 1, 3]
  E    + [0, 1, 2, 3]
  E    ?

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test to make the values on the right to match the expected values and I am green again with passing tests

.. code-block:: python

    def test_removing_any_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 3])

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if there was more than one of the same element in the list? how does python decide which to remove when I call ``.remove(element)`` on a list?

* I add a failing test to find out

  .. code-block:: python

      def test_removing_an_item_from_a_list_when_multiple_exist(self):
          a_list = [0, 2, 1, 2, 3, 2]
          self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
          a_list.remove(2)
          self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])

  the terminal shows an :doc:`/AssertionError`
* and I change the values on the right to match the expectation

  .. code-block:: python

    def test_remove_an_item_from_a_list_when_multiple_exist(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3, 2])

  the tests pass, showing from the experiment that the ``remove`` function removes the first occurrence of an item from a list

----

How to remove the last item in a list
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestLists`` in ``test_lists.py`` to test removing the last item in a list

.. code-block:: python

    def test_removing_the_last_item_of_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 0)
        self.assertEqual(a_list, [0, 1, 2, 3])


* I define ``a list`` with 4 elements and confirm the values, then call the ``pop`` method
* I check the value that gets popped and check the list to see what values remain after calling ``pop``

the terminal shows an :doc:`/AssertionError` for the test that checks the value of the popped item

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the value in the test to match the actual value popped

  .. code-block:: python

    def test_removing_the_last_item_of_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 3)
        self.assertEqual(a_list, [0, 1, 2, 3])

  the terminal shows an :doc:`/AssertionError` for the values of ``a_list`` after the last item is popped
* and I change the values in the ``self.assertEqual`` to make the tests pass

  .. code-block:: python

    def test_removing_the_last_item_of_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 3)
        self.assertEqual(a_list, [0, 1, 2])

----

How to get a specific item from a list
--------------------------------------

To view an item in a list I provide the position as an index in ``[]`` to the list. ``python`` uses zero-based indexing which means the position of elements starts at 0

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test for indexing a list

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

the terminal shows an :doc:`/AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the value on the right for the failing test

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

  the terminal shows an :doc:`/AssertionError` for the next test
* and I change the value to match the expectation

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
* I change each failing line till all the tests pass

IndexError
----------

An ``IndexError`` is raised when I try to get an item from a list but use an index that is greater than the number of items in the list

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to illustrate this

.. code-block:: python

    def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
        a_list = ['a', 'b', 'c', 'd']
        self.assertEqual(a_list[5], 'd')

the terminal shows an `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add ``IndexError`` to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

* then add a ``self.assertRaises`` to confirm that the ``IndexError`` gets raised and make the test pass. You can read more about ``self.assertRaises`` in `Exception Handling <./05_EXCEPTION_HANDLING.rst>`_

  .. code-block:: python

    def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]

----

How to view attributes and :doc:`methods <functions>` of a list
----------------------------------------------------------------

In :doc:`class </classes>` I cover how to view the ``attributes`` and ``methods`` of an object. Let us look at the same for ``lists``

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test

.. code-block:: python

    def test_attributes_and_methods_of_a_list(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            []
        )

* the terminal shows an :doc:`/AssertionError`
* ``maxDiff`` is an attribute of the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`class </classes>` that sets the maximum amount of characters to show in the comparison between the two objects that is displayed in the terminal. When it is set to :doc:`None <data_structures_none>` there is no limit to the number of characters

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test with the expected values

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

all the tests are passing again

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There are more :doc:`methods <functions>` listed than what I have reviewed. Based on their names, I can make a guess as to what they do, and I know some from the tests above

* append - adds an item to the list
* clear - does this clear the items in the list?
* copy - does this create a copy of the list?
* count - does this count the number of items in the list?
* extend - extends the list?
* index
* insert - does this place an item in the list?
* pop - removes the last item in the list
* remove - removes the first occurrence of a given item in the list
* reverse - does this reverse the list?
* sort - does this sort the elements in the list?

You can add tests for these :doc:`methods <functions>` to find out what they do or `read more about lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_
