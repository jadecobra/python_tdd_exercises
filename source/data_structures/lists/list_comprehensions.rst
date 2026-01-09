.. meta::
  :description: Master Python list comprehensions with this hands-on TDD tutorial. Learn to create lists efficiently with code examples. Start coding now!
  :keywords: Jacob Itegboje, Python list comprehensions, test-driven development, Python programming, coding tutorials, data structures, Python for beginners

.. include:: ../../links.rst

.. _list comprehension: https://docs.python.org/3/glossary.html#term-list-comprehension
.. _list comprehensions: https://docs.python.org/3/glossary.html#term-list-comprehension
.. _range: https://docs.python.org/3/library/stdtypes.html?highlight=range#range
.. _range object: range_
.. _filter: https://docs.python.org/3/library/functions.html#filter
.. _filter object: filter_
.. _filterfalse: https://docs.python.org/3/library/itertools.html#itertools.filterfalse
.. _filterfalse method: filterfalse_
.. _itertools module: https://docs.python.org/3/library/itertools.html
.. _map: https://docs.python.org/3/library/functions.html#map
.. _map object: map_
.. _tell the difference between test iterations: https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests
.. _unittest.TestCase.subTest method: https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest

#################################################################################
lists: list comprehensions
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube.com/embed/ydGHVab_YpY?si=a9D0VufncC4jlzte" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
what is a list comprehension?
*********************************************************************************

A `List Comprehension`_ is a simple way to make a :ref:`list <lists>` from an :ref:`iterable<what is an iterable?>` with one line

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_list_comprehensions.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``list_comprehensions``
* I open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux`_ use

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``lists`` to the name of this project in ``makePythonTdd.sh``

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2, 3, 5, 12, 20

    #!/bin/bash
    mkdir list_comprehensions
    cd list_comprehensions
    mkdir src
    touch src/list_comprehensions.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestListComprehensions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError
    " > tests/test_list_comprehensions.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: PowerShell
      :linenos:
      :emphasize-lines: 1-2, 4, 11, 18

      mkdir list_comprehensions
      cd list_comprehensions
      mkdir src
      New-Item src/list_comprehensions.py
      mkdir tests
      New-Item tests/__init__.py

      "import unittest


      class TestListComprehensions(unittest.TestCase):

          def test_failure(self):
              self.assertFalse(True)

      # Exceptions seen
      # AssertionError
      " | Out-File tests/test_list_comprehensions.py

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: tests/test_list_comprehensions.py:7

    ======================================= FAILURES =======================================
    _________________________ TestListComprehensions.test_failure __________________________

    self = <tests.test_lists.TestListComprehensions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_list_comprehensions.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_list_comprehensions.py::TestListComprehensions::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option` or :kbd:`command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_list_comprehensions.py:7`` to open it in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_making_a_list_w_a_for_loop
*********************************************************************************

I can make a :ref:`list<lists>` with the constructor_ (``list()``) or with square brackets (``[]``), I can also add items one at a time with the :ref:`append method<test_append_adds_item_to_end_of_a_list>`, and I can use the :ref:`extend method<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change ``test_failure`` to ``test_making_a_list_w_a_for_loop`` to show what happens when I use the :ref:`append method<test_append_adds_item_to_end_of_a_list>` with more than one item

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-9

  import unittest


  class TestListComprehensions(unittest.TestCase):

      def test_making_a_list_w_a_for_loop(self):
          a_list = []
          a_list.append(0)
          self.assertEqual(a_list, [])

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0] != []

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 1

          self.assertEqual(a_list, [0])

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I use :ref:`test_append_adds_item_to_end_of_a_list` to add another item to the :ref:`list<lists>` with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3-4

            a_list.append(0)
            self.assertEqual(a_list, [0])
            a_list.append(1)
            self.assertEqual(a_list, [0])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1] != [0]

* I add the expected value to the test

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1])

  the test passes

* I :ref:`test_append_adds_item_to_end_of_a_list` another number with an :ref:`assertion<what is an assertion?>` to check

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

            a_list.append(1)
            self.assertEqual(a_list, [0, 1])
            a_list.append(2)
            self.assertEqual(a_list, [0, 1])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2] != [0, 1]

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2])

  the test passes

* I add one more number with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

            a_list.append(2)
            self.assertEqual(a_list, [0, 1, 2])
            a_list.append(3)
            self.assertEqual(a_list, [0, 1, 2])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2]

* I change the expectation

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes

----

---------------------------------------------------------------------------------
what is a for loop?
---------------------------------------------------------------------------------

I just wrote the same things 4 times in a row, the only things that changed were the numbers I added to the :ref:`list<lists>`, there is a better way. I can use a `for loop`_.

A `for loop`_ is a way to repeat the same command over an :ref:`iterable<what is an iterable?>` (a collection of items)

