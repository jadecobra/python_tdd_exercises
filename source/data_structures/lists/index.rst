.. meta::
  :description: Learn Python lists with this TDD tutorial! Master list methods, indexing, and slicing. Start coding now!
  :keywords: Python lists, Python list methods, Python TDD tutorial, Python list operations, learn Python programming, Python list slicing, Python indexing tutorial, Jacob Itegboje

.. include:: ../../links.rst

.. _clear: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _copy: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _pop: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _list: https://docs.python.org/3/library/stdtypes.html#list

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done

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

A list_ is an :ref:`object<classes>` that can hold any objects_

* they are represented with ``[]``
* they can be made with the list_ constructor_
* they can be changed by performing an operation - they are mutable

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
          self.assertEqual(list(), None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] != None

green: make it pass
#################################################################################

I change the expectation

.. code-block:: python

  self.assertEqual(list(), [])

the test passes. This is how to make an empty list_

refactor: make it better
#################################################################################

I add another assertion, this time with input to the list_ constructor_

.. code-block:: python
  :emphasize-lines: 2

  self.assertEqual(list(), [])
  self.assertEqual(list(0), [])

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: 'int' object is not iterable

I add the error to the list of Exceptions_ encountered

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # TypeError

I change the input to a :py:class:`tuple`

.. code-block:: python
  :emphasize-lines: 2

  self.assertEqual(list(), [])
  self.assertEqual(list((0, 1, 2, 'n')), [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 'n'] != []

I change the expectation to match

.. code-block:: python

  self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

the test passes. The tests show I can make a list_ with the constructor_ and square brackets(``[]``), which uses less characters

----

*********************************************************************************
test_attributes_and_methods_of_lists
*********************************************************************************

I can use the :py:func:`dir` :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of lists_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_make_a_list(self):
      ...

  def test_attributes_and_methods_of_lists(self):
    self.assertEqual(
        dir(list),
        [

        ]
    )

the terminal shows :ref:`AssertionError`

.. code-block::python

  AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

there is also a note on how to see the full difference between ``dir(list)`` and my empty list

.. code-block:: python

  Diff is 748 characters long. Set self.maxDiff to None to see it

`unittest.TestCase.maxDiff`_ is an attribute of the `unittest.TestCase`_ :ref:`class <classes>` that sets the maximum number of characters to show when comparing 2 objects in the terminal, when it is set to :ref:`None` it shows the entire difference

green: make it pass
#################################################################################

* I move the terminal to the right then add ``self.maxDiff`` to the test

  .. code-block:: python
    :emphasize-lines: 2

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            [

            ]
        )

  the terminal shows a long list of items. I copy and paste them from the terminal and use find and replace to remove the extra characters

  .. note::

    your results can be different because of your Python version

  .. code-block:: python

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            [
                '__add__',
                ...
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

  the terminal shows passing tests and I move it back to the bottom. I ignore the names with double underscores (__) for now, then copy and paste the other names to make a TODO list

  .. code-block:: python

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

    # Exceptions Encountered
    # AssertionError
    # TypeError

----

*********************************************************************************
test_append_adds_to_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the append_ :ref:`method<functions>`

.. code-block:: python

    def test_attributes_and_methods_of_lists(self):
        ...

    def test_append(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.append())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list.append() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I add ``0`` as input

.. code-block:: python

  self.assertIsNone(a_list.append(0))

the terminal shows green, the append_ :ref:`method<functions>` returns :ref:`None` when called

refactor: make it better
#################################################################################

* I add another assertion to see what append_ did to the list_

  .. code-block:: python
    :emphasize-lines: 2

    self.assertIsNone(a_list.append(0))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 0] != [0, 1, 2, 'n']

  the :ref:`method<functions>` added a value. I change the values in the test to match the values in the terminal

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 0])

  the test passes

* I change the value given to append_ for fun

  .. code-block:: python

    self.assertIsNone(a_list.append('n+1'))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 'n+1'] != [0, 1, 2, 'n', 0]

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

  the test passes

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_append_adds_to_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.append('n+1'))
        self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

* I remove append_ from the TODO list

  .. code-block:: python

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

