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

.. _test_addition:

*********************************************************************************
test_addition
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal and run :ref:`makePythonTdd.sh` with ``calculator`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh calculator

  .. NOTE::

    If you are using Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  and it shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_calculator.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then add a TODO list to keep track of requirements for the calculator

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

* I change ``test_failure`` with ``test_addition``

  .. code-block:: python

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - I use the assertEqual_ :ref:`method<functions>` from the `unittest.TestCase`_ :doc:`class</classes/classes>` which checks if its 2 inputs are equal. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - I am sending two things for assertEqual_ to check

    * first: ``src.calculator.add(0, 1)`` calls the ``add`` function in ``calculator.py`` with ``0`` and ``1`` as inputs
    * second: ``1`` is the expected result from calling the ``add`` function in ``calculator.py`` with ``0`` and ``1`` as inputs
    * my expectation is that ``src.calculator.add(0, 1)`` is equal to ``1``

  the terminal shows a NameError because ``src`` is not defined anywhere in ``test_calculator.py``

  .. code-block:: python

    NameError: name 'src' is not defined

green: make it pass
#################################################################################

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered ::

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ for the ``calculator`` module

  .. code-block:: python

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):
    ...

  and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

  - The :ref:`AttributeError` is at line 12 in ``test_calculator.py``
  - An :ref:`AttributeError` is raised when accessing or calling an attribute that python cannot find
  - I think of ``src.calculator.add`` as an address

  * ``src.calculator`` refers to ``calculator.py`` in the ``src`` folder/directory
  * ``add`` refers to something (an attribute) within the ``calculator.py`` file

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then open ``calculator.py`` in the Integrated Development Environment (IDE) and type the name ``add``

  .. code-block:: python

    add

  the terminal shows a NameError_ because ``add`` is not defined (there is no assignment to the name)

  .. code-block:: python

    NameError: name 'add' is not defined

* I assign the name ``add`` to the null value :ref:`None`

  .. code-block:: python

    add = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  The :ref:`AttributeError` was fixed by declaring a variable called ``add`` in the ``calculator`` module

* The new error is a :ref:`TypeError` which can occur when an `object <https://docs.python.org/3/glossary.html#term-object>`_ is called in a way that disagrees with the object's definition. In this case the ``add`` variable is not callable_ because it refers to :ref:`None` which is not a callable_ object. I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I have to define ``add`` as a :ref:`function<functions>` or :doc:`class </classes/classes>` to make it callable. I know the def_ keyword is used for making :doc:`/functions/functions` and will test changing the ``add`` variable to a :ref:`function<functions>` in ``calculator.py``

  .. code-block:: python

    def add():
        return None

  the terminal still shows a :ref:`TypeError` but with a different message. Progress!

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

* This :ref:`TypeError` shows that the current definition of the ``add`` function takes in 0 inputs, but I provided 2 - ``src.calculator.add(0, 1)`` in the call. I change the definition in ``calculator.py`` to make it match the requirement of the ``add`` function taking in two numbers

  .. code-block:: python

    def add(x, y):
        return None

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 1

  An :ref:`AssertionError` is raised when an assertion is :doc:`False </data_structures/booleans/booleans>`. assertEqual_ :ref:`method<functions>` raises an :ref:`AssertionError` when the two inputs it is given are not equal. In other words the result of calling ``src.calculator.add(0, 1)`` is currently not equal to ``1``

* I make the function return the expected value

  .. code-block:: python

    def add(x, y):
        return 1

  and the test passes. Time for a victory lap.

  .. code-block:: python

    tests/test_calculator.py .               [100%]

    ============== 1 passed in 0.01s ===============


refactor: make it better
#################################################################################

Wait a minute. Is it that easy? Do I just provide the expectation of the test to make it pass? In the green phase, yes. I do whatever it takes to make the test pass even if I have to cheat.

Solving the problem this way shows a problem with the test, which means I need to "Make it Better"

* If a user tries to add other numbers that are not ``0`` and ``1``, the ``add`` function will return ``1``
* If a user tries to add negative numbers, the ``add`` function wil return ``1``
* The ``add`` function will return ``1`` no matter what inputs the user gives. It is a :doc:`singleton function </functions/test_singleton_functions>`

Even though the ``add`` function currently passes this test it does not meet the actual requirement.

red: make it fail
---------------------------------------------------------------------------------

I add a new test to ``test_addition`` in ``test_calculator.py``

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

the terminal shows an :ref:`AssertionError`, showing that the ``add`` function always returns ``1`` no matter what inputs are given

.. code-block:: python

  E    AssertionError: 1 != 0

green: make it pass
---------------------------------------------------------------------------------

I change the `return statement`_ of the ``add`` :ref:`function<functions>` to return the sum of its inputs

.. code-block:: python

  def add(x, y):
      return x + y

