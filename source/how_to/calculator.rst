.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator in python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

#################################################################################
how to make a calculator
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/i8fGEqdH3yk?si=eBow2hwdlh01aVUF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

In this chapter I write a program that does the arithmetic_ operations of addition, subtraction, multiplication and division

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
test_addition
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``calculator`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh calculator

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_calculator.py:7`` to open it in the editor in the editor
* then change ``True`` to ``False`` to make the test pass
* I add a list to keep track of the work for the program

  .. code-block:: python

        def test_failure(self):
            self.assertFalse(False)


    # TODO
    # test addition
    # test subtraction
    # test multiplication
    # test division


    # Exceptions Encountered
    # AssertionError

* and change ``test_failure`` to ``test_addition`` then change `assertFalse`_ to `assertEqual`_

  .. code-block:: python

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - the assertEqual_ :ref:`method<functions>` from the `unittest.TestCase`_ :ref:`class<classes>` checks if its 2 inputs are the same. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - the explanation I like from what I have seen is that one of them is ``reality`` - ``src.calculator.add(0, 1)``, and the other is my ``expectation`` - ``1``, because ``0`` plus ``1`` is ``1``

  but the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

  because ``src`` is not defined in ``test_calculator.py``

green: make it pass
#################################################################################

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ at the top of the file

  .. code-block:: python

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):
    ...

  and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

  I think of ``src.calculator.add`` as an address, ``add`` is something (an attribute) in the empty ``calculator.py`` file from the ``src`` folder/directory

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then click on ``calculator.py`` in ``src`` folder to open it in the editor, and I type the name

  .. code-block:: python

    add

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'add' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    add = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because the ``add`` variable is :ref:`None` which is not callable_

* I add the error to the list of Exceptions_ encountered in ``test_calculator.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then I change ``add`` to a :ref:`function<functions>` with the def_ keyword to make it callable_

  .. code-block:: python

    def add():
        return None

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

  ``add`` currently takes in 0 inputs, but 2 were provided in the test - ``0`` and ``1``

* I make it take 2 positional arguments

  .. code-block:: python

    def add(x, y):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  the ``add`` :ref:`function<functions>` returns :ref:`None` and the test expects ``1``

* when I make the `return statement`_ match the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  the test passes, time for a victory lap!

refactor: make it better
#################################################################################

The ``add`` :ref:`function<functions>` passes the test but does not meet the actual requirement because it always returns ``1``. I want it to do a calculation with the inputs and return the result

red: make it fail
---------------------------------------------------------------------------------

I add an another :ref:`assertion<AssertionError>` in ``test_calculator.py`` to show the problem with the :ref:`function<functions>`

.. code-block:: python
  :emphasize-lines: 6-9

  def test_addition(self):
      self.assertEqual(
          src.calculator.add(0, 1),
          1
      )
      self.assertEqual(
          src.calculator.add(-1, 1),
          0
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  E    AssertionError: 1 != 0

the :ref:`function<functions>` returns ``1`` and the test expects ``0``

green: make it pass
---------------------------------------------------------------------------------

when I change the `return statement`_ to the sum of the inputs

.. code-block:: python

  def add(x, y):
      return x + y

the terminal shows a passing test

refactor: make it better
---------------------------------------------------------------------------------

* I want the test to use random numbers instead of fixed numbers, so I add an `import statement`_ at the top of ``test_calculator.py`` to use random numbers in the test

  .. code-block:: python
    :emphasize-lines: 1

    import random
    import src.calculator
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_ that is used to make fake random numbers

* then I add variables and a new :ref:`assertion<AssertionError>`

  .. code-block:: python
    :emphasize-lines: 3,4,6-9

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(x, y),
                x+x
            )
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )
            self.assertEqual(
                src.calculator.add(-1, 1),
                0
            )

  because the range of numbers is small, the terminal shows random success or :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0 != 2
    AssertionError: -1 != -2
    AssertionError: -1 != 0
    AssertionError: 1 != 2

  I change the expectation of the :ref:`assertion<AssertionError>` in the test to the correct calculation

  .. code-block:: python
    :emphasize-lines: 3

    self.assertEqual(
        src.calculator.add(x, y),
        x+y
    )

  and the terminal shows passing tests

  - ``x = random.randint(-1, 1)`` points a variable called ``x`` to the result of calling ``random.randint(-1, 1)`` the terminal shows a random number from ``-1`` up to and including ``1``
  - ``-1`` for negative numbers, ``0`` for itself, and ``1`` for positive numbers

* I remove the other :ref:`assertions<AssertionError>` because they are covered by the one that uses random numbers. I do not need them anymore

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(x, y),
                x+y
            )

* When I want to use a different range of random numbers for the test, I have to make a change in more than one place

  .. code-block:: python

    def test_addition(self):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

  I add a :ref:`function<functions>` to remove the duplication of calls to `random.randint`_

  .. code-block:: python
    :emphasize-lines: 6-7

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.randint(-1, 1)


    class TestCalculator(unittest.TestCase):
        ...

  then use the new :ref:`function<functions>` for the ``x`` and ``y`` variables in ``test_addition``

  .. code-block:: python
    :emphasize-lines: 2,3

    def test_addition(self):
        x = a_random_number()
        y = a_random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

  I now only need to change the range of random numbers for the test in one place

  .. code-block:: python

      def a_random_number():
          return random.randint(-10, 10)

  and the terminal still shows green. I can use any range of numbers the computer can handle, for example

  .. code-block:: python
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10**100000, 10**100000)


    class TestCalculator(unittest.TestCase):
        ...

  the test is still green and takes longer to run. I change the range back to ``-10, 10``

* then remove ``test addition`` from the TODO list in ``test_calculator.py``

  .. code-block:: python

    # TODO
    # test subtraction
    # test multiplication
    # test division

----

*********************************************************************************
test_subtraction
*********************************************************************************

red: make it fail
#################################################################################

* I add a :ref:`method<functions>` to test subtraction in ``test_calculator.py``

  .. code-block:: python
    :emphasize-lines: 5-12

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            ...

        def test_subtraction(self):
            x = a_random_number()
            y = a_random_number()

            self.assertEqual(
                src.calculator.subtract(x, y),
                x-y
            )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

green: make it pass
#################################################################################

* I add the name to ``calculator.py``

  .. code-block:: python

    def add(x, y):
        return x + y


    subtract

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'subtract' is not defined

  I point it to :ref:`None`

  .. code-block:: python

    subtract = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I have seen this before

* I change ``subtract`` in ``calculator.py`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python
    :emphasize-lines: 5

    def add(x, y):
        ...

    def subtract():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make ``subtract`` take inputs

  .. code-block:: python
    :emphasize-lines: 4

    def add(x, y):
        ...

    def subtract(x, y):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -17
    AssertionError: None != -4
    AssertionError: None != 7
    AssertionError: None != 10

  ``subtract`` returns :ref:`None` and the test expects ``x-y``