----

*********************************************************************************
test_clear_empties_a_list
*********************************************************************************

I add a test for the clear_ :ref:`method<functions>`

.. code-block:: python

  def test_append_adds_to_a_list(self):
      ...

  def test_clear(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.clear())

the terminal shows green. The clear_ :ref:`method<functions>` returns :ref:`None` when it is called

red: make it fail
#################################################################################

I add an assertion to show what it did to the list_

.. code-block:: python

  self.assertIsNone(a_list.clear())
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [] != [0, 1, 2, 'n']

it is now empty

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_list, [])

the test passes

refactor: make it better
#################################################################################

* I change the name of the test to be more descriptive

  .. code-block:: python
    :emphasize-lines: 1

    def test_clear_empties_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.clear())
        self.assertEqual(a_list, [])

* I remove clear_ from the TODO list

  .. code-block:: python

    'copy',
    'count',
    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_copy_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add another test, I think we can guess what this one does

.. code-block:: python

  def test_clear_empties_a_list(self):
      ...

  def test_copy(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.copy())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [0, 1, 2, 'n'] is not None

the :ref:`method<functions>` returns a copy of the list_

green: make it pass
#################################################################################

I add the value to the assertion

.. code-block:: python
  :emphasize-lines: 2

  a_list = [0, 1, 2, 'n']
  self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [0, 1, 2, 'n'] is not None : [0, 1, 2, 'n']

the :ref:`method<functions>` returns a copy of the list_. I change assertIsNone_ to assertEqual_

.. code-block:: python
  :emphasize-lines: 2

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

the test passes

refactor: make it better
#################################################################################

* I add another assertion to see what happened to the original list_

  .. code-block:: python

    self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])
    self.assertEqual(a_list, [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n'] != []

  it stayed the same. I add the values

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_copy_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])
        self.assertEqual(a_list, [0, 1, 2, 'n'])

* I remove copy_ from the TODO list

  .. code-block:: python

    'count',
    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_count_number_of_times_item_is_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

  def test_count(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.count())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list.count() takes exactly one argument (0 given)

I pass a value to the call

.. code-block:: python
  :emphasize-lines: 3

  def test_count(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.count(0))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 1 is not None

green: make it pass
#################################################################################

I add the value

.. code-block:: python

  self.assertIsNone(a_list.count(0), 1)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 1 is not None : 1

I change assertIsNone_ to assertEqual_

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.count(0), 1)

the test passes

refactor: make it better
#################################################################################

* It looks like the count_ :ref:`method<functions>` returns the number of times an item is in a list_. I change it then add another assertion to be sure

  .. code-block:: python
    :emphasize-lines: 2, 4

    def test_count(self):
        a_list = [0, 1, 2, 1, 'n', 1]
        self.assertEqual(a_list.count(0), 1)
        self.assertEqual(a_list.count(1), 1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 3 != 1

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list.count(1), 3)

  the test passes

* I add another assertion to see what happens when I try to count an item that is not in the list_

  .. code-block:: python
    :emphasize-lines: 2

    self.assertEqual(a_list.count(2), 3)
    self.assertEqual(a_list.count('not in list'), 3)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 != 3

  The count_ method returns ``0`` when the item is not in the list_. I change the value to match

  .. code-block:: python

    self.assertEqual(a_list.count('not in list'), 0)

  the test passes

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_count_number_of_times_item_is_in_a_list(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertEqual(a_list.count(0), 1)
        self.assertEqual(a_list.count(2), 3)
        self.assertEqual(a_list.count(9), 0)

* I remove count_ from the TODO list

  .. code-block:: python

    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_extend_adds_items_from_an_iterable_to_a_list
*********************************************************************************

red: make it fail
#################################################################################

time for another test

.. code-block:: python

  def test_count_number_of_times_item_is_in_a_list(self):
      ...

  def test_extend(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.extend())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list.extend() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I pass a value to the call

.. code-block:: python

  self.assertIsNone(a_list.extend(0))

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: 'int' object is not iterable

I change the value to an iterable_

.. code-block:: python

  self.assertIsNone(a_list.extend((0, 1)))

the test passes. The extend_ :ref:`method<functions>` returns :ref:`None` when called

refactor: make it better
#################################################################################

* I add another assertion to see what it did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.extend((0, 1)))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 0, 1] != [0, 1, 2, 'n']

  I change the values in the test to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the test passes

