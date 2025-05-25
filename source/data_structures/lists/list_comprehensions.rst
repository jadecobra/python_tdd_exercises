.. include:: ../../links.rst

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

`List Comprehensions <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#list-comprehensions>`_ are a way to make a :ref:`list <lists>` from an iterable_. It is a simple way to go over every item in and perform an operation usually in one line

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
test_make_a_list_from_an_iterable
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list_from_an_iterable``

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

      def test_make_a_list_from_an_iterable(self):
          a_list = []

          container = range(10)
          for item in container:
              a_list.append(item)
          self.assertEqual(a_list, [])

* I make an empty list with ``a_list = []`` then make a variable with ``container = range(10)``, it makes an iterable_ of numbers with the range_ constructor_, which goes from 0 to 1 less than the number given, in this case it will be 0 to 9
* ``for item in container:`` uses a `for loop`_ to go over every item of ``container``
* ``a_list.append(item)`` adds the item from ``container`` to ``a_list`` on each cycle of the loop, using the append_ :ref:`method<functions>`, see :ref:`lists` for more details
* ``self.assertEqual(a_list, [])`` checks to see if ``a_list`` is still empty after the operation

the terminal shows :ref:`AssertionError` because ``a_list`` is no longer empty, it has 10 items after the loop runs

.. code-block:: python

  E    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []

green: make it pass
#################################################################################

I make the values in the test match the result

.. code-block:: python

  def test_make_a_list_from_an_iterable(self):
      a_list = []
      container = range(10)

      for item in container:
          a_list.append(item)

      self.assertEqual(
          a_list,
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      )

the test passes

refactor: make it better
#################################################################################

