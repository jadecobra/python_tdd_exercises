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

I change ``test_failure``

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
- ``iterable = range(0, 4)`` makes a range_ object_ that goes from the first number to the second given number minus 1, in this case it goes from ``0`` to ``3``
- ``for item in iterable:`` goes over every item in the range_ object_
- ``a_list.append(item)`` gets called every time the `for loop`_ runs

green: make it pass
#################################################################################

I change the expectation to match the values in the terminal

.. code-block:: python

  self.assertEqual(a_list, [0, 1, 2, 3])

the test passes. The :ref:`list<lists>` now has the items from the range_ object_ after the `for loop`_ runs

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` to show that I can do the same thing with the :ref:`list<lists>` constructor_

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])
    self.assertEqual(a_list, list())

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != []

  I add the iterable_ to the call

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))

  the test passes. Why use a `for loop`_ when I can use the :ref:`list<lists>` constructor_ to do the same thing with less characters? Sometimes one is better than the other, I show this before the end of the chapter

* I add another :ref:`assertion<AssertionError>` to practice writing a `for loop`_

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(
        src.list_comprehensions.a_for_loop(iterable),
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

    AttributeError: module 'src.list_comprehensions' has no attribute 'a_for_loop'

* I add it to the list of Exceptions_ encountered

  .. code-block:: python
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def a_for_loop():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: a_for_loop() takes 0 positional arguments but 1 was given

  I add the argument

  .. code-block:: python
    :emphasize-lines: 1

    def a_for_loop(a_container):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3]

  I change the `return statement`_

  .. code-block:: python
    :emphasize-lines: 2

    def a_for_loop(a_container):
        return [0, 1, 2, 3]

  the test passes

* this solution is fixed, the test fails when I change the values in the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, 5)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

* I undo the change then import the random_ :ref:`module<ModuleNotFoundError>` to add randomness to the test. I need a better solution

  .. code-block:: python
    :emphasize-lines: 1

    import random
    import src.list_comprehensions
    import unittest

* I change the second value given to the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, random.randint(2, 1000))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, ...] != [0, 1, 2, 3]

  this range_ object_ now goes from ``0`` to anywhere between ``1`` and ``999``. The values change every time the test runs

* I change the expectation in the first :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(a_list, list(iterable))

  the test passes. I remove the line because it is a duplicate

* I change the expectation of the second :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))
    self.assertEqual(
        src.list_comprehensions.a_for_loop(iterable),
        a_list
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, ...]

  I change the :ref:`function<functions>`

  .. code-block:: python

    def a_for_loop(a_container):
        result = []
        for stuff in a_container:
            result.append(stuff)
        return result
        return [0, 1, 2, 3]

  the test passes and I remove the second `return statement`_

----

****************************************************************************************
test_making_a_list_w_extend
****************************************************************************************

I can use the :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` :ref:`method<functions>` to make a :ref:`list<lists>` from an iterable_

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_making_a_list_w_a_for_loop(self):
      ...

  def test_making_a_list_w_extend(self):
      a_list = []
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

