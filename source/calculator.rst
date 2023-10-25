Create a Calculator using Test Driven Development
=================================================

We are going to explore creating a calculator with python using Test Driven Development

Prerequisites
-------------


:doc:`How I setup a Test Driven Development Environment` with ``calculator`` as the project name

----

Add Tests
---------

add a TODO list to ``test_calculator.py`` to keep track of what we are doing

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

the terminal responds to our change, with the one test still passing from :doc:`How I setup a Test Driven Development Environment`

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

add an import statement for the ``calculator`` module we are working on

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

since the test passes we can remove ``test importing`` from our TODO list

----

Test Addition
-------------

Moving on to the next item we test for addition

RED: make it fail
^^^^^^^^^^^^^^^^^


* add a method named ``test_addition`` to the ``TestCalculator`` class

.. code-block:: python
    import unittest
    import calculator

.. code-block::

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
   ```
   - we call a new testing method from the `unittest.TestCase` class ``assertEqual`` which checks if 2 things are equal. It is similar to the statement `assert x == y` or asking `is x equal to y?`
   - there are two things passed to the ``assertEqual`` method for evaluation in this case
       - first - `calculator.add(0, 1)` - where we give the values ``0`` and ``1`` as inputs to our addition function
       - second - ``1`` - our expected result from `calculator.add` when it is given ``0`` and ``1``
       - our expectation is that `calculator.add(0, 1) is equal to 1`


*
  the terminal updates to show an :doc:`AttributeError`

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

    What does this mean?


  * The error is an ``AttributeError`` at line 12 in ``test_calculator.py``
  * An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when we try to access or call an attribute that python cannot find
  * we can think of ``calculator.add`` as an address

    * ``calculator`` refers to ``calculator.py``
    * ``add`` refers to something(an attribute) within the ``calculator.py`` file

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* open ``calculator.py`` in your Interactive Development Environment (IDE) and add the name ``add``

  .. code-block:: python

       add

  the terminal updates to show a ``NameError`` because ``add`` is not defined, there is no assignment to the name

  .. code-block:: python

       E   NameError: name 'add' is not defined

* update our list of exceptions encountered with ``NameError``

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError

* assign the name ``add`` to the null value ``None``

  .. code-block:: python

       add = None

  the terminal displays a new error

  .. code-block:: python

       E       TypeError: 'NoneType' object is not callable

* The ``AttributeError`` was fixed by declaring a variable ``add`` in the ``calculator`` module, even though it is currently assigned to the null value ``None``

* The new error is :doc:`TypeError` which can occur when an ``object`` is used in a way that it was not intended for. In this case the ``add`` variable is not callable. Let us update our list of exceptions encountered

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError
       # TypeError

* To make it callable we have to define it as a :doc:`functions` or a :doc:`class`. Testing the ``def`` keyword for creating functions we update our add variable in ``calculator.py`` to

  .. code-block:: python

       def add():
           return None

  the terminal still shows a :doc:`TypeError` but with a different message. Progress

  .. code-block:: python

       E       TypeError: add() takes 0 positional arguments but 2 were given

* This ``TypeError`` indicates that the current definition of the ``add`` function takes in no arguments but we provided 2 in our call, since part of our requirement is that the ``add`` function should take in two numbers, we will update it in ``calculator.py`` to match

  .. code-block:: python

       def add(x, y):
           return None

  the terminal updates to show an :doc:`AssertionError`

  .. code-block:: python

       E       AssertionError: None != 1

  An ``AssertionError`` was the first error we encountered in :doc:`How I setup a Test Driven Development Environment` after adding a test for failure.

  It is raised when an assertion is ``False``, since we are using ``self.assertEqual`` it means the two things we provided as inputs are not equal. In other words ``calculator.add(0, 1)`` is currently not equal to ``1``. Let us update the ``add`` function in ``calculator.py`` so it gives the expected value

  .. code-block:: python

       def add(x, y):
           return 1

    Eureka! The test passes. Time for a victory lap.

  .. code-block:: python

       tests/test_calculator.py ..                             [100%]

       ===================== 2 passed in 0.01s ======================

REFACTOR: Make it Better
^^^^^^^^^^^^^^^^^^^^^^^^

Wait a minute. Is it that easy? Do we just provide the solution to make it pass? In the green phase, yes. We do whatever it takes to make the test pass even if we have to cheat. Solving the problem this way reveals a problem with our test, which means we need to "Make it Better".

There are a few scenarios we can consider from the users' perspective. If our users try to add other numbers that are not 0 and 1, the calculator will return 1. If they also try to add negative numbers, it will still return 1. The function always returns 1 regardless of the inputs the user gives. Even though the add function currently passes our existing test it still does not meet the actual requirement.


* remove ``test_failure`` from ``test_calculator.py`` since we no longer need it

  .. code-block:: python

       class TestCalculator(unittest.TestCase):

           def test_addition(self):
               self.assertEqual(
                   calculator.add(0, 1),
                   1
               )

* RED: make it fail

    add a new test to ``test_addition`` in ``test_calculator.py``

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

  the terminal responds with an :doc:`AssertionError` confirming that the ``add`` function always returns ``1`` regardless of inputs

  .. code-block:: python

       E       AssertionError: 1 != 0

* GREEN: make it pass

  update the ``add`` function in ``calculator.py`` to add up the inputs

  .. code-block:: python

       def add(x, y):
           return x + y

  and the terminal displays passing tests, increasing our confidence in the ``add`` function

  .. code-block:: python

       tests/test_calculator.py ..                      [100%]

       ====================== 2 passed in 0.01s ==============

* REFACTOR: make it better

  we can randomize the inputs to test that the function behaves the way we expect for any given numbers. Update ``test_calculator.py`` to use python's `random <https://docs.python.org/3/library/random.html?highlight=random#module-random>`_ library

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

   - we assign a variable named ``x`` to a random integer between -1 and 1 to represent the case of negative numbers, zero and positive numbers
   - we assign a variable named ``y`` to a random integer between -1 and 1 just like above
   - we test that when these two variables are given to the ``add`` function as inputs it returns the sum of the 2 variables as output

  the terminal still displays passing tests

