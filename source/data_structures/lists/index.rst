.. meta::
  :description: Learn Python lists with this TDD tutorial! Master list methods, indexing, and slicing. Start coding now!
  :keywords: Python lists, Python list methods, Python TDD tutorial, Python list operations, learn Python programming, Python list slicing, Python indexing tutorial, Jacob Itegboje

.. include:: ../../links.rst

.. _clear: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _copy: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _pop: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _list: https://docs.python.org/3/library/stdtypes.html#list
.. _lists: https://docs.python.org/3/library/stdtypes.html#list
.. _IndexError: https://docs.python.org/3/library/exceptions.html#IndexError

#################################################################################
lists
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/npXHw5-3C8s?si=K-BDxQG86CoP7rOc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

A list_ is a container :ref:`object<classes>` that can hold any objects_

* they are represented with ``[]``
* they can be made with the list_ constructor_
* they can be changed by performing an operation - they are mutable

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``lists`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh lists

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 lists

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_lists.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_lists.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestLists(unittest.TestCase):

----

*********************************************************************************
test_making_a_list
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_making_a_list``

.. code-block:: python
  :linenos:

  import unittest


  class TestLists(unittest.TestCase):

      def test_making_a_list(self):
          self.assertEqual(list(), None)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [] != None

green: make it pass
#################################################################################

I change the expectation

.. code-block:: python

  self.assertEqual(list(), [])

the test passes. This is how to make an empty list_

refactor: make it better
#################################################################################

I add another :ref:`assertion<AssertionError>`, this time with input to the list_ constructor_

.. code-block:: python
  :emphasize-lines: 2

  self.assertEqual(list(), [])
  self.assertEqual(list(0), [])

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: 'int' object is not iterable

I add the error to the list of :ref:`Exceptions<errors>` encountered

.. code-block:: python
  :emphasize-lines: 3

  # Exceptions Encountered
  # AssertionError
  # TypeError

I change the input to a tuple_

.. code-block:: python
  :emphasize-lines: 2

  self.assertEqual(list(), [])
  self.assertEqual(list((0, 1, 2, 'n')), [])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 1, 2, 'n'] != []

I change the expectation to match

.. code-block:: python

  self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

the test passes. I can make a list_ with the constructor_ or square brackets(``[]``), which uses less characters

----

*********************************************************************************
test_attributes_and_methods_of_lists
*********************************************************************************

I use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of lists_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list(self):
      ...

  def test_attributes_and_methods_of_lists(self):
      self.assertEqual(
          dir(list),
          [

          ]
      )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

there is also a note on how to see the full difference between ``dir(list)`` and my empty list_

.. code-block:: python

  Diff is 748 characters long. Set self.maxDiff to None to see it

`maxDiff`_ is an :ref:`attribute<AttributeError>` of the `unittest.TestCase`_ :ref:`class <classes>` that sets the maximum number of characters to show when comparing 2 objects in the terminal_, when it is set to :ref:`None` it shows the entire difference

green: make it pass
#################################################################################

* I add ``self.maxDiff`` to the test then move the terminal_ to the right

  .. code-block:: python
    :emphasize-lines: 2

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            [

            ]
        )

  the terminal_ shows a long list_ of items. I copy and paste them from the terminal_ then use `find and replace`_ to remove the extra characters

  .. note::

    results can be different because of the Python_ version

  .. code-block:: python

    def test_attributes_and_methods_of_lists(self):
        self.maxDiff = None
        self.assertEqual(
            dir(list),
            [
                '__add__',
                ...
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

  the test passes and I move it back to the bottom. I ignore the names with double underscores (__), then copy and paste the other names to make a TODO list

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
test_append_adds_item_to_end_of_a_list
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

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.append() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I add ``0`` as input

.. code-block:: python

  self.assertIsNone(a_list.append(0))

the terminal_ shows green, the append_ :ref:`method<functions>` returns :ref:`None` when called

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` to see what append_ did to the list_

  .. code-block:: python
    :emphasize-lines: 2

    self.assertIsNone(a_list.append(0))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 0] != [0, 1, 2, 'n']

  the :ref:`method<functions>` added a value. I change the expectation to match the values in the terminal_

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 0])

  the test passes

