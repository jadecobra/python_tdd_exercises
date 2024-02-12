.. include:: ../../links.rst

##############################################
lists: List Comprehensions
##############################################

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8v6fF6gHmE4?si=e2-lry14UZDgU6Qo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

`List Comprehensions <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#list-comprehensions>`_ are a way to create a :doc:`list </data_structures/lists/lists>` from an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_. It is a simple way to go over every item in the :doc:`list </data_structures/lists/lists>` and perform an operation usually in one line

***************************************
How to create a List from an Iterable
***************************************

red: make it fail
==================

I will add a file called ``test_list_comprehensions.py`` to the ``tests`` folder with the following code

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

      def test_creating_a_list_from_an_iterable(self):
          a_list = []
          self.assertEqual(a_list, [])

          container = range(10)
          for item in container:
              a_list.append(item)
          self.assertEqual(a_list, [])

* ``a_list = []`` creates an empty list called ``a_list``
* ``self.assertEqual(a_list, [])`` confirms that ``a_list`` is empty since it is equal to ``[]``
* ``container = range(10)`` creates an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ of numbers from 0 to 9 with the `range <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_ constructor and calls it ``container``
* `range <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_ creates an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ of numbers from 0 to the given number minus 1
* ``for item in container:`` uses a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ statement to create a loop that goes over every item of ``container``
* ``a_list.append(item)`` adds the item from ``container`` to ``a_list`` on each cycle of the loop, using the ``append`` :ref:`method<functions>`, see :doc:`/data_structures/lists/lists` for more details
* the second ``self.assertEqual(a_list, [])`` checks to see if ``a_list`` is still empty after the operation

the terminal shows an :ref:`AssertionError` because ``a_list`` is no longer empty, it contains 10 items after the loop runs

.. code-block:: python

  E    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


green: make it pass
====================

I will make the values in the test to match the result

.. code-block:: python

  def test_creating_a_list_from_an_iterable(self):
      a_list = []
      self.assertEqual(a_list, [])

      container = range(10)
      for item in container:
          a_list.append(item)
      self.assertEqual(
          a_list,
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      )

and the test passes

refactor: make it better
=========================

* I will add another test to check what happens when I use the :doc:`list </data_structures/lists/lists>` constructor on ``container``

  .. code-block:: python

      self.assertEqual(list(container), [])

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

      AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []

* I will make the empty list ``[]`` to ``a_list``

  .. code-block:: python

    self.assertEqual(list(container), a_list)

  and the test passes because calling ``list`` on an ``iterable`` creates a :doc:`list </data_structures/lists/lists>`
* I will add another test

  .. code-block:: python

      self.assertEqual(
          list_comprehensions.make_a_list(container),
          a_list
      )

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'list_comprehensions' is not defined

* I will add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

  then add an `import statement`_ for ``list_comprehensions`` at the beginning of ``test_list_comprehensions.py`` to define the name in the tests

  .. code-block:: python

    import list_comprehensions
    import unittest

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'list_comprehensions'

* I will add it to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError

  then create a file called ``list_comprehensions.py`` in the project folder and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'make_a_list'

* I will add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError

  then add a :ref:`function<functions>` definition to ``list_comprehensions.py``

  .. code-block:: python

    def make_a_list():
        return None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: make_a_list() takes 0 positional arguments but 1 was given

* I will add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

  then change the signature of the function to take in an argument

  .. code-block:: python

    def make_a_list(argument):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* When I will make the function to return the result of calling the :doc:`list </data_structures/lists/lists>` constructor with ``argument`` as input

  .. code-block:: python

    def make_a_list(argument):
        return list(argument)

  the test passes
* I will make the name of the :doc:`function's </functions/functions>` input from ``argument`` to ``iterable`` to make it more explicit

  .. code-block:: python

    def make_a_list(iterable):
        return list(iterable)

From the tests I see that I can make a :doc:`list </data_structures/lists/lists>` from any iterable by using the :doc:`list </data_structures/lists/lists>` constructor

