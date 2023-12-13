
Data Structures: Lists: List Comprehensions
============================================

`List Comprehensions <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#list-comprehensions>`_ are a way to create lists from an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_. It is a nice way to loop over elements and perform some operation usually in one line

How to create a List with an Iterable
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a file called ``test_list_comprehension.py`` to the ``tests`` folder with the following code

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

      def test_creating_a_list_from_an_iterable(self):
          collection = range(10)
          a_list = []
          self.assertEqual(a_list, [])

          for element in collection:
              a_list.append(element)
          self.assertEqual(a_list, [])

* ``collection = range(10)`` creates an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ of numbers from 0 to 9 with the `range <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_ object and calls it ``collection``
* `range <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_ creates an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ of numbers from 0 to the given number minus 1
* ``a_list = []`` creates an empty list called ``a_list``
* ``self.assertEqual(a_list, [])`` confirms that ``a_list`` is empty since it is equal to ``[]``
* ``for element in collection:`` uses a `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ statement to create a loop that goes over every element of ``collection``
* ``a_list.append(element)`` adds the element from ``collection`` to ``a_list`` on each cycle of the loop, using the ``append`` :doc:`method </functions/functions>`, see :doc:`/data_structures/lists` for more details

the terminal shows an :doc:`/exceptions/AssertionError` because ``a_list`` is no longer empty, it contains 10 elements after the loop runs

.. code-block:: python

  E    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change the values in the test to match the result

.. code-block:: python

  def test_creating_a_list_from_an_iterable(self):
      collection = range(10)
      a_list = []
      self.assertEqual(a_list, [])

      for element in collection:
          a_list.append(element)
      self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

and the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I add another test to check what happens when I use the :doc:`list </data_structures/lists>` constructor on ``collection``

  .. code-block:: python

      self.assertEqual(list(collection), a_list)

  the tests pass because calling ``list`` on an ``iterable`` creates a :doc:`list </data_structures/lists>`
* I add another test

  .. code-block:: python

      self.assertEqual(
          list_comprehensions.make_a_list(collection),
          a_list
      )

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ and I add it to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* I add an import statement for ``list_comprehensions`` at the beginning of ``test_list_comprehension.py`` to define the name in the tests

  .. code-block:: python

    import list_comprehensions
    import unittest

  the terminal shows a :doc:`/exceptions/ModuleNotFoundError` which I add to the running list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError

* I create a file called ``list_comprehensions.py`` in the project folder and the terminal shows an :doc:`/exceptions/AttributeError`\ , which I add to the expanding list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError

* then I add a :doc:`function </functions/functions>` definition to ``list_comprehensions.py``

  .. code-block:: python

    def make_a_list():
        return None

  and the terminal shows a :doc:`/exceptions/TypeError`, which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError
    # TypeError

* I change the signature of the function to take in an argument

  .. code-block:: python

    def make_a_list(argument):
        return None

  and the terminal shows an :doc:`/exceptions/AssertionError`
* When I change the function to return the result of calling ``list`` with ``argument`` as input

  .. code-block:: python

    def make_a_list(argument):
        return list(argument)

  the tests pass!

----

How to create a List with a For Loop
-------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``TestListComprehensions``

.. code-block:: python

    def test_creating_a_list_with_a_for_loop(self):
        collection = range(10)
        a_list = []
        self.assertEqual(a_list, [])

        for element in collection:
            a_list.append(element)

        self.assertEqual(a_list, [])
        self.assertEqual(
            list_comprehensions.for_loop(collection),
            a_list
        )

the terminal shows an :doc:`/exceptions/AssertionError` for the values of ``a_list`` after I loop through ``collection`` and add elements because it is no longer empty

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the values of the test to match the result

  .. code-block:: python

    def test_creating_a_list_with_a_for_loop(self):
        collection = range(10)
        a_list = []
        self.assertEqual(a_list, [])

        for element in collection:
            a_list.append(element)

        self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(
            list_comprehensions.for_loop(collection),
            a_list
        )

  the terminal shows an :doc:`/exceptions/AttributeError` since ``list_comprehensions.py`` does not have a definition for ``for_loop``

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'for_loop'

* I add a function definition for ``for_loop`` to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop():
        return None

  and the terminal shows a :doc:`/exceptions/TypeError` because the function signature does not match the call in the test

  .. code-block:: python

    TypeError: for_loop() takes 0 positional arguments but 1 was given

* I change the signature of the function to take in an input argument

  .. code-block:: python

    def for_loop(argument):
        return None

  and the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* I change the behavior of the function to use a ``for`` loop

  .. code-block:: python

    def for_loop(argument):
        result = []
        for element in argument:
            result.append(element)
        return result

  - ``result = []`` creates an empty list called ``result``
  - ``for element in argument:`` creates a loop over the elements of ``argument`` which is an `iterable <https://docs.python.org/3/glossary.html#term-iterable>`_ passed into the function
  - ``result.append(element)`` adds each element from ``argument`` to the list called ``result``
  - ``return result`` returns ``result`` after the loop completes

  the terminal shows all tests are passing

