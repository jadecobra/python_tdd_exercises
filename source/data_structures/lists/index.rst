.. meta::
  :description: Learn Python lists with this TDD tutorial! Master list methods, indexing, and slicing. Start coding now!
  :keywords: Python lists, Python list methods, Python TDD tutorial, Python list operations, learn Python programming, Python list slicing, Python indexing tutorial, Jacob Itegboje

.. include:: ../../links.rst

.. _more_on_lists: https://docs.python.org/3/tutorial/datastructures.html?highlight=list#more-on-lists
.. _count: more_on_lists_
.. _append: more_on_lists_
.. _append method: more_on_lists_
.. _clear: more_on_lists_
.. _clear method: more_on_lists_
.. _copy: more_on_lists_
.. _copy method: more_on_lists_
.. _pop: more_on_lists_
.. _pop method:
.. _insert: more_on_lists_
.. _insert method: more_on_lists_
.. _index: more_on_lists_
.. _index method: more_on_lists_
.. _remove:
.. _remove method: more_on_lists_
.. _reverse: more_on_lists_
.. _reverse method: more_on_lists_
.. _sort: more_on_lists_
.. _extend: more_on_lists_
.. _extend method: more_on_lists_
.. _list: https://docs.python.org/3/library/stdtypes.html#list
.. _lists: list_
.. _slicing: https://docs.python.org/3/reference/expressions.html#slicings
.. _IndexError: https://docs.python.org/3/library/exceptions.html#IndexError


#################################################################################
lists
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/npXHw5-3C8s?si=K-BDxQG86CoP7rOc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
what is a list?
*********************************************************************************

A list_ is a container :ref:`object<classes>` that can hold any objects_

* they are represented with ``[]``
* they can be made with the list_ constructor_ (``list()``)
* they can be changed with an operation, which means they are mutable

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_lists.py
  :language: python
  :linenos:

*********************************************************************************
questions about lists
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a list?`
* :ref:`how can I add an item to the end of a list?<test_append_adds_item_to_end_of_a_list>`
* :ref:`how can I empty a list?<test_clear_empties_a_list>`
* :ref:`how can I copy a list?<test_copy_a_list>`
* :ref:`how can I count the number of times an item is in a list?<test_count_number_of_times_item_is_in_a_list>`
* :ref:`how can I add items from an iterable to the end of a list?<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`
* :ref:`how can I get the first position of an item in a list?<test_index_returns_first_position_of_item_in_a_list>`
* :ref:`how can I put an item at an index in a list?<test_insert_item_at_given_index_in_a_list>`
* :ref:`how can I remove the last item from a list?<test_pop_removes_and_returns_last_item_from_a_list>`
* :ref:`how can I remove the first time an item is in a lsit<test_remove_first_time_item_is_in_a_list>`
* :ref:`how can I reverse a list?<test_reverse_a_list>`
* :ref:`how can I sort a list?<test_sort_a_list>`
* :ref:`how can I get items of a list?<test_getting_items_of_a_list>`
* :ref:`how can I change an item in a list?<test_setting_items_in_a_list>`
* :ref:`how can I see only parts of a list?<test_looking_at_parts_of_a_list_aka_slicing>`
* :ref:`what causes IndexError?<test_index_error>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``lists``
* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux`_ use

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``type_error`` to the name of this project in ``makePythonTdd.sh``

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir lists
    cd lists
    mkdir src
    touch src/lists.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestLists(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_lists.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: PowerShell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 18

      mkdir lists
      cd lists
      mkdir src
      New-Item src/lists.py
      mkdir tests
      New-Item tests/__init__.py

      "import unittest


      class TestTypeError(unittest.TestCase):

          def test_failure(self):
              self.assertFalse(True)

      # Exceptions seen
      # AssertionError
      " | Out-File tests/test_lists.py

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: tests/test_lists.py:7

    ======================================= FAILURES =======================================
    ________________________________ TestLists.test_failure ________________________________

    self = <tests.test_exceptions.TestLists testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_lists.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_lists.py::TestLists::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_type_error.py:7`` to open it in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_making_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change ``test_failure`` to ``test_making_a_list``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-4


  class TestLists(unittest.TestCase):

      def test_making_a_list(self):
          self.assertEqual(list(), None)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [] != None

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertEqual(list(), [])

the test passes. This is how to make an empty list_

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>`, this time with input to the list_ constructor_, I want to make a list_ that has things in it

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(list(), [])
            self.assertEqual(list(0), [])

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'int' object is not iterable

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # TypeError

