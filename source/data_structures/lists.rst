
Data Structures: Lists
======================

A `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is an `object <https://docs.python.org/3/glossary.html#term-object>`_ that holds other `objects <https://docs.python.org/3/glossary.html#term-object>`_. It is a container like `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_ and `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_, and is `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_.


* Lists are represented with ``[]``
* Lists can be created with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor
* Lists can contain any `object <https://docs.python.org/3/glossary.html#term-object>`_
* Lists can be changed after creation by performing an operation, they are mutable
* Lists can be looped over


How to create a list
----------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a file called ``test_lists.py`` in the ``tests`` folder with the following code

.. code-block:: python

  import unittest


  class TestLists(unittest.TestCase):

      def test_creating_a_list_with_the_list_keyword(self):
          self.assertEqual(list(0, 1, 2, 3), [])

the terminal shows a :doc:`/exceptions/TypeError`

.. code-block:: python

  TypeError: list expected at most 1 argument, got 4


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^
* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

  - Looking at the error I see that the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor expects one argument but four are given in the test, so I am not following the signature for creating lists
  - I read `python's documentation for lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ and see that the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor takes in an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_
  - An `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ is an object that I can loop over - `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_, `lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_, `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ and :doc:`dictionaries </data_structures/dictionaries>` are iterable

* I change the left input of the ``self.assertEqual`` statement by placing the values in parentheses to make them a `tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_, which is `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_

  .. code-block:: python

    def test_creating_a_list_with_the_list_keyword(self):
        self.assertEqual(list((0, 1, 2, 3)), [])

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    E    AssertionError: Lists differ: [0, 1, 2, 3] != []

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
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 4)))

  the terminal shows an :doc:`/exceptions/AssertionError` for the last value, and I update it to make the test pass

  .. code-block:: python

    def test_creating_a_list_with_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

----

How to add an item to a list
-----------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestLists`` in ``test_lists.py`` to test adding items to an existing list with the `append <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows an :doc:`/exceptions/AssertionError` because the values in ``a_list`` change after the call ``a_list.append(5)``

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the values on the right side of the `self.assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ statement to make it match the result

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

the terminal shows passing tests.

I started with a list that contained 4 elements, added an element using the ``append`` method, then confirmed that the element I added is now part of the list

----

How to remove an item from a list
---------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

Since I know how to add an item to a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ I want to add a test for removing an item from a list using the `remove <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method

.. code-block:: python

    def test_removing_an_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows an :doc:`/exceptions/AssertionError` because the values in ``a_list`` no longer contain ``2`` after the call ``a_list.remove(2)``

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 3] != [0, 1, 2, 3]

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test to make the values on the right match the result and the test passes

.. code-block:: python

    def test_removing_an_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 3])

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if there was more than one of the same element in the list? How does Python decide the element to remove when I call ``.remove(element)`` on a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_?

* I add a failing test to find out

  .. code-block:: python

    def test_removing_an_item_from_a_list_when_multiple_exist(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block :: python

    AssertionError: Lists differ: [0, 1, 2, 3, 2] != [0, 2, 1, 2, 3, 2]

* and I change the values on the right to match the result

  .. code-block:: python

    def test_remove_an_item_from_a_list_when_multiple_exist(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3, 2])

  the tests pass, showing from the experiment that the ``remove`` function removes the first occurrence of an item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

----

How to remove the last item in a list
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestLists`` in ``test_lists.py`` to test removing the last item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

    def test_removing_the_last_item_of_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 0)
        self.assertEqual(a_list, [0, 1, 2, 3])


* ``a_list = [0, 1, 2, 3]`` defines a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ with 4 elements called ``a_list``
* ``last_item = a_list.pop()`` calls the `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method of ``a_list`` and uses ``last_item`` as a name to represent the value that is returned
* ``self.assertEqual(last_item, 0)`` checks that ``last_item`` is equal to ``0``
* ``self.assertEqual(a_list, [0, 1, 2, 3])`` checks the values that remain in ``a_list`` after calling `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

the terminal shows an :doc:`/exceptions/AssertionError` for the test that checks the value of the popped item called ``last_item``

.. code-block:: python

  >       self.assertEqual(last_item, 0)
  E       AssertionError: 3 != 0

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

  and the terminal shows an :doc:`/exceptions/AssertionError` for the values of ``a_list`` after the last item is popped

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 3]