* I change the values given to the extend_ :ref:`method<functions>` for fun

  .. code-block:: python
    :emphasize-lines: 3

    def test_extend(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.extend((2, 1, 0)))
        self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 2, 1, 0] != [0, 1, 2, 'n', 0, 1]

  I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

  the test is green again

* I change the name of the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_extend_adds_items_from_an_iterable_to_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.extend((2, 1, 0)))
        self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

* I remove extend_ from the TODO list

  .. code-block:: python

    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_index_returns_first_position_of_item_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the index_ :ref:`method<functions>`

.. code-block:: python

  def test_extend_adds_items_from_an_iterable_to_a_list(self):
      ...

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.index())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: index expected at least 1 argument, got 0

green: make it pass
#################################################################################

I add a value to the call

.. code-block:: python
  :emphasize-lines: 3

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.index(0))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0 is not None

I add the expectation

.. code-block:: python

  AssertionError: 0 is not None : 0

I change assertIsNone_ to assertEqual_

.. code-block:: python

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertEqual(a_list.index(0), 0)

the test passes

refactor: make it better
#################################################################################

* it does not tell me if the :ref:`method<functions>` is returning the same value I give it, so I change the list_

  .. code-block:: python
    :emphasize-lines: 2

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index(0), 0)

  the terminal shows :py:exc:`ValueError`

  .. code-block:: python

    ValueError: 0 is not in list

  the index_ :ref:`method<functions>` raises :py:exc:`ValueError` when the item is not in the list_

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # ValueError

* I remove the things around the call and change the value to be more descriptive

  .. code-block:: python

    a_list.index('not in list')

  the terminal shows :py:exc:`ValueError`

  .. code-block:: python

    ValueError: 'not in list' is not in list

* I add assertRaises_ to handle the :py:exc:`Exception`

  .. code-block:: python

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the test is green again

* I add a new assertion for the index_ :ref:`method<functions>`

  .. code-block:: python

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index('1st'), '1st')

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 != '1st'

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list.index('1st'), 0)

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list.index('1st'), 0)
    self.assertEqual(a_list.index('3rd'), 0)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 2 != 0

  I change the value in the test

  .. code-block:: python

    self.assertEqual(a_list.index('3rd'), 2)

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list.index('3rd'), 2)
    self.assertEqual(a_list.index('2nd'), 2)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 1 != 2

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list.index('2nd'), 1)

  the test is green again

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list.index('2nd'), 1)
    self.assertEqual(a_list.index('...last'), 1)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 3 != 1

  I change the value to match the terminal

  .. code-block:: python

    self.assertEqual(a_list.index('...last'), 3)

  the test passes. The index_ :ref:`method<functions>` returns numbers for the position of the item in the the list_. Python uses `zero-based indexing`_ which means the first item has an index of ``0`` and the last item has an index of the length of the list_ minus ``1``

* I rename the test

  .. code-block:: python

    def test_index_returns_first_position_of_item_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index('1st'), 0)
        self.assertEqual(a_list.index('3rd'), 2)
        self.assertEqual(a_list.index('2nd'), 1)
        self.assertEqual(a_list.index('...last'), 3)

        with self.assertRaises(ValueError):
            a_list.index('not in list')

* I also remove index_ from the TODO list

  .. code-block:: python

    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_insert_item_at_given_index_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

    def test_index_returns_first_position_of_item_in_a_list(self):
        ...

    def test_insert(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.insert())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: insert expected 2 arguments, got 0

green: make it pass
#################################################################################

I pass two values to the :ref:`method<functions>`

.. code-block:: python

  def test_insert(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.insert(0, 1))

the test is green. The insert_ :ref:`method<functions>` returns :ref:`None`

refactor: make it better
#################################################################################