* I add a `for loop`_ to the test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-10, 12-13, 15

        def test_making_a_list_w_a_for_loop(self):
            a_list = []
            # a_list.append(0)
            # self.assertEqual(a_list, [0])
            # a_list.append(1)
            # self.assertEqual(a_list, [0, 1])
            # a_list.append(2)
            # self.assertEqual(a_list, [0, 1, 2])
            # a_list.append(3)
            # self.assertEqual(a_list, [0, 1, 2, 3])

            for number in (0, 1, 2, 3):
                a_list.append(number)

            self.assertEqual(a_list, [])

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3] != []

* I add the values

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

            self.assertEqual(a_list, [0, 1, 2, 3])

  the test passes

* I remove the commented lines. This `for loop`_ removed 8 lines of code and I can use it for any number of items, the other way gets busy very quickly once I have to add more than 4 numbers

  .. code-block:: python
    :lineno-start: 6

      def test_making_a_list_w_a_for_loop(self):
          a_list = []

          for number in (0, 1, 2, 3):
              a_list.append(number)

          self.assertEqual(a_list, [0, 1, 2, 3])

  - ``for number in (0, 1, 2, 3):`` goes over every number in the tuple_
  - ``a_list.append(number)`` gets called every time the `for loop`_ runs to add the number from the tuple_ to ``a_list``

* Python_ has an :ref:`iterable<what is an iterable?>` I can use to make a sequence of numbers, it is called the `range object`_. I add it to the `for loop`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5

        def test_making_a_list_w_a_for_loop(self):
            a_list = []

            # for number in (0, 1, 2, 3):
            for number in range(0, 4):
                a_list.append(number)

            self.assertEqual(a_list, [0, 1, 2, 3])

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 6

        def test_making_a_list_w_a_for_loop(self):
            a_list = []

            for number in range(0, 4):
                a_list.append(number)

            self.assertEqual(a_list, [0, 1, 2, 3])

  ``range(0, 4)`` makes a `range object`_ that goes from the first number in the parentheses to the second number minus 1, in this case it goes from ``0`` to ``3``

* The `for loop`_ is simpler than using the :ref:`append method<test_append_adds_item_to_end_of_a_list>` one a time, but there is an easier way. I can do the same thing with with the :ref:`list constructor<test_making_a_list>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

            self.assertEqual(a_list, [0, 1, 2, 3])
            self.assertEqual(list(), a_list)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [] != [0, 1, 2, 3]

* I add the `range object`_ to the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertEqual(list(range(0, 4)), a_list)

  the test passes

* I add a variable to remove the duplication of the `range object`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3, 5, 9

        def test_making_a_list_w_a_for_loop(self):
            a_list = []
            iterable = range(0, 4)

            for number in iterable:
                a_list.append(number)

            self.assertEqual(a_list, [0, 1, 2, 3])
            self.assertEqual(list(iterable), a_list)

* I add another :ref:`assertion<what is an assertion?>` to practice writing a `for loop`_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-5

        self.assertEqual(a_list, list(iterable))
        self.assertEqual(
            src.list_comprehensions.a_for_loop(iterable),
            [0, 1, 2, 3]
        )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.list_comprehensions
    import unittest

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.list_comprehensions' has no attribute 'a_for_loop'

* I add :ref:`AttributeError` to the list of :ref:`Exceptions<errors>` seen

  .. code-block::
    :lineno-start: 22
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``list_comprehensions.py`` in the :ref:`editor<2 editors>`

* then add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def a_for_loop():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: a_for_loop() takes 0 positional arguments but 1 was given

* I add a name for the argument

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def a_for_loop(a_container):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != [0, 1, 2, 3]

* I change the `return statement`_ to match

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def a_for_loop(a_container):
        return [0, 1, 2, 3]

  the test passes

* this solution fails when I change the values in the `range object`_ in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            iterable = range(0, 5)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

* I undo the change

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

            iterable = range(0, 4)

  the test is green again

* I import the `random module`_ to use random numbers in the test. I want a solution that can take any :ref:`iterable<what is an iterable?>` and return the right :ref:`list<lists>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import src.list_comprehensions
    import unittest

* I change the second value given to the `range object`_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            iterable = range(0, random.randint(2, 1000))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3, ...] != [0, 1, 2, 3]

  - ``random.randint(2, 1000)`` gives me a random integer_ between first number in parentheses and the second number minus ``1``, in this case ``2`` to ``999``
  - this `range object`_ now goes from ``0`` to anywhere between ``1`` and ``999`` because it goes from the first number in parentheses to the second number minus ``1``
  - The values change every time the test runs

* I change the expectation in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines:

            self.assertEqual(a_list, list(iterable))
            self.assertEqual(list(iterable), a_list)

  the test passes

* I remove the second line because it is now a duplicate

  .. code-block:: python
    :lineno-start: 12

            for number in iterable:
                a_list.append(number)

            self.assertEqual(a_list, list(iterable))
            self.assertEqual(
                src.list_comprehensions.a_for_loop(iterable),
                [0, 1, 2, 3]
            )