How to create a List with List Comprehensions
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``TestListComprehensions``

.. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
        collection = range(10)
        a_list = []
        self.assertEqual(a_list, [])

        for element in collection:
            a_list.append(element)

        self.assertEqual(a_list, [])
        self.assertEqual([], a_list)
        self.assertEqual(
            list_comprehensions.list_comprehension(collection),
            a_list
        )

the terminal shows an :doc:`/exceptions/AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the values to make it match the result

  .. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
        collection = range(10)
        a_list = []
        self.assertEqual(a_list, [])

        for element in collection:
            a_list.append(element)

        self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual([], a_list)
        self.assertEqual(
            list_comprehensions.list_comprehension(collection),
            a_list
        )

  and the terminal shows another :doc:`/exceptions/AssertionError` for the next line

  .. code-block:: python

    AssertionError: Lists differ: [] != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

* this time I add a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to the left side to practice writing it

  .. code-block:: python

    def test_creating_lists_with_list_comprehensions(self):
        collection = range(10)
        a_list = []
        self.assertEqual(a_list, [])

        for element in collection:
            a_list.append(element)

        self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual([element for element in collection], a_list)
        self.assertEqual(
            list_comprehensions.list_comprehension(collection),
            a_list
        )

  the terminal now shows an :doc:`/exceptions/AttributeError` for the last line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'list_comprehension'

* I add a function that uses a list comprehension to ``list_comprehensions.py``

  .. code-block:: python

    def list_comprehension(argument):
        return [element for element in argument]

  and all tests pass

----

I just created two functions, one that uses a traditional `for <https://docs.python.org/3/tutorial/controlflow.html?highlight=control%20flow#for-statements>`_ loop and another that uses a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to do the same thing. The difference between

.. code-block:: python

    a_list = []
    for element in collection:
        a_list.append()

and

.. code-block:: python

    [element for element in collection]

Is that in the first case I have to

* create a list
* loop through the iterable
* add the items I want from the iterable to the list

With the list comprehension I can get the same result with less words, lines and steps

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There is more I can do with a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_


* I add a failing test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_with_conditions_i(self):
        collection = range(10)

        even_numbers = []
        self.assertEqual(even_numbers, [])

        for element in collection:
            if element % 2 == 0:
                even_numbers.append(element)

        self.assertEqual(even_numbers, [])
        self.assertEqual(
            [],
            even_numbers
        )
        self.assertEqual(
            list_comprehensions.get_even_numbers(collection),
            even_numbers
        )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != []

  - ``if element % 2 == 0:`` checks if the element in ``collection`` leaves a remainder of ``0`` when divided by ``2``
  - ``%`` is a `modulo <https://en.wikipedia.org/wiki/Modulo>`_ operator which divides the number on the left by the number on the right and gives a remainder
  - ``even_numbers.append(element)`` adds ``element`` to ``even_numbers`` if ``element`` divided by ``2`` leaves a remainder of ``0``

