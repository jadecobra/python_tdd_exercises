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

I want to write a program_ that can ``add``, ``subtract``, ``multiply`` and ``divide``

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_calculator.py
  :language: python
  :linenos:

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``calculator`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh calculator

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 calculator

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_calculator.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestCalculator(unittest.TestCase):

* I add a TODO list to keep track of the work for the program

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-14

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(False)


    # TODO
    # test addition
    # test subtraction
    # test multiplication
    # test division


    # Exceptions Encountered
    # AssertionError

*********************************************************************************
test_addition
*********************************************************************************

* I change ``test_failure`` to ``test_addition`` then change `assertFalse`_ to `assertEqual`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - the `assertEqual method`_ from the `unittest.TestCase class`_ checks if its 2 inputs are the same. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - the explanation I like from what I have seen is that one of them is

    - ``reality`` - ``src.calculator.add(0, 1)``, and the other is my
    - ``expectation`` - ``1``, because ``0`` plus ``1`` is ``1``

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

  because ``src`` is not defined in ``test_calculator.py``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

* then I add an `import statement`_ at the top of the file

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'add'

  I think of ``src.calculator.add`` as an address, ``add`` is something (an :ref:`attribute<AttributeError>`) in the empty ``calculator.py`` file from the ``src`` `folder (directory)`_

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* then I open ``calculator.py`` from the ``src`` folder to open it in the :ref:`editor<2 editors>`, and I type the name

  .. code-block:: python
    :linenos:

    add

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'add' is not defined

* I point it to :ref:`None`

  .. code-block:: python
    :linenos:

    add = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because the ``add`` :ref:`variable<test_attribute_error_w_variables>` is :ref:`None` which is not callable_

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then I change ``add`` to a :ref:`function<functions>` to make it callable_ with the def_ keyword in ``calculator.py``

  .. code-block:: python
    :linenos:

    def add():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: add() takes 0 positional arguments but 2 were given

  the definition of ``add`` does not take input, but 2 were given in the call ``src.calculator.add(0, 1)`` - ``0`` and ``1``

* I make it take 2 arguments

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def add(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != 1

  the ``add`` :ref:`function<functions>` returns :ref:`None`, the test expects ``1``

* I make the `return statement`_ match the expected value

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return 1

  the test passes, time for a victory lap!

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

The ``add`` :ref:`function<functions>` passes the test but does not meet the actual requirement because it always returns ``1``. I want it to do a calculation with the inputs and return the result

:red:`RED`: make it fail
---------------------------------------------------------------------------------

To show the problem with the :ref:`function<functions>`, I add another :ref:`assertion<AssertionError>` in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 7
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

the terminal_ shows :ref:`AssertionError`

.. code-block:: python

  E    AssertionError: 1 != 0

the :ref:`function<functions>` returns ``1``, the test expects ``0``

:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

when I change the `return statement`_ in ``calculator.py`` to add the two inputs

.. code-block:: python
  :linenos:
  :emphasize-lines: 2

  def add(first_input, second_input):
      return first_input + second_input

the test passes

:yellow:`REFACTOR`: make it better
---------------------------------------------------------------------------------

* I want the test to use random numbers instead of numbers that do not change, so I add an `import statement`_ at the top of ``test_calculator.py`` to use random numbers in the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import src.calculator
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that is used to make fake random numbers

* then I add :ref:`variables <test_attribute_error_w_variables>` and a new :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5, 7-10

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            random_x = random.randint(-1, 1)
            random_y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(random_x, random_y),
                random_x+random_x
            )
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )
            self.assertEqual(
                src.calculator.add(-1, 1),
                0
            )

  I hit save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) a few times in the :ref:`editor<2 editors>` to run the tests and the terminal_ shows random success or :ref:`AssertionError` with random values that look like this

  .. code-block:: shell

    AssertionError: X != Y

  I change the expectation of the :ref:`assertion<AssertionError>` in the test to the correct calculation

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(random_x, random_y),
                random_x+random_y
            )

  the test passes

  - ``random.randint(-1, 1)`` returns a random number from ``-1`` up to and including ``1``

    - ``-1`` for negative numbers
    - ``0`` for ``0``
    - ``1`` for positive numbers

* I remove the other :ref:`assertions<AssertionError>` because they are covered by the one that uses random numbers. I do not need them anymore

  .. code-block:: python
    :lineno-start: 6

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            random_x = random.randint(-1, 1)
            random_y = random.randint(-1, 1)

            self.assertEqual(
                src.calculator.add(random_x, random_y),
                random_x+random_y
            )


    # TODO

* There is some duplication, I have to make a change in more than one place when I want to use a different range of random numbers for the test

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            random_x = random.randint(-10, 10)
            random_y = random.randint(-10, 10)

  I add a :ref:`function<functions>` to remove the repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.randint(-1, 1)


    class TestCalculator(unittest.TestCase):

  then I use the new :ref:`function<functions>` for the ``random_x`` and ``random_y`` :ref:`variables<test_attribute_error_w_variables>` in ``test_addition``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-3

        def test_addition(self):
            random_x = a_random_number()
            random_y = a_random_number()

  I now only need to change the range of random numbers for the test in one place

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10, 10)

  and the terminal_ still shows green. I can use any range of numbers the computer can handle, for example

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10**100000, 10**100000)

  the test is still green and takes longer to run. ``10**100000`` is how to write ``10`` raised to the power of ``100,000``. I change the range back to ``-10, 10`` to keep the test running fast

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10, 10)

* then I remove ``test addition`` from the TODO list

  .. code-block:: python
    :lineno-start: 22

    # TODO
    # test subtraction
    # test multiplication
    # test division

----

*********************************************************************************
test_subtraction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a test for subtraction in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-19

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            random_x = a_random_number()
            random_y = a_random_number()

            self.assertEqual(
                src.calculator.add(first_input, second_input),
                random_x+random_y
            )

        def test_subtraction(self):
            random_x = a_random_number()
            random_y = a_random_number()

            self.assertEqual(
                src.calculator.subtract(random_x, random_y),
                random_x-random_y
            )

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'subtract'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def add(first_input, second_input):
        return first_input + second_input


    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'subtract' is not defined

  I point ``subtract`` to :ref:`None`

  .. code-block:: python
    :lineno-start: 5

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I have seen this before

* I change ``subtract`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make ``subtract`` take inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  I hit save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) a few times in the :ref:`editor<2 editors>` to run the tests and the terminal_ shows :ref:`AssertionError` with random values that look like this

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != X

  where ``X`` is a random number.

  ``subtract`` returns :ref:`None`, the test expects ``random_x-random_y`` or ``first_input-second_input`` - the difference between the 2 numbers