* I change the value given to append_

  .. code-block:: python

    self.assertIsNone(a_list.append('n+1'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 'n+1'] != [0, 1, 2, 'n', 0]

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

  the test passes

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_append_adds_item_to_end_of_a_list(self):
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

  def test_append_adds_item_to_end_of_a_list(self):
      ...

  def test_clear(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.clear())

the terminal_ shows green. The clear_ :ref:`method<functions>` returns :ref:`None` when called

red: make it fail
#################################################################################

I add an :ref:`assertion<AssertionError>` to show what it did to the list_

.. code-block:: python
  :emphasize-lines: 2

  self.assertIsNone(a_list.clear())
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [] != [0, 1, 2, 'n']

the list_ is now empty

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

I add another test

.. code-block:: python

  def test_clear_empties_a_list(self):
      ...

  def test_copy(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.copy())

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [0, 1, 2, 'n'] is not None

the :ref:`method<functions>` returns a copy of the list_

green: make it pass
#################################################################################

I add the list_ to the :ref:`assertion<AssertionError>`

.. code-block:: python
  :emphasize-lines: 2

  a_list = [0, 1, 2, 'n']
  self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [0, 1, 2, 'n'] is not None : [0, 1, 2, 'n']

the values are the same, I change assertIsNone_ to assertEqual_

.. code-block:: python
  :emphasize-lines: 2

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

the test passes

refactor: make it better
#################################################################################

* I change the name of the test

  .. code-block::
    :emphasize-lines: 1

    def test_copy_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

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

  def test_copy_a_list(self):
      ...

  def test_count(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.count())

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.count() takes exactly one argument (0 given)

I add a value to the call

.. code-block:: python
  :emphasize-lines: 3

  def test_count(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.count(0))

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 1 is not None

green: make it pass
#################################################################################

I add the value

.. code-block:: python

  self.assertIsNone(a_list.count(0), 1)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 1 is not None : 1

I change assertIsNone_ to assertEqual_

.. code-block:: python

  self.assertEqual(a_list.count(0), 1)

the test passes

refactor: make it better
#################################################################################

* ``0`` is in the list_ 1 time, I add ``1`` to it 2 more times then add an :ref:`assertion<AssertionError>` for it

  .. code-block:: python
    :emphasize-lines: 2, 4

    def test_count(self):
        a_list = [0, 1, 2, 1, 'n', 1]
        self.assertEqual(a_list.count(0), 1)
        self.assertEqual(a_list.count(1), 1)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 3 != 1

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list.count(1), 3)

  the test passes

* I want to see what happens when I try to count an item that is not in the list_

  .. code-block:: python

    self.assertEqual(a_list.count(1), 3)
    self.assertEqual(a_list.count('not in list'), 3)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

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
test_extend_adds_items_from_an_iterable_to_end_of_a_list
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

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.extend() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I pass a value to the call

.. code-block:: python

  self.assertIsNone(a_list.extend(0))

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: 'int' object is not iterable

I change the value to an iterable_

.. code-block:: python

  self.assertIsNone(a_list.extend((0, 1)))