* I add an assertion to find out what it did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.insert(0, 1))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 0, 1, 2, 'n'] != [0, 1, 2, 'n']

  I add the new value to the list_

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 1, 2, 'n'])

  the test passes. It looks like the insert_ :ref:`method<functions>` places the second input given at the index given as the first input

* I change the second input in the call to be sure

  .. code-block:: python

    self.assertIsNone(a_list.insert(0, -1))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [-1, 0, 1, 2, 'n'] != [1, 0, 1, 2, 'n']

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the test is green again

* I add another assertion with a call to the insert_ :ref:`method<functions>`

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
    self.assertIsNone(a_list.insert(3, 1.5))

  the terminal shows green. I add an assertion to see what it did to the list

  .. code-block:: python

    self.assertIsNone(a_list.insert(3, 1.5))
    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [-1, 0, 1, 1.5, 2, 'n'] != [-1, 0, 1, 2, 'n']

  I add the value to the expectation

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

  the test passes

* I rename the test

  .. code-block:: python

    def test_insert_item_at_given_index_in_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.insert(0, -1))
        self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
        self.assertIsNone(a_list.insert(3, 1.5))
        self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

* I remove insert_ from the TODO list

  .. code-block:: python

    'pop',
    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_pop_removes_and_returns_last_item_from_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_insert_item_at_given_index_in_a_list(self):
      ...

  def test_pop(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.pop())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'n' is not None

it looks like the pop_ :ref:`method<functions>` returns the last item in the list_

green: make it pass
#################################################################################

I add the expectation

.. code-block:: python

  self.assertIsNone(a_list.pop(), 'n')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'n' is not None : n

I change assertIsNone_ to assertEqual_

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.pop(), 'n')

the test passes

refactor: make it better
#################################################################################

* I add an assertion to see what the :ref:`method<functions>` did to the list_

  .. code-block:: python

    self.assertEqual(a_list.pop(), 'n')
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 'n']

  I change the values in the test to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])
    self.assertEqual(a_list.pop(), 'n')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 2 != 'n'

  I change the value in the test

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])
    self.assertEqual(a_list.pop(), 2)

  the test passes. The pop_ :ref:`method<functions>` removes and returns the last item in the list_

* I rename the test

  .. code-block:: python

    def test_pop_removes_and_returns_last_item_from_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.pop(), 'n')
        self.assertEqual(a_list, [0, 1, 2])
        self.assertEqual(a_list.pop(), 2)

* I remove pop_ from the TODO list

  .. code-block:: python

    'remove',
    'reverse',
    'sort'

----

*********************************************************************************
test_remove_first_instance_of_item_from_a_list
*********************************************************************************

red: make it fail
#################################################################################

time for the next :ref:`method<functions>`

.. code-block:: python

  def test_remove(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.remove())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list.remove() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I add a value to the call

.. code-block:: python

  self.assertIsNone(a_list.remove(0))

the terminal shows green, the remove_ :ref:`method<functions>` returns :ref:`None`

refactor: make it better
#################################################################################

* I add an assertion to see what remove_ did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.remove(0))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 2, 'n'] != [0, 1, 2, 'n']

  the :ref:`method<functions>` removes the item given from the list_. I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, [1, 2, 'n'])

  the test passes

* I change the values in ``a_list`` to see what would happen if an item shows up more than once in the list_

  .. code-block:: python

    def test_remove(self):
        a_list = [0, 1, 0, 2, 0, 'n']
        self.assertIsNone(a_list.remove(0))
        self.assertEqual(a_list, [1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 0, 2, 0, 'n'] != [1, 2, 'n']

  the :ref:`method<functions>` removes the first instance of the given item from the list_. I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

  the test passes

* I want to know what happens when the item is not in the list_

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])
    self.assertIsNone(a_list.remove('not in list'))

  the terminal shows :py:exc:`ValueError`

  .. code-block:: python

    ValueError: list.remove(x): x not in list

  I remove the things around the call then add assertRaises_

  .. code-block:: python

    with self.assertRaises(ValueError):
        a_list.remove('not in list')

  the test passes

