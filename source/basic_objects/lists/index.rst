.. meta::
  :description: Python lists for beginners: step-by-step TDD tutorial testing mutable sequence objects with unittest and pytest. Learn how to create lists with list() and [], explore dir(list) and dir(object) with maxDiff = None, and test all list methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, and sort. Master 0-based indexing, negative indexing, item assignment (mutation), slicing ([start:stop]), and the exceptions every beginner encounters: TypeError ('int' object is not iterable), ValueError ('not in list' is not in list), and IndexError (list index out of range, pop from empty list).
  :keywords: Jacob Itegboje, Pumping Python, python lists tutorial, python list methods, list append clear copy, list count extend index, list insert pop remove, list reverse sort, python list indexing, negative indexing python, python list slicing, python list mutation, TDD python lists, unittest test list, TypeError int object is not iterable, IndexError list index out of range, IndexError pop from empty list, ValueError not in list, dir list maxDiff None, python basic objects lists, red green refactor lists, mutable sequence python


.. include:: ../../links.rst

.. _more_on_lists: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _append: more_on_lists_
.. _append method: more_on_lists_
.. _count: more_on_lists_
.. _count method: more_on_lists_
.. _clear: more_on_lists_
.. _clear method: more_on_lists_
.. _copy: more_on_lists_
.. _copy method: more_on_lists_
.. _pop: more_on_lists_
.. _pop method: more_on_lists_
.. _insert: more_on_lists_
.. _insert method: more_on_lists_
.. _index: more_on_lists_
.. _index method: more_on_lists_
.. _remove: more_on_lists_
.. _remove method: more_on_lists_
.. _reverse: more_on_lists_
.. _reverse method: more_on_lists_
.. _sort: more_on_lists_
.. _sort method: more_on_lists_
.. _extend: more_on_lists_
.. _extend method: more_on_lists_
.. _list: https://docs.python.org/3/library/stdtypes.html#list
.. _lists: list_
.. _slicing: https://docs.python.org/3/reference/expressions.html#slicings
.. _IndexError: https://docs.python.org/3/library/exceptions.html#IndexError
.. _iterable: https://docs.python.org/3/glossary.html#term-iterable


#################################################################################
what is a list?
#################################################################################

----

A list_ is a container :ref:`object<everything is an object>` that can hold any :ref:`objects<everything is an object>`

* they are represented with ``[]``
* they can be made with ``list()`` or ``[]``
* they can be changed with an operation, which means they are mutable

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :linenos:
  :lines: 1-8

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 10
  :lines: 10-27

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 29
  :lines: 29-37

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 39
  :lines: 39-47

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 49
  :lines: 49-57

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 59
  :lines: 59-68

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 70
  :lines: 70-82

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 84
  :lines: 84-95

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 97
  :lines: 97-103

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 105
  :lines: 105-115

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 117
  :lines: 117-132

.. literalinclude:: ../../code/tests/test_lists.py
  :caption: lists/tests/test_lists.py
  :language: python
  :lineno-start: 134
  :lines: 134-151

*********************************************************************************
questions about lists
*********************************************************************************

* :ref:`what is a list?`
* :ref:`how can I add an item to the end of a list?<test_append_adds_item_to_end_of_a_list>`
* :ref:`how can I empty a list?<test_clear_empties_a_list>`
* :ref:`how can I copy a list?<test_copy_a_list>`
* :ref:`how can I count the number of times an item is in a list?<test_count_number_of_times_item_is_in_a_list>`
* :ref:`how can I add items from an iterable to the end of a list?<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`
* :ref:`how can I get the first position of an item in a list?<test_index_returns_first_position_of_item_in_a_list>`
* :ref:`how can I put an item at a position in a list?<test_insert_item_at_position_in_a_list>`
* :ref:`how can I remove the last item from a list?<test_pop_removes_and_returns_last_item_from_a_list>`
* :ref:`how can I remove the first time an item is in a list?<test_remove_first_time_item_is_in_a_list>`
* :ref:`how can I reverse a list?<test_reverse_a_list>`
* :ref:`how can I sort a list?<test_sort_a_list>`
* :ref:`how can I get items of a list?<test_getting_items_of_a_list>`
* :ref:`how can I change an item in a list?<test_setting_items_in_a_list>`
* :ref:`how can I see only parts of a list?<test_getting_parts_of_a_list_aka_slicing>`
* :ref:`what causes IndexError?<test_index_error>`

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_
* I give ``lists`` as the first argument to the :ref:`makePythonTdd<makePythonTdd with variables>` program_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :caption: terminal
        :emphasize-lines: 1

        ./makePythonTdd.sh lists

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :caption: terminal
        :emphasize-lines: 1

        .\makePythonTdd.ps1 lists

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 10
    :emphasize-text: tests/test_lists.py:7

    ======================== FAILURES ==========================
    ______________ Testlists.test_failure _________________

    self = <tests.test_lists.Testlists testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_lists.py:7: AssertionError
    ================== short test summary info ==================
    FAILED tests/test_lists.py::Testlists::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =====================

* I open ``test_lists.py`` from the ``tests`` folder_

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 4
    :emphasize-lines: 4

    class Testlists(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(False)


    # Exceptions seen

  the test passes.

* I change ``Testlists`` to ``TestLists`` to match :ref:`Python convention<conventions>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :linenos:
    :emphasize-lines: 4

    import unittest


    class TestLists(unittest.TestCase):

        def test_failure(self):

* I open a new terminal_ then `change directory`_ to ``lists``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd lists

* I add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'setup project'

----

*********************************************************************************
test_making_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----


I change :ref:`test_failure` to :ref:`test_making_a_list`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 4
  :emphasize-lines: 3-4

  class TestLists(unittest.TestCase):

      def test_making_a_list(self):
          self.assertEqual(list(), None)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: [] != None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertEqual(list(), [])

the test passes. I can make an empty list_ with ``list()`` or ``[]``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` with input to ``list()``  to make a list_ that has things in it

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_list(self):
            self.assertEqual(list(), [])
            self.assertEqual(list(0), [])


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: 'int' object is not iterable

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # TypeError

----

*********************************************************************************
what is an iterable?
*********************************************************************************

An :ref:`iterable<what is an iterable?>` is an :ref:`object<everything is an object>` that can return what it has, one at a time. In order words, I can :ref:`loop<what is a for loop?>` over it. strings_, tuples_, lists_, sets_ and :ref:`dictionaries<what is a dictionary?>` are :ref:`iterable<what is an iterable?>`.

* I change the input to a tuple_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 6
    :emphasize-lines: 3

        def test_making_a_list(self):
            self.assertEqual(list(), [])
            self.assertEqual(list((0, 1, 2, 'n')), [])


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2, 'n'] != []

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 8
    :emphasize-lines: 1

            self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_making_a_list'