* I change the expectation of the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-5

            self.assertEqual(a_list, list(iterable))
            self.assertEqual(
                src.list_comprehensions.a_for_loop(iterable),
                a_list
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, ...]

* I change the :ref:`function<functions>` in ``list_comprehensions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def a_for_loop(a_container):
        result = []
        for stuff in a_container:
            result.append(stuff)
        return result
        return [0, 1, 2, 3]

  the test passes

* I remove the second `return statement`_

:ref:`I know how to make a list with a for loop<test_making_a_list_w_a_for_loop>`

Why did I use a `for loop`_ when I can use the :ref:`list constructor<test_making_a_list>` to do the same thing with less characters? :ref:`Sometimes one is better than the other<test_making_a_list_w_conditions>`

----

****************************************************************************************
test_making_a_list_w_extend
****************************************************************************************

I can also use the :ref:`extend method<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` to make a :ref:`list<lists>` from an :ref:`iterable<what is an iterable?>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 4-7

                a_list
            )

        def test_making_a_list_w_extend(self):
            a_list = []
            iterable = range(0, random.randint(2, 1000))
            self.assertIsNone(a_list.extend())


    # Exceptions seen

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: list.extend() takes exactly one argument (0 given)

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`iterable<what is an iterable?>`

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 1

          self.assertIsNone(a_list.extend(iterable))

the terminal_ shows green again, the :ref:`extend method<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` returns :ref:`None`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` to see what changed in the :ref:`list<lists>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

            self.assertIsNone(a_list.extend(iterable))
            self.assertEqual(a_list, list())

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3, ...] != []

* I change the expectation

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1

            self.assertEqual(a_list, list(iterable))

  the test passes. :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` uses less lines than the `for loop`_ but is not better than the :ref:`list constructor<test_making_a_list>`

* I made the same :ref:`variables<what is a variable?>` twice, one for the empty :ref:`list<lists>` and one for the :ref:`iterable<what is an iterable?>`, I add :ref:`class attributes<test_attribute_error_w_class_attributes>` to remove the duplication

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

    class TestListComprehensions(unittest.TestCase):

        a_list = []
        iterable = range(0, random.randint(2, 1000))

        def test_making_a_list_w_a_for_loop(self):

* then I use them in ``test_making_a_list_w_a_for_loop``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2-5

        def test_making_a_list_w_a_for_loop(self):
            # a_list = []
            # iterable = range(0, random.randint(2, 1000))
            a_list = self.a_list
            iterable = self.iterable

  the test is still green

* I remove the commented lines and use the :ref:`class attributes<test_attribute_error_w_class_attributes>` directly

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2-3, 5-6, 8, 10-11

        def test_making_a_list_w_a_for_loop(self):
            # a_list = self.a_list
            # iterable = self.iterable

            for number in self.iterable:
                self.a_list.append(number)

            self.assertEqual(self.a_list, list(self.iterable))
            self.assertEqual(
                src.list_comprehensions.a_for_loop(self.iterable),
                self.a_list
            )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 11

        def test_making_a_list_w_a_for_loop(self):
            for number in self.iterable:
                self.a_list.append(number)

            self.assertEqual(self.a_list, list(self.iterable))
            self.assertEqual(
                src.list_comprehensions.a_for_loop(self.iterable),
                self.a_list
            )

* I make the same change in ``test_making_a_list_w_extend``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-5

        def test_making_a_list_w_extend(self):
            # a_list = []
            # iterable = range(0, random.randint(2, 1000))
            a_list = self.a_list
            iterable = self.iterable

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 1, 2, 3, ... XYZ, 0, 1, 2, 3, ...XYZ] != [0, 1, 2, 3, ...XYZ]

  the values in ``a_list`` are double what the test expects. I broke something by using the :ref:`class attributes<test_attribute_error_w_class_attributes>`

* I change ``a_list`` back

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2, 4

        def test_making_a_list_w_extend(self):
            a_list = []
            # iterable = range(0, random.randint(2, 1000))
            # a_list = self.a_list
            iterable = self.iterable

  the test is green again

* The problem is that both tests :ref:`append<test_append_adds_item_to_end_of_a_list>` to ``self.a_list``. I was making an empty :ref:`list<lists>` for each test before, I need a better way. The `unittest.TestCase class`_ has a :ref:`method<functions>` I can use to make sure the :ref:`class attributes<test_attribute_error_w_class_attributes>` are always reset at the beginning of the test, so that the values are new for each test I add it to the test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-5

    class TestListComprehensions(unittest.TestCase):

        def setUp(self):
            self.a_list = []
            self.iterable = range(0, random.randint(2, 1000))

        def test_making_a_list_w_a_for_loop(self):

  the test is still green.

  The `unittest.TestCase.setUp method`_ runs before every test, in this case it sets the following :ref:`class attributes (variables)<test_attribute_error_w_class_attributes>`

  - ``self.a_list`` to an :ref:`empty list<test_making_a_list>`
  - ``self.iterable`` to a `range object`_ that goes from ``0`` to anywhere between ``1`` and ``999``

