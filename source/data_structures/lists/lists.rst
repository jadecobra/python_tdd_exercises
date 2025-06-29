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
* they can be changed by performing an operation, this means they are mutable

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
test_make_a_list_w_list_constructor
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list``

.. code-block:: python

  import unittest


  class TestLists(unittest.TestCase):

      def test_make_a_list_w_list_constructor(self):
          self.assertEqual(list(), None)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [] != None

green: make it pass
#################################################################################

I change the expectation

.. code-block:: python

  self.assertEqual(list(), [])

the test passes. This is how to make an empty `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

refactor: make it better
#################################################################################

I add another assertion, this time with input in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_

.. code-block:: python

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

I change the input to a tuple_

.. code-block:: python

  self.assertEqual(list(), [])
  self.assertEqual(list((0, 1, 2, 'n')), [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 'n'] != []

I change the expectation to match

.. code-block:: python

  self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

the test passes. The tests show I can make a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_ and square brackets - ``[]``, which uses less characters than the constructor_

----

*********************************************************************************
test_attributes_and_methods_of_lists
*********************************************************************************

I can use the dir_ :ref:`function<functions>` to see at the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

    def test_make_a_list(self):
        ...

    def test_attributes_and_methods_of_lists(self):
      self.assertEqual(
          dir(list),
          []
      )

the terminal shows :ref:`AssertionError`

  .. code-block::python

    AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

there is also a note on how to see the full difference between ``dir(list)`` and ``[]``

  .. code-block:: python

    Diff is 748 characters long. Set self.maxDiff to None to see it

`unittest.TestCase.maxDiff`_ is an attribute of the `unittest.TestCase`_ :ref:`class <classes>` that sets the maximum number of characters to show when comparing 2 objects in the terminal, when it is set to :ref:`None` it shows all the differences

green: make it pass
#################################################################################

* I add ``self.maxDiff`` to the test

  .. code-block:: python

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            []
        )

  the terminal shows a long list of items. I copy and paste them from the terminal and remove the extra characters with find and replace

  .. note::

    your results can be different because of your Python version

  .. code-block:: python

    def test_attributes_and_methods_of_lists(self):
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

  the terminal shows passing tests. I ignore the names with double underscores (__) for now, then copy and paste the other names to make a TODO list for the next tests

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

I add input

.. code-block:: python

  self.assertIsNone(a_list.append(0))

the terminal shows green, the append_ :ref:`method<functions>` returns :ref:`None` when it is called

refactor: make it better
#################################################################################

I add another assertion to see what append_ did to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

  self.assertIsNone(a_list.append(0))
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 'n', 0] != [0, 1, 2, 'n']

the :ref:`method<functions>` added a value. I change the values in the test to match the values in the terminal

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 'n', 0])

the test passes. I change the value given to append_ for fun

.. code-block:: python

  self.assertIsNone(a_list.append('n+1'))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 'n', 'n+1'] != [0, 1, 2, 'n', 0]

I change the expectation to match

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

the test passes and I rename the test

.. code-block:: python

  def test_append_adds_to_a_list(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.append('n+1'))
      self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

I remove append_ from the TODO list

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

I add a test for the `clear <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>`

.. code-block:: python

  def test_append_adds_to_a_list(self):
      ...

  def test_clear(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.clear())

the terminal shows green. The `clear <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>` returns :ref:`None` when it is called

red: make it fail
#################################################################################

We can guess what this :ref:`method<functions>` does to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. I add an assertion to show it

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

the test passes. I change the name of the test to be more descriptive

.. code-block:: python

  def test_clear_empties_a_list(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.clear())
      self.assertEqual(a_list, [])

I remove `clear <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ from the TODO list

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

I add another test

.. code-block:: python

  def test_clear_empties_a_list(self):
      ...

  def test_copy(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.copy())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [0, 1, 2, 'n'] is not None

the `copy <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>` returns a copy of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

green: make it pass
#################################################################################

I add the value to the assertion

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: [0, 1, 2, 'n'] is not None : [0, 1, 2, 'n']

the :ref:`method<functions>` returns a copy of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. I change the assert_ :ref:`method<functions>`

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

the test passes

refactor: make it better
#################################################################################

I add another assertion to see what happened to the original `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

  self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])
  self.assertEqual(a_list, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 'n'] != []

it stayed the same. I add the values

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 'n'])

the test passes and I change the name of the test

.. code-block:: python

  def test_copy_a_list(self):
      a_list = [0, 1, 2, 'n']
      self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])
      self.assertEqual(a_list, [0, 1, 2, 'n'])

I remove `copy <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ from the TODO list

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

red: make it fail
#################################################################################

I pass a value to the call

.. code-block:: python

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

I change the assert_ :ref:`method<functions>`

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.count(0), 1)

the test passes

refactor: make it better
#################################################################################

* It looks like the count_ :ref:`method<functions>` returns the number of times an item appears, I change the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ then add another assert_ call to be sure

  .. code-block:: python

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

