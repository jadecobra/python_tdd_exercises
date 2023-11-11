
Create a Calculator using Test Driven Development
==================================================

In this chapter I explore creating a calculator with python using Test Driven Development

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment` with ``calculator`` as the project name

----

Add Tests
---------

I add a TODO list to ``test_calculator.py`` to keep track of requirements for the calculator

.. code-block:: python

   import unittest


   class TestCalculator(unittest.TestCase):

       def test_failure(self):
           self.assertTrue(True)

   # TODO
   # test importing
   # test addition
   # test subtraction
   # test multiplication
   # test division

   # Exceptions Encountered
   # AssertionError

the terminal responds to the change, with one passing from :doc:`How to Setup a Test Driven Development Environment`

.. code-block:: python

   ==================== 1 passed in 0.01s ======================

   Change detected: tests/test_calculator.py

   [TODAYS_DATE] Running: py.test
   ===================== test session starts ===================
   platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION>, pytest-<VERSION>, pluggy-<VERSION>
   rootdir: <YOUR_PATH>/calculator
   collected 1 item

   tests/test_calculator.py .                                                                                                    [100%]

   ==================== 1 passed in 0.00s ======================

Test Imports
------------

I add an import statement for the ``calculator`` module

.. code-block:: python

   import calculator
   import unittest


   class TestCalculator(unittest.TestCase):

       def test_failure(self):
           self.assertTrue(True)

   # TODO
   # test importing
   # test addition
   # test subtraction
   # test multiplication
   # test division

   # Exceptions Encountered
   # AssertionError

since the test passes I can remove ``test importing`` from the TODO list

----

Test Addition
-------------


RED: make it fail
^^^^^^^^^^^^^^^^^


* I add a method called ``test_addition`` to the ``TestCalculator`` class

  .. code-block:: python

    import unittest
    import calculator


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertTrue(True)

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )

    # TODO
    # test addition
    # test subtraction
    # test multiplication
    # test division

    # Exceptions Encountered
    # AssertionError


  - I call a new testing method from the ``unittest.TestCase`` class called ``assertEqual`` which checks if its 2 inputs are equal. It is similar to the statement ``assert x == y`` or asking ``is x equal to y?``
  - there are two things passed to the ``assertEqual`` method for evaluation in this case

    * first - ``calculator.add(0, 1)`` - where I give the values ``0`` and ``1`` as inputs to the addition function
    * second - ``1`` - the expected result from calling ``calculator.add`` when it is given ``0`` and ``1`` as inputs
    * my expectation is that ``calculator.add(0, 1)`` is equal to ``1``


* the terminal updates to show an :doc:`AttributeError`

  .. code-block:: python

    ...
    collected 2 items

    tests/test_calculator.py F.                                     [100%]

    =========================== FAILURES =================================
    __________________ TestCalculator.test_addition ______________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

        def test_addition(self):
            self.assertEqual(
    >           calculator.add(0, 1),
                1
            )
    E       AttributeError: module 'calculator' has no attribute 'add'

    tests/test_calculator.py:12: AttributeError
    ==================== short test summary info =========================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - AttributeError: module 'calculator' has no attribute 'add'
    ================== 1 failed, 1 passed in 0.02s =======================

  - The error is an ``AttributeError`` at line 12 in ``test_calculator.py``
  - An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when trying to access or call an attribute that python cannot find
  - I think of ``calculator.add`` as an address

    * ``calculator`` refers to ``calculator.py``
    * ``add`` refers to something(an attribute) within the ``calculator.py`` file


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I open ``calculator.py`` in the Interactive Development Environment (IDE) and add the name ``add``

  .. code-block:: python

       add

  the terminal updates to show a ``NameError`` because ``add`` is not defined, there is no assignment to the name

  .. code-block:: python

       E   NameError: name 'add' is not defined

* I update the list of exceptions encountered with ``NameError``

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError

* I assign the name ``add`` to the null value ``None``

  .. code-block:: python

       add = None

  the terminal displays a :doc:`TypeError`

  .. code-block:: python

       E       TypeError: 'NoneType' object is not callable

  The ``AttributeError`` was fixed by declaring a variable ``add`` in the ``calculator`` module, even though it is currently assigned to the null value ``None``

* The new error is :doc:`TypeError` which can occur when an ``object`` is used in a way that it is not supposed to be used. In this case the ``add`` variable is not callable. I update the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError

* I have to define ``add`` as a :doc:`function <functions>` or a :doc:`class <classes>` to make it callable. I know the ``def`` keyword is used for creating :doc:`functions` and will test changing the ``add`` variable in ``calculator.py`` to a :doc:`function <functions>`

  .. code-block:: python

    def add():
        return None

  the terminal still shows a :doc:`TypeError` but with a different message. Progress!

  .. code-block:: python

       E       TypeError: add() takes 0 positional arguments but 2 were given

* This :doc:`TypeError` indicates that the current definition of the ``add`` function takes in no arguments but I provided 2 in the call in the test ``calculator.add(0, 1)``, since part of the requirement is that the ``add`` function should take in two numbers, I will update it in ``calculator.py`` to match

  .. code-block:: python

       def add(x, y):
           return None

  the terminal now displays an :doc:`AssertionError`

  .. code-block:: python

       E       AssertionError: None != 1

  - An ``AssertionError`` was the first error I encountered in :doc:`How to Setup a Test Driven Development Environment` after adding a test for failure, and is raised when an assertion is ``False``.
  - Since I am using ``self.assertEqual`` it means the two inputs are not equal. In other words ``calculator.add(0, 1)`` is currently not equal to ``1``.

* I update the ``add`` function in ``calculator.py`` so it gives the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  Eureka! The test passes. Time for a victory lap.

  .. code-block:: python

    tests/test_calculator.py ..                             [100%]

    ===================== 2 passed in 0.01s ======================


REFACTOR: Make it Better
^^^^^^^^^^^^^^^^^^^^^^^^

Wait a minute. Is it that easy? Do I just provide the solution to make it pass? In the green phase, yes. I do whatever it takes to make the test pass even if I have to cheat.

Solving the problem this way reveals a problem with the test, which means I need to "Make it Better".

There are a few scenarios to consider from a user's perspective.

* If a user tries to add other numbers that are not 0 and 1, the calculator will return 1.
* If they also try to add negative numbers, it will still return 1.
* The function always returns 1 no matter what inputs the user gives.

Even though the add function currently passes the existing test it still does not meet the actual requirement.

* I remove ``test_failure`` from ``test_calculator.py`` since it is no longer needed

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                calculator.add(0, 1),
                1
            )

* RED: make it fail

  I add a new test to ``test_addition`` in ``test_calculator.py``

  .. code-block:: python

    def test_addition(self):
        self.assertEqual(
            calculator.add(0, 1),
            1
        )
        self.assertEqual(
            calculator.add(-1, 1),
            0
        )

  the terminal responds with an :doc:`AssertionError`, confirmation that the ``add`` function always returns ``1`` no matter what inputs are given

  .. code-block:: python

    E       AssertionError: 1 != 0

* GREEN: make it pass

  I change the ``add`` function in ``calculator.py`` to add up the inputs

  .. code-block:: python

       def add(x, y):
           return x + y

  and the terminal displays passing tests, increasing my confidence in the ``add`` function

  .. code-block:: python

    tests/test_calculator.py ..                      [100%]

    ====================== 2 passed in 0.01s ==============

* REFACTOR: make it better

  I can use random inputs to test that the function behaves the way I expect for any given numbers. I will update ``test_calculator.py`` to use python's `random <https://docs.python.org/3/library/random.html?highlight=random#module-random>`_ library to generate random integers between -1 and 1 to represent negative numbers, zero and positive numbers

  .. code-block:: python

    import calculator
    import random
    import unittest

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.add(x, y),
                x+y
            )

  - I assign a variable called ``x`` to a random integer between -1 and 1 to represent the case of negative numbers, zero and positive numbers
  - I assign a variable called ``y`` to a random integer between -1 and 1 to represent the case of negative numbers, zero and positive numbers
  - I test that when these two variables are given to the ``add`` function as inputs it returns the sum of the 2 variables as output

  the terminal still displays passing tests

  .. code-block:: python

    tests/test_calculator.py ..                             [100%]

    ================ 2 passed in 0.01s ===========================

  - I no longer need the previous tests because this new test covers the scenarios for zero, negative and positive numbers
  - I can remove ``test addition`` from the TODO list since it passed, marking the task as completed

  .. code-block:: python

     # TODO
     # test subtraction
     # test multiplication
     # test division