* I make the ``subtract`` :ref:`function<functions>` return the difference between the inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the test passes. SUCCESS!

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I have some duplication to remove, the code below happens twice

  .. code-block:: python

    random_x = a_random_number()
    random_y = a_random_number()

  once in ``test_addition`` and again ``test_subtraction``. I add :ref:`class <classes>` :ref:`attributes (variables)<AttributeError>` to remove the duplication and use the same numbers for both tests in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    class TestCalculator(unittest.TestCase):

        random_x = a_random_number()
        random_y = a_random_number()

        def test_addition(self):

  I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in ``test_addition``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3, 5

        def test_addition(self):
            # random_x = a_random_number()
            random_x = self.random_x
            # random_y = a_random_number()
            random_y = self.random_y

            self.assertEqual(
                src.calculator.add(random_x, random_y),
                random_x+random_y
            )

  and in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 3, 5

        def test_subtraction(self):
            # random_x = a_random_number()
            random_x = self.random_x
            # random_y = a_random_number()
            random_y = self.random_y

            self.assertEqual(
                src.calculator.subtract(random_x, random_y),
                random_x-random_y
            )

  the terminal_ shows the tests are still passing. The ``first_input`` and ``second_input`` :ref:`variables<test_attribute_error_w_variables>` are made once as :ref:`class <classes>` :ref:`attributes<AttributeError>` (variables) and used later in each test with ``self.random_x`` and ``self.random_y``, the same way I use `unittest.TestCase`_ :ref:`methods<functions>` like assertEqual_ or assertFalse_

* I remove the commented lines in ``test_addition``

  .. code-block:: python
    :lineno-start: 15

        def test_addition(self):
            x = self.random_x
            y = self.random_y

  and do the same thing in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 24

        def test_subtraction(self):
            x = self.random_x
            y = self.random_y

* I can use the :ref:`class attributes<test_attribute_error_w_class_attributes>` directly in ``test_addition``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-3

            self.assertEqual(
                src.calculator.add(self.random_x, self.random_y),
                self.random_x+self.random_y
            )

  the test is still green

* I do the same thing in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2-3

            self.assertEqual(
                src.calculator.subtract(self.random_x, self.random_y),
                self.random_x-self.random_y
            )

* I remove the ``first_input`` and ``second_input`` :ref:`variables<test_attribute_error_w_variables>` from ``test_addition`` and ``test_subtraction`` since they are no longer needed

  .. code-block:: python
    :lineno-start: 10

    class TestCalculator(unittest.TestCase):

        random_x = a_random_number()
        random_y = a_random_number()

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(self.random_x, self.random_y),
                self.random_x+self.random_y
            )

        def test_subtraction(self):
            self.assertEqual(
                src.calculator.subtract(self.random_x, self.random_y),
                self.random_x-self.random_y
            )


    # TODO

  and the tests are still green!

