
List Comprehensions
===================

We will cover ``list comprehensions`` in python using Test Driven Development

Prerequisites
-------------


* :doc:`How I setup a Test Driven Development Environment`

----

Creating a List with an Iterable
--------------------------------

List comprehensions are a way to create lists from another iterable. It is a nice way to loop over elements and perform some operation

RED: make it fail
^^^^^^^^^^^^^^^^^

add a file named ``test_list_comprehension.py`` to the ``tests`` folder

.. code-block:: python

   import unittest


   class TestListComprehensions(unittest.TestCase):

       def test_creating_a_list_from_an_iterable(self):
           collection_a = range(10)
           list_a = []
           self.assertEqual(list_a, [])

           for element in collection_a:
               list_a.append(element)
           self.assertEqual(list_a, [])


* we create ``collection_a`` which uses the ``range`` object
* the ``range`` object creates an ``iterable`` of numbers from 0 to the number we give minus 1. `read more <https://docs.python.org/3/library/stdtypes.html?highlight=range#range>`_
* we create a list named ``list_a`` that has no elements and confirm it is empty with a ``self.assertEqual(list_a, [])``
* we then create a loop using the ``for`` keyword, that goes over every element of ``collection_a`` and adds it to ``list_a`` using the ``append`` method see :doc:`Lists`
* the terminal updates to show an :doc:`AssertionError` for our test that checks the elements of ``list_a`` after the loop ran, because the list is no longer empty, it now contains 10 elements
  .. code-block:: python

       E       AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != []
       E
       E       First list contains 10 additional elements.
       E       First extra element 0:
       E       0
       E
       E       - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
       E       + []

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update the tests with the expected values