the test passes. The extend_ :ref:`method<functions>` returns :ref:`None` when called

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` to see what it did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.extend((0, 1)))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 0, 1] != [0, 1, 2, 'n']

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the test passes

* I change the values given to the extend_ :ref:`method<functions>`

  .. code-block:: python
    :emphasize-lines: 3

    def test_extend(self):
        a_list = [0, 1, 2, 'n']
        self.assertIsNone(a_list.extend((2, 1, 0)))
        self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 2, 1, 0] != [0, 1, 2, 'n', 0, 1]

  I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

  the test is green again, it looks like extend_ calls append_ for each item in the iterable_

* I change the name of the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_extend_adds_items_from_an_iterable_to_end_of_a_list(self):
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

  def test_extend_adds_items_from_an_iterable_to_end_of_a_list(self):
      ...

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.index())

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: index expected at least 1 argument, got 0

green: make it pass
#################################################################################

I add a value to the call

.. code-block:: python
  :emphasize-lines: 3

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.index(0))

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 0 is not None

I add the expectation

.. code-block:: python

  self.assertIsNone(a_list.index(0), 0)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 0 is not None : 0

I change assertIsNone_ to assertEqual_

.. code-block:: python
  :emphasize-lines: 3

  def test_index(self):
      a_list = [0, 1, 2, 'n']
      self.assertEqual(a_list.index(0), 0)

the test passes

refactor: make it better
#################################################################################

* it does not tell me if the :ref:`method<functions>` returned the same value I gave, so I change the list_

  .. code-block:: python
    :emphasize-lines: 2

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index(0), 0)

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: 0 is not in list

  the index_ :ref:`method<functions>` raises ValueError_ when the item is not in the list_. I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # TypeError
    # ValueError

  I remove the things around the call and change the value to be more descriptive

  .. code-block:: python
    :emphasize-lines: 3

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        a_list.index('not in list')

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: 'not in list' is not in list

  I add assertRaises_ to handle the :ref:`Exception<errors>`

  .. code-block:: python
    :emphasize-lines: 4,5

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the test is green again

* I add a new :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 3

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last']
        self.assertEqual(a_list.index('1st'), '1st')

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != '1st'

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list.index('1st'), 0)

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.index('1st'), 0)
    self.assertEqual(a_list.index('3rd'), 0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 2 != 0

  I change the value in the test

  .. code-block:: python

    self.assertEqual(a_list.index('3rd'), 2)

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.index('3rd'), 2)
    self.assertEqual(a_list.index('2nd'), 2)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 != 2

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list.index('2nd'), 1)

  the test is green again

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.index('2nd'), 1)
    self.assertEqual(a_list.index('...last'), 1)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 3 != 1

  I change the value to match the terminal_

  .. code-block:: python

    self.assertEqual(a_list.index('...last'), 3)

  the test passes. The index_ :ref:`method<functions>` returns numbers for the position of the item in the list_. Python_ uses `zero-based indexing`_ which means the first item has an index of ``0`` and the last item has an index of the length of the list_ minus ``1``

* I want to know what would happen if I have the same item in the list_ more than once, so I add a duplicate

  .. code-block:: python
    :emphasize-lines: 2

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last', '1st']

  the terminal_ still shows green. I add an :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.index('...last'), 3)
    self.assertEqual(a_list.index('1st'), 4)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != 4

  when I first called the index_ :ref:`method<functions>`, the terminal_ showed :ref:`TypeError`

  .. code-block:: shell

    TypeError: index expected at least 1 argument, got 0

  I try a second argument

  .. code-block:: python

    self.assertEqual(a_list.index('1st', 0), 4)

  the terminal_ still shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != 4

  I change the argument

  .. code-block:: python

    self.assertEqual(a_list.index('1st', 1), 4)

  the test passes, the second input is the position I want the :ref:`method<functions>` to start from. I try the same thing with the other :ref:`assertions<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 3-6

    def test_index(self):
        a_list = ['1st', '2nd', '3rd', '...last', '1st']
        self.assertEqual(a_list.index('1st', 0), 0)
        self.assertEqual(a_list.index('3rd', 0), 2)
        self.assertEqual(a_list.index('2nd', 0), 1)
        self.assertEqual(a_list.index('...last', 0), 3)
        self.assertEqual(a_list.index('1st', 1), 4)

        with self.assertRaises(ValueError):
            a_list.index('not in list')

  the test is still green

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_index_returns_first_position_of_item_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last', '1st']
        ...

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

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: insert expected 2 arguments, got 0

green: make it pass
#################################################################################

I add two values to the call

.. code-block:: python

  def test_insert(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.insert(0, 1))

the test is green

refactor: make it better
#################################################################################

* I add an :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 2

    self.assertIsNone(a_list.insert(0, 1))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 0, 1, 2, 'n'] != [0, 1, 2, 'n']

  I add the new value to the list_

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 1, 2, 'n'])

  the test passes. The insert_ :ref:`method<functions>` places the second input given at the index given as the first , it also moves the original items from that index and on in the list_ to the right

* I change the second input in the call

  .. code-block:: python

    self.assertIsNone(a_list.insert(0, -1))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-1, 0, 1, 2, 'n'] != [1, 0, 1, 2, 'n']

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the test is green again

* I add another :ref:`assertion<AssertionError>` to see what happens when I insert_ an item in the middle of the list

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
    self.assertIsNone(a_list.insert(3, 1.5))

  the terminal_ shows green. I add an :ref:`assertion<AssertionError>` to see what it did to the list

  .. code-block:: python

    self.assertIsNone(a_list.insert(3, 1.5))
    self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-1, 0, 1, 1.5, 2, 'n'] != [-1, 0, 1, 2, 'n']

  I add the value to the expectation

  .. code-block:: python

    self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

  the test passes, it moved everything from the given :ref:`index<test_index_returns_first_position_of_item_in_a_list>` and after to the right

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

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

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'n' is not None

The pop_ :ref:`method<functions>` returns the last item in the list_

green: make it pass
#################################################################################

I add the expectation

.. code-block:: python

  self.assertIsNone(a_list.pop(), 'n')

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'n' is not None : n