:ref:`I can make a list with 'list()', or with square brackets('[]') which uses less characters<test_making_a_list>`.

----

*********************************************************************************
test_dir_list
*********************************************************************************

I want to test the things I can do with lists_. I use the `dir built-in function`_ to see the :ref:`attributes<what is an object attribute?>` and :ref:`methods<what is a method?>` of :ref:`lists<what is a list?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test for the :ref:`attributes<what is an object attribute?>` and :ref:`methods<what is a method?>` of :ref:`lists<what is a list?>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 8
  :emphasize-lines: 3-7

          self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

      def test_dir_list(self):
          self.assertEqual(
              dir(list),
              []
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__add__', '__class__', '__class_getitem_[552 chars]ort'
  ] != []

there is also a note on how to see the full difference between ``dir(list)`` and my empty list_

.. code-block:: python

  Diff is 748 characters long. Set self.maxDiff to None to see it

`maxDiff`_ is an :ref:`attribute<what causes AttributeError?>` of the :ref:`unittest.TestCase class<test_dir_unittest_testcase>` that sets the maximum number of characters to show when comparing 2 objects in the terminal_, when it is set to :ref:`None<what is None?>` it shows the full difference.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``self.maxDiff`` to the test then move the terminal_ to the right

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 10
    :emphasize-lines: 2

        def test_dir_list(self):
            self.maxDiff = None
            self.assertEqual(
                dir(list),
                []
            )

  the terminal_ is my friend, and shows a long list_ of items. I copy (:kbd:`ctrl/command+c`) and paste (:kbd:`ctrl/command+v`) them then use `find and replace`_ to remove the extra characters ``E`` and  ``-``

  .. note:: results can be different because of the Python_ version

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 10
    :emphasize-lines: 5-54

        def test_dir_list(self):
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

  the test passes. This looks like the :ref:`attributes and methods of objects<test_dir_object>` with more stuff.

* I copy (:kbd:`ctrl/command+c`) and paste (:kbd:`ctrl/command+v`) the names that do NOT have double underscores (__) to use as a TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 67
    :emphasize-lines: 1-11

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


    # Exceptions seen
    # AssertionError
    # TypeError

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_dir_list'

:ref:`The dir built-in function returns a list of attributes and methods<test_dir_list>`.

----

*********************************************************************************
test_append_adds_item_to_end_of_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `append method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 62
  :emphasize-lines: 5-7

                    'sort'
                ]
            )

        def test_append(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append())


    'append',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: list.append() takes exactly
             one argument (0 given)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``0`` as input

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 68
  :emphasize-lines: 1

          self.assertIsNone(a_list.append(0))

the test is green again, the `append method`_ returns :ref:`None<what is None?>` when :ref:`called<how to call a function with input>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to see what append_ did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 66
    :emphasize-lines: 4

        def test_append(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append(0))
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'append',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

      AssertionError: Lists differ: [0, 1, 2, 'n', 0]
                                 != [0, 1, 2, 'n']

  the `append method`_ added a value at the end of the list_.

* I change the expectation to match the values in the terminal_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 69
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 0])

  the test passes.

* I change the value given to append_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 66
    :emphasize-lines: 3

        def test_append(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append('n+1'))
            self.assertEqual(a_list, [0, 1, 2, 'n', 0])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2, 'n', 'n+1']
                               != [0, 1, 2, 'n', 0]

* I change the expectation of the :ref:`assertion<what is an assertion?>` to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 66
    :emphasize-lines: 4

        def test_append(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append('n+1'))
            self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])


    'append',

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 60
    :emphasize-lines: 7

                    'remove',
                    'reverse',
                    'sort'
                ]
            )

        def test_append_adds_item_to_end_of_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append('n+1'))
            self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

* I remove append_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 69

          self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])


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

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_append_adds_item_to_end_of_a_list'

:ref:`I know how to add things to the end of a list<test_append_adds_item_to_end_of_a_list>`

----

*********************************************************************************
test_clear_empties_a_list
*********************************************************************************

I add a test for the `clear method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 69
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

      def test_clear(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.clear())


  'clear',

the test is still green. The `clear method`_ returns :ref:`None<what is None?>` when :ref:`called<how to call a function with input>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to see what clear_ did to the list_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 71
  :emphasize-lines: 4

      def test_clear(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.clear())
          self.assertEqual(a_list, [0, 1, 2, 'n'])


  'clear',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [] != [0, 1, 2, 'n']

the list_ is now empty.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the values to match

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 74
  :emphasize-lines: 1

          self.assertEqual(a_list, [])

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test to make it "clearer"

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 69
    :emphasize-lines: 3

            self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

        def test_clear_empties_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.clear())
            self.assertEqual(a_list, [])

* I remove clear_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 74

            self.assertEqual(a_list, [])


    'copy',
    'count',
    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_clear_empties_a_list'

:ref:`I know how to empty a list<test_clear_empties_a_list>`

----