* I remove ``test subtraction`` from the TODO list

  .. code-block:: python
    :lineno-start: 28

    # TODO
    # test multiplication
    # test division


    # Exceptions Encountered

----

*********************************************************************************
test_multiplication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test for multiplication in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 7-11

      def test_subtraction(self):
          self.assertEqual(
              src.calculator.subtract(self.random_x, self.random_y),
              self.random_x-self.random_y
          )

      def test_multiplication(self):
          self.assertEqual(
              src.calculator.multiply(self.random_x, self.random_y),
              self.random_x*self.random_y
          )

  # TODO

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.calculator' has no attribute 'multiply'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

using what I know so far, I add a :ref:`function<functions>` to ``calculator.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def subtract(first_input, second_input):
      return first_input - second_input


  def multiply(first_input, second_input):
      return first_input * second_input

the test passes! I remove ``test_multiplication`` from the TODO list in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 34


  # TODO
  # test division


  # Exceptions Encountered

----

*********************************************************************************
test_division
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

time for division. I add a new test to ``test_calculator.py``

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 7-11

      def test_multiplication(self):
          self.assertEqual(
              src.calculator.multiply(self.random_x, self.random_y),
              self.random_x*self.random_y
          )

      def test_division(self):
          self.assertEqual(
              src.calculator.divide(self.random_x, self.random_y),
              self.random_x/self.random_y
          )

  # TODO

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.calculator' has no attribute 'divide'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add a :ref:`function<functions>` to ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input / second_input

  then I make the range of numbers for the tests smaller in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-1, 1)

  I hit save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) a few times to run the tests, and when ``second_input`` is randomly ``0`` the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: python

    x = -1, y = 0
    x = 0, y = 0
    x = 1, y = 0

        def divide(first_input, second_input):
    >       return first_input / second_input
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
    E       ZeroDivisionError: division by zero

  dividing by ``0`` is undefined in mathematics and raises :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` in Python

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError

how to test that ZeroDivisionError is raised
---------------------------------------------------------------------------------

:red:`RED`: make it fail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I add a line to cause :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` intentionally and comment out the code that randomly fails in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 2, 4-7

      def test_division(self):
          src.calculator.divide(self.random_x, 0)

          # self.assertEqual(
          #    src.calculator.divide(self.random_x, self.random_y),
          #    self.random_x/self.random_y
          # )

the terminal_ shows my expectation with a failure for any value of ``first_input`` since ``second_input`` is ``0``

.. code-block:: python

  x = -1, y = 0
  x = 0, y = 0
  x = 1, y = 0

      def divide(first_input, second_input):
  >       return first_input / second_input
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
  E       ZeroDivisionError: division by zero

:ref:`Exceptions(Errors)<errors>` like :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` stop a program_ from running. No code runs past the line that causes an :ref:`Exception(Error)<errors>`, which means I have to take care of this problem. See :ref:`how to test that an Exception is raised` for more

:green:`GREEN`: make it pass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* I can use the `assertRaises method`_ to make sure that :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` is raised when I try to divide a number by ``0``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

        def test_division(self):
            with self.assertRaises(AssertionError):
                src.calculator.divide(self.random_x, 0)

            # self.assertEqual(
            #   src.calculator.divide(self.random_x, self.random_y),
            #   self.random_x/self.random_y
            # )

  because I used the wrong :ref:`Exception<errors>` the terminal_ still shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: python

    ZeroDivisionError: division by zero

* I change it to the right :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_x, 0)

  the test passes, showing that ``src.calculator.divide(self.random_x, 0)`` raises :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