* I change the values in the ``self.assertEqual`` call to make the tests pass

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

To view an item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ I provide the position as an index in ``[]`` to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. Python uses zero-based indexing which means the positions of elements starts at 0. I can also view items from the right by using negative numbers

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test for indexing a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

    def test_getting_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']
        self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
        self.assertEqual(a_list[0], '')
        self.assertEqual(a_list[2], '')
        self.assertEqual(a_list[1], '')
        self.assertEqual(a_list[3], '')
        self.assertEqual(a_list[-1], '')
        self.assertEqual(a_list[-3], '')
        self.assertEqual(a_list[-2], '')
        self.assertEqual(a_list[-4], '')

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: 'first' != ''
  - first

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the value in the test to make the failing line pass

  .. code-block:: python

    def test_getting_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']
        self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[2], '')
        self.assertEqual(a_list[1], '')
        self.assertEqual(a_list[3], '')
        self.assertEqual(a_list[-1], '')
        self.assertEqual(a_list[-3], '')
        self.assertEqual(a_list[-2], '')
        self.assertEqual(a_list[-4], '')

  the terminal shows an :doc:`/exceptions/AssertionError` for the next test

  .. code-block:: python

    AssertionError: 'third' != ''
    - third

* I change the value to match the result

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

  .. code-block:: python

    AssertionError: 'second' != ''
    - second

* I change each failing line until all the tests pass

  .. code-block:: python

    def test_getting_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']
        self.assertEqual(a_list, ['first', 'second', 'third', 'fourth'])
        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[1], 'second')
        self.assertEqual(a_list[3], 'fourth')
        self.assertEqual(a_list[-1], 'fourth')
        self.assertEqual(a_list[-3], 'second')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[-4], 'first')

IndexError
----------

An `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_ is raised when I try to get an item from a list but use a number that is greater than the number of items in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_.

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to show this

.. code-block:: python

    def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
        a_list = ['first', 'second', 'third', 'fourth']
        self.assertEqual(a_list[5], 'BOOM')

the terminal shows an `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_

.. code-block:: python

  >       self.assertEqual(a_list[5], 'BOOM')
  E       IndexError: list index out of range


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add `IndexError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndexError>`_ to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # IndexError

* then add a ``self.assertRaises`` to confirm that the ``IndexError`` gets raised to make the test pass.

  .. code-block:: python

    def test_indexing_with_a_number_greater_than_the_length_of_the_list(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]

  You can read more about ``self.assertRaises`` in :doc:`/how_to/exception_handling_tests`

----

How to view attributes and :doc:`methods </functions/functions>` of a list
-----------------------------------------------------------------------------

The chapter on :doc:`/classes/classes` shows how to view the ``attributes`` and :doc:`methods </functions/functions>` of an object. Let us take a look at the ``attributes`` and :doc:`methods </functions/functions>` of `lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test using the `dir <https://docs.python.org/3/library/functions.html?highlight=dir#dir>`_ :doc:`function </functions/functions>`

.. code-block:: python

    def test_attributes_and_methods_of_a_list(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            []
        )

* the terminal shows an :doc:`/exceptions/AssertionError`
* `maxDiff <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.maxDiff>`_ is an attribute of the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`class </classes/classes>` that sets the maximum amount of characters to show in the comparison between the two objects displayed in the terminal. When it is set to :doc:`None </data_structures/none>` there is no limit to the number of characters

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the test with the expected values

.. note::

  Your results may vary based on your version of Python

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
                '__getstate__',
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

There are more :doc:`methods </functions/functions>` listed than what I have reviewed. Based on their names, I can make a guess as to what they do, and I know some from the tests above

* append - adds an item to the list
* clear - does this clear the items in the list?
* copy - does this create a copy of the list?
* count - does this count the number of items in the list?
* extend - does this extend the list?
* index
* insert - does this place an item in the list?
* pop - removes the last item in the list
* remove - removes the first occurrence of a given item in the list
* reverse - does this reverse the list?
* sort - does this sort the elements in the list?

You can add tests for these :doc:`methods </functions/functions>` to find out what they do or `read more about lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_

:doc:`/code/lists`