* I add another assertion to see what happens when I try to count an item that is not in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

    self.assertEqual(a_list.count(2), 3)
    self.assertEqual(a_list.count('not in list'), 3)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 != 3

  The count_ method returns ``0`` when the item is not in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. I change the value

  .. code-block:: python

    self.assertEqual(a_list.count('not in list'), 0)

  the test passes

* I rename the test

  .. code-block:: python

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
test_extend_makes_a_list_longer
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

* I add another assertion to see what changed in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

      self.assertIsNone(a_list.extend((0, 1)))
      self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 0, 1] != [0, 1, 2, 'n']

  I change the values in the test to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the test passes. I change the values given to the extend_ :ref:`method<functions>` for fun

  .. code-block:: python

    def test_extend(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.extend((2, 1, 0)))
        self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 'n', 2, 1, 0] != [0, 1, 2, 'n', 0, 1]

  I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7])

  the test is green again

* I change the name of the test

  .. code-block:: python

    def test_extend_makes_a_list_longer(self):
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
test_index_returns_position_of_item_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the index_ :ref:`method<functions>`

.. code-block:: python

  def test_extend_makes_a_list_longer(self):
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

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.index(0))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 0 is not None

I add the expectation

.. code-block:: python

  AssertionError: 0 is not None : 0

I change the assertion

.. code-block:: python

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertEqual(a_list.index(0), 0)

the test passes

refactor: make it better
#################################################################################

* I cannot tell from the test if the :ref:`method<functions>` is returning the same value I give it, I change the values in ``a_list`` to check

  .. code-block:: python

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index(0), 0)

  the terminal shows ValueError_

  .. code-block:: python

    ValueError: 0 is not in list

  I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # ValueError

  I remove the things around the call and change the value to be more descriptive

  .. code-block:: python

    a_list.index('not in list')

  the terminal still shows ValueError_

  .. code-block:: python

    ValueError: 'not in list' is not in list

  I add assertRaises_ to handle the Exception_

  .. code-block:: python

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the test is green again. The index_ :ref:`method<functions>` raises ValueError_ when the item is not in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

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

  I change the value in the test to match the one in the terminal

  .. code-block:: python

    self.assertEqual(a_list.index('...last'), 3)

  the test passes. The index_ :ref:`method<functions>` returns numbers for the position of the item in the the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. Python uses `zero-based indexing`_ which means the first item has an index of ``0`` and the last item has an index of the length of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ minus ``1``

* I rename the test

  .. code-block:: python

    def test_index_returns_position_of_item_in_a_list(self):
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
test_insert_places_item_at_given_index_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next :ref:`method<functions>`

.. code-block:: python

    def test_index_returns_position_of_item_in_a_list(self):
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

* I add an assertion to find out what it did to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

    self.assertIsNone(a_list.insert(0, 1))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 0, 1, 2, 'n'] != [0, 1, 2, 'n']

  I add the new value to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 1, 2, 'n'])

  the test passes. The insert_ :ref:`method<functions>` places the second input given at the index given as the first input

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

    def test_insert_places_item_at_given_index_in_a_list(self):
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
test_pop_removes_and_returns_last_item_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_insert_places_item_at_given_index_in_a_list(self):
      ...

  def test_pop(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.pop())

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'n' is not None

it looks like the `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>` returns the last item in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

green: make it pass
#################################################################################

I add the expectation

.. code-block:: python

  self.assertIsNone(a_list.pop(), 'n')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'n' is not None : n

I change the assertion

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.pop(), 'n')

the test passes

refactor: make it better
#################################################################################