* I try to use ``self.a_list`` again in ``test_making_a_list_w_extend``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 4

        def test_making_a_list_w_extend(self):
            # a_list = []
            # iterable = range(0, random.randint(2, 1000))
            a_list = self.a_list
            iterable = self.iterable

  still green

* I remove the commented lines and use the :ref:`class attributes<test_attribute_error_w_class_attributes>` directly

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2-5

        def test_making_a_list_w_extend(self):
            # a_list = self.a_list
            # iterable = self.iterable
            self.assertIsNone(self.a_list.extend(self.iterable))
            self.assertEqual(self.a_list, list(self.iterable))

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

        def test_making_a_list_w_extend(self):
            self.assertIsNone(self.a_list.extend(self.iterable))
            self.assertEqual(self.a_list, list(self.iterable))


    # Exceptions seen

:ref:`I know how to make a list with the extend method<test_making_a_list_w_extend>`

----

****************************************************************************************
test_making_a_list_w_a_list_comprehension
****************************************************************************************

Time for the title of this chapter. I can use a `list comprehension`_ to make a :ref:`list<lists>` from an :ref:`iterable<what is an iterable?>` with one line

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 3-6

          self.assertEqual(self.a_list, list(self.iterable))

      def test_making_a_list_w_a_list_comprehension(self):
          self.assertEqual(
              list(self.iterable),
              []
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 1, 2, 3, ...] != []

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a `list comprehension`_ as the expectation

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 3


          self.assertEqual(
              list(self.iterable),
              [item for item in self.iterable]
          )