* I rename the test

  .. code-block:: python

    def test_remove_first_instance_of_item_from_a_list(self):
        a_list = [0, 1, 0, 2, 0, 'n']
        self.assertIsNone(a_list.remove(0))
        self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

        with self.assertRaises(ValueError):
            a_list.remove('not in list')

* I take out remove_ from the TODO list

  .. code-block:: python

    'reverse',
    'sort'

----

*********************************************************************************
test_reverse_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add the next test

.. code-block:: python

  def test_reverse(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.reverse())

the terminal shows green. This :ref:`method<functions>` returns :ref:`None`. I add an assertion to see what it did to the list_

.. code-block:: python

  self.assertIsNone(a_list.reverse())
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['n', 2, 1, 0] != [0, 1, 2, 'n']

the :ref:`method<functions>` reverses the order of the list_

green: make it pass
#################################################################################

I change the expectation

.. code-block:: python

  self.assertEqual(a_list, ['n', 2, 1, 0])

the test passes

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_reverse_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.reverse())
        self.assertEqual(a_list, ['n', 2, 1, 0])

* I remove the name from the TODO list

  .. code-block:: python

    'sort'

----

*********************************************************************************
test_sort_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_sort(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.sort())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: '<' not supported between instances of 'str' and 'int'

I have to change ``'n'`` to a number or change the other numbers to a string_

green: make it pass
#################################################################################

I remove the things around the call then add assertRaises_

.. code-block:: python

  def test_sort(self):
      with self.assertRaises(TypeError):
          [0, 1, 2, 'n'].sort()

the test passes

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    def test_sort(self):
        with self.assertRaises(TypeError):
            [0, 1, 2, 'n'].sort()

        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.sort())


  the terminal still shows green, sort_ returns :ref:`None` when called. I add another assertion to see what it did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.sort())
    self.assertEqual(a_list, [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  the list_ is still the same. I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes. The name of the :ref:`method<functions>` is sort_ and the list_ is already sorted. I change it to see what would happen when it is not sorted

  .. code-block:: python

    a_list = [0, 1, -1, 2, -2, 3, -3]

  I get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [-3, -2, -1, 0, 1, 2, 3] != [0, 1, 2, 3]

  the sort_ :ref:`method<functions>` arranges the list_ in ascending order. I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

  the test passes

* I change the name of the test

  .. code-block:: python

    def test_sort_a_list(self):
        with self.assertRaises(TypeError):
            [0, 1, 2, 'n'].sort()

        a_list = [0, 1, -1, 2, -2, 3, -3]
        self.assertIsNone(a_list.sort())
        self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

* I remove sort_ from the TODO list

----

*********************************************************************************
test_get_items_from_a_list
*********************************************************************************

I can provide the index of an item I want to see in square brackets(``[]``) to a list_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_get_items_from_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      self.assertEqual(a_list[0], '')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '1st' != ''

the first item has an index of ``0`` as shown in :ref:`test_index_returns_first_position_of_item_in_a_list`

green: make it pass
#################################################################################

I change the value in the test

.. code-block:: python

  self.assertEqual(a_list[0], '1st')

the test passes

refactor: make it better
#################################################################################

* I can also use negative numbers. The last item has an index of ``-1`` and the first item has an index of negative the length of the list_

  .. code-block:: python

    def test_get_items_from_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list[0], '1st')
        self.assertEqual(a_list[-4], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '1st' != ''

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list[-4], '1st')

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[-4], '1st')
    self.assertEqual(a_list[2], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '3rd' != ''

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list[2], '3rd')

  the terminal shows green again

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[2], '3rd')
    self.assertEqual(a_list[-2], '')

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '3rd' != ''

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[-2], '3rd')

  the test passes

* I add another line

  .. code-block:: python

    self.assertEqual(a_list[-2], '3rd')
    self.assertEqual(a_list[1], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '2nd' != ''

  I make the test pass

  .. code-block:: python

    self.assertEqual(a_list[1], '2nd')

* I add another one

  .. code-block:: python

    self.assertEqual(a_list[1], '2nd')
    self.assertEqual(a_list[-3], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '2nd' != ''

  I change the value

  .. code-block:: python

    self.assertEqual(a_list[-3], '2nd')

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[-3], '2nd')
    self.assertEqual(a_list[3], '')

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '...last' != ''

  I change the value

  .. code-block:: python

    self.assertEqual(a_list[3], '...last')

  the test passes

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[3], '...last')
    self.assertEqual(a_list[-1], '')

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: '...last' != ''

  I make the values match

  .. code-block:: python

    self.assertEqual(a_list[-1], '...last')

  the test passes. This is also called indexing

