.. include:: ../links.rst

#################################################################################
how to make a calculator
#################################################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0gVgMoed3zI?si=FQR1fMtJzElXcQ5n" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

In this chapter I write a program that does the arithmetic operations of addition, subtraction, multiplication and division

.. contents:: table of contents
  :local:
  :depth: 1

----


*********************************************************************************
test_addition
*********************************************************************************

.. _test_addition_red:

red: make it fail
#################################################################################

* I open a terminal and run :ref:`makePythonTdd.sh` with ``calculator`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh calculator

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_calculator.py:7`` with the mouse to open it in the editor
* change ``True`` to ``False`` to make ``test_failure`` pass
* then add a TODO list to keep track of work for the calculator

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

* I change ``test_failure`` to ``test_addition``, then add an assertion

  .. code-block:: python

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - the assertEqual_ :ref:`method<functions>` from the `unittest.TestCase`_ :doc:`class</classes/classes>` checks if its 2 inputs are equal. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - the explanation I like for this is that one of them is reality and the other is my expectation. In this case my expectation is that ``src.calculator.add(0, 1)`` will return ``1`` because ``0`` plus ``1`` is ``1``

  the terminal shows a NameError because ``src`` is not defined anywhere in ``test_calculator.py``

  .. code-block:: python

    NameError: name 'src' is not defined

.. _test_addition_green:

green: make it pass
#################################################################################

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ for the ``calculator`` module from the ``src`` folder

  .. code-block:: python

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):
    ...

  and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

  I think of ``src.calculator.add`` as an address

  * ``src.calculator`` refers to ``calculator.py`` in the ``src`` folder/directory
  * ``add`` refers to something (an attribute) in the ``calculator.py`` file which is currently empty

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open ``calculator.py`` in the Integrated Development Environment (IDE) and type the name

  .. code-block:: python

    add

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'add' is not defined

  because there is no assignment to the name

* I assign it to the null value :ref:`None`

  .. code-block:: python

    add = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because the ``add`` variable refers to :ref:`None` which is not a callable_ object. I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I can define ``add`` as a :ref:`function<functions>` or :ref:`class <classes>` to make it callable. I change the ``add`` variable to a :ref:`function<functions>` with the def_ keyword

  .. code-block:: python

    def add():
        return None

  the terminal still shows a :ref:`TypeError` but with a different message. Progress!

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

  the current definition of the ``add`` function takes in 0 inputs, but two were provided 2 in the test - ``src.calculator.add(0, 1)``

* I change the definition to match the requirement of two positional arguments

  .. code-block:: python

    def add(x, y):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  the ``add`` :ref:`function<functions>` returns :ref:`None` and the test expects ``1``

* I change the `return statement`_ to match the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  and the test passes. Time for a victory lap!

.. _test_addition_refactor:

refactor: make it better
#################################################################################

Wait a minute! Is it that easy? Do I provide the expectation of the test to make it pass? In the green phase, Yes. I do the easiest thing to make the test pass.

Solving the problem this way shows it has a problem, I have to "Make it Better". The ``add`` function returns ``1`` no matter what inputs are given. It is a :doc:`singleton function </functions/test_singleton_functions>`, I want it to do a calculation with the inputs instead. Even though ``add`` currently passes the test it does not meet the actual requirement.

.. _test_addition_refactor_red:

red: make it fail
---------------------------------------------------------------------------------

I add an assertion to show that ``add`` always returns ``1``

.. code-block:: python

  def test_addition(self):
      self.assertEqual(
          src.calculator.add(0, 1),
          1
      )
      self.assertEqual(
          src.calculator.add(-1, 1),
          0
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  E    AssertionError: 1 != 0

.. _test_addition_refactor_green:

the :ref:`function<functions>` returns ``1`` but the test expects ``0``

green: make it pass
---------------------------------------------------------------------------------

I change the `return statement`_

.. code-block:: python

  def add(x, y):
      return x + y

and the terminal shows a passing test

.. _test_addition_refactor_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I used 2 examples to test the :ref:`function<functions>` and could add more but it would be better to use random numbers, so I do not need to add more assertions. I add an `import statement`_

  .. code-block:: python

    import random
    import src.calculator
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, it is used to make fake random numbers

* I add variables and a new assertion

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(x, y),
                x+y
            )
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )
            self.assertEqual(
                src.calculator.add(-1, 1),
                0
            )

  the terminal shows the test is still green

  - ``x = random.randint(-1, 1)`` assigns a variable called ``x`` to the result of calling ``random.randint(-1, 1)``
  - ``random.randint(-1, 1)`` gives me a random number from ``-1`` up to and including ``1``, ``-1`` for negative numbers, ``0`` for itself, and ``1`` for positive numbers

* I remove the other assertions because they are now covered by the one that uses the random numbers

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(x, y),
                x+y
            )

* I change the range of random numbers for the test

  .. code-block:: python

    def test_addition(self):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

  and it is still green

* then add a function to remove the duplication of the calls to `random.randint`_ with the same values

  .. code-block:: python

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.randint(-10, 10)

  and call it for the ``x`` and ``y`` variables

  .. code-block:: python

    def test_addition(self):
        x = a_random_number()
        y = a_random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

  the test still passes

* I can now change the range of random numbers for the test in one place

  .. code-block:: python

      def a_random_number():
        return random.randint(-10, 10)

* I remove ``test addition`` from the TODO list

  .. code-block:: python

    # TODO
    # test subtraction
    # test multiplication
    # test division

----

*********************************************************************************
test_subtraction
*********************************************************************************

Time to add a failing test for subtraction

.. _test_subtraction_red:

red: make it fail
#################################################################################

* I add a :ref:`method<functions>` called ``test_subtraction``

  .. code-block:: python

    def test_addition(self):
        x = a_random_number()
        y = a_random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

    def test_subtraction(self):
        x = a_random_number()
        y = a_random_number()

        self.assertEqual(
            src.calculator.subtract(x, y),
            x-y
        )

  which gives me an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

.. _test_subtraction_green:

green: make it pass
#################################################################################

* I add the name to ``calculator.py`` and assign it to :ref:`None`

  .. code-block:: python

    def add(x, y):
        return x + y


    subtract = None

  the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  this is familiar

* I change it to a :ref:`function<functions>` to make it callable

  .. code-block:: python

    def subtract():
        return None

  and the terminal shows another :ref:`TypeError` with a different error message. Progress again!

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make the ``subtract`` :ref:`function<functions>` take inputs to match the expectation

  .. code-block:: python

    def subtract(x, y):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -17
    AssertionError: None != -4
    AssertionError: None != 7
    AssertionError: None != 10

  ``subtract`` returns :ref:`None` and the test expects ``x`` minus ``y``

* When I change the `return statement`_ to return the difference between the inputs

  .. code-block:: python

    def subtract(x, y):
        return x - y

  the test passes. SUCCESS!

.. _test_subtraction_refactor:

refactor: make it better
#################################################################################

* I have some duplication to remove in keeping with `The Do Not Repeat Yourself (DRY) Principle`_

  - ``x = a_random_number()`` happens twice, once in ``test_addition`` and again in ``test_subtraction``
  - ``y = a_random_number()`` happens twice, once in ``test_addition`` and again in ``test_subtraction``

* I can use :ref:`class <classes>` attributes (variables) in the ``TestCalculator`` :ref:`class <classes>` to make the random variables once

  .. code-block:: python

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

  the ``x`` and ``y`` variables are initialized once as :ref:`class <classes>` attributes (variables) and accessed later in every test using ``self.x`` and ``self.y``, the same way I can call `unittest.TestCase`_ :ref:`methods<functions>` like assertEqual_ or assertFalse_ and the terminal still shows passing tests

* I remove the ``x`` and ``y`` variables from ``test_addition`` and ``test_subtraction``

  .. code-block:: python

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

  still green!

* then remove ``test subtraction`` from the TODO list

  .. code-block:: python

    # TODO
    # test multiplication
    # test division

----

*********************************************************************************
test_multiplication
*********************************************************************************

Moving on to test multiplication, the next item on the TODO list

.. _test_multiplication_red:

red: make it fail
#################################################################################

I add a failing test for multiplication

.. code-block:: python

  def test_subtraction(self):
      self.assertEqual(
          src.calculator.subtract(self.x, self.y),
          self.x-self.y
      )

  def test_multiplication(self):
      self.assertEqual(
          src.calculator.multiply(self.x, self.y),
          self.x*self.y
      )

and the terminal shows an :ref:`AttributeError` ::

  AttributeError: module 'src.calculator' has no attribute 'multiply'

this is definitely familiar

.. _test_multiplication_green:

green: make it pass
#################################################################################

using what I know so far I add a definition for ``multiplication`` in ``calculator.py``

.. code-block:: python

  def subtract(x, y):
      return x - y


  def multiply(x, y):
      return x * y

SUCCESS! The terminal shows passing tests and I remove ``test_multiplication`` from the TODO list

.. code-block:: python

  # TODO
  # test division

----

*********************************************************************************
test_division
*********************************************************************************

Now it is down to the test for division

.. _test_division_red_0:

red: make it fail
#################################################################################

I add a test for division

.. code-block:: python

  def test_multiplication(self):
      self.assertEqual(
          src.calculator.multiply(self.x, self.y),
          self.x*self.y
      )

  def test_division(self):
      self.assertEqual(
          src.calculator.divide(self.x, self.y),
          self.x/self.y
      )

which gives me an :ref:`AttributeError` ::

  AttributeError: module 'src.calculator' has no attribute 'divide'

.. _test_division_green_0:

green: make it pass
#################################################################################

* I add a ``divide`` :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def divide(x, y):
        return x / y

  the terminal shows a random ZeroDivisionError_ when ``y`` is ``0``

    .. code-block:: python

      x = 1, y = 0

        def divide(x, y):
      >    return x / y
      E    ZeroDivisionError: division by zero

* which I add to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError


how to Test for Errors
---------------------------------------------------------------------------------

.. _test_division_red_1:

red: make it fail
#################################################################################

I add a failing line to cause the ZeroDivisionError_ by dividing by ``0``

.. code-block:: python

  def test_division(self):
      src.calculator.divide(self.x, 0)
      self.assertEqual(
          src.calculator.divide(self.x, self.y),
          self.x/self.y
      )

the terminal shows my expectations with a failure for any value of ``x`` when ``y`` is ``0``.

.. code-block:: python

  x = 0, y = 0

    def divide(x, y):
  >    return x / y
  E    ZeroDivisionError: division by zero

:ref:`Exceptions<Exceptions>` like ZeroDivisionError_ break execution of a program. No code will run past the line that causes an :doc:`Exception </how_to/exception_handling_programs>` when it is raised which means I have to take care of it

.. _test_division_green_1:

green: make it pass
#################################################################################

I can use the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` in ``test_division`` to make sure that a ZeroDivisionError_ is raised when I try to divide a number by ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          src.calculator.divide(self.x, 0)

      self.assertEqual(
         src.calculator.divide(self.x, self.y),
         self.x/self.y
      )

