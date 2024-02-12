.. include:: ../../links.rst

##################################
lists
##################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lTL9hLjzXWc?si=0vaap7TiDXdLkTk7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

A `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is an `object <https://docs.python.org/3/glossary.html#term-object>`_ that can hold other `objects <https://docs.python.org/3/glossary.html#term-object>`_


* Lists are represented with ``[]``
* Lists can be created with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor
* Lists can contain any `object <https://docs.python.org/3/glossary.html#term-object>`_
* Lists can be changed after creation by performing an operation, they are mutable
* Lists can be looped over

**********************
How to create a list
**********************

red: make it fail
==================

I make a file called ``test_lists.py`` in the ``tests`` folder with the following code

.. code-block:: python

  import unittest


  class TestLists(unittest.TestCase):

      def test_creating_a_list_with_the_list_constructor(self):
          self.assertEqual(list(0, 1, 2, 3), None)

the terminal shows a :ref:`TypeError`

.. code-block:: python

  TypeError: list expected at most 1 argument, got 4


green: make it pass
===================
* I will add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

  - Looking at the error I see that the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor expects one argument but four are given in the test, so I am not following the signature for creating lists
  - a `constructor <https://en.wikipedia.org/wiki/Constructor_(object-oriented_programming)>`_ is a :ref:`function<functions>` that is used to create an instance of a :doc:`class </classes/classes>`
  - I read `python's documentation for lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ and see that the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor takes an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ as input
  - An `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ is an object I can go over its items one by one in a loop - `tuples <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_, `lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_, `sets <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ and :doc:`dictionaries </data_structures/dictionaries>` are iterable

* I will make the values provided to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor by placing them in parentheses to make them a `tuple <https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple>`_

  .. code-block:: python

    def test_creating_a_list_with_the_list_constructor(self):
        self.assertEqual(list((0, 1, 2, 3)), [])

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: [0, 1, 2, 3] != None

* When I will make the right side to match the values on the left from the terminal

  .. code-block:: python

    def test_creating_a_list_with_the_list_constructor(self):
        self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

  the test passes

refactor: make it better
=========================

* I can create a list with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor but the passing test also shows I can create a list with ``[]`` which uses less characters. I will add a test for it

  .. code-block:: python

    def test_creating_a_list_with_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 4)))

  the terminal shows an :ref:`AssertionError` for the last value

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 4]

* I update the test to make it pass

  .. code-block:: python

    def test_creating_a_list_with_square_brackets(self):
        self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

----

*******************************
How to add an item to a list
*******************************

red: make it fail
===================

I will add a test to for adding items to an existing list with the `append <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>`

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3])

- ``a_list = [0, 1, 2, 3]`` creates a list of 4 items and calls it ``a_list``
- the first ``self.assertEqual(a_list, [0, 1, 2, 3])`` checks that ``a_list`` contains the four items
- ``a_list.append(4)`` calls the `append <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>` of the list
- ``self.assertEqual(a_list, [0, 1, 2, 3])`` checks what ``a_list`` contains after `append <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ is called

the terminal shows an :ref:`AssertionError` because the values in ``a_list`` change after ``a_list.append(4)``

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

green: make it pass
===================

I will make the values in the test to make it match the result

.. code-block:: python

    def test_adding_an_item_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

the terminal shows passing tests.

I started with a list that contained 4 things, added something using the `append <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method, then confirmed what I will added is now part of the list

----

***********************************
How to remove an item from a list
***********************************

red: make it fail
===================

Since I know how to add an item to a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ I want to add a test for removing an item from a list using the `remove <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method

.. code-block:: python

    def test_removing_an_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows an :ref:`AssertionError` because the values in ``a_list`` no longer contain ``2`` after the call ``a_list.remove(2)``

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 3] != [0, 1, 2, 3]

green: make it pass
===================

I will make the test to make the values on the right match the result and the test passes

.. code-block:: python

    def test_removing_an_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 3])

refactor: make it better
=========================

What happens when there is more than one of the same item in a list? How does Python decide which of them to remove when I call ``.remove(item)`` on a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_?

* I will add a failing test to find out

  .. code-block:: python

    def test_removing_an_item_from_a_list_when_multiple_exist(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 2] != [0, 2, 1, 2, 3, 2]