* I add the values of the result to the test to make it pass

  .. code-block:: python

      def test_list_comprehensions_with_conditions_i(self):
          collection = range(10)

          even_numbers = []
          self.assertEqual(even_numbers, [])

          for element in collection:
              if element % 2 == 0:
                  even_numbers.append(element)

          self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
          self.assertEqual(
              [],
              even_numbers
          )
          self.assertEqual(
              list_comprehensions.get_even_numbers(collection),
              even_numbers
          )

  and the terminal shows an :doc:`/exceptions/AssertionError` for the next line

  .. code-block:: python

    AssertionError: Lists differ: [] != [0, 2, 4, 6, 8]

* I try using a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ like I did in the last example

  .. code-block:: python

      def test_list_comprehensions_with_conditions_i(self):
          collection = range(10)

          even_numbers = []
          self.assertEqual(even_numbers, [])

          for element in collection:
              if element % 2 == 0:
                  even_numbers.append(element)

          self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
          self.assertEqual(
              [element for element in collection],
              even_numbers
          )
          self.assertEqual(
              list_comprehensions.get_even_numbers(collection),
              even_numbers
          )

  and get an :doc:`/exceptions/AssertionError` because the lists are not the same, I have too many values

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

* When I add the ``if`` condition to the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

  .. code-block:: python

    self.assertEqual(
        [element for element in collection if element % 2 == 0],
        even_numbers
    )

  the terminal shows an :doc:`/exceptions/AttributeError` for the next line. Progress

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_even_numbers'

* I add a function definition to ``list_comprehensions.py`` using the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ I just wrote

  .. code-block:: python

    def get_even_numbers(argument):
        return [element for element in argument if element % 2 == 0]

  and the terminal shows passing tests, Hooray!
* I want to try another `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ with a different condition so I add a test to ``TestListComprehensions``

  .. code-block:: python

    def test_list_comprehensions_with_conditions_ii(self):
        collection = range(10)
        odd_numbers = []
        self.assertEqual(odd_numbers, [])

        for element in collection:
            if element % 2 != 0:
                odd_numbers.append(element)

        self.assertEqual(odd_numbers, [])
        self.assertEqual([], odd_numbers)
        self.assertEqual(
            list_comprehensions.get_odd_numbers(collection),
            odd_numbers
        )

  the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 3, 5, 7, 9] != []

* when I change the values to match

  .. code-block:: python

    def test_list_comprehensions_with_conditions_ii(self):
        collection = range(10)
        odd_numbers = []
        self.assertEqual(odd_numbers, [])

        for element in collection:
            if element % 2 != 0:
                odd_numbers.append(element)

        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
        self.assertEqual([], odd_numbers)
        self.assertEqual(
            list_comprehensions.get_odd_numbers(collection),
            odd_numbers
        )

  the terminal shows an :doc:`/exceptions/AssertionError` for the next test

  .. code-block:: python

    AssertionError: Lists differ: [] != [1, 3, 5, 7, 9]

* I change the value on the left with a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ that uses the same condition I used to create even numbers

  .. code-block:: python

    self.assertEqual(
        [element for element in collection if element % 2 == 0],
        odd_numbers
    )

  and the terminal shows an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 2, 4, 6, 8] != [1, 3, 5, 7, 9]

* When I change the logic in the condition so it uses not equal to ``0`` instead

  .. code-block:: python

    self.assertEqual(
        [element for element in collection if element % 2 != 0],
        odd_numbers
    )

  the terminal shows an :doc:`/exceptions/AttributeError` for the next line

  .. code-block:: python

    AttributeError: module 'list_comprehensions' has no attribute 'get_odd_numbers'

* Then I define a function that returns a list comprehension in ``list_comprehensions.py``

  .. code-block:: python

    def get_odd_numbers(argument):
        return [element for element in argument if element % 2 != 0]

  and the terminal shows all tests passed

----

If you typed along you now know a couple of ways to loop through ``iterables`` and have your program make decisions by using ``conditions``.

You also know how to do it with less words using `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_. Congratulations! Your magic powers are growing.

:doc:`/code/list_comprehensions`