.. code-block:: python

   tests/test_calculator.py ..                             [100%]

   ================ 2 passed in 0.01s ===========================

   - we no longer need the previous tests because this new test covers the scenarios for zero, negative and positive numbers
   - we can remove `test addition` from our TODO list since it passed, marking the task as completed

.. code-block:: python

   # TODO
   # test subtraction
   # test multiplication
   # test division


That's the Test Driven Development pattern at work RED GREEN REFACTOR

We make a test that fails, then make it pass by any means necessary, and make it better, repeating the process until we have a working program that has been tested and gives us confidence it will behave in an expected way

----

Test Subtraction
----------------

We will now add a failing test since addition works and our next action item from the TODO list is to test subtraction,

RED : make it fail
^^^^^^^^^^^^^^^^^^


* update ``test_calculator.py`` with a method named ``test_subtraction``

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


* add a variable assignment to ``calculator.py``

  .. code-block:: python

       def add(x, y):
           return x + y

       subtract = None

  and the terminal gives us a :doc:`TypeError`

  .. code-block:: python

       E       TypeError: 'NoneType' object is not callable

* change the definition of the ``subtract`` variable to make it callable

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract():
           return None

  the terminal displays a :doc:`TypeError` with a different error message

  .. code-block:: python

       E       TypeError: subtract() takes 0 positional arguments but 2 were given

* we change the definition of the ``subtract`` function to match our expectation

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return None

  the terminal responds with an :doc:`AssertionError`

  .. code-block:: python

       >       self.assertEqual(
                   calculator.subtract(x, y),
                   x-y
               )
       E       AssertionError: None != 0

* we update the ``subtract`` function in ``calculator.py`` to perform an operation on its inputs

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return x - y

  all tests passed - SUCCESS!

  .. code-block:: python

       tests/test_calculator.py ...                          [100%]

       ======================= 3 passed in 0.01s ==================