I change assertIsNone_ to assertEqual_

.. code-block:: python

  a_list = [0, 1, 2, 'n']
  self.assertEqual(a_list.pop(), 'n')

the test passes

refactor: make it better
#################################################################################

* I add an :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.pop(), 'n')
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 'n']

  I change the values in the test to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])
    self.assertEqual(a_list.pop(), 'n')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 2 != 'n'

  I change the value

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2])
    self.assertEqual(a_list.pop(), 2)

  the test passes. I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list.pop(), 2)
    self.assertEqual(a_list, [0, 1, 2])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1] != [0, 1, 2]

  I change the values in the test to match

  .. code-block:: python

    self.assertEqual(a_list, [0, 1])

  the test passes

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_pop_removes_and_returns_last_item_from_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(a_list.pop(), 'n')
        self.assertEqual(a_list, [0, 1, 2])
        self.assertEqual(a_list.pop(), 2)
        self.assertEqual(a_list, [0, 1])

* I take out pop_ from the TODO list

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

  def test_pop_removes_and_returns_last_item_from_a_list(self):
      ...

  def test_remove(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.remove())

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.remove() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I add a value to the call

.. code-block:: python

  self.assertIsNone(a_list.remove(0))

the terminal_ shows green, the remove_ :ref:`method<functions>` returns :ref:`None`

refactor: make it better
#################################################################################

* I add an :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertIsNone(a_list.remove(0))
    self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 2, 'n'] != [0, 1, 2, 'n']

  the :ref:`method<functions>` removes the item given from the list_. I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, [1, 2, 'n'])

  the test passes

* I change the values in the list_ to see what would happen if an item is in there more than once

  .. code-block:: python
    :emphasize-lines: 2

    def test_remove(self):
        a_list = [0, 1, 0, 2, 0, 'n']
        self.assertIsNone(a_list.remove(0))
        self.assertEqual(a_list, [1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 0, 2, 0, 'n'] != [1, 2, 'n']

  I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

  the test passes

* I want to know what would happen if I try to remove_ an item that is not in the list_

  .. code-block:: python

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])
    self.assertIsNone(a_list.remove('not in list'))

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: list.remove(x): x not in list

  I remove the things around the call then add assertRaises_

  .. code-block:: python
    :emphasize-lines: 3,4

    self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

    with self.assertRaises(ValueError):
        a_list.remove('not in list')

  the test passes

* I rename the test

  .. code-block:: python
    :emphasize-lines: 1

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

  def test_remove_first_instance_of_item_from_a_list(self):
      ...

  def test_reverse(self):
      a_list = [0, 1, 2, 'n']
      self.assertIsNone(a_list.reverse())

the terminal_ shows green. This :ref:`method<functions>` returns :ref:`None`. I add an :ref:`assertion<AssertionError>` to see what it did to the list_

.. code-block:: python

  self.assertIsNone(a_list.reverse())
  self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['n', 2, 1, 0] != [0, 1, 2, 'n']

it reversed the order of the items in the list_

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
    :emphasize-lines: 1

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

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: '<' not supported between instances of 'str' and 'int'

I have to change ``'n'`` to a number or change the other numbers to a string_

green: make it pass
#################################################################################

I remove the things around the call, and the variable name since it is not used, then add assertRaises_

.. code-block:: python

  def test_sort(self):
      with self.assertRaises(TypeError):
          [0, 1, 2, 'n'].sort()

the test passes

refactor: make it better
#################################################################################

