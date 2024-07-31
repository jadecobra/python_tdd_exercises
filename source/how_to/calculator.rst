.. include:: ../links.rst

#################################################################################
how to make a calculator
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/0gVgMoed3zI?si=FQR1fMtJzElXcQ5n" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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

* I open a terminal to run :ref:`makePythonTdd.sh` with ``calculator`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh calculator

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard then click on ``tests/test_calculator.py:7`` with the mouse to open it in the editor
* and change ``True`` to ``False`` to make the test pass
* then add a list to keep track of work for the calculator

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

  - the assertEqual_ :ref:`method<functions>` from the `unittest.TestCase`_ :doc:`class</classes/classes>` checks if its 2 inputs are the same. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - the explanation I like from what I have seen is that one of them is ``reality`` and the other is my ``expectation``. In this case, reality is the call ``src.calculator.add(0, 1)``, and my expectation is ``1`` because ``0`` plus ``1`` is ``1``

  but the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

  ``src`` is not defined anywhere in ``test_calculator.py``

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

  * ``src`` is the ``src`` folder/directory
  * ``calculator`` is ``calculator.py`` in the ``src`` directory
  * ``add`` is something (an attribute) in the ``calculator.py`` file which is currently empty

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open ``calculator.py`` in the editor to type the name

  .. code-block:: python

    add

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'add' is not defined

  because there is no assignment to the name

* I assign it to the null value :ref:`None`

  .. code-block:: python

    add = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because the ``add`` variable is :ref:`None` which is not a callable_ object

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then change ``add`` to a :ref:`function<functions>` with the def_ keyword to make it callable_

  .. code-block:: python

    def add():
        return None

  the terminal shows another :ref:`TypeError` but with a different message. Progress!

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

  ``add`` currently takes in 0 inputs, but 2 were provided in the test - ``src.calculator.add(0, 1)``

* I make it take 2 positional arguments

  .. code-block:: python

    def add(x, y):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  the ``add`` :ref:`function<functions>` returns :ref:`None` and the test expects ``1``

* when I make the `return statement`_ match the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  the test passes. Time for a victory lap!

.. _test_addition_refactor:

refactor: make it better
#################################################################################

Wait a minute! Is it that easy? Do I provide the expectation of the test to make it pass? In the green phase, Yes. I do the easiest thing that will make a failing test pass.

This solution shows a problem with the test, I have to "Make it Better". The ``add`` function returns ``1`` no matter what inputs it gets, it is a :doc:`singleton function </functions/test_singleton_functions>`. The ``add`` :ref:`function<functions>` passes the test but does not meet the actual requirement, I want it to do a calculation with the inputs instead. .

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

the ``add`` returns ``1`` and the test expects ``0``

green: make it pass
---------------------------------------------------------------------------------

I change the `return statement`_ to a calculation

.. code-block:: python

  def add(x, y):
      return x + y

and the terminal shows a passing test

.. _test_addition_refactor_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I used 2 examples to test the :ref:`function<functions>` and could add more but it would be better to use random numbers, to not need more assertions. I add an `import statement`_

  .. code-block:: python

    import random
    import src.calculator
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `python standard library`_, that is used to make fake random numbers

* then I add variables and a new assertion

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
  - ``random.randint(-1, 1)`` gives me a random number from ``-1`` up to and including ``1``
  - ``-1`` for negative numbers, ``0`` for itself, and ``1`` for positive numbers

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

* If I want to change the range of random numbers for the test, I have to do it in more than one place

  .. code-block:: python

    def test_addition(self):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

* I add a function to remove the duplication of the calls to `random.randint`_

  .. code-block:: python

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.randint(-1, 1)

  then call it for the ``x`` and ``y`` variables

  .. code-block:: python

    def test_addition(self):
        x = a_random_number()
        y = a_random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

* I can now change the range of random numbers for the test in one place

  .. code-block:: python

      def a_random_number():
        return random.randint(-10, 10)

  and the terminal still shows green

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

.. _test_subtraction_red:

red: make it fail
#################################################################################

* I add a :ref:`method<functions>` to test subtraction

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

* I make it a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def subtract():
        return None

  and the terminal shows another :ref:`TypeError` with a different message. Progress again!

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make it take inputs

  .. code-block:: python

    def subtract(x, y):
        return None

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -17
    AssertionError: None != -4
    AssertionError: None != 7
    AssertionError: None != 10

  ``subtract`` returns :ref:`None` and the test expects ``x-y``

* When I make the :ref:`function<functions>` return the difference between the inputs

  .. code-block:: python

    def subtract(x, y):
        return x - y

  the test passes. SUCCESS!

.. _test_subtraction_refactor:

refactor: make it better
#################################################################################

* I have some duplication to remove in keeping with `The Do Not Repeat Yourself (DRY) Principle`_

  .. code-block:: python

    x = a_random_number()
    y = a_random_number()

  happens twice, once in ``test_addition`` and again in ``test_subtraction``

* I can use :ref:`class <classes>` attributes (variables) to remove the duplication

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

  the terminal shows the tests are still passing, the ``x`` and ``y`` variables are made once as :ref:`class <classes>` attributes (variables) and used later in every test with ``self.x`` and ``self.y``, the same way I can call `unittest.TestCase`_ :ref:`methods<functions>` like assertEqual_ or assertFalse_.

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

Time to test multiplication, the next item on the TODO list

.. _test_multiplication_red:

red: make it fail
#################################################################################

I add a failing test

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

and the terminal shows an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'multiply'

.. _test_multiplication_green:

green: make it pass
#################################################################################

* using what I know so far I add a :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def subtract(x, y):
        return x - y


    def multiply(x, y):
        return x * y

  SUCCESS! The terminal shows passing tests

* and I remove ``test_multiplication`` from the TODO list

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

I add a test

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

which gives me an :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'divide'

.. _test_division_green_0:

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def divide(x, y):
        return x / y

  and the terminal shows a random ZeroDivisionError_ when ``y`` is ``0``

  .. code-block:: python

    x = 1, y = 0

      def divide(x, y):
    >    return x / y
    E    ZeroDivisionError: division by zero

  dividing by ``0`` is not defined in mathematics and raises a ZeroDivisionError_ in python

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

I add a line to cause the ZeroDivisionError_ and comment out the code that randomly fails

.. code-block:: python

  def test_division(self):
      src.calculator.divide(self.x, 0)

      # self.assertEqual(
      #    src.calculator.divide(self.x, self.y),
      #    self.x/self.y
      # )

the terminal shows my expectations with a failure for any value of ``x`` since ``y`` is ``0``

.. code-block:: python

  x = 0, y = 0

    def divide(x, y):
  >    return x / y
  E    ZeroDivisionError: division by zero

:ref:`Exceptions<Exceptions>` like ZeroDivisionError_ break execution of a program. No code will run past the line that causes an :doc:`Exception </how_to/exception_handling_programs>` when it is raised which means I have to take care of it

.. _test_division_green_1:

green: make it pass
#################################################################################

I can use the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` to make sure that a ZeroDivisionError_ is raised when I try to divide a number by ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          src.calculator.divide(self.x, 0)

      # self.assertEqual(
      #   src.calculator.divide(self.x, self.y),
      #   self.x/self.y
      # )