* ``test subtraction`` can now be removed from our TODO list

  .. code-block:: python

       # TODO
       # test multiplication
       # test division

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* How can we make this better? Is there any duplication that could be removed?

  - ``x = random.randint(-1, 1)`` happens twice
  - ``y = random.randint(-1, 1)`` happens twice

* we could update the ``TestCalculator`` class in ``test_calculator.py`` to create the random variables once


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

  our ``x`` and ``y`` variables are now initialized once as class attributes that can be referenced later in every test using `self.x` and `self.y`, the terminal shows all tests are still passing


----

Test Multiplication
-------------------

Moving on to test multiplication, the next item on the TODO list

RED : make it fail
^^^^^^^^^^^^^^^^^^

add a failing test to ``test_calculator.py`` named ``test_multiplication``

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

using what we know so far we update ``calculator.py`` with a definition for multiplication

.. code-block:: python

   def add(x, y):
       return x + y

   def subtract(x, y):
       return x - y

   def multiply(x, y):
       return x * y

SUCCESS! The terminal shows passing tests and we remove ``test_multiplication`` from the TODO list

.. code-block:: python

   # TODO
   # test division

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Can you think of a way to make the code better?

----

Test Division
-------------

On to the final test from the TODO list - division

RED : make it fail
^^^^^^^^^^^^^^^^^^


* update ``test_calculator.py`` with ``test_division``

.. code-block:: python

    import unittest
    import calculator
    import random


    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        def test_failure(self):
            self.assertTrue(True)

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

  once again the terminal outputs an [AttributeError](./AttributeError.rst)


GREEN : make it pass
^^^^^^^^^^^^^^^^^^^^


* update ``calculator.py`` with a ``divide`` function

  .. code-block:: python

       def add(x, y):
           return x + y

       def subtract(x, y):
           return x - y

       def multiply(x, y):
           return x * y

       def divide(x, y):
           return x / y

  here our terminal response varies, When ``y`` is 0 we get a `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ like below

.. code-block:: python

   x = 1, y = 0

       def divide(x, y):
   >       return x / y
   E       ZeroDivisionError: division by zero

* add ``ZeroDivisionError`` to the list of exceptions encountered

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # NameError
       # TypeError
       # ZeroDivisionError

Test for Errors
---------------

RED : make it fail
^^^^^^^^^^^^^^^^^^

add a failing test to ``test_calculator.py`` to intentionally trigger a ``ZeroDivisionError`` and comment out our previous test that sometimes fails, this helps us remove the variability of the test

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

the terminal confirms our expectations with a failure for any value of ``x``

.. code-block:: python

   x = 0, y = 0

       def divide(x, y):
   >       return x / y
   E       ZeroDivisionError: division by zero

GREEN : make it pass
--------------------

update ``test_calculator.py`` to confirm that a ``ZeroDivisionError`` is raised when we try to divide a number by ``0`` by using ``self.assertRaises``

.. code-block:: python

   def test_division(self):
       with self.assertRaises(ZeroDivisionError):
           calculator.divide(self.x, 0)
       # self.assertEqual(
       #     calculator.divide(self.x, self.y),
       #     self.x/self.y
       # )

the terminal displays passing tests, and we now have a way to ``catch`` Exceptions when testing, allowing us to confirm that the code raises an error, and the other tests to continue when they encounter the expected failure

REFACTOR: make it better
------------------------

update ``test_division`` to test other division cases when the divisor is not 0 by making sure our random variable ``y`` is never 0

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
* ``self.y = random.randint(-1, 1)`` assigns a random variable to ``self.y`` that could be -1, 0 or 1
* our loop tells python to assign a new random variable to ``self.y`` as long as ``self.y`` is equal to 0
* remove ``test_division`` from the TODO list since all the tests pass

----

CONGRATULATIONS! You made it through writing a program that can perform the 4 basic arithmetic operations using Test Driven Development. What would you like to do next?