*********************************************************************************
test_copy_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `copy method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 74
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [])

      def test_copy(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.copy())


  'copy',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: [0, 1, 2, 'n'] is not None

the :ref:`method<what is a method?>` returns a copy of the list_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the list_ to the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 77
    :emphasize-lines: 2

            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: [0, 1, 2, 'n'] is not None : [0, 1, 2, 'n']

  the values are the same, the problem is :ref:`assertIsNone<another way to test if something is None>` only takes 1 input and I gave it 2

* I change :ref:`assertIsNone<another way to test if something is None>` to the :ref:`assertEqual method<test_assertEqual>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 77
    :emphasize-lines: 2

            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 74
    :emphasize-lines: 3

            self.assertEqual(a_list, [])

        def test_copy_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])


    'copy',

* I remove copy_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 78

            self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])


    'count',
    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_copy_a_list'

:ref:`I know how to copy a list<test_copy_a_list>`

----

*********************************************************************************
test_count_number_of_times_item_is_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `count method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 78
  :emphasize-lines: 3-5

          self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

      def test_count(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.count())


  'count',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: list.count() takes exactly
             one argument (0 given)

I add a value to the :ref:`call<how to call a function with input>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 80
  :emphasize-lines: 3

      def test_count(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.count(0))

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 1 is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the value

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 82
  :emphasize-lines: 1

          self.assertIsNone(a_list.count(0), 1)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 1 is not None : 1

I change :ref:`assertIsNone<another way to test if something is None>` to the :ref:`assertEqual method<test_assertEqual>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 82
  :emphasize-lines: 1

          self.assertEqual(a_list.count(0), 1)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* ``0`` is in this list_ one time, I add ``1`` to the list_ two more times then add an :ref:`assertion<what is an assertion?>` for it

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 80
    :emphasize-lines: 2, 4

        def test_count(self):
            a_list = [0, 1, 2, 1, 'n', 1]
            self.assertEqual(a_list.count(0), 1)
            self.assertEqual(a_list.count(1), 1)


    'count',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 3 != 1

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 83
    :emphasize-lines: 1

            self.assertEqual(a_list.count(1), 3)

  the test passes.

* I want to see what happens when I try to count something that is not in the list_.

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 83
    :emphasize-lines: 2

            self.assertEqual(a_list.count(1), 3)
            self.assertEqual(a_list.count('not in list'), 3)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 0 != 3

  The `count method`_ returns ``0`` when the item is not in the list_

* I change the value to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 84
    :emphasize-lines: 1

            self.assertEqual(a_list.count('not in list'), 0)

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 78
    :emphasize-lines: 3

            self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

        def test_count_number_of_times_item_is_in_a_list(self):
            a_list = [0, 1, 2, 1, 'n', 1]
            self.assertEqual(a_list.count(0), 1)
            self.assertEqual(a_list.count(1), 3)
            self.assertEqual(a_list.count('not in list'), 0)


    'count',

* I remove count_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 84

            self.assertEqual(a_list.count('not in list'), 0)


    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_count_number_of_times_item_is_in_a_list'

:ref:`I know how to count how many times something is in a list<test_count_number_of_times_item_is_in_a_list>`

----

*********************************************************************************
test_extend_adds_items_from_an_iterable_to_end_of_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `extend method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 84
  :emphasize-lines: 3-5

          self.assertEqual(a_list.count('not in list'), 0)

      def test_extend(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.extend())


  'extend',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: list.extend() takes exactly
             one argument (0 given)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I pass a value to the :ref:`call<how to call a function with input>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 88
  :emphasize-lines: 1

          self.assertIsNone(a_list.extend(0))

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: 'int' object is not iterable

I change the value to an :ref:`iterable<what is an iterable?>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 88
  :emphasize-lines: 1

          self.assertIsNone(a_list.extend((0, 1)))

the test passes. The `extend method`_ returns :ref:`None<what is None?>` when :ref:`called<how to call a function with input>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 86
    :emphasize-lines: 4

        def test_extend(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.extend((0, 1)))
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'extend',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2, 'n', 0, 1]
                               != [0, 1, 2, 'n']

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 89
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the test passes.

* I change the values given to the `extend method`_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 86
    :emphasize-lines: 3

        def test_extend(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.extend((2, 1, 0)))
            self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2, 'n', 2, 1, 0]
                               != [0, 1, 2, 'n', 0, 1]

* I change the values to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 89
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

  the test is green again, it looks like extend_ calls append_ for each item in the :ref:`iterable<what is an iterable?>`.

* I add another :ref:`assertion<what is an assertion?>` to see if the `extend method`_ does the same as using a :ref:`for loop<what is a for loop?>` with the :ref:`append method<test_append_adds_item_to_end_of_a_list>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 86
    :emphasize-lines: 6-9

        def test_extend(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.extend((2, 1, 0)))
            self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

            another_list = [0, 1, 2, 'n']
            for number in (2, 1, 0):
                another_list.append(number)
            self.assertEqual(another_list, 'BOOM!!!')


    'extend',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: [0, 1, 2, 'n', 2, 1, 0] != 'BOOM!!!'

* I change the expectation to ``a_list``

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 91
    :emphasize-lines: 4

            another_list = [0, 1, 2, 'n']
            for number in (2, 1, 0):
                another_list.append(number)
            self.assertEqual(another_list, a_list)


    'extend',

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 84
    :emphasize-lines: 3

            self.assertEqual(a_list.count('not in list'), 0)

        def test_extend_adds_items_from_an_iterable_to_end_of_a_list(self):
            a_list = [0, 1, 2, 'n']

* I remove extend_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 94

            self.assertEqual(another_list, a_list)


    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_extend_adds_items_from_an_iterable_to_end_of_a_list'

:ref:`I know how to add items from an iterable to a list<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`

----

*********************************************************************************
test_index_returns_first_position_of_item_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `index method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 94
  :emphasize-lines: 3-5

          self.assertEqual(another_list, a_list)

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.index())


  'index',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: index expected at least 1 argument, got 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a value to the :ref:`call<how to call a function with input>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 96
  :emphasize-lines: 3

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.index(0))

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 0 is not None