----

*********************************************************************************
test_set_items_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_set_items_in_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      a_list[-1] = '4th'
      self.assertEqual(a_list, ['1st', '2nd', '3rd', '...last'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['1st', '2nd', '3rd', '4th'] != ['1st', '2nd', '3rd', '...last']

I can use the index of an item to change its value in a list_

green: make it pass
#################################################################################

I change the expectation to match the terminal

.. code-block:: python

  self.assertEqual(a_list, ['1st', '2nd', '3rd', '4th'])

the test passes

----

*********************************************************************************
test_view_parts_of_a_list_aka_slicing
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_set_items_in_a_list(self):
      ...

  def test_view_parts_of_a_list(self):
      a_list = ['a', 'b', 'c', 'd']
      self.assertEqual(a_list[0:2], [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['a', 'b'] != []

viewing parts of a list_ is like indexing, it takes two values in square brackets(``[]``), separated by a ``:``, the first value is the starting index you want and the second value is the ending index plus ``1``

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_list[0:2], ['a', 'b'])

the test passes

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[0:2], ['a', 'b'])
    self.assertEqual(a_list[1:4], [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

  I add the missing values

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['b', 'c', 'd'])

  the test passes

* I add another line

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
    self.assertEqual(a_list[0:3], [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['a', 'b', 'c'] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['a', 'b', 'c'])

  the test is green again

* One more assert_ method for good measure

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
    self.assertEqual(a_list[1:3], [])

  I get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['b', 'c'] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[1:3], ['b', 'c'])

  the test is green again

* This is also called slicing, I change the name of the test

  .. code-block:: python

    def test_view_parts_of_a_list_aka_slicing(self):
        a_list = ['a', 'b', 'c', 'd']
        self.assertEqual(a_list[0:2], ['a', 'b'])
        self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
        self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
        self.assertEqual(a_list[1:3], ['b', 'c'])

----

*********************************************************************************
test_index_error
*********************************************************************************

:py:exc:`ValueError` was raised earlier in :ref:`test_remove_first_instance_of_item_from_a_list` and :ref:`test_index_returns_first_position_of_item_in_a_list`, there is another :py:exc:`Exception`that is important to know, the :ref:`IndexError<test_index_error>` is raised when I try to get an item from a list_ but use a number that is NOT in the range of indexes for it

red: make it fail
#################################################################################

I add a failing test to show this

.. code-block:: python

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']
      a_list[4]

the terminal shows :ref:`IndexError<test_index_error>`

.. code-block:: python

  IndexError: list index out of range

green: make it pass
#################################################################################

* I add :ref:`IndexError<test_index_error>` to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # ValueError
    # IndexError

* I add assertRaises_ to handle the error

  .. code-block:: python

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(IndexError):
            a_list[4]

  the test passes

refactor: make it better
#################################################################################

* I add another assertion to test indexing with a negative number that is outside the range of numbers that can be used to index the list_

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[4]
    a_list[-5]

  the terminal shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

  I add another assertRaises_

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[4]
    with self.assertRaises(IndexError):
        a_list[-5]

  the test passes

* :ref:`IndexError<test_index_error>` is also raised with the pop_ :ref:`method<functions>` when the the list_ is empty

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[-5]
    [].pop()

  the terminal shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: pop from empty list

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[-5]
    with self.assertRaises(IndexError):
        [].pop()

  the terminal shows green

----

*********************************************************************************
review
*********************************************************************************

I ran tests for `lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_

* they are represented with ``[]``
* they can be made with the list_ constructor_
* they can hold any :ref:`object<classes>`
* they can be changed by performing an operation

Would you like to :ref:`test list comprehensions?<lists: list comprehensions>`

----

:doc:`/code/code_lists`