the test passes. The `list comprehension`_ is like the `for loop`_ without the :ref:`append<test_append_adds_item_to_end_of_a_list>` line

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` for practice

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5-8

            self.assertEqual(
                list(self.iterable),
                [item for item in self.iterable]
            )
            self.assertEqual(
                src.list_comprehensions.a_list_comprehension(self.iterable),
                [item for item in self.iterable]
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.list_comprehensions' has no attribute 'a_list_comprehension'

* I add the :ref:`function<functions>` in ``list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 4-5

        return result


    def a_list_comprehension(a_collection):
        return [element for element in a_collection]

  the test passes

* I made 2 :ref:`functions<functions>` that do the same thing - one that uses a `for loop`_ and another that uses a `list comprehension`_

  .. code-block:: python

      result = []
      for stuff in a_container:
          result.append(stuff)

  and

  .. code-block:: python

      [element for element in a_collection]

  the difference between them is that in the first case I have to

  * make a :ref:`list<lists>`
  * loop through the :ref:`iterable<what is an iterable?>`
  * do the operation I want on every item of the :ref:`iterable<what is an iterable?>`

  with the `list comprehension`_, I do all the steps in one line, and still none of the other ways are better than using the :ref:`list constructor<test_making_a_list>`, yet.

:ref:`I know how to use a list comprehension to make a list<test_making_a_list_w_a_list_comprehension>`

----

****************************************************************************************
test_making_a_list_w_conditions
****************************************************************************************

What if I had to make a :ref:`list<lists>` from an :ref:`iterable<what is an iterable?>` based on a condition?

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test to ``test_list_comprehensions.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 4-8, 10-13

              [item for item in self.iterable]
          )

      def test_making_a_list_w_conditions(self):
          even_numbers = []
          for item in self.iterable:
              if item % 2 == 0:
                  even_numbers.append(item)

          self.assertEqual(
              even_numbers,
              list(self.iterable)
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 2, 4, 6, 8, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8...]

* ``if item % 2 == 0:`` checks if the number in ``self.iterable`` leaves a remainder of ``0`` when it is divided by ``2``, this is the rule for even numbers
* ``%`` is the modulo_ operator, which divides the number on the left by the number on the right and returns a remainder, there's a test for it in :ref:`test_the_modulo_operation`

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

How can I make the ``even_numbers`` :ref:`list<lists>` with the constructor_ without changing the :ref:`iterable<what is an iterable?>`? Since I can make the :ref:`list<lists>` with a `for loop`_, I can do it with a `list comprehension`_. I change the expectation

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 3

          self.assertEqual(
              even_numbers,
              [item for item in self.iterable]
          )

the terminal_ still shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 2, 4, 6, 8, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8...]

I add the :ref:`if statement<if statements>`

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 3

          self.assertEqual(
              even_numbers,
              [item for item in self.iterable if item % 2 == 0]
          )

the test passes. This is a case where a `list comprehension`_ or a `for loop`_ is better than using the :ref:`list constructor<test_making_a_list>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` for practice

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3-6

                [item for item in self.iterable if item % 2 == 0]
            )
            self.assertEqual(
                src.list_comprehensions.get_even_numbers(self.iterable),
                [item for item in self.iterable if item % 2 == 0]
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_even_numbers'

* I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-6

    def a_list_comprehension(a_collection):
        return [element for element in a_collection]


    def get_even_numbers(numbers):
        return [number for number in numbers if number % 2 == 0]

  the test passes

* I wrote the same condition in the test 3 times. I have to make the same change everywhere I wrote it if I want to change it. Let us say the new condition is that the number should be divisible by ``3``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4

    def test_making_a_list_w_conditions(self):
        even_numbers = []
        for item in self.iterable:
            if item % 3 == 0:
                even_numbers.append(item)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 3, 6, 9, ...] != [0, 2, 4, 6, ...]

* I change the condition in the `list comprehension`_ of the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 3

            self.assertEqual(
                even_numbers,
                [item for item in self.iterable if item % 3 == 0]
            )

  the terminal_ shows green

* I change the condition in the `list comprehension`_ of the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3

            self.assertEqual(
                src.list_comprehensions.get_even_numbers(self.iterable),
                [item for item in self.iterable if item % 3 == 0]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 2, 4, 6, ...] != [0, 3, 6, 9, ...]

* I change the condition in the solution

  .. code-block:: python
    :emphasize-lines: 2

    def get_even_numbers(numbers):
        return [number for number in iterable if number % 3 == 0]

  the test passes

* I add a :ref:`function<functions>` to remove the duplication in ``test_list_comprehensions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import unittest


    def condition(number):
        return number % 3 == 0


    class TestListComprehensions(unittest.TestCase):

* I change the :ref:`if statement<if statements>` in the test to call the new :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5

        def test_making_a_list_w_conditions(self):
            even_numbers = []
            for item in self.iterable:
                # if item % 3 == 0:
                if condition(item):
                    even_numbers.append(item)

  the terminal_ still shows green

* I remove the commented line and do the same thing in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 9-10

        def test_making_a_list_w_conditions(self):
            even_numbers = []
            for item in self.iterable:
                if condition(item):
                    even_numbers.append(item)

            self.assertEqual(
                even_numbers,
                # [item for item in self.iterable if item % 3 == 0]
                [item for item in self.iterable if condition(item)]
            )

  still green

* I remove the commented line and use the new :ref:`function<functions>` in the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 7-8

            self.assertEqual(
                even_numbers,
                [item for item in self.iterable if condition(item)]
            )
            self.assertEqual(
                src.list_comprehensions.get_even_numbers(self.iterable),
                # [item for item in self.iterable if item % 3 == 0]
                [item for item in self.iterable if condition(item)]
            )

  the terminal_ still shows green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 50

            self.assertEqual(
                src.list_comprehensions.get_even_numbers(self.iterable),
                [item for item in self.iterable if condition(item)]
            )


    # Exceptions seen

  .. NOTE:: ``condition`` is not a good name for a :ref:`function<functions>` because it is general, it does not tell what it does. I use it to show that I think of a `list comprehension`_ as ``[item for item in iterable if condition]``

* I change the condition in the :ref:`function<functions>` in ``test_list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def condition(number):
        return number % 2 == 0

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 3, 6, 9, ...] != [0, 2, 4, 6, ...]

* I change the condition in ``get_even_numbers`` in ``list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

    def get_even_numbers(numbers):
        return [number for number in numbers if number % 2 == 0]

  the test passes. Adding the :ref:`function<functions>` adds extra lines, and makes managing the code easier because I now only have to make a change in one place in the test when I need

* I add a new empty :ref:`list<lists>` to test another condition in ``test_list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2

        def test_making_a_list_w_conditions(self):
            even_numbers, odd_numbers = [], []
            for item in self.iterable:

  ``even_numbers, odd_numbers = [], []`` makes 2 empty :ref:`lists` and names them

* I add an `else clause`_ to the :ref:`if statement<if statements>` in the `for loop`_

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5-6

            even_numbers, odd_numbers = [], []
            for item in self.iterable:
                if condition(item):
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3-6

                [item for item in self.iterable if condition(item)]
            )
            self.assertEqual(
                odd_numbers,
                [item for item in self.iterable]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 3, 5, 7, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8, ...]

* I add the :ref:`if statement<if statements>` to the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3

            self.assertEqual(
                odd_numbers,
                [item for item in self.iterable if not condition(item)]
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-6

                [item for item in self.iterable if not condition(item)]
            )
            self.assertEqual(
                src.list_comprehensions.get_odd_numbers(self.iterable),
                [item for item in self.iterable if not condition(item)]
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_odd_numbers'. Did you mean: 'get_even_numbers'?

* I add the :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5-6

    def get_even_numbers(numbers):
        return [number for number in numbers if number % 2 == 0]


    def get_odd_numbers(numbers):
        return [number for number in numbers if number % 2 != 0]

  the test passes

* These two conditions look the same

  .. code-block:: python

    if number % 2 == 0
    if number % 2 != 0

  the difference is the equality symbols ``==`` and ``!=``

  I add a :ref:`function<functions>` to remove the duplication

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-5

        return [element for element in a_collection]


    def is_even(number):
        return number % 2 == 0


    def get_even_numbers(numbers):

* I call the :ref:`function<functions>` in ``get_even_numbers``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

    def get_even_numbers(numbers):
        return [number for number in numbers if is_even(number)]
        return [number for number in numbers if number % 2 == 0]

  the test is still green

* I remove the second `return statement`_ and use :ref:`logical negation (NOT)<test_logical_negation>` with the new :ref:`function<functions>` in ``get_odd_numbers``

  .. code-block:: python
    :lineno-start: 17

        return [number for number in numbers if is_even(number)]


    def get_odd_numbers(numbers):
        return [number for number in numbers if not is_even(number)]
        return [number for number in numbers if number % 2 != 0]

  the test is still passing

* I remove the second `return statement`_

* There is a `Python Built-in Function`_ I can use to do the same thing as the `list comprehension`_, it is called filter_, which is a way to say "make a list based on a condition" or "give me only the things that meet this condition". I try it in the ``get_even_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

    def get_even_numbers(numbers):
        return filter(is_even, numbers)
        return [number for number in numbers if is_even(number)]

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: <filter object at 0xffffab1c23d4> != [0, 2, ...]

  I have to make the `filter object`_ a :ref:`list<lists>`

* I put it in the :ref:`list constructor<test_making_a_list>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

        return list(filter(is_even, numbers))

  the test passes. Which do you like better: `filter`_ or the `list comprehension`_?