I add the expectation

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 98
  :emphasize-lines: 1

          self.assertIsNone(a_list.index(0), 0)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 0 is not None : 0

I change :ref:`assertIsNone<another way to test if something is None>` to the :ref:`assertEqual method<test_assertEqual>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 96
  :emphasize-lines: 3

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertEqual(a_list.index(0), 0)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the list_ to find to make sure the :ref:`method<what is a method?>` did not return the same value I gave

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 2

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list.index(0), 0)

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: 0 is not in list

  the `index method`_ raises ValueError_ if the item is not in the list_

* I add ValueError_ to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 106
    :emphasize-lines: 7

    'sort'


    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError

* I remove the things around the :ref:`call to the index method<test_index_returns_first_position_of_item_in_a_list>` and change the value to make it clearer

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 3

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            a_list.index('not in list')

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: 'not in list' is not in list

* I add :ref:`assertRaises<another way to test if an Exception is raised>` to handle the :ref:`Exception<how to test that an Exception is raised>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 4,5

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']

            with self.assertRaises(ValueError):
                a_list.index('not in list')

  the test is green again

* I add a new :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 3

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list.index('1st'), '1st')

            with self.assertRaises(ValueError):
                a_list.index('not in list')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 0 != '1st'

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 98
    :emphasize-lines: 1

        self.assertEqual(a_list.index('1st'), 0)

  the test passes. The `index method`_ does not just return the value I give it

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 4

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list.index('1st'), 0)
            self.assertEqual(a_list.index('3rd'), 0)

            with self.assertRaises(ValueError):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 2 != 0

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 99
    :emphasize-lines: 1

        self.assertEqual(a_list.index('3rd'), 2)

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 99
    :emphasize-lines: 2

          self.assertEqual(a_list.index('3rd'), 2)
          self.assertEqual(a_list.index('2nd'), 2)

          with self.assertRaises(ValueError):
              a_list.index('not in list')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 1 != 2

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 100
    :emphasize-lines: 1

            self.assertEqual(a_list.index('2nd'), 1)

  the test is green again

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 100
    :emphasize-lines: 2

            self.assertEqual(a_list.index('2nd'), 1)
            self.assertEqual(a_list.index('...last'), 1)

            with self.assertRaises(ValueError):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 3 != 1

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 101
    :emphasize-lines: 1

            self.assertEqual(a_list.index('...last'), 3)

  the test passes.

  - The `index method`_ returns numbers for the position of the item in the list_.
  - Python_ uses `zero-based indexing`_ which means the first item has an index of ``0`` and the last item has an index of the length of the list_ minus ``1``.

* I add something in the list_ again to see what happens if I have the same item in the list_ more than once

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
    :emphasize-lines: 2

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last', '1st']

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 101
    :emphasize-lines: 2

            self.assertEqual(a_list.index('...last'), 3)
            self.assertEqual(a_list.index('1st'), 4)

            with self.assertRaises(ValueError):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 0 != 4

  when I first :ref:`called<how to call a function with input>` the `index method`_, the terminal_ showed :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :caption: terminal

    TypeError: index expected at least 1 argument, got 0

  which means I should be able to send more than one argument.

* I add a second argument

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 102
    :emphasize-lines: 1

            self.assertEqual(a_list.index('1st', 0), 4)

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 0 != 4

* I change the argument

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 102
    :emphasize-lines: 1

    self.assertEqual(a_list.index('1st', 1), 4)

  the test passes, the second input is the position I want the `index method`_ to start from

* I try the same thing with the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 96
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

  the test is still green.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 94
    :emphasize-lines: 3

            self.assertEqual(another_list, a_list)

        def test_index_returns_first_position_of_item_in_a_list(self):
            a_list = ['1st', '2nd', '3rd', '...last', '1st']

* I remove index_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 104
    :emphasize-lines: 5

            with self.assertRaises(ValueError):
                a_list.index('not in list')


    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_index_returns_first_position_of_item_in_a_list'

:ref:`I know how to find the position of something in a list<test_index_returns_first_position_of_item_in_a_list>`.

----

*********************************************************************************
test_insert_item_at_position_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the next :ref:`method<what is a method?>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 104
  :emphasize-lines: 4-6

          with self.assertRaises(ValueError):
              a_list.index('not in list')

      def test_insert(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.insert())


  'insert',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: insert expected 2 arguments, got 0

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add two values to the call

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 107
  :emphasize-lines: 3

      def test_insert(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.insert(0, 1))

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to see what the `insert method`_ did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 107
    :emphasize-lines: 4

        def test_insert(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.insert(0, 1))
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'insert',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [1, 0, 1, 2, 'n']
                               != [0, 1, 2, 'n']

  there is an extra value at the beginning of the list_.

* I add the new value to the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 110
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 0, 1, 2, 'n'])

  the test passes.

  The `insert method`_

  - puts the second input given at the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the list_ given as the first input
  - it also moves the original items from that :ref:`index<test_index_returns_first_position_of_item_in_a_list>` and after in the list_, to the right

* I change the second input in the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 107
    :emphasize-lines: 3

        def test_insert(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.insert(0, -1))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [-1, 0, 1, 2, 'n']
                               != [0, 1, 2, 'n']

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 110
    :emphasize-lines: 1

            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the test is green again

* I add another :ref:`assertion<what is an assertion?>` to see what happens when I insert_ an item in the middle of the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 105
    :emphasize-lines: 4-5

        def test_insert(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.insert(0, -1))
            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
            self.assertIsNone(a_list.insert(3, 1.5))
            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])


    'insert',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [-1, 0, 1, 1.5, 2, 'n']
                               != [-1, 0, 1, 2, 'n']

* I add the value to the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 112
    :emphasize-lines: 1

            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

  the test passes. The `insert method`_ moved everything in the list_ from the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` I gave and after, to the right.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 104
    :emphasize-lines: 4

            with self.assertRaises(ValueError):
                a_list.index('not in list')

        def test_insert_item_at_position_in_a_list(self):
            a_list = [0, 1, 2, 'n']