.. code-block:: python

       def test_creating_a_list_from_an_iterable(self):
           collection_a = range(10)
           list_a = []
           self.assertEqual(list_a, [])

           for element in collection_a:
               list_a.append(element)
           self.assertEqual(list_a, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* add another test to check what happens when we call the ``list`` keyword on the ``collection_a`` iterable
  .. code-block:: python

           self.assertEqual(list(collection_a), list_a)
    the tests pass because calling ``list`` on an ``iterable`` creates a :doc:`list`
* add another test
  .. code-block:: python

           self.assertEqual(list_comprehensions.make_a_list(collection_a), list_a)
    the terminal updates to show a ``NameError`` and we add it to our list of exceptions encountered
  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError

* add an import statement for ``list_comprehensions`` at the beginning of ``test_list_comprehension.py`` to define the name in our tests
  .. code-block:: python

       import list_comprehensions
       import unittest
    the terminal displays a :doc:`ModuleNotFoundError` and we add that to our running list of exceptions
  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError
       # ModuleNotFoundError

* create a file named ``list_comprehensions.py`` in the project folder and the terminal updates to show an :doc:`AttributeError`\ , which we add to our expanding list of exceptions encountered
  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError
       # ModuleNotFoundError
       # AttributeError

* we then add a :doc:`functions` definition to ``list_comprehensions.py``
  .. code-block:: python

       def make_a_list():
           return None
    and the terminal updates to show a :doc:`TypeError`\ , updating our list of exceptions encountered to
  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError
       # ModuleNotFoundError
       # AttributeError
       # TypeError

* we update the signature of the function to take in an argument
  .. code-block:: python

       def make_a_list(argument):
           return None
    the terminal shows an :doc:`AssertionError`
* update the function to return a list of whatever argument it gets
  .. code-block:: python

       def make_a_list(argument):
           return list(argument)
    and the tests pass. Phew!

Creating a List with a For Loop
-------------------------------

What if we test creating a list with a for loop like the example above

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test to ``TestListComprehensions``

.. code-block:: python

       def test_creating_a_list_with_a_for_loop(self):
           collection = range(10)
           a_list = []
           self.assertEqual(a_list, [])

           for element in collection:
               a_list.append(element)

           self.assertEqual(a_list, [])
           self.assertEqual(list_comprehensions.for_loop(collection), a_list)

the terminal updates to show an :doc:`AssertionError` for the values of ``a_list`` after we loop through ``collection`` and add elements because it is no longer empty

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


*
  update the right side of the test with the expected values

  .. code-block:: python

           def test_creating_a_list_with_a_for_loop(self):
               collection = range(10)
               a_list = []
               self.assertEqual(a_list, [])

               for element in collection:
                   a_list.append(element)

               self.assertEqual(a_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
               self.assertEqual(list_comprehensions.for_loop(collection), a_list)

    the terminal updates to show an :doc:`AttributeError` since ``list_comprehensions.py`` does not have a definition for ``for_loop``

* we add a function definition for ``for_loop`` to ``list_comprehensions.py``
  .. code-block:: python

       def for_loop():
           return None
    the terminal updates to show a :doc:`TypeError`
* we update the signature of the function to take in an input argument
  .. code-block:: python

       def for_loop(argument):
           return None
    the terminal updates to show an :doc:`AssertionError`
*
  we change the behavior of the function by adding a ``for`` loop

  .. code-block:: python

       def for_loop(argument):
           result = []
           for element in argument:
               result.append(element)
           return result

    in this :doc:`functions`


  * we create an empty list
  * loop over the elements of ``argument`` which is an ``iterable`` passed into the function
  * append each element from ``argument`` to the empty list
  *
    return the result after the loop

    the terminal displays all tests are passing

List Comprehension
------------------

Now that we know how to create a ``list`` using ``[]``, ``list`` and ``for``, What if we try creating a :doc:`list` using a ``list comprehension``. It looks similar to a ``for`` loop but allows us to achieve the same thing with less words

RED: make it fail
^^^^^^^^^^^^^^^^^

add a failing test to ``TestListComprehensions``

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

the terminal updates to show an :doc:`AssertionError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


*
  update the values to make it pass

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

    the terminal updates to show another :doc:`AssertionError` for the next line

*
  this time we add a ``list comprehension`` to the left side to practice writing it

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

    the terminal now outputs an :doc:`AttributeError` for the last line

* update ``list_comprehensions.py`` with a function that uses a list comprehension
  .. code-block:: python

       def list_comprehension(argument):
           return [element for element in argument]
    all tests pass

We just created two functions, one that uses a traditional for loop and another that uses a list comprehension to achive the same thing. The difference between

.. code-block:: python

       a_list = []
       for element in collection:
           a_list.append()

and

.. code-block:: python

       [element for element in collection]

Is in the first case we have to declare a variable, create a loop then update the variable we declared, with the list comprehension we can achieve the same thing with less words/lines

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Let us explore what else we can do with a ``list comprehension``


*
  add a failing test to ``TestListComprehensions``

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

    the terminal updates to show an :doc:`AssertionError`


  * In this loop we update the empty list after the condition ``if element % 2 == 0`` is met.
  * The ``%`` is a modulo operator for modulo division which divides the number on the left by the number on the right and gives the remainder.
  * If the remainder is ``0``, it means the number is divisible by 2 with no remainder meaning its an even number

*
  we update the test with the expected values to make it pass

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

    the terminal updates to show an :doc:`AssertionError`

*
  try using a ``list comprehension`` like we did in the last example

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

    the terminal displays an :doc:`AssertionError` because our lists are not the same, we have too many values

  .. code-block:: python

       AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

    we have not added the ``if`` condition to the ``list comprehension``, let's do that now

  .. code-block:: python

               self.assertEqual(
                   [element for element in collection if element % 2 == 0],
                   even_numbers
               )

    the terminal outputs an :doc:`AttributeError` for the next test

* add a function definition to ``list_comprehensions.py`` using the ``list comprehension`` we just wrote
  .. code-block:: python

       def get_even_numbers(argument):
           return [element for element in argument if element % 2 == 0]
    and the terminal shows passing tests! Hooray
*
  What if we try another ``list comprehension`` with a different condition. Add a test to ``TestListComprehensions``

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
               self.assertEqual(list_comprehensions.get_odd_numbers(collection), odd_numbers)

    the terminal updates to show an :doc:`AssertionError`

*
  when we update the values to match

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
               self.assertEqual(list_comprehensions.get_odd_numbers(collection), odd_numbers)

    the terminal shows an :doc:`AssertionError` for the next test

*
  after updating the value on the left with a ``list comprehension`` that uses the same condition we used to create ``odd_numbers``

  .. code-block:: python

           def test_list_comprehensions_with_conditions_ii(self):
               collection = range(10)
               odd_numbers = []
               self.assertEqual(odd_numbers, [])

               for element in collection:
                   if element % 2 != 0:
                       odd_numbers.append(element)

               self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
               self.assertEqual(
                   [element for element in collection if element % 2 != 0],
                   odd_numbers
               )
               self.assertEqual(list_comprehensions.get_odd_numbers(collection), odd_numbers)

    the terminal updates to show an :doc:`AttributeError`

* define a function that returns a list comprehension in ``list_comprehensions.py`` to make the test pass
  .. code-block:: python

       def get_odd_numbers(argument):
           return [element for element in argument if element % 2 != 0]

*WOW!*

You now know a couple of ways to loop through ``iterables`` and have your program make decisions by using ``conditions``. You also know how to do it with less words using ``list comprehensions``. Well done!