* If I want to use filter_ in ``get_odd_numbers``, I have to make a :ref:`function<functions>` like I did for ``is_even`` because filter_ takes a :ref:`function<functions>` as input

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def get_odd_numbers(numbers):
        return list(filter(not is_even, numbers))
        return [number for number in numbers if not is_even(number)]

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'bool' object is not callable

* I do not want to write a new :ref:`function<functions>`. I can use a :ref:`function<functions>` with no name to make it work

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def get_odd_numbers(numbers):
        return list(filter(lambda x: not is_even(x), numbers))
        return [number for number in numbers if not is_even(number)]

  the test passes, but this is not sexy

* another option is to use the `filterfalse method`_ from the `itertools module`_, it is part of the `Python standard library`_ and needs an `import statement`_

  .. code-block:: python
    :lineno-start: 21

    def get_odd_numbers(numbers):
        import itertools
        return list(itertools.filterfalse(is_even, numbers))
        return list(filter(lambda x: not is_even(x), numbers))
        return [number for number in numbers if not is_even(number)]

  the test is still green

  filterfalse_ returns the items from the :ref:`iterable<what is an iterable?>` that do not meet the condition of the :ref:`function<functions>`

I like the `list comprehension`_ from the options, it is simpler, easier to remember, and does not need any `import statements`_. :ref:`I know how to filter a list<test_making_a_list_w_conditions>`

----

*********************************************************************************
test_making_a_list_w_processes
*********************************************************************************

I can do other operations in a `list comprehension`_ not just :ref:`append<test_append_adds_item_to_end_of_a_list>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test to ``test_list_comprehensions.py``

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 4-7, 9-12

              [item for item in self.iterable if not condition(item)]
          )

      def test_making_a_list_w_processes(self):
          square_club = []
          for item in self.iterable:
              square_club.append(item*item)

          self.assertEqual(
              square_club,
              [item for item in self.iterable]
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 1, 4, 9, ...] != [0, 1, 2, 3, ...]

the numbers on the left are squares of the numbers on the right

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the calculation to the `list comprehension`_

.. code-block:: python
  :lineno-start: 70
  :emphasize-lines: 3

          self.assertEqual(
              square_club,
              [item*item for item in self.iterable]
          )

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 3-6

                [item*item for item in self.iterable]
            )
            self.assertEqual(
                src.list_comprehensions.square(self.iterable),
                [item*item for item in self.iterable]
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.list_comprehensions' has no attribute 'square'

* I add the :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5


        return [number for number in numbers if not is_even(number)]


    def square(numbers):
        return [number**2 for number in numbers]

  the test passes

  ``x**y`` is how to write ``x`` raised to the power of ``y``

  .. math::

    x ^ y

* There is a `Python Built-in Function`_ that I can use to process a :ref:`list<lists>`, just like filter_, this one is called map_, I add it to the ``square`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2

    def square(numbers):
        return map(lambda x: x**2, numbers)
        return [number**2 for number in numbers]

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: <map object at 0xffffa1b234c5> != [0, 1, 4, 9, ...]

  I have to change the `map object`_ to a :ref:`list<lists>`