* I remove insert_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 112

            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])


    'pop',
    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_insert_item_at_position_in_a_list'

:ref:`I know how to put an item at a position in a list<test_insert_item_at_position_in_a_list>`

----

*********************************************************************************
test_pop_removes_and_returns_last_item_from_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `pop method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 112
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

      def test_pop(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.pop())


  'pop',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 'n' is not None

The `pop method`_ returns the last item in the list_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the expectation

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 111
  :emphasize-lines: 1

          self.assertIsNone(a_list.pop(), 'n')

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: 'n' is not None : n

I change :ref:`assertIsNone<another way to test if something is None>` to the :ref:`assertEqual method<test_assertEqual>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 114
  :emphasize-lines: 3

      def test_pop(self):
          a_list = [0, 1, 2, 'n']
          self.assertEqual(a_list.pop(), 'n')

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to see what happened to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 114
    :emphasize-lines: 4

        def test_pop(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.pop(), 'n')
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'pop',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2]
                               != [0, 1, 2, 'n']

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 117
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2])

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` with the `pop method`_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 114
    :emphasize-lines: 5

        def test_pop(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.pop(), 'n')
            self.assertEqual(a_list, [0, 1, 2])
            self.assertEqual(a_list.pop(), 'n')


    'pop',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: 2 != 'n'

  The `pop method`_ returns the last item in the list_.

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 118
    :emphasize-lines: 1

            self.assertEqual(a_list.pop(), 2)

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to see what changed in the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 114
    :emphasize-lines: 2

        def test_pop(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.pop(), 'n')
            self.assertEqual(a_list, [0, 1, 2])
            self.assertEqual(a_list.pop(), 2)
            self.assertEqual(a_list, [0, 1, 2])


    'pop',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1] != [0, 1, 2]

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 119
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1])

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 112
    :emphasize-lines: 3

            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

        def test_pop_removes_and_returns_last_item_from_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.pop(), 'n')

* I take out pop_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 119

            self.assertEqual(a_list, [0, 1])


    'remove',
    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_pop_removes_and_returns_last_item_from_a_list'

:ref:`I know how to get and remove the last item from a list<test_pop_removes_and_returns_last_item_from_a_list>`.

----

*********************************************************************************
test_remove_first_time_item_is_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

time for the `remove method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 119
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [0, 1])

      def test_remove(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.remove())


  'remove',

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: list.remove() takes exactly
             one argument (0 given)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a value to the :ref:`call<how to call a function with input>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 123
  :emphasize-lines: 1

          self.assertIsNone(a_list.remove(0))

the test is green again. The `remove method`_ returns :ref:`None<what is None?>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 121
    :emphasize-lines: 4

        def test_remove(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'remove',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [1, 2, 'n'] != [0, 1, 2, 'n']

  the `remove method`_ removes the item given as input, from the list_.

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 124
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 2, 'n'])

  the test passes.

* I change the values in the list_ to see what happens when an item is in there more than one time

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 121
    :emphasize-lines: 2

        def test_remove(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [1, 2, 'n'])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [1, 0, 2, 0, 'n'] != [1, 2, 'n']

* I change the values to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 119
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

  the test passes. The `remove method`_ only removes the first time something shows up in the list_.

* I want to see what happens when I try to remove_ something that is not in the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 119
    :emphasize-lines: 5

        def test_remove(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])
            self.assertIsNone(a_list.remove('not in list'))


    'remove',

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: list.remove(x): x not in list

* I remove the things around the :ref:`call<how to call a function with input>` then add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 121
    :emphasize-lines: 6-7

        def test_remove(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

            with self.assertRaises(ValueError):
                a_list.remove('not in list')


    'remove',

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 119
    :emphasize-lines: 3

            self.assertEqual(a_list, [0, 1])

        def test_remove_first_time_item_is_in_a_list(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))

* I take out remove_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 126

            with self.assertRaises(ValueError):
                a_list.remove('not in list')


    'reverse',
    'sort'

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_remove_first_time_item_is_in_a_list'

:ref:`I know how to remove the first time something is in a list<test_remove_first_time_item_is_in_a_list>`.

----

*********************************************************************************
test_reverse_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for the `reverse method`_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 126
    :emphasize-lines: 4-6

            with self.assertRaises(ValueError):
                a_list.remove('not in list')

        def test_reverse(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.reverse())


    'reverse',

  the `reverse method`_ returns :ref:`None<what is None?>`.

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start:  129
    :emphasize-lines: 2

        def test_reverse(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.reverse())
            self.assertEqual(a_list, [0, 1, 2, 'n'])


    'reverse',

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['n', 2, 1, 0]
                               != [0, 1, 2, 'n']

  the `reverse method`_ reversed the order of the items in the list_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 132
  :emphasize-lines: 1

          self.assertEqual(a_list, ['n', 2, 1, 0])

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 126
    :emphasize-lines: 4

            with self.assertRaises(ValueError):
                a_list.remove('not in list')

        def test_reverse_a_list(self):
            a_list = [0, 1, 2, 'n']

* I remove reverse_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 132

            self.assertEqual(a_list, ['n', 2, 1, 0])


    'sort'


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_reverse_a_list'

:ref:`I know how to reverse a list<test_reverse_a_list>`

----

*********************************************************************************
test_sort_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the `sort method`_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 132
  :emphasize-lines: 3-5

          self.assertEqual(a_list, ['n', 2, 1, 0])

      def test_sort(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.sort())


  'sort'

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python
  :caption: terminal

  TypeError: '<' not supported between instances
             of 'str' and 'int'