:yellow:`REFACTOR`: make it better
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* I still have a problem because ``self.random_y`` can sometimes be ``0``, I use a `while statement`_ to make a never ending loop to make sure it never happens in the :ref:`assertion<AssertionError>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-11

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_x, 0)

            while self.random_y == 0:
                self.random_y = a_random_number()
            else:
                self.assertEqual(
                    src.calculator.divide(self.random_x, self.random_y),
                    self.random_x/self.random_y
                )

  here is what it does

  - when the value of ``self.random_y`` is ``0``

    * it points ``self.random_y`` to the result of calling ``a_random_number()``
    * then it checks if the value of ``self.random_y`` is ``0`` again. The process happens again non stop until ``self.random_y`` is not ``0``

  - when the value of ``self.random_y`` is not ``0``, it leaves the while_ loop and runs the code in the ``else`` block

* Since ``self.random_y`` is ``0`` in the first part of the `while statement`_ I can add a call that fails to the ``divide`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_x, 0)

            while self.random_y == 0:
                src.calculator.divide(self.random_x, self.random_y)
                self.random_y = a_random_number()
            else:
                self.assertEqual(
                    src.calculator.divide(self.random_x, self.random_y),
                    self.random_x/self.random_y
                )

  I hit save (``ctrl+s`` (Windows/Linux) or ``command+s`` (mac)) in the :ref:`editor<2 editors>` a few times to run the tests, and when ``self.random_y`` is randomly ``0``, the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add assertRaises_ to catch the :ref:`Exception<errors>` in the `while statement`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6-7

        def test_division(self):
            with self.assertRaises(ZeroDivisionError):
                src.calculator.divide(self.random_x, 0)

            while self.random_y == 0:
                with self.assertRaises(ZeroDivisionError):
                      src.calculator.divide(self.random_x, self.random_y)
                self.random_y = a_random_number()
            else:
                self.assertEqual(
                    src.calculator.divide(self.random_x, self.random_y),
                    self.random_x/self.random_y
                )

* I no longer need the first assertRaises_ and remove it from the test because it is now part of the while_ loop

  .. code-block:: python
    :lineno-start: 33

        def test_division(self):
            while self.random_y == 0:
                with self.assertRaises(ZeroDivisionError):
                    src.calculator.divide(self.random_x, self.random_y)
                self.random_y = a_random_number()
            else:
                self.assertEqual(
                    src.calculator.divide(self.random_x, self.random_y),
                    self.random_x/self.random_y
                )


    # TODO

  the terminal_ shows all tests are passing with no random failures

* I use a bigger range of numbers for the tests

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10**1000000, 10**1000000)

  the terminal_ still shows green and it takes longer to run the tests. I change the range back to ``-10, 10`` to keep the tests fast

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.randint(-10, 10)

* then I remove the TODO list

  .. code-block:: python
    :lineno-start: 45

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can write the program_ that makes the tests pass without looking at them

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I close ``test_calculator.py``
* then delete all the text in ``calculator.py``, the terminal_ shows 4 failures, I start with the last :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'subtract'

  What :ref:`Exceptions<errors>` do you think are raised as I go along?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'subtract' is not defined

  I point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I change ``subtract`` to a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: subtract() takes 0 positional arguments but 2 were given

  I add :ref:`positional arguments<test_functions_w_positional_arguments>` to the :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != X

* I change the `return statement`_ to see the difference between the inputs and expected output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input, second_input

  the terminal_ shows random numbers with :ref:`AssertionError` that look like this

  .. code-block:: shell

    AssertionError: (X, Y) != Z

  the name of the :ref:`function<functions>` is ``subtract`` and the test expects the difference between the 2 inputs

* I make the `return statement`_ match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'multiply'

* I add a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: multiply() takes 0 positional arguments but 2 were given

  I add 2 :ref:`variables<test_attribute_error_w_variables>` for the positional arguments

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def multiply(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != X

* I change the `return statement`_ to see the difference between the inputs and the expected output

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input, second_input

  the terminal_ shows random numbers with :ref:`AssertionError` that look like this

  .. code-block:: shell

    AssertionError: (X, Y) != Z

  I change it to the multiplication of the inputs to match the name of the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input * second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add another :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError` with random numbers that look like this

  .. code-block:: shell

    AssertionError: (-10, 6) != -1.6666666666666667
    AssertionError: (-6, -6) != 1.0
    AssertionError: (5, 7) != 0.7142857142857143
    AssertionError: (10, 9) != 1.1111111111111112

  or

  .. code-block:: shell

    AssertionError: ZeroDivisionError not raised

  when I change the `return statement`_ to match the expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def divide(first_input, second_input):
        return first_input / second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'add'

* the `return statement`_ of the last 3 :ref:`functions` matched their names, I do the same thing for the new one

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13-14

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input / second_input


    def add(first_input, second_input):
        return first_input + second_input

  and all the tests are passing with no random failures. Lovely! I am a Programmer!

----

*********************************************************************************
review
*********************************************************************************

I wrote the following tests for a program_ that can :ref:`add<test_addition>`, :ref:`subtract<test_subtraction>`, :ref:`multiply<test_multiplication>` and :ref:`divide<test_division>`

* `test_addition`_
* `test_subtraction`_
* `test_multiplication`_
* `test_division`_

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`
* :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

----

:ref:`Click Here to see the code from this chapter<how to make a calculator: tests and solutions>`

----

you know a lot

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>` and
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions with assert methods?<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator<how to make a calculator>`

Would you like to know :ref:`how to test that an Exception is raised?<how to test that an Exception is raised>`

-----


.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->