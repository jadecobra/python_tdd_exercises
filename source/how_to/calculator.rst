.. include:: ../links.rst

#################################################################################
how to make a calculator
#################################################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0gVgMoed3zI?si=FQR1fMtJzElXcQ5n" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

In this chapter I make a basic calculator that performs addition, subtraction, multiplication and division

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

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  the terminal shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_calculator.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
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

* I change ``test_failure`` to ``test_addition``

  .. code-block:: python

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - the assertEqual_ :ref:`method<functions>` from the `unittest.TestCase`_ :doc:`class</classes/classes>` checks if its 2 inputs are equal. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - in this case my expectation is that ``src.calculator.add(0, 1)`` is equal to ``1``

  the terminal shows a NameError because ``src`` is not defined anywhere in ``test_calculator.py``

  .. code-block:: python

    NameError: name 'src' is not defined

.. _test_addition_green:

green: make it pass
#################################################################################

* I add the error to the list of :ref:`Exceptions` encountered

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

  An :ref:`AttributeError` is raised when accessing or calling an attribute that python cannot find. I think of ``src.calculator.add`` as an address

  * ``src.calculator`` refers to ``calculator.py`` in the ``src`` folder/directory
  * ``add`` refers to something (an attribute) within the ``calculator.py`` file which is currently empty

* I add the error to the list of :ref:`Exceptions` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open ``calculator.py`` in the Integrated Development Environment (IDE) and type the name ``add``

  .. code-block:: python

    add

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'add' is not defined

  because ``add`` is not defined (there is no assignment to the name)

* I assign it to the null value :ref:`None`

  .. code-block:: python

    add = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  The :ref:`AttributeError` was fixed by declaring a variable called ``add`` in the ``calculator`` module

* The new error is a :ref:`TypeError` which can occur when an object_ is called in a way that disagrees with its definition. In this case the ``add`` variable is not callable_ because it refers to :ref:`None` which is not a callable_ object. I add the error to the list of :ref:`Exceptions` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I have to define ``add`` as a :ref:`function<functions>` or :doc:`class </classes/classes>` to make it callable. I change the ``add`` variable to a :ref:`function<functions>` with the def_ keyword

  .. code-block:: python

    def add():
        return None

  the terminal still shows a :ref:`TypeError` but with a different message. Progress!

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

* This :ref:`TypeError` shows that the current definition of the ``add`` function takes in 0 inputs, but I provided 2 in when I called it in the test - ``src.calculator.add(0, 1)``. I change the definition in ``calculator.py`` to match the requirement of the ``add`` function taking in two numbers

  .. code-block:: python

    def add(x, y):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  the result of ``src.calculator.add(0, 1)`` is not equal to ``1`` because the ``add`` :ref:`function<functions>` returns :ref:`None`

* I change it to return the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  and the test passes. Time for a victory lap.

  .. code-block:: python

    tests/test_calculator.py .               [100%]

    ============== 1 passed in X.YZs ===============

.. _test_addition_refactor:

refactor: make it better
#################################################################################

Wait a minute! Is it that easy? Do I just provide the expectation of the test to make it pass? In the green phase, Yes. I do whatever it takes to make the test pass even if I have to cheat.

Solving the problem this way shows a problem with the test, which means I need to "Make it Better"

* When a user tries to add other numbers that are not ``0`` and ``1``, the ``add`` function returns ``1``
* When a user tries to add negative numbers, the ``add`` function returns ``1``
* The ``add`` function returns ``1`` no matter what inputs are given. It is a :doc:`singleton function </functions/test_singleton_functions>`

Even though the ``add`` function currently passes this test it does not meet the actual requirement.

.. _test_addition_refactor_red:

red: make it fail
---------------------------------------------------------------------------------

I add a new test to ``test_addition`` in ``test_calculator.py`` to show that ``add`` always returns ``1``

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

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  E    AssertionError: 1 != 0

.. _test_addition_refactor_green:

green: make it pass
---------------------------------------------------------------------------------

I change the `return statement`_ of the ``add`` :ref:`function<functions>` to return the sum of its inputs

.. code-block:: python

  def add(x, y):
      return x + y

and the terminal shows passing tests

.. _test_addition_refactor_refactor:

refactor: make it better
---------------------------------------------------------------------------------

* I want to test the function with random numbers, so I do not need to add more tests to check the ``add`` :ref:`function<functions>`. I import python's random_ library to generate random numbers for the test

  .. code-block:: python

    import random
    import src.calculator
    import unittest

* then assign a random number to the x and y variables and change the test to use these variables

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(x, y),
                x+y
            )

  - ``x = random.randint(-1, 1)`` assigns a variable called ``x`` to the result of calling ``random.randint(-1, 1)``
  - ``random.randint(-1, 1)`` returns a random digit that is either -1, 0 or 1 to represent the case of negative numbers, zero and positive numbers

  the terminal still shows passing tests