the terminal shows passing tests, proof that the code raises an :ref:`Exception<exceptions>`

.. _test_division_refactor_1:

refactor: make it better
#################################################################################

* I use a `while statement`_ for the other cases when the divisor is not ``0`` by making sure the value of ``y`` that is passed from the test to ``src.calculator.divide`` is never ``0``

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

  - if the value of ``self.y`` is ``0``

    * it assigns ``self.y`` to the result of calling the ``random_number`` :ref:`function<functions>`
    * and checks again, repeating the process until ``self.y`` is not ``0``

  - if the value of ``self.y`` is not ``0`` it leaves the loop and runs what is in the ``else`` block

* Since ``self.y`` is ``0`` in the first part of the `while statement`_ I can add a call to the ``divide`` function that will always raise a ZeroDivisionError_

  .. code-block:: python

    def test_division(self):
        while self.y == 0:
            src.calculator.divide(self.x, self.y)
            self.y = a_random_number()
        else:
            self.assertEqual(
                src.calculator.divide(self.x, self.y),
                self.x/self.y
            )

  and the terminal shows a ZeroDivisionError_ when ``self.y`` is randomly ``0``

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add an assertRaises_ block to catch the :ref:`Exception<Exceptions>` and remove the previous assertRaises_ block

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

  and the terminal shows passing tests

