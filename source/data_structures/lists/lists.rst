.. include:: ../../links.rst

#################################################################################
lists
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/lTL9hLjzXWc?si=0vaap7TiDXdLkTk7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

A `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is an :ref:`object<classes>` that can hold other objects_

* they are represented with ``[]``
* they can be made with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_
* they can be changed after they exist by performing an operation, this means they are mutable

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``lists`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh lists

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 lists

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_lists.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_lists.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass

----

*********************************************************************************
test_make_a_list
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list``

.. code-block:: python

  import unittest


  class TestLists(unittest.TestCase):

      def test_make_a_list(self):
          self.assertEqual(list(0, 1, 2, 3), None)

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list expected at most 1 argument, got 4

* :ref:`TypeError` is raised because the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_ expects one argument but I gave four in the test. I am not following the signature for making lists
* An iterable_ is an object with items I can go over one by one in a loop - tuples_, `lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_, sets_ and :ref:`dictionaries` are iterable_

green: make it pass
#################################################################################

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError

* I change the values provided to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_ to a tuple_ by placing them in parentheses

  .. code-block:: python

    def test_make_a_list(self):
        self.assertEqual(list((0, 1, 2, 3)), None)

  and get :ref:`AssertionError` in the terminal

  .. code-block:: python

    AssertionError: [0, 1, 2, 3] != None

* When I change the right side to match the values on the left from the terminal

  .. code-block:: python

    def test_make_a_list(self):
        self.assertEqual(list((0, 1, 2, 3)), [0, 1, 2, 3])

  the test passes

refactor: make it better
#################################################################################

I can make a list with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_ and the passing test shows I can make a list with ``[]`` which uses less characters. I add a test for it

.. code-block:: python

  def test_make_a_list_w_square_brackets(self):
      self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 4)))

the terminal shows :ref:`AssertionError` for the last value

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 4]

I change the value in the test to make it pass

.. code-block:: python

  def test_make_a_list_w_square_brackets(self):
      self.assertEqual([0, 1, 2, 3], list((0, 1, 2, 3)))

----

*********************************************************************************
test_make_a_list_from_an_iterable
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list_from_an_iterable``

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

      def test_make_a_list_from_an_iterable(self):
          iterable = range(4)
          self.assertEqual(iterable, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: range(0, 4) != []

``range(x)`` makes an iterable_ of numbers that go from a default of ``0`` to the given number minus ``1``, in this case it will be ``0`` to ``3``

green: make it pass
#################################################################################

I add the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertEqual(list(iterable), [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != []

I copy the values from the terminal and paste it as the expectation

.. code-block:: python

  self.assertEqual(
      list(iterable),
      [0, 1, 2, 3]
  )

the test passes. I can make a :ref:`list <lists>` from any iterable_ by using the :ref:`list <lists>` constructor_

----

*********************************************************************************
test_add_to_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for adding items to an existing `lists <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ with the append_ :ref:`method<functions>`

.. code-block:: python

    def test_add_to_a_list(self):
        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.append(4))

the terminal shows green. The append_ :ref:`method<functions>` returns None_ when it is called, but what does it do to the list?

.. code-block:: python

  self.assertIsNone(a_list.append(4))
  self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows :ref:`AssertionError` because the values in ``a_list`` change after ``a_list.append(4)`` is called

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

green: make it pass
#################################################################################

I change the values in the test to match the values in the terminal

.. code-block:: python

    def test_add_to_a_list(self):
        a_list = [0, 1, 2, 3]

        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.append(4)
        self.assertEqual(a_list, [0, 1, 2, 3, 4])

the test passes

I started with a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ that had 4 things, added something using the append_ :ref:`method<functions>`, then checked if the things stayed the same

----

*********************************************************************************
test_remove_from_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for removing an item from a list with the remove_ :ref:`method<functions>`

.. code-block:: python

    def test_remove_from_a_list(self):
        a_list = [0, 1, 2, 3]

        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 3] != [0, 1, 2, 3]

because ``2`` is no longer in ``a_list`` after ``a_list.remove(2)`` is called

green: make it pass
#################################################################################

I change the values to match the terminal