* I no longer need the previous tests because this new test covers the cases for negative numbers, zero and positive numbers
* I remove ``test addition`` from the TODO list

  .. code-block:: python

    # TODO
    # test subtraction
    # test multiplication
    # test division

* then add a function to remove the duplication of the calls to `random.randint`_ with the same values

  .. code-block:: python

    import random
    import src.calculator
    import unittest



    def random_number():
        return random.randint(-1, 1)


  and call it for the ``x`` and ``y`` variables

  .. code-block:: python

    def test_addition(self):
        x = random_number()
        y = random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

  the test still passes

* I can now change the range of random numbers I use in the test in one place instead of two, for example

  .. code-block:: python

      def random_number():
        return random.randint(-10**9, 10**9)

  to use a range of numbers from minus 1 billion to 1 billion

----

*********************************************************************************
test_subtraction
*********************************************************************************

Since addition works, it is time to add a failing test for subtraction

.. _test_subtraction_red:

red: make it fail
#################################################################################

* I add a :ref:`method<functions>` called ``test_subtraction`` to ``test_calculator.py``

  .. code-block:: python

    def test_addition(self):
        x = random_number()
        y = random_number()

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

    def test_subtraction(self):
        x = random_number()
        y = random_number()

        self.assertEqual(
            src.calculator.subtract(x, y),/
            x-y
        )

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

.. _test_subtraction_green:

green: make it pass
#################################################################################

* I add a variable assignment in ``calculator.py``

  .. code-block:: python

    def add(x, y):
        return x + y


    subtract = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  this is familiar

* I change ``subtract`` to a :ref:`function<functions>` to make it callable

  .. code-block:: python

    def subtract():
        return None

  and the terminal shows a :ref:`TypeError` with a different error message. Progress again!

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make the ``subtract`` :ref:`function<functions>` take inputs to match the expectation

  .. code-block:: python

    def subtract(x, y):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != -2
    AssertionError: None != -1
    AssertionError: None != 0
    AssertionError: None != 1

* When I change the `return statement`_ in ``subtract`` to return the difference between the inputs

  .. code-block:: python

    def subtract(x, y):
        return x - y

  all the tests pass. SUCCESS!

* ``test subtraction`` can now be removed from the TODO list

  .. code-block:: python

    # TODO
    # test multiplication
    # test division

.. _test_subtraction_refactor:

refactor: make it better
#################################################################################

* I have some duplication to remove in keeping with `The Do Not Repeat Yourself (DRY) Principle`_

  - ``x = random_number()`` happens twice
  - ``y = random_number()`` happens twice

* I can use :doc:`class </classes/classes>` attributes (variables) in the ``TestCalculator`` :doc:`class </classes/classes>` in ``test_calculator.py`` to make the random variables only once and reference them later in the tests by using ``self``

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        x = random_number()
        y = random_number()

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

  - all tests are still passing, so my change did not break anything. Fantastic!
  - The ``x`` and ``y`` variables are initialized once as :doc:`class </classes/classes>` attributes (variables) and accessed later in every test using ``self.x`` and ``self.y``, the same way I can call `unittest.TestCase`_ :ref:`methods<functions>` like assertEqual_ by using ``self.assertEqual``


----

*********************************************************************************
test_multiplication
*********************************************************************************

Moving on to test multiplication, the next item on the TODO list

.. _test_multiplication_red:

red: make it fail
#################################################################################

I add a failing test called ``test_multiplication`` to ``test_calculator.py``

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

the terminal shows an :ref:`AttributeError` ::

  AttributeError: module 'src.calculator' has no attribute 'multiply'

this is definitely familiar

.. _test_multiplication_green:

green: make it pass
#################################################################################

using what I know so far I add a definition for ``multiplication`` to ``calculator.py``

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

I add ``test_division`` to ``test_calculator.py``

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

the terminal shows an :ref:`AttributeError` ::

  AttributeError: module 'src.calculator' has no attribute 'divide'

.. _test_division_green_0:

green: make it pass
#################################################################################

* I add a ``divide`` :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def divide(x, y):
        return x / y

  the test result changes because of the value of ``y``

  - when ``y`` is ``-1`` or ``1`` the test passes
  - when ``y`` is ``0`` it raises a ZeroDivisionError_, for example

    .. code-block:: python

      x = 1, y = 0

        def divide(x, y):
      >    return x / y
      E    ZeroDivisionError: division by zero

* I add ZeroDivisionError_ to the list of :ref:`Exceptions` encountered

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