I have to change ``'n'`` to a number or change the other numbers to strings_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the things around the call then add :ref:`assertRaises<another way to test if an Exception is raised>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 134
  :emphasize-lines: 3-4

      def test_sort(self):
          a_list = [0, 1, 2, 'n']
          with self.assertRaises(TypeError):
              a_list.sort()


  'sort'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can use the list_ directly in the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 134
    :emphasize-lines: 4

      def test_sort(self):
          a_list = [0, 1, 2, 'n']
          with self.assertRaises(TypeError):
              [0, 1, 2, 'n'].sort()

  the test is still green.

* I remove the :ref:`variable<what is a variable?>` because it is no longer used

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 134
    :emphasize-lines: 2

        def test_sort(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

  still green.

* I add a new list_ that has only numbers, then add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 134
    :emphasize-lines: 5-6

        def test_sort(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

            a_list = [0, 1, 2, 3]
            self.assertIsNone(a_list.sort())


    'sort'

  the test is still green. The `sort method`_ returns :ref:`None<what is None?>` when :ref:`called<how to call a function with input>`.

* I add an :ref:`assertion<what is an assertion?>` to see what the `sort method`_ did to the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 138
    :emphasize-lines: 3

            a_list = [0, 1, 2, 3]
            self.assertIsNone(a_list.sort())
            self.assertEqual(a_list, [])


    'sort'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  the list_ stayed the same.

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 140
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes. The name of the :ref:`method<what is a method?>` is sort_ and I gave it a list_ that is sorted.

* I change the list_ to see what happens when it is NOT sorted

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 134
    :emphasize-lines: 5

        def test_sort(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

            a_list = [0, 1, -1, 2, -2, 3, -3]
            self.assertIsNone(a_list.sort())
            self.assertEqual(a_list, [0, 1, 2, 3])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: [-3, -2, -1, 0, 1, 2, 3]
                               != [0, 1, 2, 3]

  the `sort method`_ changed the order of the list_ from smallest to biggest number.

* I change the expectation of the :ref:`assertion<what is an assertion?>` to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 140
    :emphasize-lines: 1

            self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

  the test passes.

* I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 132
    :emphasize-lines: 3

            self.assertEqual(a_list, ['n', 2, 1, 0])

        def test_sort_a_list(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

* I remove sort_ from the TODO list

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 140

            self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])


    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_sort_a_list'

:ref:`I know how to sort a list<test_sort_a_list>`.

----

*********************************************************************************
test_getting_items_of_a_list
*********************************************************************************

When I want an item that is in a list_, I can give its :ref:`index<test_index_returns_first_position_of_item_in_a_list>` in square brackets(``[]``) to get it.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for getting items of a list_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 140
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

      def test_getting_items_of_a_list(self):
          a_list = ['1st', '2nd', '3rd', '...last']
          self.assertEqual(a_list[0], '')


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: '1st' != ''

the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``0``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the value of the expectation

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 144
  :emphasize-lines: 1

          self.assertEqual(a_list[0], '1st')

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* this is the opposite of the `index method`_ which takes in the item and returns its position, in this case I provide the :ref:`index (position)<test_index_returns_first_position_of_item_in_a_list>` and it returns the item, which means I can write this

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 142
    :emphasize-lines: 4

        def test_getting_items_of_a_list(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list[0], '1st')
            self.assertEqual(a_list[a_list.index('1st')], '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '1st' != ''

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 145
    :emphasize-lines: 1

            self.assertEqual(a_list[a_list.index('1st')], '1st')

  the test passes because

  - ``a_list.index('1st')`` returns ``0``
  - ``a_list[0]`` returns ``1st``

* I can also use negative numbers. The last item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``-1`` and the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of negative the length of the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 145
    :emphasize-lines: 2

            self.assertEqual(a_list[a_list.index('1st')], '1st')
            self.assertEqual(a_list[-4], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '1st' != ''

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 146
    :emphasize-lines: 1

            self.assertEqual(a_list[-4], '1st')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 146
    :emphasize-lines: 2

            self.assertEqual(a_list[-4], '1st')
            self.assertEqual(a_list[2], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '3rd' != ''

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 147
    :emphasize-lines: 1

            self.assertEqual(a_list[2], '3rd')

  the test is green again

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 147
    :emphasize-lines: 2

            self.assertEqual(a_list[2], '3rd')
            self.assertEqual(a_list[-2], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '3rd' != ''

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 148
    :emphasize-lines: 1

            self.assertEqual(a_list[-2], '3rd')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 148
    :emphasize-lines: 2

            self.assertEqual(a_list[-2], '3rd')
            self.assertEqual(a_list[1], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '2nd' != ''

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 149
    :emphasize-lines: 1

            self.assertEqual(a_list[1], '2nd')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 149
    :emphasize-lines: 2

            self.assertEqual(a_list[1], '2nd')
            self.assertEqual(a_list[-3], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '2nd' != ''

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 150
    :emphasize-lines: 1

            self.assertEqual(a_list[-3], '2nd')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 150
    :emphasize-lines: 2

            self.assertEqual(a_list[-3], '2nd')
            self.assertEqual(a_list[3], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '...last' != ''

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 151
    :emphasize-lines: 1

            self.assertEqual(a_list[3], '...last')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 151
    :emphasize-lines: 2

            self.assertEqual(a_list[3], '...last')
            self.assertEqual(a_list[-1], '')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: '...last' != ''

* I make the expectation match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 142
    :emphasize-lines: 11

        def test_getting_items_of_a_list(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list[0], '1st')
            self.assertEqual(a_list[a_list.index('1st')], '1st')
            self.assertEqual(a_list[-4], '1st')
            self.assertEqual(a_list[2], '3rd')
            self.assertEqual(a_list[-2], '3rd')
            self.assertEqual(a_list[1], '2nd')
            self.assertEqual(a_list[-3], '2nd')
            self.assertEqual(a_list[3], '...last')
            self.assertEqual(a_list[-1], '...last')


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_getting_items_of_a_list'

:ref:`I know how to get things that are in a list<test_getting_items_of_a_list>`.

----

*********************************************************************************
test_setting_items_in_a_list
*********************************************************************************

I can also use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of an item in a list_ to change the item.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for setting items in a list_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 152
  :emphasize-lines: 3-8

          self.assertEqual(a_list[-1], '...last')

      def test_setting_items_in_a_list(self):
          a_list = ['1st', '2nd', '3rd', '...last']
          a_list[-1] = '4th'
          self.assertEqual(
              a_list, ['1st', '2nd', '3rd', '...last']
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: ['1st', '2nd', '3rd', '4th']
                             != ['1st', '2nd', '3rd', '...last']

I can use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of an item to change its value in a list_ the way I point a name to a value when I make a :ref:`variable<what is a variable?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation to match the values in the terminal_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 157
    :emphasize-lines: 2

            self.assertEqual(
                a_list, ['1st', '2nd', '3rd', '4th']
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_setting_items_in_a_list'

:ref:`I know how to change the value of an item in a list<test_setting_items_in_a_list>`.

----

*********************************************************************************
test_getting_parts_of_a_list_aka_slicing
*********************************************************************************

I can use :ref:`indices<test_index_returns_first_position_of_item_in_a_list>` to look at parts of a list_, this is called slicing_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for looking at parts of a list_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 157
  :emphasize-lines: 5-7

          self.assertEqual(
              a_list, ['1st', '2nd', '3rd', '4th']
          )

      def test_getting_parts_of_a_list(self):
          a_list = ['a', 'b', 'c', 'd']
          self.assertEqual(a_list[0:2], [])


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: ['a', 'b'] != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 163
  :emphasize-lines: 1

          self.assertEqual(a_list[0:2], ['a', 'b'])

the test passes.

I give two values in square brackets(``[]``), separated by a ``:``

* the first value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to start from
* the second value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to stop at, plus ``1`` because Python_ uses `zero-based indexing`_

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can skip the first number if the starting :ref:`index<test_index_returns_first_position_of_item_in_a_list>` is ``0``

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 161
    :emphasize-lines: 4

        def test_getting_parts_of_a_list(self):
            a_list = ['a', 'b', 'c', 'd']
            self.assertEqual(a_list[0:2], ['a', 'b'])
            self.assertEqual(a_list[:2], [])


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['a', 'b'] != []

* I change the expectation to match

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 164
    :emphasize-lines: 1

            self.assertEqual(a_list[:2], ['a', 'b'])

  the test is green again. ``[0:2]`` and ``[:2]`` are the same.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 164
    :emphasize-lines: 2

            self.assertEqual(a_list[:2], ['a', 'b'])
            self.assertEqual(a_list[1:4], [])


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

* I add the missing values

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 165
    :emphasize-lines: 1

            self.assertEqual(a_list[1:4], ['b', 'c', 'd'])

  the test passes.

* I can skip the second number when it is bigger than or the same as the number of things in the list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 165
    :emphasize-lines: 2

            self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
            self.assertEqual(a_list[1:], [])


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

* I add the missing values

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 166
    :emphasize-lines: 1

            self.assertEqual(a_list[1:], ['b', 'c', 'd'])

  the test passes. ``[1:4]`` and ``[1:]`` are the same because this list_ has 4 things.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 166
    :emphasize-lines: 2

            self.assertEqual(a_list[1:], ['b', 'c', 'd'])
            self.assertEqual(a_list[0:3], [])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['a', 'b', 'c'] != []

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 167
    :emphasize-lines: 1

            self.assertEqual(a_list[0:3], ['a', 'b', 'c'])

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 167
    :emphasize-lines: 2

            self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
            self.assertEqual(a_list[1:3], [])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['b', 'c'] != []

* I change the expectation

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 168
    :emphasize-lines: 1

            self.assertEqual(a_list[1:3], ['b', 'c'])

  the test passes.

* I can also skip the starting and ending numbers

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 168
    :emphasize-lines: 2

            self.assertEqual(a_list[1:3], ['b', 'c'])
            self.assertEqual(a_list[:], [])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    AssertionError: Lists differ: ['a', 'b', 'c', 'd'] != []

  I get the entire list_ back or a :ref:`copy<test_copy_a_list>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 169
    :emphasize-lines: 1

            self.assertEqual(a_list[:], a_list.copy())

  the test passes.

* This is also called slicing_, I change the name of the test

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 157
    :emphasize-lines: 5

            self.assertEqual(
                a_list, ['1st', '2nd', '3rd', '4th']
            )

        def test_getting_parts_of_a_list_aka_slicing(self):
            a_list = ['a', 'b', 'c', 'd']

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'add test_getting_parts_of_a_list_aka_slicing'

:ref:`I know how to look at parts of a list<test_getting_parts_of_a_list_aka_slicing>`.

----

*********************************************************************************
test_index_error
*********************************************************************************

IndexError_ is raised when I try to get an item from a list_ and use a number that points to something that is NOT in the list_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for IndexError_

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 169
  :emphasize-lines: 3-5

          self.assertEqual(a_list[:], a_list.copy())

      def test_index_error(self):
          a_list = ['a', 'b', 'c', 'd']
          a_list[4]


  # Exceptions seen

the terminal_ is my friend, and shows IndexError_

.. code-block:: python
  :caption: terminal

  IndexError: list index out of range

when I use an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` that is greater than or the same as the number of things in the list_, I am pointing to something that is NOT in the list_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add :ref:`assertRaises<another way to test if an Exception is raised>`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 171
  :emphasize-lines: 4-5

      def test_index_error(self):
          a_list = ['a', 'b', 'c', 'd']

          with self.assertRaises(IndexError):
              a_list[4]

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add IndexError_ to the list of :ref:`Exceptions<how to test that an Exception is raised>` seen

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 178
    :emphasize-lines: 5

    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError
    # IndexError

* I get IndexError_ when I use a number that is smaller than the number of things in the list_ as a negative number

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 174
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-5]

  the terminal_ is my friend, and shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add the :ref:`assertRaises method<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 174
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]


    # Exceptions seen

  the test passes.

* IndexError_ is also raised when I call the `pop method`_ with an empty list_

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 174
    :emphasize-lines: 5

            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]
            [].pop()


    # Exceptions seen

  the terminal_ is my friend, and shows IndexError_

  .. code-block:: python

    IndexError: pop from empty list

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 176
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                a_list[-5]
            with self.assertRaises(IndexError):
                [].pop()


    # Exceptions seen

  the test passes.

* I cannot remove the last item from a list_ that has no items, this is the same as trying to get an item from a list_ that has no items

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 178
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                [].pop()
            [][-1]


    # Exceptions seen

  the terminal_ is my friend, and shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add :ref:`assertRaises<another way to test if an Exception is raised>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 178
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                [].pop()
            with self.assertRaises(IndexError):
                [][-1]


    # Exceptions seen

  the test passes. Any :ref:`index<test_index_returns_first_position_of_item_in_a_list>` given to an empty list_ raises IndexError_.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'add test_index_error'