* When I make the ``subtract`` :ref:`function<functions>` return the difference between the inputs

  .. code-block:: python
    :emphasize-lines: 2

    def subtract(x, y):
        return x - y

  the test passes. SUCCESS!

refactor: make it better
#################################################################################

* I have some duplication to remove, the code below happens twice

  .. code-block:: python

    x = a_random_number()
    y = a_random_number()

  once in ``test_addition`` and again in ``test_subtraction``. I can use :ref:`class <classes>` :ref:`attributes<AttributeError>` (variables) to remove them and use the same numbers for both tests

  .. code-block:: python
    :emphasize-lines: 3-4,7-8, 15-16

    class TestCalculator(unittest.TestCase):

        x = a_random_number()
        y = a_random_number()

        def test_addition(self):
            x = self.x
            y = self.y

            self.assertEqual(
                src.calculator.add(x, y),
                x+y
            )

        def test_subtraction(self):
            x = self.x
            y = self.y

            self.assertEqual(
                src.calculator.subtract(x, y),
                x-y
            )

  the terminal shows the tests are still passing. The ``x`` and ``y`` variables are made once as :ref:`class <classes>` :ref:`attributes<AttributeError>` (variables) and used later in each test with ``self.x`` and ``self.y``, the same way I use `unittest.TestCase`_ :ref:`methods<functions>` like assertEqual_ or assertFalse_

* I remove the ``x`` and ``y`` variables from ``test_addition`` and ``test_subtraction`` and use ``self.x`` and ``self.y`` instead

  .. code-block:: python
    :emphasize-lines: 8-9, 14-15

    class TestCalculator(unittest.TestCase):

        x = a_random_number()
        y = a_random_number()

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(self.x, self.y),
                self.x+self.y
            )

        def test_subtraction(self):
            self.assertEqual(
                src.calculator.subtract(self.x, self.y),
                self.x-self.y
            )

  and the tests are still green!