* I remove the TODO list since all tests are passing
* and change the range of random numbers for the tests to be from minus 10 to 10

  .. code-block:: python

      def a_random_number():
        return random.randint(-10, 10)

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can have some fun and write the program that makes the tests in ``test_calculator.py`` pass without looking at them

.. _test_calculator_red:

red: make it fail
#################################################################################

* I close ``test_calculator.py``
* then delete all the text in ``calculator.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

.. _test_calculator_green:

green: make it pass
#################################################################################

* I add the name to ``calculator.py``

  .. code-block:: python

    subtract

  and get a NameError_

  .. code-block:: python

    NameError: name 'subtract' is not defined

  I assign it to :ref:`None`

  .. code-block:: python

    subtract = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I define it as a :ref:`function<functions>`

  .. code-block:: python

    def subtract():
        return None

  which gives me another :ref:`TypeError` with a different message

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

  then I add positional arguments to the :ref:`function<functions>`

  .. code-block:: python

    def subtract(a, b):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -10
    AssertionError: None != -9
    AssertionError: None != 0
    AssertionError: None != 12

* I change the `return statement`_ to see the difference between the inputs and expected output

  .. code-block:: python

    def subtract(a, b):
        return a, b

  which gives me another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-10, 2) != -12
    AssertionError: (-1, 7) != -8
    AssertionError: (10, 6) != 4
    AssertionError: (7, -10) != 17

  as the name suggests, the tests expects the difference between the two inputs