* I add another :ref:`assertion<AssertionError>` to see what changed in the :ref:`list<lists>`

  .. code-block:: python

    self.assertIsNone(a_list.extend(iterable))
    self.assertEqual(a_list, list())

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, ...] != []

  I change the expectation

  .. code-block:: python

    self.assertEqual(a_list, list(iterable))

  the test passes. :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` uses less lines than the `for loop`_ but is not yet better than the :ref:`list<lists>` constructor_

* I made the same variables twice, one for the empty :ref:`list<lists>` and one for the iterable_, I add them to the setUp_ :ref:`method<functions>` to remove duplication and change the tests to use the new :ref:`class<classes>` :ref:`attributes<AttributeError>`

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
                src.list_comprehensions.a_for_loop(self.iterable),
                self.a_list
            )

        def test_making_a_list_w_extend(self):
            self.assertIsNone(self.a_list.extend(self.iterable))
            self.assertEqual(self.a_list, list(self.iterable))

  the terminal still shows green

----

****************************************************************************************
test_making_a_list_w_a_list_comprehension
****************************************************************************************

I can use a `list comprehension`_ to make a :ref:`list<lists>` from an iterable_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_extend(self):
      ...

  def test_making_a_list_w_a_list_comprehension(self):
      self.assertEqual(
          list(self.iterable),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, ...] != []

green: make it pass
#################################################################################

The `list comprehension`_ is like the `for loop`_ without the :ref:`append<test_append_adds_item_to_end_of_a_list>`. I add one as the expectation

.. code-block:: python

  self.assertEqual(
      list(self.iterable),
      [item for item in self.iterable]
  )

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` for practice

  .. code-block:: python

    self.assertEqual(
        list(self.iterable),
        [item for item in self.iterable]
    )
    self.assertEqual(
        src.list_comprehensions.a_list_comprehension(self.iterable),
        [item for item in self.iterable]
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'a_list_comprehension'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def a_for_loop(a_container):
        result = []
        for stuff in a_container:
            result.append(stuff)
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
  * loop through the iterable_
  * do the operation I want on every item of the iterable_

  with the `list comprehension`_, I do all the steps in one line, but none of the other ways are better than using the :ref:`list<lists>` constructor_, yet.

----

****************************************************************************************
test_making_a_list_w_conditions
****************************************************************************************

What if I had to make a :ref:`list<lists>` from an iterable_ based on a condition?

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_conditions(self):
      even_numbers = []
      for item in self.iterable:
          if item % 2 == 0:
              even_numbers.append(item)

      self.assertEqual(
          even_numbers,
          list(self.iterable)
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 2, 4, 6, 8, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8...]

* ``if item % 2 == 0:`` checks if the item in ``iterable`` leaves a remainder of ``0`` when divided by ``2``
* ``%`` is the modulo_ operator, which divides the number on the left by the number on the right and returns a remainder, there's a test for it in :ref:`test_the_modulo_operation`

green: make it pass
#################################################################################

How can I make the ``even_numbers`` :ref:`list<lists>` with the constructor_ without changing the iterable_? Since I can make the :ref:`list<lists>` with a `for loop`_, I can do it with a `list comprehension`_, I change the expectation

.. code-block:: python

  self.assertEqual(
      even_numbers,
      [item for item in self.iterable]
  )

the terminal still shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 2, 4, 6, 8, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8...]

I add the condition

.. code-block:: python

  self.assertEqual(
      even_numbers,
      [item for item in self.iterable if item % 2 == 0]
  )