----

***************************************
How to create a List with a For Loop
***************************************

red: make it fail
^^^^^^^^^^^^^^^^^

I will add a test for creating a list with a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ loop

.. code-block:: python

    def test_creating_a_list_with_a_for_loop(self):
        a_list = []
        self.assertEqual(a_list, [])

        container = range(10)
        for item in container:
            a_list.append(item)

        self.assertEqual(a_list, [])
        self.assertEqual(
            list_comprehensions.for_loop(container),
            a_list
        )

the terminal shows an :ref:`AssertionError` for the values of ``a_list`` because it is no longer empty after I loop through ``container`` and add items

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


green: make it pass
====================

* I will make the values of the test to match the result

  .. code-block:: python

    def test_creating_a_list_with_a_for_loop(self):
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

  the terminal shows an :ref:`AttributeError` since ``list_comprehensions.py`` does not have a definition for ``for_loop``

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'for_loop'

* I will add a function definition called ``for_loop`` to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop():
        return None

  and the terminal shows a :ref:`TypeError` because the :doc:`function signature </functions/functions>` does not match the call in the test

  .. code-block:: python

    TypeError: for_loop() takes 0 positional arguments but 1 was given

* I will make the signature of the function to take input

  .. code-block:: python

    def for_loop(argument):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* I will make the behavior of the function to use a ``for`` loop

  .. code-block:: python

    def for_loop(argument):
        result = []
        for item in argument:
            result.append(item)
        return result

  - ``result = []`` creates an empty list called ``result``
  - ``for item in argument:`` creates a loop over the items of ``argument`` which is an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ passed into the function
  - ``result.append(item)`` adds each item from ``argument`` to the list called ``result``
  - ``return result`` returns ``result`` after the loop completes

  the terminal shows all tests are passing
* I rename the input from ``argument`` to ``iterable`` to be more explicit

  .. code-block:: python

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

  all tests are still passing

From the tests I see that I can make a :doc:`list </data_structures/lists/lists>` from any iterable by using

* a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ loop
* the :doc:`list </data_structures/lists/lists>` constructor

**********************************************
How to create a List with List Comprehensions
**********************************************

red: make it fail
==================

I will add a failing test to ``TestListComprehensions``

.. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


green: make it pass
=====================

* I will make the values to make it match the result

  .. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
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

* this time I will add a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to show how it is written

  .. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
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

  the terminal now shows an :ref:`AttributeError` for the last line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'list_comprehension'

* I will add a function that uses a list comprehension to ``list_comprehensions.py``

  .. code-block:: python

    def list_comprehension(argument):
        return [item for item in argument]

  and all tests pass
* I rename ``argument`` to ``iterable`` to be more explicit

  .. code-block:: python

    def list_comprehension(iterable):
        return [item for item in iterable]

----

I made two :ref:`functions<functions>`, one that uses a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ loop and another that uses a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to do the same thing. The difference between

.. code-block:: python

    a_list = []
    for item in container:
        a_list.append()

and

.. code-block:: python

    [item for item in container]

Is that in the first case I have to

* create a list
* loop through the iterable
* add the items I want from the iterable to the list

With the list comprehension I can get the same result with less words, lines and steps

refactor: make it better
=========================

There is more I can do with `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I can add conditions to the operations performed


* I will add a failing test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_with_conditions_i(self):
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

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != []

  - ``if item % 2 == 0:`` checks if the item in ``container`` leaves a remainder of ``0`` when divided by ``2``
  - ``%`` is a `modulo <https://en.wikipedia.org/wiki/Modulo>`_ operator which divides the number on the left by the number on the right and gives a remainder
  - ``even_numbers.append(item)`` adds ``item`` to ``even_numbers`` if ``item`` divided by ``2`` leaves a remainder of ``0``

* I will add the values of the result to the test to make it pass

  .. code-block:: python

      def test_list_comprehensions_with_conditions_i(self):
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

  and the terminal shows an :ref:`AssertionError` for the next line

  .. code-block:: python

    AssertionError: Lists differ: [] != [0, 2, 4, 6, 8]