I add a failing line to ``test_division``, I want to cause a ZeroDivisionError_ by dividing by ``0``, and comment out the test that sometimes fails, while I figure out the error

.. code-block:: python

  def test_division(self):
      src.calculator.divide(self.x, 0)
      # self.assertEqual(
      #     src.calculator.divide(self.x, self.y),
      #     self.x/self.y
      # )

the terminal shows my expectations with a failure for any value of ``x`` when ``y`` is ``0``.

.. code-block:: python

  x = 0, y = 0

    def divide(x, y):
  >    return x / y
  E    ZeroDivisionError: division by zero

:doc:`Exceptions </how_to/exception_handling_programs>` like ZeroDivisionError_ break execution of a program. No code will run past the line that causes an :doc:`Exception </how_to/exception_handling_programs>` when it is raised which means I have to take care of this error, so I do not have random failures in the test

.. _test_division_green_1:

green: make it pass
#################################################################################

I can use the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` in ``test_division`` to make sure that a ZeroDivisionError_ is raised when I try to divide a number by ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          src.calculator.divide(self.x, 0)
      # self.assertEqual(
      #     src.calculator.divide(self.x, self.y),
      #     self.x/self.y
      # )

the terminal shows passing tests, and I have a way to handle :doc:`Exceptions </how_to/exception_handling_programs>` when testing, which helps to confirm that the code raises an error while allowing other tests to continue running. There is more of this in :doc:`/how_to/exception_handling_tests`

.. _test_division_refactor_1:

refactor: make it better
#################################################################################

I can use a `while statement`_ for the other cases when the divisor is not ``0`` by making sure the value of ``y`` that is passed from the test to ``src.calculator.divide`` is never ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          src.calculator.divide(self.x, 0)

      while self.y == 0:
          self.y = random_number()
      self.assertEqual(
          src.calculator.divide(self.x, self.y),
          self.x/self.y
      )

* ``while self.y == 0:`` makes a loop that repeats as long as ``self.y`` is equal to ``0``

  - the loop checks if the value of ``self.y`` is ``0``

    * if it is then it assigns it a new value with ``self.y = random_number()`` and does the check again, repeating the process until ``self.y`` is not ``0``
    * if it is not then it stops and moves on to the rest of the code
  - the loop stops when ``self.y`` is not equal to ``0``

* I can remove the TODO list since all the tests are passing

----

*********************************************************************************
test_calculator
*********************************************************************************

I want to write the program that makes the tests in ``test_calculator.py`` pass without looking at them

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

    AssertionError: None != -1
    AssertionError: None != 0
    AssertionError: None != 1
    AssertionError: None != 2

* I change the `return statement`_ to see the difference between the inputs and expected output

  .. code-block:: python

    def subtract(a, b):
        return (a, b)

  which gives me another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-1, 1) != -2
    AssertionError: (0, 1) != -1
    AssertionError: (0, 0) != 0
    AssertionError: (0, -1) != 1

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

    AssertionError: None != -1
    AssertionError: None != 0
    AssertionError: None != 1

* I change the `return statement` to see the difference between the inputs and the expected output

  .. code-block:: python

    def multiply(a, b):
        return (a, b)

  and the terminal shows another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-1, 1) != -1
    AssertionError: (0, -1) != 0
    AssertionError: (0, 0) != 0
    AssertionError: (1, 1) != 1

  I change the `return statement` to return the product of the inputs, matching the name of the :ref:`function<functions>`

  .. code-block:: python

    def multiply(a, b):
        return a * b


  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def divide(a, b):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: ZeroDivisionError not raised

  this test expects an :ref:`Exception<exceptions>` which is raised when a number is divided by 0. I change the `return statement`_ to match the name of the :ref:`function<functions>`

  .. code-block:: python

    def divide(a, b):
        return a / b

  and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* I add a :ref:`function<functions>`

  .. code-block:: python

    def add(a, b):
        return None

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 0

  then change the `return statement`_ to show the difference between the inputs and the expected output

  .. code-block:: python

    def add(a, b):
      return (a, b)

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (-1, -1) != -2
    AssertionError: (-1, 0) != -1
    AssertionError: (1, -1) != 0
    AssertionError: (0, 1) != 1

  when I change the `return statement`_ to the sum of the inputs

  .. code-block:: python

    def add(a, b):
        return a + b

  the terminal shows all tests are passing

----

*********************************************************************************
review
*********************************************************************************

CONGRATULATIONS! You used Test Driven Development to write a program that can perform the 4 basic arithmetic operations of addition, subtraction, multiplication and division.

You also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* ZeroDivisionError_

Would you like to test :doc:`passing values</how_to/pass_values>`?


----

:doc:`/code/code_calculator`