* and I will make the values on the right to match the result

  .. code-block:: python

    def test_remove_an_item_from_a_list_when_multiple_exist(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3, 2])

  From the test I see that teh `remove <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`function<functions>` removes the first item when there is more than one of the same item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

----

****************************************
How to remove the last item from a list
****************************************

red: make it fail
===================

I will add a test for removing the last item from a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

    def test_removing_the_last_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 0)
        self.assertEqual(a_list, [0, 1, 2, 3])

* ``last_item = a_list.pop()`` calls the `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ method of ``a_list`` and uses ``last_item`` as a name to represent the value that is returned
* ``self.assertEqual(last_item, 0)`` checks that ``last_item`` is equal to ``0``
* ``self.assertEqual(a_list, [0, 1, 2, 3])`` checks the values that remain in ``a_list`` after calling `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

the terminal shows an :ref:`AssertionError` for the test that checks the value of the popped item called ``last_item``

.. code-block:: python

  >       self.assertEqual(last_item, 0)
  E       AssertionError: 3 != 0

green: make it pass
===================

* I will make the value in the test to match the actual value popped

  .. code-block:: python

    self.assertEqual(last_item, 3)

  and the terminal shows an :ref:`AssertionError` for the values of ``a_list`` after the last item is popped

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 3]

* I will make the values in the test that checks the values of ``a_list`` after calling `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

  .. code-block:: python

    def test_removing_the_last_item_from_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertEqual(a_list, [0, 1, 2, 3])
        last_item = a_list.pop()
        self.assertEqual(last_item, 3)
        self.assertEqual(a_list, [0, 1, 2])

  the terminal shows passing tests

----

****************************************
How to get a specific item from a list
****************************************

To view an item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ I can provide the position as an index in ``[]`` to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. Python uses zero-based indexing which means the positions of items starts at 0. I can also view items from the right side of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ by using negative numbers

red: make it fail
===================

I will add a failing test for indexing a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'first' != ''
  - first

green: make it pass
===================

* I will make the value in the test to make the failing line pass

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

  the terminal shows an :ref:`AssertionError` for the next test

  .. code-block:: python

    AssertionError: 'third' != ''
    - third

* I will make the value to match the result

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

* I will make each failing line until all the tests pass

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

----

************
IndexError
************

An IndexError_ is raised when I try to get an item from a list but use a number that is greater than the number of items in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_.

red: make it fail
===================

I will add a failing test to show this

.. code-block:: python

    def test_indexing_with_number_greater_than_length_of_list(self):
        a_list = ['first', 'second', 'third', 'fourth']
        a_list[5]

the terminal shows an IndexError_

.. code-block:: python

  >       a_list[5]
  E       IndexError: list index out of range

green: make it pass
===================

* I will add IndexError_ to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # IndexError

* then add a ``self.assertRaises`` to confirm that the ``IndexError`` gets raised and the test passes

  .. code-block:: python

    def test_indexing_with_number_greater_than_length_of_list(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]

  `unittest.TestCase.assertRaises`_ takes an `Exception <https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception>`_ as input and confirms that it is raised. You can read more about ``self.assertRaises`` in :doc:`/how_to/exception_handling_tests`

refactor: make it better
=========================

* I will add one more line to test indexing with a negative number that is greater than the length of the list

  .. code-block:: python

    def test_indexing_with_number_greater_than_length_of_list(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]
        a_list[-5]

  the terminal shows an IndexError_
* When I indent the line under the `self.assertRaises` context, the test passes

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[5]
        a_list[-5]

----

**************************************************
How to view the attributes and methods of a list
**************************************************

The chapter on :doc:`/classes/classes` shows how to view the :doc:`attributes </exceptions/AttributeError>` and :ref:`methods<functions>` of an `object <https://docs.python.org/3/glossary.html#term-object>`_ by using the dir_ :ref:`function<functions>`. Let us try it for `lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

red: make it fail
===================

I will add a failing test using the dir_ :ref:`function<functions>`

.. code-block:: python

    def test_attributes_and_methods_of_a_list(self):
        self.assertEqual(
            dir(list),
            []
        )

the terminal shows an :ref:`AssertionError`

  .. code-block::python

    AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

green: make it pass
===================

* The terminal also shows a recommendation on how to see the difference between ``dir(list)`` and ``[]``

  .. code-block:: python

    Diff is 748 characters long. Set self.maxDiff to None to see it

  `maxDiff <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.maxDiff>`_ is an attribute of the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`class </classes/classes>` that sets the maximum amount of characters to show in the comparison between the two objects displayed in the terminal. When it is set to :ref:`None` there is no limit to the number of characters
* I will add ``self.maxDiff`` to the test

  .. code-block:: python

    def test_attributes_and_methods_of_a_list(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            []
        )

  the terminal shows a long list of items

I copy the items from the terminal and remove the extra characters

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

the terminal shows passing tests

refactor: make it better
=========================

There are more :ref:`methods<functions>` listed than what I have reviewed. Based on their names, I can make a guess as to what they do, and I know some from the tests above

* append - adds an item to the list
* clear - does this clear the items in the list?
* copy - does this create a copy of the list?
* count - does this count the number of items in the list?
* extend - does this extend the list?
* index
* insert - does this place an item in the list? what's the difference between this and append?
* pop - removes the last item in the list
* remove - removes the first occurrence of a given item in the list
* reverse - does this reverse the list?
* sort - does this sort the items in the list?

You can add tests for these :ref:`methods<functions>` to find out what they do or `read more about lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_

you encountered the following exceptions

* :ref:`AssertionError`
* :ref:`TypeError`
* IndexError_

----

:doc:`/code/code_lists`