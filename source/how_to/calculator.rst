
###########################
How to create a Calculator
###########################

In this chapter I will create a basic calculator that performs addition, subtraction, division and multiplication

****************
Prerequisites
****************


:doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``calculator`` as the project name

----


****************
Add Tests
****************

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

the terminal responds to the change, the test from :doc:`How to create a Test Driven Development Environment </how_to/create_tdd_environment>` is still passing

.. code-block:: python

  ==================== 1 passed in 0.01s ======================

  Change detected: tests/test_calculator.py

  [TODAYS_DATE] Running: py.test
  ===================== test session starts ===================
  platform <YOUR_OPERATING_SYSTEM> -- python <YOUR_python_VERSION>, pytest-<VERSION>, pluggy-<VERSION>
  rootdir: <YOUR_PATH>/calculator
  collected 1 item

  tests/test_calculator.py .                                             [100%]

  ==================== 1 passed in 0.00s ======================

****************
Test Imports
****************

I add an import statement for the ``calculator`` module that will contain the source code for the program I am testing

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

since there is no failure I can remove ``test importing`` from the TODO list

----

****************
Test Addition
****************


RED: make it fail
==================


* I add a :doc:`method </functions/functions>` called ``test_addition`` to the ``TestCalculator`` :doc:`class </classes/classes>`

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


  - I use the `assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ :doc:`method </functions/functions>` from the `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`class </classes/classes>` which checks if its 2 inputs are equal. It is similar to the statement ``assert x == y`` or asking ``is x equal to y?``
  - there are two things passed to `assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ for evaluation in this case

  * first - ``calculator.add(0, 1)`` - where I give the values ``0`` and ``1`` as inputs to the addition function
  * second - ``1`` - the expected result from calling ``calculator.add`` when it is given ``0`` and ``1`` as inputs
  * my expectation is that ``calculator.add(0, 1)`` is equal to ``1``


* the terminal shows an :doc:`/exceptions/AttributeError`

  .. code-block:: python

    ...
    collected 2 items

    tests/test_calculator.py F.                 [100%]

    =========================== FAILURES =================================
    __________________ TestCalculator.test_addition ______________________

    self = <tests.test_calculator.TestCalculator testMethod=test_addition>

      def test_addition(self):
        self.assertEqual(
    >      calculator.add(0, 1),
          1
        )
    E    AttributeError: module 'calculator' has no attribute 'add'

    tests/test_calculator.py:12: AttributeError
    ==================== short test summary info =========================
    FAILED tests/test_calculator.py::TestCalculator::test_addition - AttributeError: module 'calculator' has no attribute 'add'
    ================== 1 failed, 1 passed in 0.02s =======================

  - The :doc:`/exceptions/AttributeError` is at line 12 in ``test_calculator.py``
  - An :doc:`/exceptions/AttributeError` is raised when accessing or calling an attribute that python cannot find
  - I think of ``calculator.add`` as an address

  * ``calculator`` refers to ``calculator.py``
  * ``add`` refers to something (an attribute) within the ``calculator.py`` file


GREEN: make it pass
====================

* I open ``calculator.py`` in the Interactive Development Environment (IDE) and type the name ``add``

  .. code-block:: python

    add

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``add`` is not defined (there is no assignment to the name)

  .. code-block:: python

    E  NameError: name 'add' is not defined

* I add the error to the list of exceptions encountered with `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then assign the name ``add`` to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    add = None

  the terminal displays a :doc:`/exceptions/TypeError`

  .. code-block:: python

    E    TypeError: 'NoneType' object is not callable

  The :doc:`/exceptions/AttributeError` was fixed by declaring a variable ``add`` in the ``calculator`` module, even though it is currently assigned to the null value :doc:`None </data_structures/none>`

* The new error is a :doc:`/exceptions/TypeError` which can occur when an `object <https://docs.python.org/3/glossary.html#term-object>`_ is used in a way that it is not supposed to be used. In this case the ``add`` variable is not `callable <https://docs.python.org/3/glossary.html#term-callable>`_ because it refers to :doc:`None </data_structures/none>` which is not a `callable <https://docs.python.org/3/glossary.html#term-callable>`_ object. I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError

* I have to define ``add`` as a :doc:`function </functions/functions>` or a :doc:`class </classes/classes>` to make it callable. I know the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword is used for creating :doc:`/functions/functions` and will test changing the ``add`` variable to a :doc:`function </functions/functions>` in ``calculator.py``

  .. code-block:: python

    def add():
        return None

  the terminal still shows a :doc:`/exceptions/TypeError` but with a different message. Progress!

  .. code-block:: python

    E    TypeError: add() takes 0 positional arguments but 2 were given