* I change the input to a tuple_ (anything in parentheses (``()``), separated by a comma)

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

            self.assertEqual(list(), [])
            self.assertEqual(list((0, 1, 2, 'n')), [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n'] != []

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1

            self.assertEqual(list((0, 1, 2, 'n')), [0, 1, 2, 'n'])

  the test passes.

I can make a list_ with the constructor_ or square brackets(``[]``), which uses less characters

----

*********************************************************************************
test_attributes_and_methods_of_lists
*********************************************************************************

=================================================================================
how to see the the attributes and methods of an object
=================================================================================

I want to test the things I can do with lists_. I can use the dir_ :ref:`function<functions>` to see the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of :ref:`objects<classes>`, it is part of `Python's Built-in Functions`_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 3-7

          self.assertEqual(list(0, 1, 2, 'n'), [0, 1, 2, 'n'])

      def test_attributes_and_methods_of_lists(self):
          self.assertEqual(
              dir(list),
              []
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['__add__', '__class__', '__class_getitem_[552 chars]ort'] != []

there is also a note on how to see the full difference between ``dir(list)`` and my empty list_

.. code-block:: python

  Diff is 748 characters long. Set self.maxDiff to None to see it

`maxDiff`_ is an :ref:`attribute<AttributeError>` of the `unittest.TestCase class`_ that sets the maximum number of characters to show when comparing 2 objects in the terminal_, when it is set to :ref:`None` it shows the full difference

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add ``self.maxDiff`` to the test then move the terminal_ to the right

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

        def test_attributes_and_methods_of_lists(self):
            self.maxDiff = None
            self.assertEqual(
                dir(list),
                []
            )

  the terminal_ shows a long list_ of items. I copy and paste them from the terminal_ then use `find and replace`_ to remove the extra characters

  .. note::

    results can be different because of the Python_ version

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-54

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

  the test passes and I move the terminal_ back to the bottom

* I copy and paste the names that do NOT have double underscores (__) to use as a TODO list

  .. code-block:: python
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


----

*********************************************************************************
test_append_adds_item_to_end_of_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the `append method`_

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 5-7

                    'sort'
                ]
            )

        def test_append(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append())


    'append',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.append() takes exactly one argument (0 given)

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add ``0`` as input

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 1

          self.assertIsNone(a_list.append(0))

the terminal_ shows green, the `append method`_ returns :ref:`None` when called

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` to see what append_ did to the list_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 2

            self.assertIsNone(a_list.append(0))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 0] != [0, 1, 2, 'n']

  the `append method`_ added a value

* I change the expectation to match the values in the terminal_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 0])

  the test passes

* I change the value given to append_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 1

            self.assertIsNone(a_list.append('n+1'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 'n+1'] != [0, 1, 2, 'n', 0]

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 1

        def test_append_adds_item_to_end_of_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.append('n+1'))
            self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

* I remove append_ from the TODO list

  .. code-block:: python
    :lineno-start: 72

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

:ref:`I know how to add things to the end of a list<test_append_adds_item_to_end_of_a_list>`

----

*********************************************************************************
test_clear_empties_a_list
*********************************************************************************

I add a test for the `clear method`_

.. code-block:: python
  :lineno-start: 69
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [0, 1, 2, 'n', 'n+1'])

      def test_clear(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.clear())


  'clear',

the terminal_ shows green. The `clear method`_ returns :ref:`None` when called

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add an :ref:`assertion<what is an assertion?>` to clear_ did to the list_

.. code-block:: python
  :lineno-start: 73
  :emphasize-lines: 2

          self.assertIsNone(a_list.clear())
          self.assertEqual(a_list, [0, 1, 2, 'n'])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [] != [0, 1, 2, 'n']

the list_ is now empty

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the values to match

.. code-block:: python
  :lineno-start: 74
  :emphasize-lines: 1

          self.assertEqual(a_list, [])

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the name of the test to make it "clearer"

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 1

        def test_clear_empties_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.clear())
            self.assertEqual(a_list, [])

* I remove clear_ from the TODO list

  .. code-block:: python
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

:ref:`I know how to empty a list<test_clear_empties_a_list>`

----

*********************************************************************************
test_copy_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another test

.. code-block:: python
  :lineno-start: 74
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [])

      def test_copy(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.copy())


  'copy',

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [0, 1, 2, 'n'] is not None

the :ref:`method<functions>` returns a copy of the list_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the list_ to the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.copy(), [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 'n'] is not None : [0, 1, 2, 'n']

  the values are the same, the problem is assertIsNone_ only takes 1 input and I gave it 2

* I change assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the name of the test

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 1

        def test_copy_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

* I remove copy_ from the TODO list

  .. code-block:: python
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

:ref:`I know how to copy a list<test_copy_a_list>`

----

*********************************************************************************
test_count_number_of_times_item_is_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the next :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 78
  :emphasize-lines: 3-5

          self.assertEqual(a_list.copy(), [0, 1, 2, 'n'])

      def test_count(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.count())


  'extend',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.count() takes exactly one argument (0 given)

I add a value to the call

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 3

      def test_count(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.count(0))

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 1 is not None

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the value

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 1

          self.assertIsNone(a_list.count(0), 1)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 1 is not None : 1

I change assertIsNone_ to assertEqual_

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 1

          self.assertEqual(a_list.count(0), 1)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* ``0`` is in the list_ 1 time, I add ``1`` to the list_ 2 more times then add an :ref:`assertion<what is an assertion?>` for it

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2, 4

        def test_count(self):
            a_list = [0, 1, 2, 1, 'n', 1]
            self.assertEqual(a_list.count(0), 1)
            self.assertEqual(a_list.count(1), 1)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 3 != 1

* I change the value to match

  .. code-block::
    :lineno-start: 83
    :emphasize-lines: 1

            self.assertEqual(a_list.count(1), 3)

  the test passes

* I want to see what happens when I try to count something that is not in the list_

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2

            self.assertEqual(a_list.count(1), 3)
            self.assertEqual(a_list.count('not in list'), 3)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != 3

  The count_ method returns ``0`` when the item is not in the list_

* I change the value to match

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 1

            self.assertEqual(a_list.count('not in list'), 0)

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 1

        def test_count_number_of_times_item_is_in_a_list(self):
            a_list = [0, 2, 1, 2, 3, 2]
            self.assertEqual(a_list.count(0), 1)
            self.assertEqual(a_list.count(2), 3)
            self.assertEqual(a_list.count(9), 0)

* I remove count_ from the TODO list

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 4

            self.assertEqual(a_list.count(9), 0)


    'extend',
    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

:ref:`I know how to count how many times something is in a list<test_count_number_of_times_item_is_in_a_list>`

----

*********************************************************************************
test_extend_adds_items_from_an_iterable_to_end_of_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

time for another test

.. code-block:: python
  :lineno-start: 84
  :emphasize-lines: 3-5

          self.assertEqual(a_list.count('not in list'), 0)

      def test_extend(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.extend())


  'extend',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.extend() takes exactly one argument (0 given)

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I pass a value to the call

.. code-block:: python
  :lineno-start: 88
  :emphasize-lines: 1

          self.assertIsNone(a_list.extend(0))

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: 'int' object is not iterable

I change the value to an iterable_

.. code-block:: python
  :lineno-start: 88
  :emphasize-lines: 1

          self.assertIsNone(a_list.extend((0, 1)))

the test passes. The `extend method`_ returns :ref:`None` when called

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2

            self.assertIsNone(a_list.extend((0, 1)))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 0, 1] != [0, 1, 2, 'n']

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the test passes

* I change the values given to the `extend method`_

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3

        def test_extend(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.extend((2, 1, 0)))
            self.assertEqual(a_list, [0, 1, 2, 'n', 0, 1])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 'n', 2, 1, 0] != [0, 1, 2, 'n', 0, 1]

* I change the values to match

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

  the test is green again, it looks like extend_ calls append_ for each item in the iterable_

* I change the name of the test

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 1

        def test_extend_adds_items_from_an_iterable_to_end_of_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.extend((2, 1, 0)))
            self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

* I remove extend_ from the TODO list

  .. code-block:: python
    :lineno-start: 89

            self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])


    'index',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

:ref:`I know how to add items from an iterable to a list<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`

----

*********************************************************************************
test_index_returns_first_position_of_item_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the `index method`_

.. code-block:: python
  :lineno-start: 89
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [0, 1, 2, 'n', 2, 1, 0])

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.index())


  'index',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: index expected at least 1 argument, got 0

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a value to the call

.. code-block:: python
  :lineno-start: 91
  :emphasize-lines: 3

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.index(0))

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 0 is not None

I add the expectation

.. code-block:: python
  :lineno-start: 93
  :emphasize-lines: 1

          self.assertIsNone(a_list.index(0), 0)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 0 is not None : 0

I change assertIsNone_ to assertEqual_

.. code-block:: python
  :lineno-start: 91
  :emphasize-lines: 3

      def test_index(self):
          a_list = [0, 1, 2, 'n']
          self.assertEqual(a_list.index(0), 0)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* it does not tell me if the :ref:`method<functions>` returned the same value I gave, so I change the list_

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 2

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list.index(0), 0)

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: 0 is not in list

  the index_ :ref:`method<functions>` raises ValueError_ when the item is not in the list_

* I add ValueError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError

* I remove the things around the call and change the value to be clearer

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            a_list.index('not in list')

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: 'not in list' is not in list

* I add assertRaises_ to handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 4,5

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']

            with self.assertRaises(ValueError):
                a_list.index('not in list')

  the test is green again

* I add a new :ref:`assertion<what is an assertion?>`

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

* I change the expectation

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 1

        self.assertEqual(a_list.index('1st'), 0)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 4

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last']
            self.assertEqual(a_list.index('1st'), 0)
            self.assertEqual(a_list.index('3rd'), 0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 2 != 0

* I change the value in the test

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 1

        self.assertEqual(a_list.index('3rd'), 2)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2

          self.assertEqual(a_list.index('3rd'), 2)
          self.assertEqual(a_list.index('2nd'), 2)

          with self.assertRaises(ValueError):
              a_list.index('not in list')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 != 2

* I change the value to match

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 1

            self.assertEqual(a_list.index('2nd'), 1)

  the test is green again

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 2

            self.assertEqual(a_list.index('2nd'), 1)
            self.assertEqual(a_list.index('...last'), 1)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 3 != 1

* I change the value to match the terminal_

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 1

            self.assertEqual(a_list.index('...last'), 3)

  the test passes. The index_ :ref:`method<functions>` returns numbers for the position of the item in the list_. Python_ uses `zero-based indexing`_ which means the first item has an index of ``0`` and the last item has an index of the length of the list_ minus ``1``

* I want to know what happens when I have the same item in the list_ more than once, so I add something in the list_ again

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 2

        def test_index(self):
            a_list = ['1st', '2nd', '3rd', '...last', '1st']

  the terminal_ still shows green

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

            self.assertEqual(a_list.index('...last'), 3)
            self.assertEqual(a_list.index('1st'), 4)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != 4

  when I first called the index_ :ref:`method<functions>`, the terminal_ showed :ref:`TypeError`

  .. code-block:: shell

    TypeError: index expected at least 1 argument, got 0

* I add a second argument

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 1

            self.assertEqual(a_list.index('1st', 0), 4)

  the terminal_ still shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 != 4

* I change the argument

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 1

    self.assertEqual(a_list.index('1st', 1), 4)

  the test passes, the second input is the position I want the :ref:`method<functions>` to start from

* I try the same thing with the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 91
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

* I change the name of the test

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 1

    def test_index_returns_first_position_of_item_in_a_list(self):
        a_list = ['1st', '2nd', '3rd', '...last', '1st']

* I also remove index_ from the TODO list

  .. code-block:: python
    :lineno-start: 5

            with self.assertRaises(ValueError):
                a_list.index('not in list')


    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'

:ref:`I know how to find the position of something in a list<test_index_returns_first_position_of_item_in_a_list>`

----

*********************************************************************************
test_insert_item_at_given_index_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the next :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 99
  :emphasize-lines: 4-6

          with self.assertRaises(ValueError):
              a_list.index('not in list')

      def test_insert(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.insert())


  'insert',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: insert expected 2 arguments, got 0

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add two values to the call

.. code-block:: python
  :lineno-start: 102
  :emphasize-lines: 3

      def test_insert(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.insert(0, 1))

the test passes. What did the `insert method`_ do to the list_?

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`assertion<what is an assertion?>` to find out

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 2

            self.assertIsNone(a_list.insert(0, 1))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 0, 1, 2, 'n'] != [0, 1, 2, 'n']

  there is an extra value at the beginning of the list_

* I add the new value to the expectation

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 0, 1, 2, 'n'])

  the test passes.

  The `insert method`_

  - puts the second input given at the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the list_ given as the first input
  - it also moves the original items from that :ref:`index<test_index_returns_first_position_of_item_in_a_list>` and after in the list_ to the right

* I change the second input in the call

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 3

        def test_insert(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.insert(0, -1))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-1, 0, 1, 2, 'n'] != [1, 0, 1, 2, 'n']

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 1

            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the test is green again

* I add another :ref:`assertion<what is an assertion?>` to see what happens when I insert_ an item in the middle of the list_

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 2

            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
            self.assertIsNone(a_list.insert(3, 1.5))

  the terminal_ shows green

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the list

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2

            self.assertIsNone(a_list.insert(3, 1.5))
            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-1, 0, 1, 1.5, 2, 'n'] != [-1, 0, 1, 2, 'n']

* I add the value to the expectation

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 1

            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

  the test passes, it moved everything in the list_ from the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` I gave and after to the right

* I change the name of the test

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 1

        def test_insert_item_at_given_index_in_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.insert(0, -1))
            self.assertEqual(a_list, [-1, 0, 1, 2, 'n'])
            self.assertIsNone(a_list.insert(3, 1.5))
            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

    'insert',