* I add the :ref:`list constructor<test_making_a_list>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2

    def square(numbers):
        return list(map(lambda x: x**2, numbers))
        return [number**2 for number in numbers]

  the test passes. map_ takes in a :ref:`function<functions>` as input, so once again I like the `list comprehension`_ better

* I add a :ref:`function<functions>` for the calculation I just did 3 times in ``test_list_comprehensions.py``

  .. code-block:: python
    :lineno-start: 3
    :emphasize-lines: 4-5

    import unittest


    def process(number):
        return number ** 2


    def condition(number):

* I call the new :ref:`function<functions>` in the `for loop`_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4-5

    def test_making_a_list_w_processes(self):
        square_club = []
        for item in self.iterable:
            # square_club.append(item*item)
            square_club.append(process(item))

  the test is still green

* I remove the commented line and call the :ref:`function<functions>` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 6-7

            for item in self.iterable:
                square_club.append(process(item))

            self.assertEqual(
                square_club,
                # [item*item for item in self.iterable]
                [process(item) for item in self.iterable]
            )

  still green

* I remove the commented line and call the :ref:`function<functions>` in the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 6-7

                square_club,
                [process(item) for item in self.iterable]
            )
            self.assertEqual(
                src.list_comprehensions.square(self.iterable),
                # [item*item for item in self.iterable]
                [process(item) for item in self.iterable]
            )

  the terminal_ still shows green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 78

            self.assertEqual(
                src.list_comprehensions.square(self.iterable),
                [process(item) for item in self.iterable]
            )


    # Exceptions seen

  .. NOTE:: ``process`` is not a good name for a :ref:`function<functions>` because it is general, it does not tell what it does. I use it to show that I think of a `list comprehension`_ as ``[process(item) for item in iterable]``

:ref:`I know how to process(transform) a list with list comprehensions<test_making_a_list_w_processes>`

----

*********************************************************************************
test_making_a_list_w_processes_and_conditions
*********************************************************************************

I can use both :ref:`processes<test_making_a_list_w_processes>` and :ref:`conditions<test_making_a_list_w_conditions>` in a `list comprehension`_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 4-10, 12-15

              [process(item) for item in self.iterable]
          )

      def test_making_a_list_w_processes_and_conditions(self):
          even_squares, odd_squares = [], []
          for item in self.iterable:
              if condition(item):
                  even_squares.append(process(item))
              else:
                  odd_squares.append(process(item))

          self.assertEqual(
              even_squares,
              [item for item in self.iterable]
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: Lists differ: [0, 4, 16, ...] != [0, 1, 2, 3, 4, ...]

the numbers on the left are the squares of the even numbers from the right

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add a call to the ``condition`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3

            self.assertEqual(
                even_squares,
                [item for item in self.iterable if condition(item)]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [0, 4, 16, 36, ...] != [0, 2, 4, 6, ...]

  the numbers on the left are squares of the numbers on the right

* I add a call to the ``process`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3

            self.assertEqual(
                even_squares,
                [process(item) for item in self.iterable if condition(item)]
            )

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3-6

                [process(item) for item in self.iterable if condition(item)]
            )
            self.assertEqual(
                odd_squares,
                [item for item in self.iterable]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 9, 25, 49, ...] != [0, 1, 2, 3, 4, 5, 6, 7, ...]

  the numbers on the left are the squares of the odd numbers from the right

* I add a call to ``condition`` with :ref:`logical negation(NOT)<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3

            self.assertEqual(
                odd_squares,
                [item for item in self.iterable if not condition(item)]
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: Lists differ: [1, 9, 25, 49, ...] != [1, 3, 5, 7, ...]

  the numbers on the left are squares of the numbers on the right

* I add a call to ``process``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3

            self.assertEqual(
                odd_squares,
                [process(item) for item in self.iterable if not condition(item)]
            )

  the test passes

:ref:`I know how to make a list based on conditions (filter) with processes (transform) it with list comprehensions<test_making_a_list_w_processes_and_conditions>`

----


*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/list_comprehensions

* I `change directory`_ to the parent of ``list_comprehensions``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
how to make sure the calculator tests use new numbers for every test
*********************************************************************************

I used the `setUp method`_ earlier to make sure that I had a new :ref:`list<lists>` and iterable_ for every test. I want to do the same thing with the :ref:`calculator<how to make a calculator>`, to make sure that each test uses 2 new different random numbers, not the same random numbers for every test

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

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

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
    collected 7 items

    tests/test_calculator.py ....                                        [100%]

    ============================ 7 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I add the `setUp method`_ to the ``TestCalculator`` :ref:`class<classes>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 3-5

  class TestCalculator(unittest.TestCase):

      def setUp(self):
          self.random_first_number = a_random_number()
          self.random_second_number = a_random_number()

      def test_addition(self):

the test is still green. The `setUp method`_ runs before every test, giving ``random_first_number`` and ``random_second_number`` new random values for each test

----

*************************************************************************************
a better way to test the calculator with inputs that are NOT numbers
*************************************************************************************

I have tested the :ref:`calculator functions<how to make a calculator>` with :ref:`None`, strings_ and :ref:`lists`, I want to test them with the other the basic :ref:`Python basic data types<data structures>`: :ref:`booleans`, tuples_, sets_ and :ref:`dictionaries`. Since I know how to use a `for loop`_ and `list comprehensions`_, I can do this with one test for all of them instead of a different test for each :ref:`data type<data structures>`

=================================================================================
:yellow:`RED`: make it fail
=================================================================================

I add a new :ref:`assertion<what is an assertion?>` to ``test_calculator_sends_message_when_input_is_not_a_number``

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 4-16

      def test_calculator_sends_message_when_input_is_not_a_number(self):
          error_message = 'Excuse me?! I only work with numbers. Please try again...'

          for data_type in (
              None,
              True,
              False,
              str(),
              tuple(),
              list(),
              set(),
              dict(),
          ):
              self.assertEqual(
                  src.calculator.add(data_type, a_random_number()),
                  'BOOM!!!'
              )

          self.assertEqual(
              src.calculator.add(None, None),
              error_message
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BOOM!!!'

Lovely! The :ref:`if statement<if statements>` in the ``only_takes_numbers`` :ref:`function<functions>` in ``calculator.py`` is doing its job, the :ref:`calculator<how to make a calculator>` only takes numbers

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

                self.assertEqual(
                    src.calculator.add(data_type, a_random_number()),
                    error_message
                )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: ABCDE.FGHIJKLMNOPQRST != 'Excuse me?! I only work with numbers. Please try again...'

  there is a problem. One of the :ref:`data types<data structures>` I am testing is being allowed by the :ref:`if statement<if statements>`, which means one of them is also either an integer_ or a float_. I need a way to tell which one is causing the problem

* the `unittest.TestCase class`_ has a way to tell which item is causing my failure when I am using a loop, I add it to the test

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3-7

                dict(),
            ):
                with self.subTest(i=data_type):
                    self.assertEqual(
                        src.calculator.add(data_type, a_random_number()),
                        error_message
                    )

            self.assertEqual(
                src.calculator.add(None, None),
                error_message
            )

  the terminal_ shows :ref:`AssertionError` for two of the :ref:`data types<data structures>` I am testing

  .. code-block:: shell
    :emphasize-lines: 3, 4
    :emphasize-text: SUBFAILED True False

    tests/test_calculator.py:72: AssertionError
    ============= short test summary info ==============
    SUBFAILED(i=True) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: UVW.XYZABCDEFGHIJKL != 'Excuse ...
    SUBFAILED(i=False) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: MNO.PQRSTUVWXYZABCD != 'Excuse ...
    =========== 2 failed, 7 passed in X.YZs ============

  the `unittest.TestCase.subTest method`_ runs the code in its context as a sub test, showing the values I give in ``i=data_type`` so that I can see which one caused the error

* I add a condition for :ref:`booleans` in the ``only_takes_numbers`` :ref:`function<functions>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

            error_message = 'Excuse me?! I only work with numbers. Please try again...'

            if isinstance(first_input, bool) or isinstance(second_input, bool):
                return error_message
            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 6-9

                with self.subTest(i=data_type):
                    self.assertEqual(
                        src.calculator.add(data_type, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.divide(data_type, a_random_number),
                        'BOOM!!!'
                    )

  the terminal_ shows :ref:`AssertionError` for all the :ref:`data types<data structures>` in the test

  .. code-block:: shell

    AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BOOM!!!'

* I think you can tell what will happen next. I change the expectation to match

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

                    self.assertEqual(
                        src.calculator.divide(data_type, a_random_number()),
                        error_message
                    )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5-8

                    self.assertEqual(
                        src.calculator.divide(data_type, a_random_number),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.multiply(data_type, a_random_number()),
                        'BOOM!!!'
                    )

  the terminal_ shows :ref:`AssertionError` for each :ref:`data type<data structures>`

  .. code-block:: shell

    AssertionError: 'Excuse me?! I only work with numbers. Please try again...' != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 3

                    self.assertEqual(
                        src.calculator.multiply(data_type, a_random_number()),
                        error_message
                    )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start:
    :emphasize-lines:

                    self.assertEqual(
                        src.calculator.multiply(data_type, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.subtract(data_type, a_random_number()),
                        'BOOM!!!'
                    )

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: list comprehensions: tests and solutions>`

----

*********************************************************************************
review
*********************************************************************************

The tests show I can make a :ref:`list<lists>` from an :ref:`iterable<what is an iterable?>` with

* the :ref:`list <lists>` constructor_
* a `for loop`_
* the :ref:`extend method<test_extend_adds_items_from_an_iterable_to_end_of_a_list>`
* and `list comprehensions`_

I can use :ref:`functions` and :ref:`conditions<test_making_a_list_w_conditions>` with `list comprehensions`_ to make a :ref:`list<lists>` with one line. I think of it as ``[process(item) for item in iterable if condition/NOT condition]``

I can also do this with :ref:`dictionaries`, it is called a dict comprehension and the syntax is any mix of the following

.. code-block:: shell

  {a_process(key): another_process(value) for key/value in iterable if condition/NOT condition}

----

*********************************************************************************
what is next?
*********************************************************************************

you know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<lists: list comprehensions>`

:ref:`Would you like to test making a person?<how to make a person>`

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