* This :doc:`/exceptions/TypeError` shows that the current definition of the ``add`` function takes in no inputs but I provided 2 in the call in the test ``calculator.add(0, 1)``. Since part of the requirement is that the ``add`` function should take in two numbers, I will change it in ``calculator.py`` to match

  .. code-block:: python

    def add(x, y):
        return None

  the terminal now displays an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    E    AssertionError: None != 1

  - An :doc:`/exceptions/AssertionError` is raised when an assertion is :doc:`False </data_structures/booleans>`
  - Since I am using ``self.assertEqual`` it means the two inputs are not equal. In other words the result of calling ``calculator.add(0, 1)`` is currently not equal to ``1``

* I change the ``add`` function in ``calculator.py`` so it returns the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  Eureka! The test passed. Time for a victory lap.

  .. code-block:: python

    tests/test_calculator.py ..              [100%]

    ============== 2 passed in 0.01s ===============


REFACTOR: Make it Better
=========================

Wait a minute. Is it that easy? Do I just provide the expectation of the test to make it pass? In the green phase, yes. I do whatever it takes to make the test pass even if I have to cheat.

Solving the problem this way reveals a problem with the test, which means I need to "Make it Better"

There are a few scenarios to consider from a user's perspective

* If a user tries to add other numbers that are not 0 and 1, the calculator will return 1
* If they also try to add negative numbers, it will still return 1
* The function always returns 1 no matter what inputs the user gives

Even though the add function currently passes the existing test it does not meet the actual requirement.

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

  the terminal responds with an :doc:`/exceptions/AssertionError`, proof that the ``add`` function always returns ``1`` no matter what inputs are given

  .. code-block:: python

    E    AssertionError: 1 != 0

* GREEN: make it pass

  I change the ``add`` function in ``calculator.py`` to add up the inputs

  .. code-block:: python

    def add(x, y):
        return x + y

  and the terminal displays passing tests, increasing my confidence in the ``add`` function

  .. code-block:: python

    tests/test_calculator.py ..          [100%]

    ============== 2 passed in 0.01s ==============

* REFACTOR: make it better

  I can use random inputs to test that the function behaves the way I expect for any given numbers. I will change ``test_calculator.py`` to use python's `random <https://docs.python.org/3/library/random.html?highlight=random#module-random>`_ library to generate random integers between -1 and 1 to represent negative numbers, zero and positive numbers

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
  - I test that when these two random numbers are given to the ``add`` function as inputs it returns their sum  as output and the terminal still displays passing tests

  .. code-block:: python

    tests/test_calculator.py ..              [100%]

    ============= 2 passed in 0.01s ===============

  - I no longer need the previous tests because this new test shows the scenarios for zero, negative and positive numbers
  - I can remove ``test addition`` from the TODO list since it passed, marking the task as completed

  .. code-block:: python

    # TODO
    # test subtraction
    # test multiplication
    # test division

----

This is the Test Driven Development cycle in practice

* **RED**: I write a failing test
* **GREEN**: I make the test pass by any means necessary
* **REFACTOR**: I make it better

I repeat this process until I have a working program that has been tested which gives me confidence it will behave in an expected way that meets the requirements of the program.

----

*****************
Test Subtraction
*****************

Since addition works and the next item from the TODO list is test subtraction, I will add a failing test for it

RED : make it fail
===================


* I add a :doc:`method </functions/functions>` called ``test_subtraction`` to ``test_calculator.py``

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

  the terminal responds with an :doc:`/exceptions/AttributeError`

  .. code-block:: python

      self.assertEqual(
   >      calculator.subtract(x, y),
        x-y
      )
   E    AttributeError: module 'calculator' has no attribute 'subtract'

GREEN : make it pass
=====================


* I add a variable assignment in ``calculator.py``

  .. code-block:: python

    def add(x, y):
        return x + y

    subtract = None

  and the terminal shows a :doc:`/exceptions/TypeError`

  .. code-block:: python

    E    TypeError: 'NoneType' object is not callable

* I change the definition of the ``subtract`` variable to make it callable

  .. code-block:: python

    def add(x, y):
        return x + y

    def subtract():
        return None

  and the terminal displays a :doc:`/exceptions/TypeError` with a different error message. Progress!

  .. code-block:: python

    E    TypeError: subtract() takes 0 positional arguments but 2 were given