* I remove ``test subtraction`` from the TODO list

  .. code-block:: python

    # TODO
    # test multiplication
    # test division

----

*********************************************************************************
test_multiplication
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test for multiplication in ``test_calculator.py``

.. code-block:: python

  class TestCalculator(unittest.TestCase):

      def test_addition(self):
          ...

      def test_subtraction(self):
          ...

      def test_multiplication(self):
          self.assertEqual(
              src.calculator.multiply(self.x, self.y),
              self.x*self.y
          )

and the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'multiply'

green: make it pass
#################################################################################

using what I know so far, I add a :ref:`function<functions>` to ``calculator.py``

.. code-block:: python
  :emphasize-lines: 5-6

  def subtract(x, y):
      ...


  def multiply(x, y):
      return x * y

the test passes! I remove ``test_multiplication`` from the TODO list

.. code-block:: python

  # TODO
  # test division

----

*********************************************************************************
test_division
*********************************************************************************


red: make it fail
#################################################################################

time for division. I add a new test to ``test_calculator.py``

.. code-block:: python

  class TestCalculator(unittest.TestCase):

      def test_addition(self):
          ...

      def test_subtraction(self):
          ...

      def test_multiplication(self):
          ...

      def test_division(self):
          self.assertEqual(
              src.calculator.divide(self.x, self.y),
              self.x/self.y
          )

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'divide'


green: make it pass
#################################################################################

* I add a :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def add(x, y):
        ...

    def subtract(x, y):
        ...

    def multiply(x, y):
        ...

    def divide(x, y):
        return x / y

  then make the range of numbers for the tests smaller

  .. code-block:: python

      def a_random_number():
          return random.randint(-1, 1)

  and when ``y`` is randomly ``0`` the terminal shows a ZeroDivisionError_

  .. code-block:: python

    x = 1, y = 0

      def divide(x, y):
    >    return x / y
    E    ZeroDivisionError: division by zero

  dividing by ``0`` is not defined in mathematics and raises an Exception_ in Python

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError


how to test that an Exception is raised
---------------------------------------------------------------------------------

red: make it fail
#################################################################################

I add a line to cause the ZeroDivisionError_ and comment out the code that randomly fails in ``test_calculator.py``

.. code-block:: python
  :emphasize-lines: 2

  def test_multiplication(self):
      ...

  def test_division(self):
      src.calculator.divide(self.x, 0)

      # self.assertEqual(
      #    src.calculator.divide(self.x, self.y),
      #    self.x/self.y
      # )

the terminal shows my expectation with a failure for any value of ``x`` since ``y`` is ``0``

.. code-block:: python

  x = 0, y = 0

    def divide(x, y):
  >    return x / y
  E    ZeroDivisionError: division by zero

Exceptions_ like ZeroDivisionError_ break execution of a program. No code will run past the line that causes an Exception_, which means I have to take care of this problem. See :ref:`how to test that an Exception is raised` for more


green: make it pass
#################################################################################