:ref:`I know what causes IndexError<test_index_error>`.

----

*********************************************************************************
test_dir_list with extend and sort
*********************************************************************************

The :ref:`attributes and methods of a list<test_dir_list>` look like the :ref:`attributes and methods of 'object'<test_dir_object>` with extra things, and since they are both lists_, I should be able to make the :ref:`attributes and methods of a list<test_dir_list>` by adding the "extra" to the :ref:`attributes and methods of 'object'<test_dir_object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`variable<what is a variable?>` for the :ref:`attributes and methods of a list<test_dir_list>`, then add an :ref:`assertion<what is an assertion?>` for it, in :ref:`test_dir_list`

.. code-block:: python
  :caption: lists/tests/test_lists.py
  :lineno-start: 10
  :emphasize-lines: 4-11

        def test_dir_list(self):
            self.maxDiff = None

            dir_list = dir(object)
            dir_list.extend((
                'append', 'clear', 'copy',
                'count', 'extend', 'index',
                'insert', 'pop', 'remove',
                'reverse', 'sort',
            ))
            self.assertEqual(dir(list), dir_list)

            self.assertEqual(
                dir(list),
                [
                    '__add__',

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  AssertionError: Lists differ: [
      '__add__', '__class__', '__class_getitem__',[549 chars]ort'
  ] != [
      '__class__', '__delattr__', '__dir__', '__do[370 chars]ort'
  ]

with a note

.. code-block:: python
  :caption: terminal

  First list contains 13 additional elements.

I am close, but not quite.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to :ref:`append<test_append_adds_item_to_end_of_a_list>` the thirteen additional elements

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 14
    :emphasize-lines: 2-7

            dir_list.extend((
                '__add__', '__class_getitem__',
                '__contains__', '__delitem__',
                '__getitem__', '__iadd__',
                '__imul__', '__iter__', '__len__',
                '__mul__', '__reversed__',
                '__rmul__', '__setitem__',
                'append', 'clear', 'copy',
                'count', 'extend', 'index',
                'insert', 'pop', 'remove',
                'reverse', 'sort',
            ))

  the terminal_ does not feel like my friend, it shows :ref:`AssertionError<what causes AssertionError?>`. The details show what I added as missing and as extra. How can it be both? It looks like the problem is the position of the extra items.

* I add a :ref:`call to the sort method<test_sort_a_list>`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 14
    :emphasize-lines: 13

            dir_list.extend((
                '__add__', '__class_getitem__',
                '__contains__', '__delitem__',
                '__getitem__', '__iadd__',
                '__imul__', '__iter__', '__len__',
                '__mul__', '__reversed__',
                '__rmul__', '__setitem__',
                'append', 'clear', 'copy',
                'count', 'extend', 'index',
                'insert', 'pop', 'remove',
                'reverse', 'sort',
            ))
            dir_list.sort()
            self.assertEqual(dir(list), dir_list)

            self.assertEqual(
                dir(list),
                [
                    '__add__',
                    '__class__',

  the test passes, a reminder that :ref:`all objects inherit from 'object'<test_making_an_object_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertion<what is an assertion?>` from :ref:`test_dir_list`

  .. code-block:: python
    :caption: lists/tests/test_lists.py
    :lineno-start: 26

            dir_list.sort()
            self.assertEqual(dir(list), dir_list)

        def test_append_adds_item_to_end_of_a_list(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_dir_list with extend and sort'

:ref:`All objects inherit attributes and methods from 'object'<test_making_an_object_w_object>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_lists.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``lists``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can make a list_ with ``list()`` or square brackets (``[]``), then I ran these tests for the :ref:`methods of lists<test_dir_list>` from append_ to sort_