* I change the `return statement`_ to match the expectation

  .. code-block:: python

    def subtract(a, b):
        return a - b

  and get another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiply'

* I add a :ref:`function<functions>` for ``multiply``

  .. code-block:: python

    def multiply():
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: multiply() takes 0 positional arguments but 2 were given

  then add 2 variables for the positional arguments

  .. code-block:: python

    def multiply(a, b):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -42
    AssertionError: None != -10
    AssertionError: None != 20
    AssertionError: None != 36

* I change the `return statement` to see the difference between the inputs and the expected output

  .. code-block:: python

    def multiply(a, b):
        return a, b

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-6, 6) != -36
    AssertionError: (-2, 3) != -6
    AssertionError: (2, 5) != 10
    AssertionError: (-9, -5) != 45

  I change the `return statement` to return the product of the inputs, matching the name of the :ref:`function<functions>`

  .. code-block:: python

    def multiply(a, b):
        return a * b


  the terminal shows another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def divide(a, b):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -0.1111111111111111
    AssertionError: None != -1.0
    AssertionError: None != 0.25
    AssertionError: None != 1.3333333333333333

  I change the `return statement`_ to show the difference between the inputs and the expected output

  .. code-block: python

    def divide(a, b):
        return a, b

  and get an :ref:`AssertionError` that shows the expected output is the result of dividing the inputs

  .. code-block:: python

    AssertionError: (-10, 6) != -1.6666666666666667
    AssertionError: (-6, -6) != 1.0
    AssertionError: (5, 7) != 0.7142857142857143
    AssertionError: (10, 9) != 1.1111111111111112

  or

  .. code-block:: python

    AssertionError: ZeroDivisionError not raised

  I change the `return statement`_ to match the expectation

  .. code-block:: python

    def divide(a, b):
        return a / b

  and get another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* I add a :ref:`function<functions>` using what I know so far

  .. code-block:: python

    def add(a, b):
        return a + b

  and the terminal shows all tests are passing with no random failures

----

*********************************************************************************
review
*********************************************************************************

CONGRATULATIONS! You used Test Driven Development to write a program that performs the 4 basic arithmetic operations of addition, subtraction, multiplication and division.

You also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* ZeroDivisionError_

Would you like to test :doc:`passing values</how_to/pass_values>`?


----

:doc:`/code/code_calculator`