.. code-block:: python

    def test_remove_from_a_list(self):
        a_list = [0, 1, 2, 3]

        self.assertEqual(a_list, [0, 1, 2, 3])
        a_list.remove(2)
        self.assertEqual(a_list, [0, 1, 3])

the test passes

refactor: make it better
#################################################################################

I want to see which item Python removes when there is more than one of the same item in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ and I call ``list.remove(item)``

.. code-block:: python

  def test_remove_from_a_list_when_multiple_exist(self):
      a_list = [0, 2, 1, 2, 3, 2]

      self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
      a_list.remove(2)
      self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 2] != [0, 2, 1, 2, 3, 2]

I change the values on the right to match the values from the terminal

.. code-block:: python

  def test_remove_from_a_list_when_multiple_exist(self):
      a_list = [0, 2, 1, 2, 3, 2]

      self.assertEqual(a_list, [0, 2, 1, 2, 3, 2])
      a_list.remove(2)
      self.assertEqual(a_list, [0, 1, 2, 3, 2])

the remove_ :ref:`method<functions>` takes away the first item when the item exists more than once in a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

----

*********************************************************************************
test_remove_last_item_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_remove_last_item_in_a_list(self):
      a_list = [0, 1, 2, 3]

      self.assertEqual(a_list, [0, 1, 2, 3])
      last_item = a_list.pop()
      self.assertEqual(last_item, 0)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  >       self.assertEqual(last_item, 0)
  E       AssertionError: 3 != 0

``last_item = a_list.pop()`` calls the pop_ :ref:`method<functions>` of ``a_list`` and names the result ``last_item``

green: make it pass
#################################################################################

I change the value in the test to match the value that was popped

.. code-block:: python

  self.assertEqual(last_item, 3)

the test passes

refactor: make it better
#################################################################################

I add another failing line

.. code-block:: python

  def test_remove_last_item_in_a_list(self):
      a_list = [0, 1, 2, 3]

      self.assertEqual(a_list, [0, 1, 2, 3])
      last_item = a_list.pop()
      self.assertEqual(last_item, 3)
      self.assertEqual(a_list, [0, 1, 2, 3])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 3]

I change the expected values to match

.. code-block:: python

  def test_remove_last_item_in_a_list(self):
      a_list = [0, 1, 2, 3]

      self.assertEqual(a_list, [0, 1, 2, 3])
      last_item = a_list.pop()
      self.assertEqual(last_item, 3)
      self.assertEqual(a_list, [0, 1, 2])

all the tests are still green

----

*********************************************************************************
test_view_items_in_a_list
*********************************************************************************

I can provide the position of an item I want to see, as an index in ``[]``. Python uses zero-based indexing which means the positions of items starts at ``0``. I can also view items from the right side of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ by using negative numbers

red: make it fail
#################################################################################

I add a failing test for indexing a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

  def test_view_items_in_a_list(self):
      a_list = ['first', 'second', 'third', 'fourth']

      self.assertEqual(a_list[0], '')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'first' != ''

green: make it pass
#################################################################################

I change the value in the test

.. code-block:: python

  self.assertEqual(a_list[0], 'first')

the test passes

refactor: make it better
#################################################################################

* I add another line, this time with a negative number

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'first' != ''

  then I change the value to match

  .. code-block:: python

    self.assertEqual(a_list[-4], 'first')

  the test passes

* I add a failing line

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'third' != ''

  I change the test to match

  .. code-block:: python

    self.assertEqual(a_list[2], 'third')

  the terminal shows green again

* I add another line with a negative number

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], '')

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'third' != ''

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[-2], 'third')

  the test passes

* I add another line

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[1], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'second' != ''

  I make the test pass

  .. code-block:: python

    self.assertEqual(a_list[1], 'second')

* I add another one

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[1], 'second')
        self.assertEqual(a_list[-3], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'second' != ''

  I change the value

  .. code-block:: python

    self.assertEqual(a_list[-3], 'second')

  the test passes

* I add another line

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[1], 'second')
        self.assertEqual(a_list[-3], 'second')
        self.assertEqual(a_list[3], '')

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'fourth' != ''

  I make the test pass

  .. code-block:: python

    self.assertEqual(a_list[3], 'fourth')