the test passes. This is a case where a `list comprehension`_ or a `for loop`_ is better than using the :ref:`list<lists>` constructor_

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>` for practice

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

    def a_list_comprehension(a_collection):
        ...


    def get_even_numbers(numbers):
        return [number for number in iterable if number % 2 == 0]

  the test passes

* I wrote the same condition in the test 3 times. If I want to change it, I have to make the same change everywhere I wrote it. Let us say the new condition is that the number should be divisible by ``3``

  .. code-block:: python
    :emphasize-lines: 4

    def test_making_a_list_w_conditions(self):
        even_numbers = []
        for item in self.iterable:
            if item % 3 == 0:
                even_numbers.append(item)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 3, 6, 9, ...] != [0, 2, 4, 6, ...]

  I change the condition in the `list comprehension`_ of the first :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 3

    self.assertEqual(
        even_numbers,
        [item for item in self.iterable if item % 3 == 0]
    )

  the terminal shows green. I change the condition in the `list comprehension`_ of the second :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 3

    self.assertEqual(
        src.list_comprehensions.get_even_numbers(self.iterable),
        [item for item in self.iterable if item % 3 == 0]
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, ...] != [0, 3, 6, 9, ...]

  I change the condition in the solution

  .. code-block:: python
    :emphasize-lines: 2

    def get_even_numbers(numbers):
        return [number for number in iterable if number % 3 == 0]

  the test passes

* I add a :ref:`function<functions>` to remove the duplication

  .. code-block:: python

    import unittest


    def condition(number):
        return number % 3 == 0

  then change the condition in the test to call the new :ref:`function<functions>`

  .. code-block:: python
    :emphasize-lines: 5

    def test_making_a_list_w_conditions(self):
        even_numbers = []
        for item in self.iterable:
            # if item % 3 == 0:
            if condition(item):
                even_numbers.append(item)

  the terminal still shows green. I remove the commented line and do the same thing in the first :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 4

    self.assertEqual(
        even_numbers,
        # [item for item in self.iterable if item % 3 == 0]
        [item for item in self.iterable if condition(item)]
    )

  still green. I do it again with the next one

  .. code-block:: python
    :emphasize-lines: 8

    self.assertEqual(
        even_numbers,
        [item for item in self.iterable if condition(item)]
    )
    self.assertEqual(
        src.list_comprehensions.get_even_numbers(self.iterable),
        # [item for item in self.iterable if item % 3 == 0]
        [item for item in self.iterable if condition(item)]
    )

  the terminal still shows green. I do NOT recommend using ``condition`` as a name for a :ref:`function<functions>` because it is general, it does not tell what it does. I use it to show that I think of a `list comprehension`_ as ``[item for item in iterable if condition]``. I change the condition in the :ref:`function<functions>`

  .. code-block:: python
    :emphasize-lines: 2

    def condition(number):
        return number % 2 == 0

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 3, 6, 9, ...] != [0, 2, 4, 6, ...]

  I change the condition in ``get_even_numbers``

  .. code-block:: python

    def get_even_numbers(numbers):
        return [number for number in numbers if number % 2 == 0]

  the test passes. Yes, adding the :ref:`function<functions>` adds extra lines, and it makes managing the code easier since I now only have to make a change in one place in the test when I need

* I add a new empty :ref:`list<lists>` to test another condition

  .. code-block:: python
    :emphasize-lines: 2

    def test_making_a_list_w_conditions(self):
        even_numbers, odd_numbers = [], []
        for item in self.iterable:
            ...

  ``even_numbers, odd_numbers = [], []`` makes 2 empty :ref:`lists` and names them

* I add an else_ clause in the `for loop`_

  .. code-block:: python
    :emphasize-lines: 4-5

    for item in self.iterable:
        if condition(item):
            even_numbers.append(item)
        else:
            odd_numbers.append(item)

  I add an :ref:`assertion<AssertionError>`

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

    AssertionError: Lists differ: [1, 3, 5, 7, ...] != [0, 1, 2, 3, 4, 5, 6, 7, 8, ...]

  I add the condition to the :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        odd_numbers,
        [item for item in self.iterable if not condition(item)]
    )

  the test passes. I add another :ref:`assertion<AssertionError>`

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

    def get_even_numbers(numbers):
        ...


    def get_odd_numbers(numbers):
        return [number for number in numbers if number % 2 != 0]

  the test passes

* I add a :ref:`function<functions>` for the condition to remove duplication and use a more descriptive name then call it in ``get_even_numbers``

  .. code-block:: python

    def a_list_comprehension(a_collection):
        ...


    def is_even(number):
        return number % 2 == 0


    def get_even_numbers(numbers):
        return [number for number in numbers if is_even(number)]
        return [number for number in numbers if number % 2 == 0]

  the test is still passing. I remove the second `return statement`_ then call the new :ref:`function<functions>` in ``get_odd_numbers``

  .. code-block:: python

    def get_even_numbers(numbers):
        return [number for number in numbers if is_even(number)]


    def get_odd_numbers(numbers):
        return [number for number in numbers if not is_even(number)]
        return [number for number in numbers if number % 2 != 0]

  the terminal still shows green, I remove the second `return statement`_

----

*********************************************************************************
test_making_a_list_w_processes
*********************************************************************************

red: make it fail
#################################################################################

I add a test to show I can do other operations in a `list comprehension`_ not just :ref:`append<test_append_adds_item_to_end_of_a_list>`

.. code-block:: python

  def test_making_a_list_w_conditions(self):
      ...

  def test_making_a_list_w_processes(self):
      square_club = []
      for item in self.iterable:
          square_club.append(item*item)

      self.assertEqual(
          square_club,
          [item for item in self.iterable]
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 4, 9, ...] != [0, 1, 2, 3, ...]

green: make it pass
#################################################################################

I add the calculation to the `list comprehension`_

.. code-block:: python

  self.assertEqual(
      square_club,
      [item*item for item in self.iterable]
  )

the test passes

refactor: make it better
#################################################################################

* I add another :ref:`assertion<AssertionError>`

  .. code-block:: python

    self.assertEqual(
        square_club,
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

    def get_odd_numbers(numbers):
        ...


    def square(numbers):
        return [number**2 for number in numbers]

  the test passes. ``x**y`` is how to write ``x`` raised to the power of ``y``

  .. math::

    x ^ y

* I add a :ref:`function<functions>` for the calculation I did 3 times in this test

  .. code-block:: python

    import unittest


    def process(number):
        return number ** 2

  I call it in the test

  .. code-block:: python

    def test_making_a_list_w_processes(self):
        square_club = []
        for item in self.iterable:
            # square_club.append(item*item)
            square_club.append(process(item))

        self.assertEqual(
            square_club,
            # [item*item for item in self.iterable]
            [process(item) for item in self.iterable]

        self.assertEqual(
            src.list_comprehensions.square(self.iterable),
            # [item*item for item in self.iterable]
            [process(item) for item in self.iterable]
        )

  the terminal still shows green. I remove the commented lines. I do NOT recommend using ``process`` as a name for a :ref:`function<functions>` because it is general, it does not tell what it does. I use it to show that I think of a `list comprehension`_ as ``[process(item) for item in iterable]``

----

*********************************************************************************
test_making_a_list_w_processes_and_conditions
*********************************************************************************

I can use both :ref:`processes<test_making_a_list_w_processes>` and :ref:`conditions<test_making_a_list_w_conditions>` in a `list comprehension`_

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_making_a_list_w_processes(self):
      ...

  def test_making_a_list_w_processes_and_conditions(self):
      even_squares, odd_squares = [], []
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

  AssertionError: Lists differ: [0, 4, 16, 36, ...] != [0, 1, 2, 3, 4, ...]

green: make it pass
#################################################################################

I add a call to ``condition``

.. code-block:: python
  :emphasize-lines: 3

    self.assertEqual(
        even_squares,
        [item for item in self.iterable if condition(item)]
    )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 4, 16, 36, ...] != [0, 2, 4, 6, ...]

I add a call to ``process``

.. code-block:: python
  :emphasize-lines: 3

  self.assertEqual(
      even_squares,
      [process(item) for item in self.iterable if condition(item)]
  )

the test passes

refactor: make it better
#################################################################################

I add another :ref:`assertion<AssertionError>`

.. code-block:: python

  self.assertEqual(
      odd_squares,
      [item for item in self.iterable]
  )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [1, 9, 25, 49, ...] != [0, 1, 2, 3, 4, 5, 6, 7, ...]

I add a call to ``condition``

.. code-block:: python

  self.assertEqual(
      odd_squares,
      [item for item in self.iterable if not condition(item)]
  )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [1, 9, 25, 49, ...] != [1, 3, 5, 7, ...]

I add a call to ``process``

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

The tests show I can make a :ref:`list<lists>` from an iterable_ with

* the :ref:`list <lists>` constructor_
* a `for loop`_
* the :ref:`extend<test_extend_adds_items_from_an_iterable_to_end_of_a_list>` :ref:`method<functions>`
* and `list comprehensions`_

I can use :ref:`functions` and :ref:`conditions<test_making_a_list_w_conditions>` with `list comprehensions`_ to make a :ref:`list<lists>` with one line. I think of it as ``[process(item) for item in iterable if condition/NOT condition]``

I can also do this with :ref:`dictionaries`, it is called a dict comprehension and the syntax is any mix of the following

.. code-block:: python
  :force:

  {a_process(key): another_process(value) for key/value in iterable if condition/NOT condition}

Would you like to test :ref:`dictionaries`?

----

:doc:`/code/code_list_comprehensions`