the test passes, showing that the code raises a ZeroDivisionError_

.. _test_division_refactor_1:

refactor: make it better
#################################################################################

* I still have a problem since ``self.y`` can sometimes be ``0``, I use a `while statement`_ to make sure it is never ``0`` in the assertion

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

    * it will be assigned to the result of calling ``a_random_number``
    * and checked again, repeating the process until ``self.y`` is not ``0``

  - if the value of ``self.y`` is not ``0`` at any point, the loop will be exited and the code in the ``else`` block will run

* Since ``self.y`` is ``0`` in the first part of the `while statement`_ I can add a call to the ``divide`` function that will always raise a ZeroDivisionError_

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

  and the terminal shows a ZeroDivisionError_ when ``self.y`` is ``0``

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add an assertRaises_ block to catch the :ref:`Exception<Exceptions>` in the `while statement`_ and remove the previous one from the test

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

  the terminal shows passing tests

* I remove the TODO list

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can have some fun and write the program that makes the tests in ``test_calculator.py`` pass without looking at them

.. _test_calculator_red:

red: make it fail
#################################################################################

* I close ``test_calculator.py``
* then delete the text in ``calculator.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

  see if you can tell what :ref:`Exceptions<Exceptions>` will show up as I go along

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

  which gives me a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I make it a :ref:`function<functions>`

  .. code-block:: python

    def subtract():
        return None

  and the terminal shows another :ref:`TypeError` with a different message

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

  then I add positional arguments to the :ref:`function<functions>`

  .. code-block:: python

    def subtract(a, b):
        return None

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -10
    AssertionError: None != -9
    AssertionError: None != 0
    AssertionError: None != 12

* I change the `return statement`_ to see the difference between the inputs and expected output

  .. code-block:: python

    def subtract(a, b):
        return a, b

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-10, 2) != -12
    AssertionError: (-1, 7) != -8
    AssertionError: (10, 6) != 4
    AssertionError: (7, -10) != 17

  as the name suggests, the test expects the difference between the two inputs

* I make the `return statement`_ match the expectation

  .. code-block:: python

    def subtract(a, b):
        return a - b

  and the terminal shows another :ref:`AttributeError`

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

* I make it return the inputs to see the difference between them and the expected output

  .. code-block:: python

    def multiply(a, b):
        return a, b

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-6, 6) != -36
    AssertionError: (-2, 3) != -6
    AssertionError: (2, 5) != 10
    AssertionError: (-9, -5) != 45

  I make it return the product of the inputs, matching the name of the :ref:`function<functions>`

  .. code-block:: python

    def multiply(a, b):
        return a * b

  and get another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def divide(a, b):
        return a, b

  which gives me an :ref:`AssertionError` that shows the expected output is the result of dividing the inputs

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

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* the return statements of the last 3 have matched the names of the :ref:`functions`, I add a new one

  .. code-block:: python

    def add(a, b):
        return a + b

  and the terminal shows all tests are passing with no random failures

----

*********************************************************************************
review
*********************************************************************************

I wrote the following tests for a program that performs the arithmetic operations

* `test_addition`_
* `test_subtraction`_
* `test_multiplication`_
* `test_division`_

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* ZeroDivisionError_

Would you like to test :doc:`passing values</how_to/pass_values>`?

----

:doc:`/code/code_calculator`