* I add another test to check what happens when I use the :ref:`list <lists>` constructor_ with ``container``

  .. code-block:: python

    self.assertEqual(
        a_list,
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    )
    self.assertEqual(list(container), [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []

* I change the expectation to match the result

  .. code-block:: python

    self.assertEqual(list(container), a_list)

  the test passes, calling the :ref:`list <lists>` constructor_ with an iterable_ makes a :ref:`list <lists>`

* I add another test

  .. code-block:: python

    self.assertEqual(list(container), a_list)
    self.assertEqual(
        src.list_comprehensions.make_a_list(container),
        a_list
    )

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

  then add an `import statement`_

  .. code-block:: python

    import unittest
    import src.list_comprehensions

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'make_a_list'

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

  then add a :ref:`function<functions>` definition to ``list_comprehensions.py``

  .. code-block:: python

    def make_a_list():
        return None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: make_a_list() takes 0 positional arguments but 1 was given

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

  then change the signature of the :ref:`function<functions>` to take in an argument

  .. code-block:: python

    def make_a_list(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* When I make the :ref:`function<functions>` return the result of calling the :ref:`list <lists>` constructor_ with ``argument`` as input

  .. code-block:: python

    def make_a_list(argument):
        return list(argument)

  the test passes

* I change the name of the :ref:`function's<functions>` input from ``argument`` to ``iterable`` to make it more explicit

  .. code-block:: python

    def make_a_list(iterable):
        return list(iterable)

I can make a :ref:`list <lists>` from any iterable_ by using the :ref:`list <lists>` constructor

----

*********************************************************************************
test_make_a_list_w_a_for_loop
*********************************************************************************

red: make it fail
#################################################################################

I add a test for making a list with a `for loop`_ loop

.. code-block:: python

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        container = range(10)

        for item in container:
            a_list.append(item)

        self.assertEqual(a_list, [])
        self.assertEqual(
            list_comprehensions.for_loop(container),
            a_list
        )

the terminal shows :ref:`AssertionError` for the values of ``a_list`` because it is no longer empty after I loop through ``container`` then add items

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []

green: make it pass
#################################################################################

* I make the values of the test match the result

  .. code-block:: python

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            a_list.append(item)

        self.assertEqual(
            a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            list_comprehensions.for_loop(container),
            a_list
        )

  the terminal shows :ref:`AttributeError` since ``list_comprehensions.py`` does not have a definition for ``for_loop``

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'for_loop'

* I add a :ref:`function<functions>` definition called ``for_loop`` to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop():
        return None

  and the terminal shows :ref:`TypeError` because the :ref:`function<functions>` signature does not match the call in the test

  .. code-block:: python

    TypeError: for_loop() takes 0 positional arguments but 1 was given

* I make the signature of the :ref:`function<functions>` to take input

  .. code-block:: python

    def for_loop(argument):
        return None

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* I make the behavior of the :ref:`function<functions>` to use a ``for`` loop

  .. code-block:: python

    def for_loop(argument):
        result = []
        for item in argument:
            result.append(item)
        return result

  - ``result = []`` makes an empty list called ``result``
  - ``for item in argument:`` makes a loop over the items of ``argument`` which is an iterable_ passed into the function
  - ``result.append(item)`` adds each item from ``argument`` to the list called ``result``
  - ``return result`` returns ``result`` after the loop completes

  the terminal shows all tests are passing
* I change the input name from ``argument`` to ``iterable`` to be more explicit

  .. code-block:: python

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

  all tests are still passing

From the tests I see that I can make a :ref:`list <lists>` from any iterable by using

* a `for loop`_ loop
* the :ref:`list <lists>` constructor

----

****************************************************************************************
test_making_lists_w_list_comprehensions
****************************************************************************************

red: make it fail
#################################################################################

I add a failing test to ``TestListComprehensions``

.. code-block:: python

    def test_making_lists_w_list_comprehensions(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            a_list.append(item)

        self.assertEqual(a_list, [])
        self.assertEqual([], a_list)
        self.assertEqual(
            list_comprehensions.list_comprehension(container),
            a_list
        )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []

green: make it pass
#################################################################################

* I make the values in the test match the terminal

  .. code-block:: python

    def test_making_lists_w_list_comprehensions(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            a_list.append(item)

        self.assertEqual(
            a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual([], a_list)
        self.assertEqual(
            list_comprehensions.list_comprehension(container),
            a_list
        )

  and the terminal shows another :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: Lists differ: [] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* this time I add a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to show how it is written

  .. code-block:: python

    def test_making_lists_w_list_comprehensions(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            a_list.append(item)

        self.assertEqual(
            a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            [item for item in container],
            a_list
        )
        self.assertEqual(
            list_comprehensions.list_comprehension(container),
            a_list
        )

  the terminal now shows :ref:`AttributeError` for the last line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'list_comprehension'

* I add a :ref:`function<functions>` that uses a list comprehension to ``list_comprehensions.py``

  .. code-block:: python

    def list_comprehension(argument):
        return [item for item in argument]

  and all tests pass
* I change ``argument`` to ``iterable`` to be more explicit

  .. code-block:: python

    def list_comprehension(iterable):
        return [item for item in iterable]

  I made 2 :ref:`functions<functions>`, one that uses a `for loop`_ loop and another that uses a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to do the same thing. The difference between

  .. code-block:: python

      a_list = []
      for item in container:
          a_list.append()

  and

  .. code-block:: python

      [item for item in container]

  Is that in the first case I have to

  * make a list
  * loop through the iterable
  * add the items I want from the iterable to the list

  With the list comprehension I can get the same result with less words, lines and steps

refactor: make it better
#################################################################################

There is more I can do with `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I can add conditions to the operations performed


* I add a failing test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_w_conditions_i(self):
        even_numbers = []
        self.assertEqual(even_numbers, [])

        container = range(10)
        for item in container:
            if item % 2 == 0:
                even_numbers.append(item)

        self.assertEqual(even_numbers, [])
        self.assertEqual(
            [],
            even_numbers
        )
        self.assertEqual(
            list_comprehensions.get_even_numbers(container),
            even_numbers
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != []

  - ``if item % 2 == 0:`` checks if the item in ``container`` leaves a remainder of ``0`` when divided by ``2``
  - ``%`` is a `modulo <https://en.wikipedia.org/wiki/Modulo>`_ operator which divides the number on the left by the number on the right and gives a remainder
  - ``even_numbers.append(item)`` adds ``item`` to ``even_numbers`` if ``item`` divided by ``2`` leaves a remainder of ``0``

* I add the values of the result to the test to make it pass

  .. code-block:: python

      def test_list_comprehensions_w_conditions_i(self):
          even_numbers = []
          self.assertEqual(even_numbers, [])

          container = range(10)
          for item in container:
              if item % 2 == 0:
                  even_numbers.append(item)

          self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
          self.assertEqual(
              [],
              even_numbers
          )
          self.assertEqual(
              list_comprehensions.get_even_numbers(container),
              even_numbers
          )

  and the terminal shows :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: Lists differ: [] != [0, 2, 4, 6, 8]

* I try using a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ like I did in the last example

  .. code-block:: python

      def test_list_comprehensions_w_conditions_i(self):
          even_numbers = []
          self.assertEqual(even_numbers, [])

          container = range(10)
          for item in container:
              if item % 2 == 0:
                  even_numbers.append(item)

          self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
          self.assertEqual(
              [item for item in container],
              even_numbers
          )
          self.assertEqual(
              list_comprehensions.get_even_numbers(container),
              even_numbers
          )

  and get :ref:`AssertionError` because the lists are not the same, I have too many values

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

* When I add the ``if`` condition to the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 == 0],
        even_numbers
    )

  the terminal shows :ref:`AttributeError` for the next line. Progress

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_even_numbers'

* I add a :ref:`function<functions>` definition to ``list_comprehensions.py`` using the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ I just wrote

  .. code-block:: python

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

  and the terminal shows passing tests, Hooray!
* I want to try another `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ with a different condition so I add a test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []
        self.assertEqual(odd_numbers, [])

        container = range(10)
        for item in container:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(odd_numbers, [])
        self.assertEqual([], odd_numbers)
        self.assertEqual(
            list_comprehensions.get_odd_numbers(container),
            odd_numbers
        )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 3, 5, 7, 9] != []

* when I make the values to match

  .. code-block:: python

    def test_list_comprehensions_w_conditions_ii(self):
        odd_numbers = []
        self.assertEqual(odd_numbers, [])

        container = range(10)
        for item in container:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
        self.assertEqual([], odd_numbers)
        self.assertEqual(
            list_comprehensions.get_odd_numbers(container),
            odd_numbers
        )

  the terminal shows :ref:`AssertionError` for the next test

  .. code-block:: python

    AssertionError: Lists differ: [] != [1, 3, 5, 7, 9]

* I make the value on the left with a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ that uses the same condition I used to make even numbers

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 == 0],
        odd_numbers
    )

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != [1, 3, 5, 7, 9]

* When I make the logic in the condition so it uses not equal to ``0`` instead

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 != 0],
        odd_numbers
    )

  the terminal shows :ref:`AttributeError` for the next line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_odd_numbers'

* I define a :ref:`function<functions>` that returns a list comprehension in ``list_comprehensions.py``

  .. code-block:: python

    def get_odd_numbers(iterable):
        return [item for item in iterable if item % 2 != 0]

  and the terminal shows all tests passed


  I see from the tests that I can make a :ref:`list <lists>` from any iterable by using

  * a `for loop`_ loop
  * the :ref:`list <lists>` constructor
  * `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

  If you typed along you now know a couple of ways to loop through ``iterables`` and have your program make decisions by using ``conditions``.

  You also know how to do it with less words using `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_. Your magic powers are growing.

* I have written the same thing multiple times in these tests and since the programming gods told me `to not repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_, It is time to remove the repetition in the code. In each test I make an empty list, verify it is empty and then perform operations on it. Since that part is the same for every test I can add it to the `unittest.TestCase.setUp <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.setUp>`_ :ref:`method<functions>` which is called before a test method. Anything I place in this :ref:`method<functions>` will run before the tests, I place my empty list creation and verification in here ::

    def setUp(self):
        self.a_list = []
        self.assertEqual(self.a_list, [])

* I make a reference to ``self.a_list`` in ``test_make_a_list_from_an_iterable``

  .. code-block:: python

    def test_make_a_list_from_an_iterable(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            self.a_list.append(item)
        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(list(container), self.a_list)
        self.assertEqual(
            list_comprehensions.make_a_list(container),
            self.a_list
        )

  the terminal still shows passing tests
* I remove the creation of the empty list and verification from ``test_make_a_list_from_an_iterable``

  .. code-block:: python

    def test_make_a_list_from_an_iterable(self):
        container = range(10)
        for item in container:
            self.a_list.append(item)
        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(list(container), self.a_list)
        self.assertEqual(
            list_comprehensions.make_a_list(container),
            self.a_list
        )

  the terminal still shows passing tests
* I make the same change in the other tests

  .. code-block:: python

    def test_make_a_list_w_a_for_loop(self):
        container = range(10)
        for item in container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            list_comprehensions.for_loop(container),
            self.a_list
        )

    def test_making_lists_w_list_comprehensions(self):
        container = range(10)
        for item in container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            [item for item in container],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.list_comprehension(container),
            self.a_list
        )

    def test_list_comprehensions_w_conditions_i(self):
        container = range(10)
        for item in container:
            if item % 2 == 0:
                self.a_list.append(item)

        self.assertEqual(self.a_list, [0, 2, 4, 6, 8])
        self.assertEqual(
            [item for item in container if item % 2 == 0],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.get_even_numbers(container),
            self.a_list
        )

    def test_list_comprehensions_w_conditions_ii(self):
        container = range(10)
        for item in container:
            if item % 2 != 0:
                self.a_list.append(item)

        self.assertEqual(self.a_list, [1, 3, 5, 7, 9])
        self.assertEqual(
            [item for item in container if item % 2 != 0],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.get_odd_numbers(container),
            self.a_list
        )

  the terminal still shows passing test
* In each test I make a range_ object named ``container``, I can add this to the ``setUp`` :ref:`method<functions>` and reference it in the tests

  .. code-block:: python

    def setUp(self):
        self.a_list = []
        self.assertEqual(self.a_list, [])
        self.container = range(10)

    def test_make_a_list_from_an_iterable(self):
        for item in self.container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(list(self.container), self.a_list)
        self.assertEqual(
            list_comprehensions.make_a_list(self.container),
            self.a_list
        )

    def test_make_a_list_w_a_for_loop(self):
        for item in self.container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            list_comprehensions.for_loop(self.container),
            self.a_list
        )

    def test_making_lists_w_list_comprehensions(self):
        for item in self.container:
            self.a_list.append(item)

        self.assertEqual(
            self.a_list,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
        self.assertEqual(
            [item for item in self.container],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.list_comprehension(self.container),
            self.a_list
        )

    def test_list_comprehensions_w_conditions_i(self):
        for item in self.container:
            if item % 2 == 0:
                self.a_list.append(item)

        self.assertEqual(self.a_list, [0, 2, 4, 6, 8])
        self.assertEqual(
            [item for item in self.container if item % 2 == 0],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.get_even_numbers(self.container),
            self.a_list
        )

    def test_list_comprehensions_w_conditions_ii(self):
        for item in self.container:
            if item % 2 != 0:
                self.a_list.append(item)

        self.assertEqual(self.a_list, [1, 3, 5, 7, 9])
        self.assertEqual(
            [item for item in self.container if item % 2 != 0],
            self.a_list
        )
        self.assertEqual(
            list_comprehensions.get_odd_numbers(self.container),
            self.a_list
        )

  the terminal shows all tests are still passing

----

*********************************************************************************
review
*********************************************************************************

I also ran into the following Exceptions_

* :ref:`AssertionError`
* NameError_
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :ref:`dictionaries`?

----

:doc:`/code/code_list_comprehensions`