* I add a new list_ and another :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 5,6

    def test_sort(self):
        with self.assertRaises(TypeError):
            [0, 1, 2, 'n'].sort()

        a_list = [0, 1, 2, 3]
        self.assertIsNone(a_list.sort())


  the terminal_ still shows green, sort_ returns :ref:`None` when called. I add another :ref:`assertion<AssertionError>` to see what it did to the list_

  .. code-block:: python

    self.assertIsNone(a_list.sort())
    self.assertEqual(a_list, [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  the list_ stayed the same. I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes. The name of the :ref:`method<functions>` is sort_ and I gave it a list_ that is sorted, I change it to see what would happen when it is not sorted

  .. code-block:: python

    a_list = [0, 1, -1, 2, -2, 3, -3]

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-3, -2, -1, 0, 1, 2, 3] != [0, 1, 2, 3]

  the sort_ :ref:`method<functions>` arranged the list_ in ascending order. I change the values to match

  .. code-block:: python

    self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

  the test passes

* I change the name of the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_sort_a_list(self):
        with self.assertRaises(TypeError):
            [0, 1, 2, 'n'].sort()

        a_list = [0, 1, -1, 2, -2, 3, -3]
        self.assertIsNone(a_list.sort())
        self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

* I remove sort_ from the TODO list

----

*********************************************************************************
test_getting_items_of_a_list
*********************************************************************************

When I want an item that is in a list_, I can give its :ref:`index<test_index_returns_first_position_of_item_in_a_list>` in square brackets(``[]``)

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_sort_a_list(self):
      ...

  def test_getting_items_of_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      self.assertEqual(a_list[0], '')

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '1st' != ''

the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``0``

green: make it pass
#################################################################################

I change the value in the test

.. code-block:: python

  self.assertEqual(a_list[0], '1st')

the test passes

refactor: make it better
#################################################################################

* this is the reverse of the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` :ref:`method<functions>` which takes in the item and returns its position, in this case I provide the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` and it returns the item, which means I can write this

  .. code-block:: python

    self.assertEqual(a_list[0], '1st')
    self.assertEqual(a_list[a_list.index('1st')], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '1st' != ''

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list[a_list.index('1st')], '1st')

  the test passes

* I can also use negative numbers. The last item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``-1`` and the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of negative the length of the list_

  .. code-block:: python

    self.assertEqual(a_list[a_list.index('1st')], '1st')
    self.assertEqual(a_list[-4], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '1st' != ''

  I change the value to match

  .. code-block:: python

    self.assertEqual(a_list[-4], '1st')

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list[-4], '1st')
    self.assertEqual(a_list[2], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '3rd' != ''

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(a_list[2], '3rd')

  the terminal_ shows green again

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list[2], '3rd')
    self.assertEqual(a_list[-2], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '3rd' != ''

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[-2], '3rd')

  the test passes

* I add another line

  .. code-block:: python

    self.assertEqual(a_list[-2], '3rd')
    self.assertEqual(a_list[1], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '2nd' != ''

  I make the test pass

  .. code-block:: python

    self.assertEqual(a_list[1], '2nd')

* I add another

  .. code-block:: python

    self.assertEqual(a_list[1], '2nd')
    self.assertEqual(a_list[-3], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '2nd' != ''

  I change the value

  .. code-block:: python

    self.assertEqual(a_list[-3], '2nd')

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list[-3], '2nd')
    self.assertEqual(a_list[3], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '...last' != ''

  I change the value

  .. code-block:: python

    self.assertEqual(a_list[3], '...last')

  the test passes

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list[3], '...last')
    self.assertEqual(a_list[-1], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '...last' != ''

  I make the values match

  .. code-block:: python

    self.assertEqual(a_list[-1], '...last')

  the test passes

----

*********************************************************************************
test_setting_items_in_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_getting_items_of_a_list(self):
      ...

  def test_setting_items_in_a_list(self):
      a_list = ['1st', '2nd', '3rd', '...last']
      a_list[-1] = '4th'
      self.assertEqual(a_list, ['1st', '2nd', '3rd', '...last'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['1st', '2nd', '3rd', '4th'] != ['1st', '2nd', '3rd', '...last']

I can use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of an item to change its value in a list_, the way I point a name to a value

green: make it pass
#################################################################################

I change the expectation to match the terminal_

.. code-block:: python

  self.assertEqual(a_list, ['1st', '2nd', '3rd', '4th'])

the test passes

----

*********************************************************************************
test_viewing_parts_of_a_list_aka_slicing
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_setting_items_in_a_list(self):
      ...

  def test_viewing_parts_of_a_list(self):
      a_list = ['a', 'b', 'c', 'd']
      self.assertEqual(a_list[0:2], [])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['a', 'b'] != []

green: make it pass
#################################################################################

I change the values to match

.. code-block:: python

  self.assertEqual(a_list[0:2], ['a', 'b'])

the test passes. I give two values in square brackets(``[]``), separated by a ``:``, the first value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to start from, and the second value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to stop at plus ``1``

refactor: make it better
#################################################################################

* I can skip the first number when the starting :ref:`index<test_index_returns_first_position_of_item_in_a_list>` is ``0``

  .. code-block:: python

    self.assertEqual(a_list[0:2], ['a', 'b'])
    self.assertEqual(a_list[:2], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b'] != []

  I change the values to match

  .. code-block:: python

    self.assertEqual(a_list[:2], ['a', 'b'])

  the terminal_ shows green again

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list[:2], ['a', 'b'])
    self.assertEqual(a_list[1:4], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

  I add the missing values

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['b', 'c', 'd'])

  the test passes

* I can skip the second number when it is bigger than or the same as the length of the list_

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
    self.assertEqual(a_list[1:], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

  I add the missing values

  .. code-block:: python

    self.assertEqual(a_list[1:], ['b', 'c', 'd'])

  the test passes

* I add another line

  .. code-block:: python

    self.assertEqual(a_list[1:], ['b', 'c', 'd'])
    self.assertEqual(a_list[0:3], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b', 'c'] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['a', 'b', 'c'])

  the test is green again

* I add another

  .. code-block:: python

    self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
    self.assertEqual(a_list[1:3], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c'] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list[1:3], ['b', 'c'])

  the test is green again

* I can also skip both numbers

  .. code-block:: python

    self.assertEqual(a_list[1:3], ['b', 'c'])
    self.assertEqual(a_list[:], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b', 'c', 'd'] != []

  I get the entire list_ back or a copy_

  .. code-block:: python

    self.assertEqual(a_list[:], a_list.copy())

  the test is green again

* This is also called slicing, I change the name of the test

  .. code-block:: python
    :emphasize-lines: 1

    def test_viewing_parts_of_a_list_aka_slicing(self):
        a_list = ['a', 'b', 'c', 'd']
        self.assertEqual(a_list[0:2], ['a', 'b'])
        self.assertEqual(a_list[:2], ['a', 'b'])
        self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
        self.assertEqual(a_list[1:], ['b', 'c', 'd'])
        self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
        self.assertEqual(a_list[1:3], ['b', 'c'])
        self.assertEqual(a_list[:], a_list.copy())

----

*********************************************************************************
test_index_error
*********************************************************************************

IndexError_ is raised when I try to get an item from a list_ but use a number that points to something that is NOT in it. When I see this :ref:`Exception<errors>` I know the underlying data structure is a list_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_viewing_parts_of_a_list_aka_slicing(self):
      ...

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']
      a_list[4]

the terminal_ shows IndexError_

.. code-block:: shell

  IndexError: list index out of range

when I use an index that is the same as or greater than the length of the list_ I am pointing to something that is NOT in it

green: make it pass
#################################################################################

I add it to the list of :ref:`Exceptions<errors>` encountered

.. code-block:: python
  :emphasize-lines: 5

  # Exceptions Encountered
  # AssertionError
  # TypeError
  # ValueError
  # IndexError

I add assertRaises_

.. code-block:: python
  :emphasize-lines: 4,5

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']

      with self.assertRaises(IndexError):
          a_list[4]

the test passes

refactor: make it better
#################################################################################

* the same thing happens when I use a negative number that is lower than the length of the list_ as a negative number

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[4]
    a_list[-5]

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

  I add another assertRaises_

  .. code-block:: python
    :emphasize-lines: 3

    with self.assertRaises(IndexError):
        a_list[4]
    with self.assertRaises(IndexError):
        a_list[-5]

  the test passes

* IndexError_ is also raised when I call the pop_ :ref:`method<functions>` with an empty list_

  .. code-block:: python

    with self.assertRaises(IndexError):
        a_list[-5]
    [].pop()

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: pop from empty list

  I add assertRaises_

  .. code-block:: python
    :emphasize-lines: 3

    with self.assertRaises(IndexError):
        a_list[-5]
    with self.assertRaises(IndexError):
        [].pop()

  the terminal_ shows green. I cannot remove the last item from a list_ that has no items, this is like trying to get an item from a list_ that has no items

  .. code-block:: python
    :emphasize-lines: 3

    with self.assertRaises(IndexError):
        [].pop()
    [][-1]

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

  I add assertRaises_

  .. code-block:: python

    with self.assertRaises(IndexError):
        [][-1]

  the test passes. Any :ref:`index<test_index_returns_first_position_of_item_in_a_list>` given to an empty list_ will raise IndexError_

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can make a list_ with the constructor_ or square brackets (``[]``), then tested the different :ref:`methods<functions>` from append_ to sort_, added tests for :ref:`getting items of a list<test_getting_items_of_a_list>`, :ref:`setting items in a list<test_setting_items_in_a_list>`, :ref:`slicing a list<test_viewing_parts_of_a_list_aka_slicing>` and :ref:`IndexError<test_index_error>`

Would you like to :ref:`test list comprehensions?<lists: list comprehensions>`

----

:ref:`data structures: lists: tests`