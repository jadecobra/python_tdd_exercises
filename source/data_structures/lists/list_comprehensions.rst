.. meta::
  :description: Master Python list comprehensions with this hands-on TDD tutorial. Learn to create lists efficiently with code examples. Start coding now!
  :keywords: Jacob Itegboje, Python list comprehensions, test-driven development, Python programming, coding tutorials, data structures, Python for beginners

.. include:: ../../links.rst

.. _list comprehension: https://docs.python.org/3/glossary.html#term-list-comprehension
.. _list comprehensions: https://docs.python.org/3/glossary.html#term-list-comprehension

#################################################################################
lists: list comprehensions
#################################################################################

.. raw:: html

    <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/8v6fF6gHmE4?si=e2-lry14UZDgU6Qo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

`List Comprehensions`_ are a simple way to make a :ref:`list <lists>` from an iterable_ with one line

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``list_comprehensions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh list_comprehensions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 list_comprehensions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_list_comprehensions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_list_comprehensions.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass

----

*********************************************************************************
test_making_a_list_w_a_for_loop
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_making_a_list_w_a_for_loop``

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

    def test_making_a_list_w_a_for_loop(self):
        a_list = []
        iterable = range(0, 4)

        for item in iterable:
            a_list.append(item)

        self.assertEqual(a_list, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != []

- ``a_list = []`` makes an empty list and gives it a name
- ``iterable = range(0, 4)`` makes a range_ object_ that goes from the first number given to the second number given minus 1, in this case it goes from 0 to 3
- ``for item in iterable:`` goes over every item in the range_ object_
- ``a_list.append(item)`` is called for every item in the range_ object_

the list is no longer empty after the operation

green: make it pass
#################################################################################

I change the expectation to match the values in the terminal

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 3])

the test passes

refactor: make it better
#################################################################################

* I add another assertion to show that I can get the same result with the :ref:`list<lists>` constructor_

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])
    self.assertEqual(a_list, list())

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  I add the iterable_ to the call

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))

  the test passes. Why use a `for loop`_ when I can use the :ref:`list<lists>` constructor_ to get the same thing? I will show this in a little bit

* first, I add another assertion to practice writing a `for loop`_

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(
        src.list_comprehensions.for_loop(iterable),
        [0, 1, 2, 3]
    )

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* I add it to the list of Exceptions_ encountered

  .. code-block:: python
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

* I add an `import statement`_

  .. code-block:: python
    :emphasize-lines: 1

    import src.list_comprehensions
    import unittest

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'for_loop'

* I add it to the list of Exceptions_ encountered

  .. code-block:: python
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: for_loop() takes 0 positional arguments but 1 was given

  I add the argument

  .. code-block:: python
    :emphasize-lines: 1

    def for_loop(iterable):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3]

  I change the `return statement`_

  .. code-block:: python
    :emphasize-lines: 2

    def for_loop(iterable):
        return [0, 1, 2, 3]

  the test passes

* I need a better test, this one breaks when I change the values in the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, 5)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

* I undo the change then import the random_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python
    :emphasize-lines: 1

    import random
    import src.list_comprehensions
    import unittest

* I change the values given to the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, random.randint(2, 1000))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, ...] != [0, 1, 2, 3]

  the values change every time the test runs because I am using random integers_

* I change the expectation in the first assertion

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(a_list, list(iterable))

  the test passes. Since it is a duplication I remove the line

* I change the expectation of the second assertion

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(
        src.list_comprehensions.for_loop(iterable),
        a_list
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, ...]

  I change the `return statement`_ in the :ref:`function<functions>`

  .. code-block:: python

    def for_loop(iterable):
        return list(iterable)

  the test passes. I made this :ref:`function<functions>` to practice writing a `for loop`_, I change it

  .. code-block:: python

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

  the test is still green, though this is not yet better than using the :ref:`list<lists>` constructor_

----

****************************************************************************************
test_making_a_list_w_extend
****************************************************************************************

I can also use the extend_ :ref:`method<function>` to make a list from an iterable_

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_making_a_list_w_a_for_loop(self):
      ...

  def test_making_a_list_w_extend(self):
      a_ list = []
      iterable = range(0, random.randint(2, 1000))
      self.assertIsNone(a_list.extend())

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: list.extend() takes exactly one argument (0 given)

green: make it pass
#################################################################################

I add the iterable_

.. code-block:: python

  self.assertIsNone(a_list.extend(iterable))

the terminal shows green again

refactor: make it better
#################################################################################

