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

`List Comprehensions`_ are a simple to make a :ref:`list <lists>` from an iterable_, by going over every item and performing operations with one line

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
test_make_a_list_w_a_for_loop
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list_w_a_for_loop``

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        iterable = range(0, 4)

        for item in iterable:
            a_list.append(item)

        self.assertEqual(a_list, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != []

the list is no longer empty after calling the append_ :ref:`method<functions>` in the `for loop`_ which goes over every item in the iterable_

green: make it pass
#################################################################################

I change the expectation to match the values in the terminal

.. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])

the test passes

refactor: make it better
#################################################################################

* I add another assertion to show that this could have been achieved with the :ref:`list<lists>` constructor_

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])
    self.assertEqual(a_list, list(iterable))

  the test is still green. Why use a `for loop`_ when you can use the :ref:`list<lists>` constructor_ to get the same thing? I will show this in a little bit

* but first for some practice with the `for loop`_ I add another assertion

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

    # Exceptions Encountered
    # AssertionError
    # NameError

* I add an `import statement`_

  .. code-block:: python

    import src.list_comprehensions
    import unittest

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'for_loop'

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop(iterable):
        return [0, 1, 2, 3]

  the test passes

* I need a better test, this one breaks if I change the values in the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, 5)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4] != [0, 1, 2, 3]

* I undo the change then import the random_ :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import random
    import src.list_comprehensions
    import unittest

* I change the values given to the range_ :ref:`object<classes>`

  .. code-block:: python

    iterable = range(0, random.randint(2, 1000))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[2158 chars] 464] != [0, 1, 2, 3]
    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[2283 chars] 489] != [0, 1, 2, 3]
    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[2118 chars] 456] != [0, 1, 2, 3]
    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[773 chars] 187] != [0, 1, 2, 3]

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
        list(iterable)
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[1393 chars] 311]
    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[3743 chars] 781]
    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[2208 chars] 474]
    AssertionError: Lists differ: [0, 1, 2, 3] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1[4778 chars] 988]

  I change the `return statement`_ in the :ref:`function<functions>`

  .. code-block:: python

    def for_loop(iterable):
        return list(iterable)

  the test passes, but I want to practice writing a `for loop`_, I change the :ref:`function<functions>`

  .. code-block:: python

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

  the test is green, this is not yet better than using the :ref:`list<lists>` constructor, there is another way

----

****************************************************************************************
test_make_a_list_w_list_comprehensions
****************************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_make_a_list_w_a_for_loop(self):
      ...

  def test_make_a_list_w_list_comprehensions(self):
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

  then use it in :ref:`test_make_a_list_w_a_for_loop`

  .. code-block:: python

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        for item in self.iterable:
            a_list.append(item)

        self.assertEqual(a_list, list(self.iterable))
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            list(self.iterable)
        )

  the test is still green. I do the same with :ref:`test_make_a_list_w_list_comprehensions`

  .. code-block:: python

    def test_make_a_list_w_list_comprehensions(self):
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

  When I use `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I get the same result with one line that covers all those steps



----

****************************************************************************************
test_list_comprehensions_w_conditions_i
****************************************************************************************

There is more I can do with `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I can add conditions when I perform an operation

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_list_comprehensions_w_conditions_i(self):
      iterable = range(10)

      even_numbers = []
      for item in iterable:
          if item % 2 == 0:
              even_numbers.append(item)

      self.assertEqual(even_numbers, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 2, 4, 6, 8] != []

* ``if item % 2 == 0:`` checks if the item in ``iterable`` leaves a remainder of ``0`` when divided by ``2``
* ``%`` is the modulo_ operator, it divides the number on the left by the number on the right and returns a remainder

green: make it pass
#################################################################################

I copy the values from the terminal and paste in the test

.. code-block:: python

  self.assertEqual(even_numbers, [0, 2, 4, 6, 8])

the test passes

refactor: make it better
#################################################################################

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
    self.assertEqual(
        [item for item in iterable],
        even_numbers
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

  the `list comprehension`_ is missing the condition, I add it

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 == 0],
        even_numbers
    )

  the test passes, I add another assert_ statement

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 == 0],
        even_numbers
    )
    self.assertEqual(
        src.list_comprehensions.get_even_numbers(iterable),
        even_numbers
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_even_numbers'

  I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def list_comprehension(iterable):
        return [item for item in iterable]

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

  the test passes

----

****************************************************************************************
test_list_comprehensions_w_conditions_ii
****************************************************************************************

I add another test

.. code-block:: python

  def test_list_comprehensions_w_conditions_ii(self):
      iterable = range(10)

      odd_numbers = []
      for item in iterable:
          if item % 2 != 0:
              odd_numbers.append(item)

      self.assertEqual(odd_numbers, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [1, 3, 5, 7, 9] != []

I change the expectation to match

.. code-block:: python

  self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])

the test passes. I add another assert_ statement

.. code-block:: python

  self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
  self.assertEqual(
      [item for item in iterable],
      odd_numbers
  )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [1, 3, 5, 7, 9]

I add the condition to the `list comprehension`_

.. code-block:: python

  self.assertEqual(
      [item for item in iterable if item % 2 != 0],
      odd_numbers
  )

the test passes and I add another assert_ statement

.. code-block:: python

  self.assertEqual(
      [item for item in iterable if item % 2 != 0],
      odd_numbers
  )
  self.assertEqual(
      src.list_comprehensions.get_odd_numbers(iterable),
      odd_numbers
  )

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.list_comprehensions' has no attribute 'get_odd_numbers'. Did you mean: 'get_even_numbers'?

I add the :ref:`function<functions>`

.. code-block:: python

  def get_even_numbers(iterable):
      return [item for item in iterable if item % 2 == 0]


  def get_odd_numbers(iterable):
      return [item for item in iterable if item % 2 != 0]

----

I used the same iterable_ for every test, I can remove the repetition by using the setUp_ :ref:`method<functions>`

.. code-block:: python

  class TestListComprehensions(unittest.TestCase):

      def setUp(self):
          self.iterable = range(10)

then change all the references to the variable

.. code-block:: python

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        for item in self.iterable:
            a_list.append(item)

        self.assertEqual(a_list, list(self.iterable))
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            a_list
        )

    def test_make_a_list_w_list_comprehensions(self):
        self.assertEqual(
            src.list_comprehensions.for_loop(self.iterable),
            [item for item in self.iterable]
        )
        self.assertEqual(
            src.list_comprehensions.list_comprehension(self.iterable),
            src.list_comprehensions.for_loop(self.iterable)
        )

    def test_list_comprehensions_w_conditions_i(self):
        even_numbers = []
        for item in self.iterable:
            if item % 2 == 0:
                even_numbers.append(item)

        self.assertEqual(
            [item for item in self.iterable if item % 2 == 0],
            even_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_even_numbers(self.iterable),
            even_numbers
        )

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []
        for item in self.iterable:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(
            [item for item in self.iterable if item % 2 != 0],
            odd_numbers
        )
        self.assertEqual(
            src.list_comprehensions.get_odd_numbers(self.iterable),
            odd_numbers
        )

the terminal shows all tests are still passing

----

*********************************************************************************
review
*********************************************************************************

From the tests I can make a :ref:`list<lists>` from an iterable_ by using

* a `for loop`_ loop
* the :ref:`list <lists>` constructor_
* `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

I also ran into the following Exceptions_

* :ref:`AssertionError`
* NameError_
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :ref:`dictionaries`?

----

:doc:`/code/code_list_comprehensions`