* then add another line

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[1], 'second')
        self.assertEqual(a_list[-3], 'second')
        self.assertEqual(a_list[3], 'fourth')
        self.assertEqual(a_list[-1], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'fourth' != ''

  I make the test pass

  .. code-block:: python

    def test_view_items_in_a_list(self):
        a_list = ['first', 'second', 'third', 'fourth']

        self.assertEqual(a_list[0], 'first')
        self.assertEqual(a_list[-4], 'first')
        self.assertEqual(a_list[2], 'third')
        self.assertEqual(a_list[-2], 'third')
        self.assertEqual(a_list[1], 'second')
        self.assertEqual(a_list[-3], 'second')
        self.assertEqual(a_list[3], 'fourth')
        self.assertEqual(a_list[-1], 'fourth')

  all tests are still passing

----

*********************************************************************************
test_index_error
*********************************************************************************

IndexError_ is raised when I try to get an item from a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ but use a number that is greater than range of indexes for it

red: make it fail
#################################################################################

I add a failing test to show this

.. code-block:: python

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']
      a_list[5]

the terminal shows IndexError_

.. code-block:: python

  IndexError: list index out of range

green: make it pass
#################################################################################

* I add IndexError_ to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # IndexError

* then I use `unittest.TestCase.assertRaises`_ to make sure that IndexError_ gets raised

  .. code-block:: python

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]

  the test passes. `unittest.TestCase.assertRaises`_ takes an Exception_ as input and makes sure it is raised by the code in its context. You can read more about in :doc:`/how_to/exception_handling_tests`

refactor: make it better
#################################################################################

* I add one more line to test indexing with a negative number that is greater than the length of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ as a negative number

  .. code-block:: python

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]
        a_list[-5]

  the terminal shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add another assertRaises_

  .. code-block:: python

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']
        with self.assertRaises(IndexError):
            a_list[5]
        with self.assertRaises(IndexError):
            a_list[-5]

  the test passes

----

*********************************************************************************
test_list_attributes_and_methods
*********************************************************************************

The chapter on :ref:`classes` shows how to view the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of an :ref:`object<classes>` by using the dir_ :ref:`function<functions>`. Let us try it for `lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_list_attributes_and_methods(self):
      self.assertEqual(
          dir(list),
          []
      )

the terminal shows :ref:`AssertionError`

  .. code-block::python

    AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

green: make it pass
#################################################################################

* The terminal also shows a recommendation on how to see the differences between ``dir(list)`` and ``[]``

  .. code-block:: python

    Diff is 748 characters long. Set self.maxDiff to None to see it

* `unittest.TestCase.maxDiff`_ is an attribute of the `unittest.TestCase`_ :ref:`class <classes>` that sets the maximum number of characters to show when comparing 2 objects in the terminal. When it is set to :ref:`None` there is no limit to the number of characters

* I add ``self.maxDiff`` to the test

  .. code-block:: python

    def test_list_attributes_and_methods(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            []
        )

  and the terminal shows a long list of items

* I copy and paste the items from the terminal and remove the extra characters

  .. note::

    Your results may vary based on your version of Python

  .. code-block:: python

    def test_list_attributes_and_methods(self):
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

  and the terminal shows passing tests

refactor: make it better
#################################################################################

There are more :ref:`methods<functions>` listed than what have been tested, You can make a guess at what some of them do from their names

* :ref:`append<test_add_to_a_list>` - adds an item to the list
* clear - does this clear the items in the list?
* copy - does this make a copy of the list?
* count - does this count the number of items in the list?
* extend - does this extend the list?
* index
* insert - does this place an item in the list? what's the difference between this and append?
* :ref:`pop<test_remove_last_item_in_a_list>` - takes away the last item in the list
* :ref:`remove<test_remove_from_a_list>` - takes away the first occurrence of a given item in the list
* reverse - does this reverse the list?
* sort - does this sort the items in the list?

You can add tests for these :ref:`methods<functions>` to find out what they do or `read more about lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_

.. _lists_review:

*********************************************************************************
review
*********************************************************************************

* Lists are represented with ``[]``
* Lists can be made with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_
* Lists can hold any :ref:`object<classes>`
* Lists can be changed after creation by performing an operation, this means they are mutable

Would you like to :ref:`test list comprehensions?<lists: list comprehensions>`

----

:doc:`/code/code_lists`