* I change the definition of the ``subtract`` :doc:`function </functions/functions>` to match the expectation

  .. code-block:: python

    def add(x, y):
        return x + y

    def subtract(x, y):
        return None

  and the terminal responds with an :doc:`/exceptions/AssertionError`

  .. code-block:: python

    >    self.assertEqual(
         calculator.subtract(x, y),
         x-y
       )
    E    AssertionError: None != 0

* I change the ``subtract`` function in ``calculator.py`` to perform a subtraction operation on its inputs

  .. code-block:: python

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

  and all the tests pass - SUCCESS!

  .. code-block:: python

  tests/test_calculator.py ...            [100%]

  ======================= 3 passed in 0.01s ==================

* ``test subtraction`` can now be removed from the TODO list

  .. code-block:: python

    # TODO
    # test multiplication
    # test division


REFACTOR: make it better
=========================

* There is some duplication to remove so `I Do Not Repeat myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_

  - ``x = random.randint(-1, 1)`` happens twice
  - ``y = random.randint(-1, 1)`` happens twice

* I could change the ``TestCalculator`` :doc:`class </classes/classes>` in ``test_calculator.py`` to create the random variables only once by using :doc:`class </classes/classes>` attributes (variables) and reference them in the tests

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

  - all tests are still passing, so my change did not break anything. Fantastic!
  - The ``x`` and ``y`` variables are now initialized once as :doc:`class </classes/classes>` attributes (variables) and can be accessed later in every test using ``self.x`` and ``self.y`` the same way I can call `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`methods </functions/functions>` like `assertEqual <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertEqual>`_ by typing ``self.assertEqual``


----

********************
Test Multiplication
********************

Moving on to test multiplication, the next item on the TODO list

RED : make it fail
===================

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

the terminal responds with an :doc:`/exceptions/AttributeError`

GREEN : make it pass
=====================

using what I know so far I add a definition for ``multiplication`` to ``calculator.py``

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
=========================

I cannot think of a way to make the code better so I move on to the final test from the TODO list - test division

----

********************
Test Division
********************

RED : make it fail
===================

I add ``test_division`` to ``test_calculator.py``

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

once again the terminal shows an :doc:`/exceptions/AttributeError`


GREEN : make it pass
=====================


* I add a ``divide`` :doc:`function </functions/functions>` to ``calculator.py``

  .. code-block:: python

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

  the terminal response varies since I am using random variables, When ``y`` is 0 I get a `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ and when ``y`` is -1 or 1 it passes

  .. code-block:: python

    x = 1, y = 0

      def divide(x, y):
    >    return x / y
    E    ZeroDivisionError: division by zero

* I add `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # TypeError
    # ZeroDivisionError

************************
How to Test for Errors
************************

RED : make it fail
===================

I add a failing test to ``test_calculator.py`` to make  a `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ happen, then comment out the previous test that sometimes fails, to remove the variability of the test while I figure out the error

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

the terminal confirms my expectations with a failure for any value of ``x`` when ``y`` is 0. :doc:`Exceptions </how_to/exception_handling>` like `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ break execution of a program. No further code is run when an :doc:`Exception </how_to/exception_handling>` is raised which means that no other tests will run until I take care of this error

.. code-block:: python

  x = 0, y = 0

    def divide(x, y):
  >    return x / y
  E    ZeroDivisionError: division by zero

GREEN : make it pass
=====================

I can use the `unittest.TestCase.assertRaises <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises>`_ :doc:`method </functions/functions>` in ``test_division`` to confirm that a `ZeroDivisionError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ZeroDivisionError>`_ is raised when I try to divide a number by ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          calculator.divide(self.x, 0)
      # self.assertEqual(
      #     calculator.divide(self.x, self.y),
      #     self.x/self.y
      # )

the terminal displays passing tests, and I now have a way to ``catch`` :doc:`Exceptions </how_to/exception_handling>` when testing, which helps to confirm that the code raises an error, and other tests can continue to run

REFACTOR: make it better
=========================

I change ``test_division`` to test other division cases when the divisor is not 0 by making sure the value of ``y`` that is passed to ``calculator.divide`` is never 0

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
* the loop tells python to assign a new random variable to ``self.y`` as long as it is equal to 0. The loop stops when ``self.y`` is not equal to 0
* I remove ``test_division`` from the TODO list since all the tests pass

----

CONGRATULATIONS! You made it through writing a program that can perform the 4 basic arithmetic operations using Test Driven Development. What would you like to do next?

:doc:`/code/code_calculator`