* I remove insert_ from the TODO list

  .. code-block:: python
    :lineno-start: 107

            self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])


    'pop',
    'remove',
    'reverse',
    'sort'

:ref:`I know how to put an item at a position in a list<test_insert_item_at_given_index_in_a_list>`

----

*********************************************************************************
test_pop_removes_and_returns_last_item_from_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test

.. code-block:: python
  :lineno-start: 107
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [-1, 0, 1, 1.5, 2, 'n'])

      def test_pop(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.pop())


  'pop',

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'n' is not None

The pop_ :ref:`method<functions>` returns the last item in the list_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the expectation

.. code-block:: python
  :lineno-start: 111
  :emphasize-lines: 1

          self.assertIsNone(a_list.pop(), 'n')

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'n' is not None : n

I change assertIsNone_ to assertEqual_

.. code-block:: python
  :lineno-start: 109
  :emphasize-lines: 3

      def test_pop(self):
          a_list = [0, 1, 2, 'n']
          self.assertEqual(a_list.pop(), 'n')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` to see what happened to the list_

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2

            self.assertEqual(a_list.pop(), 'n')
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2] != [0, 1, 2, 'n']

* I change the values in the test to match

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2])

  the test passes

* I add another :ref:`assertion<what is an assertion?>` with the `pop method`_

  .. code-block:: python

            self.assertEqual(a_list, [0, 1, 2])
            self.assertEqual(a_list.pop(), 'n')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 2 != 'n'

* I change the value in the expectation

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 1

            self.assertEqual(a_list.pop(), 2)

  the test passes

* I add another :ref:`assertion<what is an assertion?>` to see what changed in the list_

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2

            self.assertEqual(a_list.pop(), 2)
            self.assertEqual(a_list, [0, 1, 2])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1] != [0, 1, 2]

* I change the values in the test to match

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1])

  the test passes

* I change the name of the test

  .. code-block:: python
    :emphasize-lines: 1

        def test_pop_removes_and_returns_last_item_from_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertEqual(a_list.pop(), 'n')
            self.assertEqual(a_list, [0, 1, 2])
            self.assertEqual(a_list.pop(), 2)
            self.assertEqual(a_list, [0, 1])


    'pop',

* I take out pop_ from the TODO list

  .. code-block:: python
    :lineno-start: 114

            self.assertEqual(a_list, [0, 1])


    'remove',
    'reverse',
    'sort'

:ref:`I know how to get and remove the last item in a list<test_pop_removes_and_returns_last_item_from_a_list>`

----

*********************************************************************************
test_remove_first_time_item_is_in_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

time for the next :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 114
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [0, 1])

      def test_remove(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.remove())


  'remove',

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.remove() takes exactly one argument (0 given)

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a value to the call

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 1

          self.assertIsNone(a_list.remove(0))

the terminal_ shows green. The remove_ :ref:`method<functions>` returns :ref:`None`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 2

            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 2, 'n'] != [0, 1, 2, 'n']

  the :ref:`method<functions>` removes the item given from the list_

* I change the expectation

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 2, 'n'])

  the test passes

* I change the values in the list_ to see what happens when an item is in there more than one time

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 2

        def test_remove(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 0, 2, 0, 'n'] != [1, 2, 'n']

* I change the values to match

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 1

            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

  the test passes. The `remove method`_ only removes the first time something shows up in the list

* I want to see what happens when I try to remove_ something that is not in the list_

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 2

            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])
            self.assertIsNone(a_list.remove('not in list'))

  the terminal_ shows ValueError_

  .. code-block:: shell

    ValueError: list.remove(x): x not in list

* I remove the things around the call then add assertRaises_

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 3-4

            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

            with self.assertRaises(ValueError):
                a_list.remove('not in list')


    'remove',

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 1

        def test_remove_first_time_item_is_in_a_list(self):
            a_list = [0, 1, 0, 2, 0, 'n']
            self.assertIsNone(a_list.remove(0))
            self.assertEqual(a_list, [1, 0, 2, 0, 'n'])

            with self.assertRaises(ValueError):
                a_list.remove('not in list')


    'remove'

* I take out remove_ from the TODO list

  .. code-block:: python
    :lineno-start: 121

            with self.assertRaises(ValueError):
                a_list.remove('not in list')


    'reverse',
    'sort'

:ref:`I know how to remove the first time something is in a list<test_remove_first_time_item_is_in_a_list>`

----

*********************************************************************************
test_reverse_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add the next test

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 4-6

            with self.assertRaises(ValueError):
                a_list.remove('not in list')

        def test_reverse(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.reverse())


    'reverse',

  the terminal_ shows green. The `reverse method`_ returns :ref:`None`.

* I add an :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :lineno-start:  126
    :emphasize-lines: 2

            self.assertIsNone(a_list.reverse())
            self.assertEqual(a_list, [0, 1, 2, 'n'])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['n', 2, 1, 0] != [0, 1, 2, 'n']

  it reversed the order of the items in the list_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation

.. code-block:: python
  :lineno-start: 127
  :emphasize-lines: 1

          self.assertEqual(a_list, ['n', 2, 1, 0])

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I change the name of the test

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 1

        def test_reverse_a_list(self):
            a_list = [0, 1, 2, 'n']
            self.assertIsNone(a_list.reverse())
            self.assertEqual(a_list, ['n', 2, 1, 0])


    'reverse',

* I remove the name from the TODO list

  .. code-block:: python
    :lineno-start: 127

            self.assertEqual(a_list, ['n', 2, 1, 0])


    'sort'


    # Exceptions seen

:ref:`I know how to reverse a list<test_reverse_a_list>`

----

*********************************************************************************
test_sort_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the last :ref:`method<functions>` in the TODO list

.. code-block:: python
  :lineno-start: 127
  :emphasize-lines: 3-5

          self.assertEqual(a_list, ['n', 2, 1, 0])

      def test_sort(self):
          a_list = [0, 1, 2, 'n']
          self.assertIsNone(a_list.sort())


  'sort'

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: '<' not supported between instances of 'str' and 'int'

I have to change ``'n'`` to a number or change the other numbers to a string_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the things around the call then add assertRaises_

.. code-block:: python
  :lineno-start: 129
  :emphasize-lines: 3-4

      def test_sort(self):
          a_list = [0, 1, 2, 'n']
          with self.assertRaises(TypeError):
              a_list.sort()

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I remove the :ref:`variable<test_attribute_error_w_variables>` because it is not used, I can use the list_ directly

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 2-3

        def test_sort(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

  the test is still green

* I add a new list_ where all the items are numbers and another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :emphasize-lines: 5,6

        def test_sort(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

            a_list = [0, 1, 2, 3]
            self.assertIsNone(a_list.sort())

  the terminal_ still shows green, sort_ returns :ref:`None` when called

* I add another :ref:`assertion<what is an assertion?>` to see what it did to the list_

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 3

            a_list = [0, 1, 2, 3]
            self.assertIsNone(a_list.sort())
            self.assertEqual(a_list, [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  the list_ stayed the same

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes. The name of the :ref:`method<functions>` is sort_ and I gave it a list_ that is sorted

* I change the list_ to see what happens when it is not sorted

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 1

            a_list = [0, 1, -1, 2, -2, 3, -3]
            self.assertIsNone(a_list.sort())
            self.assertEqual(a_list, [0, 1, 2, 3])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [-3, -2, -1, 0, 1, 2, 3] != [0, 1, 2, 3]

  the sort_ :ref:`method<functions>` arranged the list_ in ascending order

* I change the values to match

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 1

            self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

  the test passes

* I change the name of the test

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 1

        def test_sort_a_list(self):
            with self.assertRaises(TypeError):
                [0, 1, 2, 'n'].sort()

            a_list = [0, 1, -1, 2, -2, 3, -3]
            self.assertIsNone(a_list.sort())
            self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])


    'sort'

* I remove sort_ from the TODO list

  .. code-block:: python
    :lineno-start: 135

            self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])


    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError

:ref:`I know how to sort a list<test_sort_a_list>`

----

*********************************************************************************
test_getting_items_of_a_list
*********************************************************************************

When I want an item that is in a list_, I can give its :ref:`index<test_index_returns_first_position_of_item_in_a_list>` in square brackets(``[]``)

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test to show what I mean

.. code-block:: python
  :lineno-start: 135
  :emphasize-lines: 3-5

          self.assertEqual(a_list, [-3, -2, -1, 0, 1, 2, 3])

      def test_getting_items_of_a_list(self):
          a_list = ['1st', '2nd', '3rd', '...last']
          self.assertEqual(a_list[0], '')


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '1st' != ''

the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``0``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the value in the test

.. code-block:: python
  :lineno-start: 139
  :emphasize-lines: 1

          self.assertEqual(a_list[0], '1st')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* this is the opposite of the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` :ref:`method<functions>` which takes in the item and returns its position, in this case I provide the :ref:`index (position)<test_index_returns_first_position_of_item_in_a_list>` and it returns the item, which means I can write this

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 2

            self.assertEqual(a_list[0], '1st')
            self.assertEqual(a_list[a_list.index('1st')], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '1st' != ''

  I change the value to match

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 1

            self.assertEqual(a_list[a_list.index('1st')], '1st')

  the test passes

* I can also use negative numbers. The last item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of ``-1`` and the first item has an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of negative the length of the list_

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 2

            self.assertEqual(a_list[a_list.index('1st')], '1st')
            self.assertEqual(a_list[-4], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '1st' != ''

  I change the value to match

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 1

            self.assertEqual(a_list[-4], '1st')

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 2

            self.assertEqual(a_list[-4], '1st')
            self.assertEqual(a_list[2], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '3rd' != ''

  I change the expectation to match

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 1

            self.assertEqual(a_list[2], '3rd')

  the terminal_ shows green again

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 2

            self.assertEqual(a_list[2], '3rd')
            self.assertEqual(a_list[-2], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '3rd' != ''

  I change the expectation

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 1

            self.assertEqual(a_list[-2], '3rd')

  the test passes

* I add another line

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 2

            self.assertEqual(a_list[-2], '3rd')
            self.assertEqual(a_list[1], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '2nd' != ''

  I change the expectation

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 1

            self.assertEqual(a_list[1], '2nd')

* I add another

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 2

            self.assertEqual(a_list[1], '2nd')
            self.assertEqual(a_list[-3], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '2nd' != ''

  I change the value

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 1

            self.assertEqual(a_list[-3], '2nd')

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 2

            self.assertEqual(a_list[-3], '2nd')
            self.assertEqual(a_list[3], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '...last' != ''

  I change the value

  .. code-block:: python
    :lineno-start: 146
    :emphasize-lines: 1

            self.assertEqual(a_list[3], '...last')

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 146
    :emphasize-lines: 2

            self.assertEqual(a_list[3], '...last')
            self.assertEqual(a_list[-1], '')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: '...last' != ''

  I make the values match

  .. code-block:: python
    :lineno-start: 137
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

  the test passes

:ref:`I know how to get things that are in a list<test_getting_items_of_a_list>`

----

*********************************************************************************
test_setting_items_in_a_list
*********************************************************************************

I can also use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of an item in a list_ to change the item

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add an :ref:`assertion<what_is_an_assertion?>`

.. code-block:: python
  :lineno-start: 147
  :emphasize-lines: 3-6

          self.assertEqual(a_list[-1], '...last')

      def test_setting_items_in_a_list(self):
          a_list = ['1st', '2nd', '3rd', '...last']
          a_list[-1] = '4th'
          self.assertEqual(a_list, ['1st', '2nd', '3rd', '...last'])


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['1st', '2nd', '3rd', '4th'] != ['1st', '2nd', '3rd', '...last']

I can use the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of an item to change its value in a list_, the way I point a name to a value when I make a :ref:`variable<what is a variable?>`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match the values in the terminal_

.. code-block:: python
  :lineno-start: 152
  :emphasize-lines: 1

          self.assertEqual(a_list, ['1st', '2nd', '3rd', '4th'])

the test passes. :ref:`I know how to change the value of an item in a list<test_setting_items_in_a_list>`

----

*********************************************************************************
test_looking_at_parts_of_a_list_aka_slicing
*********************************************************************************

I can use :ref:`indices<test_index_returns_first_position_of_item_in_a_list>` to look at parts of a list_, this is called slicing_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another test

.. code-block:: python
  :lineno-start: 152
  :emphasize-lines: 3-5

            self.assertEqual(a_list, ['1st', '2nd', '3rd', '4th'])

        def test_looking_at_parts_of_a_list(self):
            a_list = ['a', 'b', 'c', 'd']
            self.assertEqual(a_list[0:2], [])


    # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: ['a', 'b'] != []

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the values to match

.. code-block:: python
  :lineno-start: 156
  :emphasize-lines: 1

          self.assertEqual(a_list[0:2], ['a', 'b'])

the test passes.

I give two values in square brackets(``[]``), separated by a ``:``, the first value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to start from, and the second value is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the item I want to stop at plus ``1``

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I can skip the first number when the starting :ref:`index<test_index_returns_first_position_of_item_in_a_list>` is ``0``

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 2

            self.assertEqual(a_list[0:2], ['a', 'b'])
            self.assertEqual(a_list[:2], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b'] != []

  I change the values to match

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 1

            self.assertEqual(a_list[:2], ['a', 'b'])

  the terminal_ shows green again. ``[0:2]`` and ``[:2]`` are the same

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 2

            self.assertEqual(a_list[:2], ['a', 'b'])
            self.assertEqual(a_list[1:4], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

  I add the missing values

  .. code-block:: python

    self.assertEqual(a_list[1:4], ['b', 'c', 'd'])

  the test passes

* I can skip the second number when it is bigger than or the same as the number of things in the list_

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 2

            self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
            self.assertEqual(a_list[1:], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c', 'd'] != []

  I add the missing values

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 1

            self.assertEqual(a_list[1:], ['b', 'c', 'd'])

  the test passes. ``[1:4]`` and ``[1:]`` are the same because this list_ has 4 things

* I add another line

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 2

            self.assertEqual(a_list[1:], ['b', 'c', 'd'])
            self.assertEqual(a_list[0:3], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b', 'c'] != []

  I change the expectation

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 1

            self.assertEqual(a_list[0:3], ['a', 'b', 'c'])

  the test passes

* I add another

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 2

            self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
            self.assertEqual(a_list[1:3], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['b', 'c'] != []

  I change the expectation

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 1

            self.assertEqual(a_list[1:3], ['b', 'c'])

  the test is green again

* I can also skip both numbers

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 2

            self.assertEqual(a_list[1:3], ['b', 'c'])
            self.assertEqual(a_list[:], [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: ['a', 'b', 'c', 'd'] != []

  I get the entire list_ back or a :ref:`copy<test_copy_a_list>`

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 1

            self.assertEqual(a_list[:], a_list.copy())

  the test is green again

* This is also called slicing_, I change the name of the test

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 1

        def test_looking_at_parts_of_a_list_aka_slicing(self):
            a_list = ['a', 'b', 'c', 'd']
            self.assertEqual(a_list[0:2], ['a', 'b'])
            self.assertEqual(a_list[:2], ['a', 'b'])
            self.assertEqual(a_list[1:4], ['b', 'c', 'd'])
            self.assertEqual(a_list[1:], ['b', 'c', 'd'])
            self.assertEqual(a_list[0:3], ['a', 'b', 'c'])
            self.assertEqual(a_list[1:3], ['b', 'c'])
            self.assertEqual(a_list[:], a_list.copy())


    # Exceptions seen

----

*********************************************************************************
test_index_error
*********************************************************************************

IndexError_ is raised when I try to get an item from a list_ but use a number that points to something that is NOT in it. When I see this :ref:`Exception<errors>` I know the underlying data structure is a list_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 162
  :emphasize-lines: 3-5

          self.assertEqual(a_list[:], a_list.copy())

      def test_index_error(self):
          a_list = ['a', 'b', 'c', 'd']
          a_list[4]


  # Exceptions seen

the terminal_ shows IndexError_

.. code-block:: shell

  IndexError: list index out of range

when I use an :ref:`index<test_index_returns_first_position_of_item_in_a_list>` that is greater than or the same as the number of things in the list_, I am pointing to something that is NOT in the list_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 164
  :emphasize-lines: 4-5

  def test_index_error(self):
      a_list = ['a', 'b', 'c', 'd']

      with self.assertRaises(IndexError):
          a_list[4]

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add IndexError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :emphasize-lines: 5

    # Exceptions seen
    # AssertionError
    # TypeError
    # ValueError
    # IndexError

* I get IndexError_ when I use a negative number that is smaller than the number of things in the list_ as a negative number

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-5]

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]


    # Exceptions seen

  the test passes

* IndexError_ is also raised when I call the `pop method`_ with an empty list_

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 5

            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]
            [].pop()

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: pop from empty list

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 169
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                a_list[-5]
            with self.assertRaises(IndexError):
                [].pop()

  the terminal_ shows green

* I cannot remove the last item from a list_ that has no items, this is like trying to get an item from a list_ that has no items

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                [].pop()
            [][-1]

  the terminal_ shows IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                [].pop()
            with self.assertRaises(IndexError):
                [][-1]

  the test passes. Any :ref:`index<test_index_returns_first_position_of_item_in_a_list>` given to an empty list_ raises IndexError_

:ref:`I know what causes IndexError<test_index_error>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_lists.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

.. NOTE:: on Windows_ without `Windows Subsystem for Linux`_

  * the terminal_ shows

    .. code-block:: shell

      (.venv) ...\pumping_python\lists

  * I deactivate the `virtual environment`_

    .. code-block:: shell
      :emphasize-lines: 1

      deactivate

    the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

    .. code-block:: shell

      ...\pumping_python\lists

  * I `change directory`_ to the parent of ``lists``

    .. code-block:: shell
      :emphasize-lines: 1

      cd ..

    the terminal_ shows

    .. code-block:: shell

      ...\pumping_python

    I am back in the ``pumping_python`` directory_

----

*********************************************************************************
test_calculator_sends_message_when_input_is_a_list
*********************************************************************************

I want to see what happens when I send a list_ as input to the :ref:`calculator program<how to make a calculator>`, will it send a message or raise :ref:`TypeError`?

=================================================================================
open the project
=================================================================================

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I use ``pytest-watch`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 5 items

    tests/test_calculator.py ....                                        [100%]

    ============================ 5 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to see what happens when I send a list_ as input

.. code-block:: python
  :lineno-start: 88
  :emphasize-lines: 6-7, 9-12

          self.assertEqual(
              src.calculator.subtract('1', '1'),
              error_message
          )

      def test_calculator_sends_message_when_input_is_a_list(self):
          a_list = [0, 1, 2, 3]

          self.assertEqual(
              src.calculator.add(a_list, 0),
              'BOOM!!!'
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BOOM!!!'

=================================================================================
:green:`green`: make it pass
=================================================================================

I change the expectation to match

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(a_list, 0),
              'Excuse me?! I only work with numbers. Please try again...'
          )

the test passes

=================================================================================
:yellow:`refactor`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` for the next :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(a_list, 0),
                'Excuse me?! I only work with numbers. Please try again...'
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                'BAP!!!'
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BAP!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(a_list, 1),
                'Excuse me?! I only work with numbers. Please try again...'
            )

  the test passes. Wait a minute! I just wrote the same thing twice, and I did it 8 times before in :ref:`test_calculator_sends_message_when_input_is_not_a_number` and 2 times in the ``only_takes_numbers`` :ref:`function<functions>`, never again

* I add a :ref:`variable<what is a variable?>` to remove the repetition

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3, 7, 11

        def test_calculator_sends_message_when_input_is_a_list(self):
            a_list = [0, 1, 2, 3]
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )

  the test is still green

---------------------------------------------------------------------------------
how to multiply a list
---------------------------------------------------------------------------------

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                'BOOM!!!'
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 3, 0, 1, 2, 3] != 'BOOM!!!'

  :ref:`I know how to multiply a list<how to multiply a list>`

* I change the expectation of the test to the error message

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3] != 'Excuse me?! I only work with numbers. Please try again...'

* I add an :ref:`if statement<if statements>` to the ``only_takes_numbers`` :ref:`function<functions>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-13

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if isinstance(first_input, str) or isinstance(second_input, str):
                return error_message
            if isinstance(first_input, list) or isinstance(second_input, list):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  the test passes. The ``only_takes_numbers`` :ref:`function<functions>` looks ugly now, there has to be a better way

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>` to ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                'BOOM!!!'
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BOOM!!!'

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )

  the test passes

* I remove the name of the test to move the new :ref:`assertions<what is an assertion?>` to ``test_calculator_sends_message_when_input_is_not_a_number``

  .. code-block:: python
    :lineno-start: 88

            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

            a_list = [0, 1, 2, 3]
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )


    # Exceptions seen

  the tests are still green

* I remove the duplication of the ``error_message`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 88

            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

            a_list = [0, 1, 2, 3]

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )

  still green. This test looks long, there has to be :ref:`a better way to test the calculator with inputs that are NOT numbers<lists: list comprehensions>`

----

*********************************************************************************
how to test if something is an instance of more than one type
*********************************************************************************

The `isinstance function`_ can take a tuple_ as the second input, which allows me to check if the first input is an instance of any of the :ref:`objects<classes>` in the tuple_

* I add a :ref:`variable<what is a variable?>` to the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 5-8, 11-12

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            bad_types = (str, list)
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            # if isinstance(first_input, str) or isinstance(second_input, str):
            #     return error_message
            # if isinstance(first_input, list) or isinstance(second_input, list):
            #     return error_message

            if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  the tests are still green

* I remove the comments

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            bad_types = (str, list)
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  still green

* I could write :ref:`Logical Negation (NOT)<test_logical_negation_aka_not>` to test only the types of numbers the :ref:`calculator<how to make a calculator>` can handle

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 7-8, 10-16

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            bad_types = (str, list)
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            # if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
            #     return error_message

            if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still green

* I remove the comments and the ``bad_types`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still passing

* "not_" happens twice in the `if statement<if statements>`, I write the line in terms of it

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

            # if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
            if (not isinstance(first_input, good_types)) (not and) ((not isinstance(second_input, good_types))):
                return error_message

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 7

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError
    # SyntaxError

* I fix the `if statement<if statement>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

            # if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
            # if (not isinstance(first_input, good_types)) (not and) ((not isinstance(second_input, good_types))):
            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
                return error_message

  the test is green again

* I remove the comments

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  all the tests are still passing. I wonder if there is a way to write this :ref:`function<functions>` with only one `return statement`_ for the error message

----

*********************************************************************************
test_calculator_w_list_items
*********************************************************************************

I can use a list_ to test the :ref:`calculator functions<how to make a calculator>` as long as its items are numbers

=================================================================================
:red:`red`: make it fail
=================================================================================

I add a new test to use the :ref:`index of the items in the list<test_index_returns_first_position_of_item_in_a_list>` to test the :ref:`calculator<how to make a calculator>`

.. code-block:: python
  :lineno-start: 107
  :emphasize-lines: 5-6, 7-10

            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )

        def test_calculator_w_list_items(self):
            a_list = [self.random_first_number, self.random_second_number]

            self.assertEqual(
                src.calculator.add(a_list[0], a_list[1]),
                self.random_first_number-self.random_second_number
            )


    # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: ABC.DEFGHIJKLMNOPQ != RST.UVWXYZABCDEFG

=================================================================================
:green:`green`: make it pass
=================================================================================

I change the expectation to the right calculation

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(a_list[0], a_list[1]),
              self.random_first_number+self.random_second_number
          )

the test passes

=================================================================================
:yellow:`refactor`: make it better
=================================================================================

* I add an :ref:`assertion<what is an assertion>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(a_list[0], a_list[1]),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(a_list[-2], a_list[-1]),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: D.EFGHIJKLMNOPQRST != UVWXY.ZABCDEFGHIJ

* I change the calculation

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3

          self.assertEqual(
              src.calculator.divide(a_list[-2], a_list[-1]),
              self.random_first_number/self.random_second_number
          )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(a_list[-2], a_list[-1]),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(a_list[1], a_list[-1]),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: EFGHIJ.KLMNOPQRSTU != VWXYZ.ABCDEFGHIJKL

* I change the expectation

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(a_list[1], a_list[-1]),
                self.random_second_number*self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(a_list[1], a_list[-1]),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(a_list[-2], a_list[0]),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.0 != FGH.IJKLMNOPQRSTU

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(a_list[-2], a_list[0]),
                self.random_first_number-self.random_first_number
            )

  the test passes

* Python_ allows me use a star expression like I did in :ref:`test_functions_w_unknown_arguments`. I add an :ref:`assertion<what is an assertion?>` with it

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.subtract(a_list[-2], a_list[0]),
                self.random_first_number-self.random_first_number
            )
            self.assertEqual(
                src.calculator.add(*a_list),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: GHI.JKLMNOPQRSTUVW != XYZ.ABCDEFGHIJKLMN

* I change the expectation

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(*a_list),
                self.random_first_number+self.random_second_number
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(*a_list),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(*a_list),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: H.IJKLMNOPQRSTUVWX != YZABCD.EFGHIJKLMNO

* I change the calculation

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(*a_list),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(*a_list),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(*a_list),
                self.random_first_number/self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: IJKLMN.OPQRSTUVWX != Y.ZABCDEFGHIJKLMNOP

* I change the calculation

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(*a_list),
                self.random_first_number*self.random_second_number
            )

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(*a_list),
                self.random_first_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(*a_list),
                self.random_first_number+self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: JKL.MNOPQRSTUVWXYZ != ABC.DEFGHIJKLMNOP

* I change the expectation

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(*a_list),
                self.random_first_number-self.random_second_number
            )

  the test passes

It is important to note that the star expression always gives the items from the list in order, and I cannot use a list_ that has more than 2 items with the :ref:`calculator functions<how to make a calculator>`

*********************************************************************************
test_calculator_raises_type_error_when_given_more_than_two_inputs
*********************************************************************************

* I add a new test to show the problem when I have more than 2 inputs and use a star expression

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 6-7, 9

            self.assertEqual(
                src.calculator.subtract(*a_list),
                self.random_first_number-self.random_second_number
            )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            another_list = [0, 1, 2]

            src.calculator.add(*another_list)


    # Exceptions seen

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I add the `assertRaises method`_ to handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 4-5

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            another_list = [0, 1, 2]

            with self.assertRaises(TypeError):
                src.calculator.add(*another_list)

  the test passes

* I add a failing line for :ref:`division<test_division>` with the new list_

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.add(*another_list)
            src.calculator.divide(*another_list)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.add(*another_list)
            with self.assertRaises(TypeError):
                src.calculator.divide(*another_list)

    the test passes

* I add a line for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide(*another_list)
            src.calculator.multiply(*another_list)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide(*another_list)
            with self.assertRaises(TypeError):
                src.calculator.multiply(*another_list)

  the test passes

* I add the last line

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply(*another_list)
            src.calculator.subtract(*another_list)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 10-11

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            another_list = [0, 1, 2]

            with self.assertRaises(TypeError):
                src.calculator.add(*another_list)
            with self.assertRaises(TypeError):
                src.calculator.divide(*another_list)
            with self.assertRaises(TypeError):
                src.calculator.multiply(*another_list)
            with self.assertRaises(TypeError):
                src.calculator.subtract(*another_list)

  the test passes

----

=================================================================================
close the project
=================================================================================

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/calculator

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can make a list_ with the constructor_ or square brackets (``[]``), then I ran the following tests for the :ref:`methods of lists<test_attributes_and_methods_of_lists>` from append_ to sort_

* :ref:`test_append_adds_item_to_end_of_a_list`
* :ref:`test_clear_empties_a_list`
* :ref:`test_copy_a_list`
* :ref:`test_count_number_of_times_item_is_in_a_list`
* :ref:`test_extend_adds_items_from_an_iterable_to_end_of_a_list`
* :ref:`test_index_returns_first_position_of_item_in_a_list`
* :ref:`test_insert_item_at_given_index_in_a_list`
* :ref:`test_pop_removes_and_returns_last_item_from_a_list`
* :ref:`test_remove_first_time_item_is_in_a_list`
* :ref:`test_reverse_a_list`
* :ref:`test_sort_a_list`

I also added tests for

* :ref:`getting items of a list<test_getting_items_of_a_list>`
* :ref:`setting items in a list<test_setting_items_in_a_list>`
* :ref:`slicing a list<test_looking_at_parts_of_a_list_aka_slicing>`
* :ref:`the Exception to know when working with lists (IndexError) <test_index_error>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about lists>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: lists: tests and solutions>`

----

*********************************************************************************
what is next?
*********************************************************************************

you know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what None is<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`how to make the calculator check if its inputs are numbers<test_calculator_sends_message_when_input_is_not_a_number>`
* :ref:`what you can do with Lists<lists>`

:ref:`Would you like to test list comprehensions?<lists: list comprehensions>` They are a quick way to make :ref:`lists`

-----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->