* I try using a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ like I did in the last example

  .. code-block:: python

      def test_list_comprehensions_with_conditions_i(self):
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

  and get an :ref:`AssertionError` because the lists are not the same, I have too many values

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

* When I will add the ``if`` condition to the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 == 0],
        even_numbers
    )

  the terminal shows an :ref:`AttributeError` for the next line. Progress

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_even_numbers'

* I will add a function definition to ``list_comprehensions.py`` using the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ I just wrote

  .. code-block:: python

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

  and the terminal shows passing tests, Hooray!
* I want to try another `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ with a different condition so I will add a test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_with_conditions_ii(self):
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

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 3, 5, 7, 9] != []

* when I will make the values to match

  .. code-block:: python

    def test_list_comprehensions_with_conditions_ii(self):
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

  the terminal shows an :ref:`AssertionError` for the next test

  .. code-block:: python

    AssertionError: Lists differ: [] != [1, 3, 5, 7, 9]

* I will make the value on the left with a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ that uses the same condition I used to create even numbers

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 == 0],
        odd_numbers
    )

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != [1, 3, 5, 7, 9]

* When I will make the logic in the condition so it uses not equal to ``0`` instead

  .. code-block:: python

    self.assertEqual(
        [item for item in container if item % 2 != 0],
        odd_numbers
    )

  the terminal shows an :ref:`AttributeError` for the next line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_odd_numbers'

* I define a function that returns a list comprehension in ``list_comprehensions.py``

  .. code-block:: python

    def get_odd_numbers(iterable):
        return [item for item in iterable if item % 2 != 0]

  and the terminal shows all tests passed

----

I see from the tests that I can make a :doc:`list </data_structures/lists/lists>` from any iterable by using

* a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ loop
* the :doc:`list </data_structures/lists/lists>` constructor
* `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

If you typed along you now know a couple of ways to loop through ``iterables`` and have your program make decisions by using ``conditions``.

You also know how to do it with less words using `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_. Your magic powers are growing.


***************************************
refactor: make it better
***************************************

I have written the same thing multiple times in these tests and since the programming gods told me `Do Not Repeat Yourself! <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_ It is time to remove the repetition in the code.

* In each test I make an empty list, verify it is empty and then perform operations on it. Since that part is the same for every test I can add it to the `unittest.TestCase.setUp <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.setUp>`_ :ref:`method<functions>` which is called before a test method. Anything I place in this :ref:`method<functions>` will run before the tests, I place my empty list creation and verification in here ::

    def setUp(self):
        self.a_list = []
        self.assertEqual(self.a_list, [])

* I make a reference to ``self.a_list`` in ``test_creating_a_list_from_an_iterable`` ::

    def test_creating_a_list_from_an_iterable(self):
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
* I remove the creation of the empty list and verification from ``test_creating_a_list_from_an_iterable`` ::

    def test_creating_a_list_from_an_iterable(self):
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
* I make the same change in the other tests ::

    def test_creating_a_list_with_a_for_loop(self):
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

    def test_creating_lists_with_list_comprehensions(self):
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

    def test_list_comprehensions_with_conditions_i(self):
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

    def test_list_comprehensions_with_conditions_ii(self):
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
* In each test I make a `range <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_ object named ``container``, I can add this to the ``setUp`` :ref:`method<functions>` and reference it in the tests ::

    def setUp(self):
        self.a_list = []
        self.assertEqual(self.a_list, [])
        self.container = range(10)

    def test_creating_a_list_from_an_iterable(self):
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

    def test_creating_a_list_with_a_for_loop(self):
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

    def test_creating_lists_with_list_comprehensions(self):
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

    def test_list_comprehensions_with_conditions_i(self):
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

    def test_list_comprehensions_with_conditions_ii(self):
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

I also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* :ref:`TypeError`

----

:doc:`/code/code_list_comprehensions`