* :ref:`test_append_adds_item_to_end_of_a_list`
* :ref:`test_clear_empties_a_list`
* :ref:`test_copy_a_list`
* :ref:`test_count_number_of_times_item_is_in_a_list`
* :ref:`test_extend_adds_items_from_an_iterable_to_end_of_a_list`
* :ref:`test_index_returns_first_position_of_item_in_a_list`
* :ref:`test_insert_item_at_position_in_a_list`
* :ref:`test_pop_removes_and_returns_last_item_from_a_list`
* :ref:`test_remove_first_time_item_is_in_a_list`
* :ref:`test_reverse_a_list`
* :ref:`test_sort_a_list`

I also added tests for

* :ref:`getting items of a list<test_getting_items_of_a_list>`
* :ref:`setting items in a list<test_setting_items_in_a_list>`
* :ref:`slicing a list<test_getting_parts_of_a_list_aka_slicing>`
* :ref:`the Exception to know when working with lists (IndexError) <test_index_error>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about lists>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<lists: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.
* :ref:`I know how to use lists<what is a list?>`.

.. toctree::
  :titlesonly:
  :maxdepth: 1

  ../../how_to/make_person/make_person_w_lists
  list_comprehensions

:ref:`Would you like to refactor the attributes of the person object and instance with lists?<test person with lists>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->