* I add an assertion to see what the :ref:`method<functions>` did to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

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

  the test passes. The `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ :ref:`method<functions>` removes and returns the last item in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_.

* I rename the test

  .. code-block:: python

    def test_pop_removes_and_returns_the_last_item_in_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.pop(), 'n')
        self.assertEqual(a_list, [0, 1, 2])
        self.assertEqual(a_list.pop(), 2)

* I remove `pop <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists>`_ from the TODO list

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

* I add an assertion to see what remove_ did to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

    self.assertIsNone(a_list.remove(0))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 2, 'n'] != [0, 1, 2, 'n']

  the :ref:`method<functions>` removes the item given from the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, [1, 2, 'n'])

  the test passes

* I change the values in ``a_list`` to see what would happen if an item shows up more than once in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

    def test_remove(self):
        a_list = [0, 1, 0, 2, 0, 'n']
        self.assertIsNone(a_list.remove(0))
        self.assertEqual(a_list, [1, 2, 'n'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 0, 2, 0, 'n'] != [1, 2, 'n']

  the :ref:`method<functions>` removes the first instance of the given item from the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_. I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

  the test passes

* I want to know what happens if the item is not in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

  .. code-block:: python

        self.assertEqual(a_list, [1, 0, 2, 0, 'n'])
        self.assertIsNone(a_list.remove('not in list'))

  the terminal shows ValueError_

  .. code-block:: python

    ValueError: list.remove(x): x not in list

  I remove the things around the call then add assertRaises_

  .. code-block:: python

    with self.assertRaises(ValueError):
        a_list.remove('not in list')

  the test passes

* I rename the test

  .. code-block:: python

    def test_remove_first_instance_of_item_in_a_list(self):
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

the terminal shows green. This :ref:`method<functions>` returns :ref:`None`. I add an assertion to see what has changed in the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

  self.assertIsNone(a_list.reverse())
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal show :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [3, 2, 1, 0] != [0, 1, 2, 'n']

the :ref:`method<functions>` reverses the order of the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

green: make it pass
#################################################################################

I change the expectation

.. code-block:: python

  self.assertEqual(a_list, [3, 2, 1, 0])

the test passes

refactor: make it better
#################################################################################

* I rename the test

  .. code-block:: python

    def test_reverse_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.reverse())
        self.assertEqual(a_list, [3, 2, 1, 0])

* I remove the :ref:`method<functions>` from the TODO list

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

the terminal still shows green. sort_ returns :ref:`None` when called, what does it do to the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_?

.. code-block:: python

  def test_sort(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.sort())
      self.assertEqual(a_list, [0, 1, 2, 'n'])

the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is still the same. I change the values in ``a_list`` to see if it makes a difference

.. code-block:: python

    def test_sort(self):
        a_list = [0, 2, 1, 2, 3, 2]

I get :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 2, 2, 3] != [0, 1, 2, 'n']

the sort_ :ref:`method<functions>` arranges the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ in ascending order by default

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 2, 2, 3])

the test passes

refactor: make it better
#################################################################################

* I change the name of the test

  .. code-block:: python

    def test_sort_a_list(self):
        a_list = [0, 2, 1, 2, 3, 2]
        self.assertIsNone(a_list.sort())
        self.assertEqual(a_list, [0, 1, 2, 2, 2, 3])

  still green

* I remove sort_ from the TODO list

----

*********************************************************************************
test_view_items_in_a_list
*********************************************************************************

I can provide the index of an item I want to see in ``[]`` to a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_view_items_in_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      self.assertEqual(a_list[0], '')

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: '1st' != ''

Python starts indexing at ``0`` as shown in :ref:`test_index_returns_position_of_item_in_a_list`

green: make it pass
#################################################################################

I change the value in the test

.. code-block:: python

  self.assertEqual(a_list[0], '1st')

the test passes

refactor: make it better
#################################################################################

* I add another line, this time with a negative number

  .. code-block:: python

    def test_view_items_in_a_list(self):
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

* I add another assert_ statement

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

* I add another line with a negative number

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

  all tests are still passing

----

*********************************************************************************
test_view_parts_of_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_view_items_in_a_list(self):
      ...

  def test_view_parts_of_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      self.assertEqual(a_list[0:2], [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: ['1st', '2nd'] != []

viewing parts of a `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ is like indexing, it takes two values in square brackets ``[]``, seperated by a ``:``, the first value is the starting index you want and the second value is the ending index plus ``1``

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_list[0:2], ['1st', '2nd'])

the test passes

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    self.assertEqual(a_list[0:2], ['1st', '2nd'])
    self.assertEqual(a_list[0:3], ['1st', '2nd'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['1st', '2nd', '3rd'] != ['1st', '2nd']

  I add the missing value

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['1st', '2nd', '3rd'])

  the test passes

* I add another line

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['1st', '2nd', '3rd'])
    self.assertEqual(a_list[1:4], ['2nd', '3rd'])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['2nd', '3rd', '...last'] != ['2nd', '3rd']

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['2nd', '3rd', '...last'])

  the test is green again

* One more assert_ statement for good measure

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['2nd', '3rd', '...last'])
        self.assertEqual(a_list[1:3], ['2nd', '3rd', '...last'])

  I get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: ['2nd', '3rd'] != ['2nd', '3rd', '...last']

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[1:3], ['2nd', '3rd'])

  the test is green again

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
      a_list[4]

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
    # ValueError
    # IndexError

* I add assertRaises_ to handle the error

  .. code-block:: python

    def test_index_error(self):
        a_list = ['a', 'b', 'c', 'd']

        with self.assertRaises(IndexError):
            a_list[5]

  the test passes

refactor: make it better
#################################################################################

I add one more line to test indexing with a negative number that is outside the range of numbers that can be used to index the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_

.. code-block:: python

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']

      with self.assertRaises(IndexError):
          a_list[5]
      a_list[-5]

the terminal shows IndexError_

.. code-block:: python

  IndexError: list index out of range

I add another assertRaises_

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
review
*********************************************************************************

I ran tests for `lists <https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20remove#more-on-lists>`_

* they are represented with ``[]``
* they can be made with the `list <https://docs.python.org/3/library/stdtypes.html?highlight=list#list>`_ constructor_
* they can hold any :ref:`object<classes>`
* they can be changed by performing an operation, this means they are mutable

Would you like to :ref:`test list comprehensions?<lists: list comprehensions>`

----

:doc:`/code/code_lists`