and the terminal shows passing tests which increases my confidence in the ``add`` function

.. code-block:: python

  tests/test_calculator.py .              [100%]

  ============== 1 passed in 0.01s ==============

refactor: make it better
---------------------------------------------------------------------------------

* I want to test the function with random numbers, so import python's random_ library to generate random numbers for the test

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
  - ``random.randint(-1, 1)`` returns a random digit that is -1, 0 or 1 to represent the case of negative numbers, zero and positive numbers
  - the ``assertEqual`` tests that when these two random numbers are given to the ``add`` function as inputs, the output returned is the result of adding them together

  the terminal still shows passing tests

    .. code-block:: python

      tests/test_calculator.py ..              [100%]

      ============= 1 passed in 0.01s ===============

* I no longer need the previous tests because this new test shows the scenarios for negative numbers, zero and positive numbers
* I remove ``test addition`` from the TODO list since it passes

    .. code-block:: python

      # TODO
      # test subtraction
      # test multiplication
      # test division

----

*********************************************************************************
test_subtraction
*********************************************************************************

Since addition works, it is time to add a failing test that tests subtraction

red: make it fail
#################################################################################

* I add a :ref:`method<functions>` called ``test_subtraction`` to ``test_calculator.py``

  .. code-block:: python

    def test_addition(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        self.assertEqual(
            src.calculator.add(x, y),
            x+y
        )

    def test_subtraction(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

        self.assertEqual(
            src.calculator.subtract(x, y),
            x-y
        )

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

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

refactor: make it better
#################################################################################

* I have some duplication to remove in keeping with `The Do Not Repeat Yourself (DRY) Principle`_

  - ``x = random.randint(-1, 1)`` happens twice
  - ``y = random.randint(-1, 1)`` happens twice

* I can use :doc:`class </classes/classes>` attributes (variables) in the ``TestCalculator`` :doc:`class </classes/classes>` in ``test_calculator.py`` to make the random variables only once and reference them later in the tests by using ``self``

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

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

.. _test_multiplication:

*********************************************************************************
test_multiplication
*********************************************************************************

Moving on to test multiplication, the next item on the TODO list

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

.. _test_division:

*********************************************************************************
test_division
*********************************************************************************

Now it is down to the test for division

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

  AttributeError: module 'src.calculator' has no attribute 'division'

green: make it pass
#################################################################################

* I add a ``divide`` :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python

    def divide(x, y):
        return x / y

  the test result changes depending on the variables of ``y``

  - when ``y`` is ``-1`` or ``1`` the test passes
  - when ``y`` is ``0`` it raises a ZeroDivisionError_, for example

    .. code-block:: python

      x = 1, y = 0

        def divide(x, y):
      >    return x / y
      E    ZeroDivisionError: division by zero

* I add ZeroDivisionError_ to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError


how to Test for Errors
---------------------------------------------------------------------------------

red: make it fail
#################################################################################

I add a failing line to ``test_division``, I want to cause a ZeroDivisionError_ by dividing by 0, and comment out test that sometimes fails to remove the variability of the test while I figure out the error

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

:doc:`Exceptions </how_to/exception_handling_programs>` like ZeroDivisionError_ break execution of a program. No code will run past the line that causes an :doc:`Exception </how_to/exception_handling_programs>` when it is raised which means that no other tests will run until I take care of this error

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

the terminal shows passing tests, and I now have a way to ``catch`` :doc:`Exceptions </how_to/exception_handling_programs>` when testing, which helps to confirm that the code raises an error while allowing other tests to continue running

refactor: make it better
#################################################################################

I can use a `while statement`_ for the other cases when the divisor is not ``0`` by making sure the value of ``y`` that is passed from the test to ``src.calculator.divide`` is never ``0``

.. code-block:: python

  def test_division(self):
      with self.assertRaises(ZeroDivisionError):
          src.calculator.divide(self.x, 0)
      while self.y == 0:
          self.y = random.randint(-1, 1)
      self.assertEqual(
          src.calculator.divide(self.x, self.y),
          self.x/self.y
      )

* ``while self.y == 0:`` makes a loop that repeats as long as ``self.y`` is equal to ``0``

  -  ``self.y = random.randint(-1, 1)`` assigns a new random variable to ``self.y`` that could be -1, 0 or 1
  - the loop tells python to assign a new random variable to ``self.y`` as long as the current value of ``self.y`` is equal to ``0``
  - the loop stops when ``self.y`` is not equal to ``0``

* I can remove the TODO list since all the tests are passing

----

*********************************************************************************
review
*********************************************************************************

CONGRATULATIONS! You made it through writing a program that can perform the 4 basic arithmetic operations of addition, subtraction, multiplication and division using Test Driven Development.

You also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* ZeroDivisionError_

Would you like to learn :doc:`/how_to/pass_values`?

----

:doc:`/code/code_calculator`