* I add another assertion to see what changed in ``a_list``

  .. code-block:: python

    self.assertIsNone(a_list.extend(iterable))
    self.assertEqual(
        a_list,
        []
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, ...] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(
        a_list,
        src.list_comprehensions.for_loop(iterable)
    )

  the test passes. Still not better than the :ref:`list<lists>` constructor_ yet, but less lines than the `for loop`_

* I made the same variables twice, one for the empty :ref:`list<lists>` and another for the iterable_, I add them to the setUp_ :ref:`method<functions>` to remove duplication and change the tests to use the class variables

  .. code-block:: python

    class TestListComprehensions(unittest.TestCase):

        def setUp(self):
            self.a_list = []
            self.iterable = range(0, random.randint(2, 1000))

        def test_making_a_list_w_a_for_loop(self):
            for item in self.iterable:
                self.a_list.append(item)

            self.assertEqual(self.a_list, list(self.iterable))
            self.assertEqual(
                src.list_comprehensions.for_loop(self.iterable),
                self.a_list
            )

        def test_making_a_list_w_extend(self):
            self.assertIsNone(self.a_list.extend(self.iterable))
            self.assertEqual(
                self.a_list,
                src.list_comprehensions.for_loop(self.iterable)
            )

  the terminal still shows green

----

****************************************************************************************
test_making_a_list_w_a_list_comprehension
****************************************************************************************

I can also use a `list comprehension`_ to make a list from an iterable_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_extend(self):
      ...

  def test_making_a_list_w_a_list_comprehension(self):
      iterable = range(0, random.randint(2, 1000))
      self.assertEqual(
          src.list_comprehensions.for_loop(iterable),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[413 chars] 113] != []
  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[3178 chars] 666] != []
  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[568 chars] 144] != []
  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[3253 chars] 681] != []

green: make it pass
#################################################################################

I use the :ref:`list<lists>` constructor_

.. code-block:: python

  self.assertEqual(
      src.list_comprehensions.for_loop(iterable),
      list(iterable)
  )

the test passes

refactor: make it better
#################################################################################

* I can do the same thing with a `list comprehension`_

  .. code-block:: python

    self.assertEqual(
        src.list_comprehensions.for_loop(iterable),
        # list(iterable)
        [item for item in iterable]
    )

  the terminal still shows green. I remove the comment then add another assertion for practice

  .. code-block:: python

    self.assertEqual(
        src.list_comprehensions.for_loop(iterable),
        [item for item in iterable]
    )
    self.assertEqual(
        src.list_comprehensions.list_comprehension(iterable),
        [item for item in iterable]
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'list_comprehension'

  I add the :ref:`function<functions>`

    .. code-block:: python

      def for_loop(iterable):
          ...


      def list_comprehension(iterable):
          return [item for item in iterable]

  the test passes

* I made the same variable twice for the iterable_, I will move it to the setUp_ :ref:`method<functions>` to remove duplication

  .. code-block:: python

    def setUp(self):
        self.iterable = range(0, random.randint(2, 1000))

  then use it in :ref:`test_making_a_list_w_a_for_loop`

  .. code-block:: python

    def test_making_a_list_w_a_for_loop(self):
        a_list = []
        for item in self.iterable:
            a_list.append(item)

        self.assertEqual(a_list, list(self.iterable))
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            list(self.iterable)
        )

  the test is still green. I do the same with :ref:`test_making_a_list_w_a_list_comprehension`

  .. code-block:: python

    def test_making_a_list_w_a_list_comprehension(self):
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            [item for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.iterable),
            [item for item in self.iterable]
        )

  the terminal still shows green