* I can use the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` to make sure that a ZeroDivisionError_ is raised when I try to divide a number by ``0``

  .. code-block:: python
    :emphasize-lines: 2-3

    def test_division(self):
        with self.assertRaises(AssertionError):
            src.calculator.divide(self.x, 0)

        # self.assertEqual(
        #   src.calculator.divide(self.x, self.y),
        #   self.x/self.y
        # )

  because I used the wrong Exception_ the terminal still shows a ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

* When I change it to use the right Exception_

  .. code-block:: python
    :emphasize-lines: 2

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            src.calculator.divide(self.x, 0)

  the test passes, showing that the code raises the Exception_

refactor: make it better
#################################################################################

* I still have a problem because ``self.y`` can sometimes be ``0``, I use a `while statement`_ to make sure it never happens in the :ref:`assertion<AssertionError>`

  .. code-block:: python

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            src.calculator.divide(self.x, 0)

        while self.y == 0:
            self.y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.x, self.y),
                self.x/self.y
            )

  here is what it does

  - when the value of ``self.y`` is ``0``

    * it points ``self.y`` to the result of calling ``a_random_number``
    * then checks if the value of ``self.y`` is ``0`` again, repeating the process until ``self.y`` is not ``0``

  - when the value of ``self.y`` is not ``0``, it leaves the loop and runs the code in the ``else`` block

* Since ``self.y`` is ``0`` in the first part of the `while statement`_ I can add a call to the ``divide`` :ref:`function<functions>` that will fail

  .. code-block:: python

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            src.calculator.divide(self.x, 0)

        while self.y == 0:
            src.calculator.divide(self.x, self.y)
            self.y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.x, self.y),
                self.x/self.y
            )

  when ``self.y`` is randomly ``0``, the terminal shows ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add an assertRaises_ block to catch the Exception_ in the `while statement`_ and remove the previous statement from the test because it is now part of the loop

  .. code-block:: python

    def test_division(self):
        while self.y == 0:
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.x, self.y)
            self.y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.x, self.y),
                self.x/self.y
            )

  the terminal shows all tests are passing with no random failures

* I use a bigger range of numbers for the tests

  .. code-block:: python

    def a_random_number():
        return random.randint(-10**1000000, 10**1000000)

  the terminal still shows green and it takes longer to run the tests. I change the range back to ``-10, 10``

* then remove the TODO list

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can write the program that makes the tests pass without looking at them

red: make it fail
#################################################################################

* I close ``test_calculator.py``
* then delete all the text in ``calculator.py`` and the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

  can you tell what Exceptions_ will show up as I go along?

green: make it pass
#################################################################################

* I add the name to ``calculator.py``

  .. code-block:: python

    subtract

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'subtract' is not defined

  I point it to :ref:`None`

  .. code-block:: python

    subtract = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I change ``subtract`` to a :ref:`function<functions>`

  .. code-block:: python

    def subtract():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

  I add positional arguments to the :ref:`function<functions>`

  .. code-block:: python
    :emphasize-lines: 1

    def subtract(a, b):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -10
    AssertionError: None != -9
    AssertionError: None != 0
    AssertionError: None != 12

* then change the `return statement`_ to see the difference between the inputs and expected output

  .. code-block:: python

    def subtract(a, b):
        return a, b

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-10, 2) != -12
    AssertionError: (-1, 7) != -8
    AssertionError: (10, 6) != 4
    AssertionError: (7, -10) != 17

  the name of the :ref:`function<functions>` is ``subtract`` and the test expects the difference between the 2 inputs

* I make the `return statement`_ match the expectation

  .. code-block:: python

    def subtract(a, b):
        return a - b

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiply'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def multiply():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: multiply() takes 0 positional arguments but 2 were given

  then add 2 variables for the positional arguments

  .. code-block:: python

    def multiply(a, b):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -42
    AssertionError: None != -10
    AssertionError: None != 20
    AssertionError: None != 36

* I change the `return statement`_ to see the difference between the inputs and the expected output

  .. code-block:: python

    def multiply(a, b):
        return a, b

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-6, 6) != -36
    AssertionError: (-2, 3) != -6
    AssertionError: (2, 5) != 10
    AssertionError: (-9, -5) != 45

  I change it to the product of the inputs, matching the name of the :ref:`function<functions>`

  .. code-block:: python

    def multiply(a, b):
        return a * b

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def divide(a, b):
        return a, b

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-10, 6) != -1.6666666666666667
    AssertionError: (-6, -6) != 1.0
    AssertionError: (5, 7) != 0.7142857142857143
    AssertionError: (10, 9) != 1.1111111111111112

  or

  .. code-block:: python

    AssertionError: ZeroDivisionError not raised

  when I change the `return statement`_ to match the expectation

  .. code-block:: python

    def divide(a, b):
        return a / b

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* the `return statement`_ of the last 3 :ref:`functions` matched their names, I use that for the new one

  .. code-block:: python

    def add(a, b):
        return a + b

  and all tests are passing with no random failures. Lovely!

----

*********************************************************************************
review
*********************************************************************************

I wrote the following tests for a program that performs the arithmetic_ operations

* `test_addition`_
* `test_subtraction`_
* `test_multiplication`_
* `test_division`_

I also ran into the following Exceptions_

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* ZeroDivisionError_

Would you like to test :doc:`passing values?</how_to/pass_values>`

----

:doc:`/code/code_calculator`