This is the Test Driven Development cycle in practice: RED GREEN REFACTOR

* **RED**: make it fail - I write a failing test
* **GREEN**: make it pass - I make the test pass by any means necessary
* **REFACTOR**: make it better

I repeat the process until I have a working program that has been tested and gives me confidence it will behave in an expected way that meets the requirements of the program

----

Test Subtraction
----------------

I will now add a failing test since addition works and the next action item from the TODO list is to test subtraction,

RED : make it fail
^^^^^^^^^^^^^^^^^^


* I update ``test_calculator.py`` with a method called ``test_subtraction``

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.add(x, y),
                x+y
            )

        def test_subtraction(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.assertEqual(
                calculator.subtract(x, y),
                x-y
            )

  the terminal responds with an :doc:`AttributeError`

  .. code-block:: python

             self.assertEqual(
     >           calculator.subtract(x, y),
                 x-y
             )
     E       AttributeError: module 'calculator' has no attribute 'subtract'

GREEN : make it pass
^^^^^^^^^^^^^^^^^^^^


* I add a variable assignment in ``calculator.py``

  .. code-block:: python

    def add(x, y):
        return x + y

    subtract = None

  and the terminal shows a :doc:`TypeError`

  .. code-block:: python

       E       TypeError: 'NoneType' object is not callable

* I change the definition of the ``subtract`` variable to make it callable

  .. code-block:: python

    def add(x, y):
        return x + y

    def subtract():
        return None

  and the terminal displays a :doc:`TypeError` with a different error message

  .. code-block:: python

       E       TypeError: subtract() takes 0 positional arguments but 2 were given

* I change the definition of the ``subtract`` function to match the expectation

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return None

  and the terminal responds with an :doc:`AssertionError`

  .. code-block:: python

       >       self.assertEqual(
                   calculator.subtract(x, y),
                   x-y
               )
       E       AssertionError: None != 0

* I update the ``subtract`` function in ``calculator.py`` to perform a subtraction operation on its inputs

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return x - y

  and all the tests pass - SUCCESS!

  .. code-block:: python

    tests/test_calculator.py ...                          [100%]

    ======================= 3 passed in 0.01s ==================

* ``test subtraction`` can now be removed from the TODO list

  .. code-block:: python

    # TODO
    # test multiplication
    # test division


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* There is some duplication to remove so I `Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

  - ``x = random.randint(-1, 1)`` happens twice
  - ``y = random.randint(-1, 1)`` happens twice

* I could update the ``TestCalculator`` class in ``test_calculator.py`` to create the random variables only once by using class variables and reference the variables in the tests

  .. code-block:: python

    import calculator
    import random
    import unittest


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

  - all tests are still passing, so my change did not break anything
  - The ``x`` and ``y`` variables are now initialized once as class attributes and can be accessed later in every test using ``self.x`` and ``self.y`` the same way I can call ``unittest.TestCase`` methods like ``assertEqual`` by typing ``self.assertEqual``


----

Test Multiplication
-------------------

Moving on to test multiplication, the next item on the TODO list

RED : make it fail
^^^^^^^^^^^^^^^^^^

I add a failing test called ``test_multiplication`` to ``test_calculator.py``

.. code-block:: python

  import unittest
  import calculator
  import random


  class TestCalculator(unittest.TestCase):

     x = random.randint(-1, 1)
     y = random.randint(-1, 1)

     def test_addition(self):
         self.assertEqual(
             calculator.add(self.x, self.y),
             self.x+self.y
         )

     def test_subtraction(self):
         self.assertEqual(
             calculator.subtract(self.x, self.y),
             self.x-self.y
         )

     def test_multiplication(self):
         self.assertEqual(
             calculator.multiply(self.x, self.y),
             self.x*self.y
         )

the terminal responds with an :doc:`AttributeError`

GREEN : make it pass
^^^^^^^^^^^^^^^^^^^^

using what I know so far I update ``calculator.py`` with a definition for multiplication

.. code-block:: python

   def add(x, y):
       return x + y

   def subtract(x, y):
       return x - y

   def multiply(x, y):
       return x * y

SUCCESS! The terminal shows passing tests and I remove ``test_multiplication`` from the TODO list

.. code-block:: python

   # TODO
   # test division

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I cannot think of a way to make the code better so I move on to the final test from the TODO list - division

----

Test Division
-------------

RED : make it fail
^^^^^^^^^^^^^^^^^^

I update ``test_calculator.py`` with ``test_division``

.. code-block:: python

    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_addition(self):
            self.assertEqual(
                calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                calculator.subtract(self.x, self.y),
                self.x-self.y
            )

        def test_multiplication(self):
            self.assertEqual(
                calculator.multiply(self.x, self.y),
                self.x*self.y
            )

        def test_division(self):
            self.assertEqual(
                calculator.divide(self.x, self.y),
                self.x/self.y
            )

once again the terminal outputs an :doc:`AttributeError`


GREEN : make it pass
^^^^^^^^^^^^^^^^^^^^


* I update ``calculator.py`` with a ``divide`` function

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return x - y

       def multiply(x, y):
           return x * y

       def divide(x, y):
           return x / y

  the terminal response varies since I am using random variables, When ``y`` is 0 I get a `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ like below

  .. code-block:: python

     x = 1, y = 0

         def divide(x, y):
     >       return x / y
     E       ZeroDivisionError: division by zero

* I add ``ZeroDivisionError`` to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # ZeroDivisionError

How to Test for Errors
----------------------

RED : make it fail
^^^^^^^^^^^^^^^^^^

I am going to add a failing test to ``test_calculator.py`` to intentionally trigger a ``ZeroDivisionError`` and comment out the previous test that sometimes fails, this helps me remove the variability of the test for some time while I figure out the error

.. code-block:: python

    def test_division(self):
        self.assertEqual(
            calculator.divide(self.x, 0),
            self.x/0
        )
        # self.assertEqual(
        #     calculator.divide(self.x, self.y),
        #     self.x/self.y
        # )

the terminal confirms my expectations with a failure for any value of ``x`` when ``y`` is 0

.. code-block:: python

   x = 0, y = 0

       def divide(x, y):
   >       return x / y
   E       ZeroDivisionError: division by zero

GREEN : make it pass
--------------------

I can use the ``unittest.TestCase.assertRaises`` :doc:`method <functions>` in ``test_division`` to confirm that a ``ZeroDivisionError`` is raised when I try to divide a number by ``0``

.. code-block:: python

   def test_division(self):
       with self.assertRaises(ZeroDivisionError):
           calculator.divide(self.x, 0)
       # self.assertEqual(
       #     calculator.divide(self.x, self.y),
       #     self.x/self.y
       # )

the terminal displays passing tests, and I now have a way to ``catch`` Exceptions when testing, allowing me to confirm that the code raises an error, and the other tests can continue when they encounter the expected failure

REFACTOR: make it better
------------------------

I update ``test_division`` to test other division cases when the divisor is not 0 by making sure the random variable ``y`` is never 0

.. code-block:: python

   def test_division(self):
       with self.assertRaises(ZeroDivisionError):
           calculator.divide(self.x, 0)
       while self.y == 0:
           self.y = random.randint(-1, 1)
       self.assertEqual(
           calculator.divide(self.x, self.y),
           self.x/self.y
       )


* ``while self.y == 0:`` creates a loop that repeats whatever indented code follows as long as ``self.y`` is equal to ``0``
* ``self.y = random.randint(-1, 1)`` assigns a new random variable to ``self.y`` that could be -1, 0 or 1
* the loop tells python to assign a new random variable to ``self.y`` as long as ``self.y`` is equal to 0
* I remove ``test_division`` from the TODO list since all the tests pass

----

CONGRATULATIONS! You made it through writing a program that can perform the 4 basic arithmetic operations using Test Driven Development. What would you like to do next?