* I made 2 :ref:`functions<functions>` - one that uses a `for loop`_ and another that uses a `list comprehension`_ to do the same thing difference between

  .. code-block:: python

      a_list = []
      for item in iterable:
          a_list.append()

  and

  .. code-block:: python

      [item for item in iterable]

  the difference between them is that in the first case I have to

  * make a :ref:`list<lists>`
  * loop through the iterable_
  * do the operation I want on the item of the iterable_

  When I use `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I get the same result with one line that covers all those steps, but so far none of this is better than using the :ref:`list<lists>` constructor_

----

****************************************************************************************
test_making_a_list_w_conditions
****************************************************************************************

What if I had to build a list from an iterable but based on a condition? This is where a `for loop`_ or a `list comprehension`_ works better

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_conditions(self):
      even_numbers = []
      for item in self.iterable:
          if item % 2 == 0:
              even_numbers.append(item)

      self.assertEqual(even_numbers, list(self.iterable))

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 2[2375 chars] 990] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[4800 chars] 991]
  AssertionError: Lists differ: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 2[680 chars] 312] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[1410 chars] 313]
  AssertionError: Lists differ: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 2[137 chars], 94] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[320 chars], 94]
  AssertionError: Lists differ: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 2[670 chars] 308] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[1390 chars] 309]

* ``if item % 2 == 0:`` checks if the item in ``iterable`` leaves a remainder of ``0`` when divided by ``2``
* ``%`` is the modulo_ operator, it divides the number on the left by the number on the right and returns a remainder, it is covered in :ref:`test_the_modulo_operation`

green: make it pass
#################################################################################

I change the expectation to use a `list comprehension`_

.. code-block:: python

  self.assertEqual(
      even_numbers,
      [item for item in self.iterable]
  )

the terminal still shows :ref:`AssertionError`, I add the condition

.. code-block:: python

  self.assertEqual(
      even_numbers,
      [item for item in self.iterable if item % 2 == 0]
  )

the test passes

refactor: make it better
#################################################################################

* I add another assertion for practice

  .. code-block:: python

    self.assertEqual(
        even_numbers,
        [item for item in self.iterable if item % 2 == 0]
    )
    self.assertEqual(
        src.list_comprehensions.get_even_numbers(self.iterable),
        [item for item in self.iterable if item % 2 == 0]
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_even_numbers'

  I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def list_comprehension(iterable):
        ...


    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

  the test passes

* I wrote the same condition in the test 3 times. I add a :ref:`function<functions>` for it

  .. code-block:: python

    import unittest


    def condition(number):
        return number % 2 == 0

  I change the condition in the test

  .. code-block:: python

    def test_making_a_list_w_conditions(self):
        even_numbers = []
        for item in self.iterable:
            # if item % 2 == 0:
            if condition(item):
                even_numbers.append(item)

  the terminal still shows green. I remove the commented line and do the same thing in the first assertion

  .. code-block:: python

    self.assertEqual(
        even_numbers,
        # [item for item in self.iterable if item % 2 == 0]
        [item for item in self.iterable if condition(item)]
    )

  still green. I do it again with the next one

  .. code-block:: python

    self.assertEqual(
        even_numbers,
        [item for item in self.iterable if condition(item)]
    )
    self.assertEqual(
        src.list_comprehensions.get_even_numbers(self.iterable),
        # [item for item in self.iterable if item % 2 == 0]
        [item for item in self.iterable if condition(item)]
    )

  the terminal still shows green

* I add a new empty list

  .. code-block:: python

    even_numbers = []
    odd_numbers = []

  then add an else_ clause in the `for loop`_

  .. code-block:: python

    for item in self.iterable:
        if condition(item):
            even_numbers.append(item)
        else:
            odd_numbers.append(item)

  I add an assertion

  .. code-block:: python

    self.assertEqual(
        src.list_comprehensions.get_even_numbers(self.iterable),
        [item for item in self.iterable if condition(item)]
    )
    self.assertEqual(
        odd_numbers,
        [item for item in self.iterable]
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23[333 chars] 173] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[713 chars] 173]
    AssertionError: Lists differ: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23[1723 chars] 729] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[3493 chars] 729]
    AssertionError: Lists differ: [1, 3] != [0, 1, 2, 3, 4]
    AssertionError: Lists differ: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23[1958 chars] 823] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[3963 chars] 823]

  I add the condition to the assertion

  .. code-block:: python

    self.assertEqual(
        odd_numbers,
        [item for item in self.iterable if not condition(item)]
    )

  the test passes. I add another assertion

  .. code-block:: python

    self.assertEqual(
        odd_numbers,
        [item for item in self.iterable if not condition(item)]
    )
    self.assertEqual(
        src.list_comprehensions.get_odd_numbers(self.iterable),
        [item for item in self.iterable if not condition(item)]
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_odd_numbers'. Did you mean: 'get_even_numbers'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def get_even_numbers(iterable):
        ...


    def get_odd_numbers(iterable):
        return [item for item in iterable if item % 2 != 0]

  the test passes

* ``condition`` is not a descriptive name in this case, I am only using it to show that I can use any condition with the `list comprehension`_. I add a function for the conditions in ``list_comprehensions.py`` and use a descriptive name

  .. code-block:: python

    def list_comprehension(iterable):
        ...


    def is_even(number):
        return number % 2 == 0

  then reference it in ``get_even_numbers``

  .. code-block:: python

    def is_even(number):
        ...


    def get_even_numbers(iterable):
        return [item for item in iterable if is_even(item)]
        return [item for item in iterable if item % 2 == 0]

  the test is still passing. I remove the second `return statement`_ and use the new :ref:`function<functions>` in ``get_odd_numbers``

  .. code-block:: python

    def get_even_numbers(iterable):
        ...


    def get_odd_numbers(iterable):
        return [item for item in iterable if not is_even(item)]
        return [item for item in iterable if item % 2 != 0]

  the terminal still shows green, I remove the second `return statement`+

----

*********************************************************************************
test_making_a_list_w_processes
*********************************************************************************

red: make it fail
#################################################################################

I add a test to show I can perform operations in a `list comprehension`_

.. code-block:: python

  def test_making_a_list_w_processes(self):
      squares = []
      for item in self.iterable:
          squares.append(item*item)

      self.assertEqual(
          squares,
          [item for item in self.iterable]
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 1[2036 chars]1124] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1[1432 chars] 318]
  AssertionError: Lists differ: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 1[1775 chars]8961] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1[1247 chars] 281]
  AssertionError: Lists differ: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 1[6028 chars]7489] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1[3927 chars] 817]
  AssertionError: Lists differ: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 1[1852 chars]5264] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1[1302 chars] 292]

green: make it pass
#################################################################################

I add the calculation to the `list comprehension`_

.. code-block:: python

  self.assertEqual(
      squares,
      [item*item for item in self.iterable]
  )

the test passes

refactor: make it better
#################################################################################

* I add another assertion

  .. code-block:: python

    self.assertEqual(
        squares,
        [item*item for item in self.iterable]
    )
    self.assertEqual(
        src.list_comprehensions.square(self.iterable),
        [item*item for item in self.iterable]
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'square'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def get_odd_numbers(iterable):
        ...


    def square(iterable):
        return [item**2 for item in iterable]

  the test passes

* I add a :ref:`function<functions>` for the calculation I did 3 times in this test

  .. code-block:: python

    import unittest


    def process(number):
        return number ** 2

  I reference the new :ref:`function<functions>` in the test

  .. code-block:: python

    def test_making_a_list_w_processes(self):
        squares = []
        for item in self.iterable:
            # squares.append(item*item)
            squares.append(process(item))

        self.assertEqual(
            squares,
            # [item*item for item in self.iterable]
            [process(item) for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.square(self.iterable),
            # [item*item for item in self.iterable]
            [process(item) for item in self.iterable]
        )

  the terminal still shows green. I remove the commented lines

----

*********************************************************************************
test_making_a_list_w_processes_and_conditions
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_processes_and_conditions(self):
      even_squares = []
      odd_squares = []
      for item in self.iterable:
          if condition(item):
              even_numbers.append(process(item))
          else:
              odd_numbers.append(process(item))

      self.assertEqual(
          even_squares,
          [item for item in self.iterable]
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

AssertionError: Lists differ: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 4[3142 chars]9316] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[4120 chars] 855]
AssertionError: Lists differ: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 4[2750 chars]1536] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[3630 chars] 757]
AssertionError: Lists differ: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 4[2574 chars]6944] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[3405 chars] 712]
AssertionError: Lists differ: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 4[1934 chars]4704] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13[2605 chars] 552]

green: make it pass
#################################################################################

I add a call to ``process`` and ``condition``

.. code-block:: python

  self.assertEqual(
      even_squares,
      [process(item) for item in self.iterable if condition(item)]
  )

the test passes

refactor: make it better
#################################################################################

I add an assertion for ``odd_squares``

.. code-block:: python

  self.assertEqual(
      odd_squares,
      [item for item in self.iterable]
  )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361[1978 chars]6969] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[2668 chars] 564]
  AssertionError: Lists differ: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361[356 chars]8225] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[523 chars] 135]
  AssertionError: Lists differ: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361[629 chars]5369] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,[918 chars] 214]
  AssertionError: Lists differ: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

I add the calls

.. code-block:: python

  self.assertEqual(
      odd_squares,
      [process(item) for item in self.iterable if not condition(item)]
  )

the test passes

----

*********************************************************************************
review
*********************************************************************************

From the tests I can make a :ref:`list<lists>` from an iterable_ by using

* a `for loop`_ loop
* the :ref:`list <lists>` constructor_
* and `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_
* I can use :ref:`functions` and conditions with `list comprehensions` to make a list with one line

Would you like to test :ref:`dictionaries`?

----

:doc:`/code/code_list_comprehensions`