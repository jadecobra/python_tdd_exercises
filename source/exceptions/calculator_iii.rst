.. meta::
  :description: Facing a Python TypeError? Learn to fix common errors like 'unsupported operand type' and 'int object is not callable'. Watch the full tutorial to debug now.
  :keywords: Jacob Itegboje, python typeerror unsupported operand type, python typeerror 'int' object is not callable, python typeerror can only concatenate str, how to fix typeerror in python, python typeerror string and integer, python typeerror list indices must be integers, python typeerror 'str' object is not callable, python typeerror float object is not iterable

.. include:: ../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
how to make a calculator part 3
#################################################################################

*********************************************************************************
test_calculator_raises_type_error
*********************************************************************************

I want to use TypeError_ with :ref:`exception handlers<how to use try...except...else>` to make sure that the :ref:`calculator program<how to make a calculator part 1>` only works with numbers, the way a Calculator would in the real world.

=================================================================================
open the project
=================================================================================

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I use ``pytest-watch`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 4 items

    tests/test_calculator.py ....                                        [100%]

    ============================ 4 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new failing test to show that the :ref:`calculator<how to make a calculator part 1>` raises TypeError_ when one of the inputs is :ref:`None`, just like in :ref:`test_type_error_w_objects_that_do_not_mix`

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 16-17

      def test_division(self):
          try:
              self.assertEqual(
                  src.calculator.divide(
                      self.random_first_number,
                      self.random_second_number
                  ),
                  self.random_first_number/self.random_second_number
              )
          except ZeroDivisionError:
              self.assertEqual(
                  src.calculator.divide(self.random_first_number, 0),
                  'undefined: I cannot divide by 0'
              )

      def test_calculator_raises_type_error_w_none(self):
          src.calculator.add(None, None)


  # Exceptions seen

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-3

      def test_calculator_raises_type_error_w_none(self):
          with self.assertRaises(TypeError):
              src.calculator.add(None, None)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add a failing line for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

        def test_calculator_raises_type_error_w_none(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None None)
            src.calculator.divide(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.add(self.random_first_number, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(self.random_first_number, None)

  the test passes

* I add another failing line, this time for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            src.calculator.multiply(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)

  the test passes

* I add another one for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)
            src.calculator.subtract(None, None)

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

  I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-9

        def test_calculator_raises_type_error_w_none(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply(None, None)
            with self.assertRaises(TypeError):
                src.calculator.subtract(None, None)


    # Exceptions seen

  the test passes

The ``calculator`` raises TypeError_ when given :ref:`None` as input. What does it do when the input is a :ref:`boolean<booleans>`, string_, tuple_, :ref:`list<lists>`, set_ or :ref:`a dictionary<dictionaries>`?

*********************************************************************************
test_calculator_raises_type_error_w_strings
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test with an :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_an_assertion`  to test the :ref:`add function<test_addition>` with strings_

.. code-block:: python
  :lineno-start: 64
  :emphasize-lines: 4-5

          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

      def test_calculator_with_strings(self):
          self.assertEqual(src.calculator.add('1', '1'), '2')


  # Exceptions seen

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '11' != '2'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 1

          self.assertEqual(src.calculator.add('1', '1'), '11')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            self.assertEqual(src.calculator.divide('1', '1'), '11')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

  I change assertEqual_ to assertRaises_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-4

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the test passes

* I try it with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            src.calculator.multiply('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: none

    TypeError: can't multiply sequence by non-int of type 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            src.calculator.subtract('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-9

        def test_calculator_w_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None, None)
            with self.assertRaises(TypeError):
                src.calculator.divide(None, None)
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  the test passes

---------------------------------------------------------------------------------
how to test if something is an instance of an object in a program
---------------------------------------------------------------------------------

I want the :ref:`add function<test_addition>` to raise TypeError_ when it gets a string_, the same way the other :ref:`functions` raise TypeError_ when one of the inputs is a string_. I can use the `isinstance function`_ which is like the `assertIsInstance method`_ from when I tested :ref:`None`, it checks if one thing is an instance or child of a :ref:`class<classes>`

* I change the assertEqual_ to assertRaises_ in ``test_calculator_with_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

        def test_calculator_with_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I open ``calculator.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add an :ref:`if statement<if statements>` to the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-7

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            raise TypeError
        else:
            return first_input + second_input

  the test passes

  .. NOTE::

    - the `isinstance function`_ like the `assertIsInstance method`_ checks if the first input it is given is an instance (child) of the :ref:`class<classes>` it is given as the second input. It is part of `Python's Built-in Functions`_
    - the :ref:`if statement<if statements>` ``if isinstance(first_input, str) or isinstance(second_input, str):`` is :ref:`True<test_what_is_true>` if

      * ``first_input`` is a string_ and ``second_input`` is NOT a string_
      * ``first_input`` is NOT a string_ and ``second_input`` is a string_
      * ``first_input`` is a string_ and ``second_input`` is a string_

      the statement is only :ref:`False<test_what_is_false>` if ``first_input`` is NOT a string_ and ``second_input`` is NOT a string_. This is :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`, which only returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`False<test_what_is_false>`

* I change the name of the test to be clearer

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

        def test_calculator_raises_type_error_w_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')


    # Exceptions seen

----

*********************************************************************************
test_calculator_sends_message_when_input_is_not_a_number
*********************************************************************************

I want the :ref:`calculator functions<how to make a calculator part 1>` to send a message when the input is not a number, not raise TypeError_ which causes the program to stop. I want the user to be able to try again with different input

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in ``test_calculator_raises_type_error_w_none``

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-5

      def test_calculator_raises_type_error_w_none(self):
          self.assertEqual(
              src.calculator.add(None, None),
              'Excuse me?! Numbers only! try again...'
          )
          with self.assertRaises(TypeError):
              src.calculator.divide(None, None)
          with self.assertRaises(TypeError):
              src.calculator.multiply(None, None)
          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

the terminal_ shows TypeError_

.. code-block:: shell

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add an :ref:`exception handler<how to use try...except...else>` to the `else clause`_ of the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 4-8

  def add(first_input, second_input):
      if isinstance(first_input, str) or isinstance(second_input, str):
          raise TypeError
      else:
          try:
              return first_input + second_input
          except TypeError:
              return 'Excuse me?! Numbers only! try again...'

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I want the same thing to happen when the :ref:`add function<test_addition>` gets a string_ as input. I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2-5

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError

* I change the `raise statement`_ to a `return statement`_ in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'Excuse me?! Numbers only! try again...'
        else:
            try:
                return first_input + second_input
            except TypeError:
                return 'Excuse me?! Numbers only! try again...'

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 6-9

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

* I add another :ref:`except clause<how to use try...except...else>` to the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7

    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'
        except TypeError:
            return 'Excuse me?! Numbers only! try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  ``test_calculator_raises_type_error_w_none`` fails because it expects TypeError_ when the inputs are not numbers

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in ``test_calculator_raises_type_error_w_none`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-9

    def test_calculator_raises_type_error_w_none(self):
        self.assertEqual(
            src.calculator.add(None, None),
            'Excuse me?! Numbers only! try again...'
        )
        self.assertEqual(
            src.calculator.divide(None, None),
            'Excuse me?! Numbers only! try again...'
        )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in ``test_calculator_raises_type_error_w_none``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 5-8


            self.assertEqual(
                src.calculator.divide(None, None),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.multiply(None, None),
                'Excuse me?! Numbers only! try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: shell

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`multiply function<test_multiplication>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-5

    def multiply(first_input, second_input):
        try:
            return first_input * second_input
        except TypeError:
            return 'Excuse me?! Numbers only! try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in ``test_calculator_raises_type_error_w_strings`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in ``test_calculator_raises_type_error_w_strings``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )


    # Exceptions seen

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`subtract function<test_subtraction>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def subtract(first_input, second_input):
        try:
            return first_input - second_input
        except TypeError:
            return 'Excuse me?! Numbers only! try again...'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in ``test_calculator_raises_type_error_w_none`` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(None, None),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                'Excuse me?! Numbers only! try again...'
            )


        def test_calculator_raises_type_error_w_strings(self):

  the test passes

  That was a lot of doing the same thing over and over again.

  - ``test_calculator_raises_type_error_w_none`` and ``test_calculator_raises_type_error_w_strings`` both look the same
  - the :ref:`calculator<how to make a calculator part 1>` no longer raises TypeError_ when any of the inputs are NOT a number

* I remove the name of ``test_calculator_raises_type_error_w_strings`` to make its :ref:`assertions<what is an assertion?>` part of ``test_calculator_raises_type_error_w_none``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 5-20

            self.assertEqual(
                src.calculator.subtract(None, None),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.add('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'Excuse me?! Numbers only! try again...'
            )


    # Exceptions seen

* I change the name from ``test_calculator_raises_type_error_w_none`` to ``test_calculator_sends_message_when_input_is_not_a_number`` to be clearer

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            self.assertEqual(

  the tests are still green

* I have the same error message 8 times in this test. I use a :ref:`variable<what is a variable?>` to make it better

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2, 6, 10, 14, 18, 22, 26, 30, 34

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'Excuse me?! Numbers only! try again...'

            self.assertEqual(
                src.calculator.add(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                error_message
            )
            self.assertEqual(
                src.calculator.add('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

  still green. All these :ref:`assertions<what is an assertion?>` look the same, they check that the :ref:`calculator<how to make a calculator part 1>` :ref:`functions` return an error message when they get input that is NOT a number

  .. code-block:: python

    self.assertEqual(
        src.calculator.function(NOT_A_NUMBER, ALSO_NOT_A_NUMBER),
        error_message
    )

  there has to be :ref:`a better way to test the calculator with inputs that are NOT numbers`

----

*********************************************************************************
how to make a decorator function
*********************************************************************************

All the :ref:`functions` in the :ref:`calculator program<how to make a calculator part 1>` have the same :ref:`exception handler<how to use try...except...else>`


.. code-block:: python

  try:
      something
  except TypeError:
      return 'Excuse me?! Numbers only! try again...'

the :ref:`divide function<test_division>` is different because it has another :ref:`except clause<how to use try...except...else>`

.. code-block:: python

  except ZeroDivisionError:
      return 'undefined: I cannot divide by 0'

the other part that is different for all the :ref:`functions` are the calculations

.. code-block:: python

  return first_input - second_input
  return first_input * second_input
  return first_input / second_input
  return first_input + second_input

=================================================================================
what is a decorator function?
=================================================================================

A decorator or wrapper :ref:`function<functions>` takes another :ref:`function<functions>` as input and returns a :ref:`function<functions>`. I can use it to remove the :ref:`exception handler<how to use try...except...else>` that is the same in all of the :ref:`calculator functions<how to make a calculator part 1>`

* I add a new :ref:`function<functions>` add the top of ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            try:
                return function(first_input, second_input)
            except TypeError:
                return 'Excuse me?! Numbers only! try again...'
        return wrapper


    def subtract(first_input, second_input):

  The ``only_takes_numbers`` :ref:`function<functions>` takes a :ref:`function<functions>` as input

  - it tries to return the result of the :ref:`function<functions>` working on the two inputs
  - if TypeError_ is raised it returns the error message

* I use it to wrap the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

    @only_takes_numbers
    def subtract(first_input, second_input):
        try:

  the test is still green

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):

  still green

* I do the same thing with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

    @only_takes_numbers
    def multiply(first_input, second_input):
        try:

  the terminal_ shows green

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):

  the tests are still passing

* on to the :ref:`divide function<test_functions>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

    @only_takes_numbers
    def divide(first_input, second_input):
        try:

  still green

* I remove the :ref:`except clause<how to use try...except...else>` for TypeError_

  .. code-block:: python
    :lineno-start: 20

    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    def add(first_number, second_input):

  all the tests are still green

* one more to go, I wrap the :ref:`add function<test_addition>` with the ``only_takes_numbers`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):

  the test is still passing

* I remove the :ref:`exception handler<how to use try...except...else>` from the `else clause`_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'Excuse me?! Numbers only! try again...'
        else:
            return first_input + second_input

  green! Lovely!

* I can make a :ref:`function<functions>` for the condition in the :ref:`if statement<if statements>` in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def is_string(something):
        return isinstance(something, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if is_string(first_input) or is_string(second_input):
            return 'Excuse me?! Numbers only! try again...'
        else:
            return first_input + second_input

  the test is still green

  - This removes the duplication of ``str`` in the call to the `isinstance function`_

    .. code-block:: python

      isinstance(first_input, str)
      isinstance(second_input, str):

  - it also adds 2 lines of code to remove 6 characters. WOW!

* I can make a :ref:`function<functions>` for the whole :ref:`if statement<if statements>` in the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def one_input_is_a_string(first_input, second_input):
        return isinstance(first_input, str) or isinstance(second_input, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if one_input_is_a_string(first_input, second_input):
            return 'Excuse me?! Numbers only! try again...'
        else:
            return first_input + second_input

  the test is still green.

  - the ``one_input_is_a_string`` :ref:`function<functions>` looks the same as :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`
  - this makes it easier to change the :ref:`condition<if statements>` later without touching the :ref:`add function<test_addition>`
  - it still adds 2 lines of code

* I can also make a decorator :ref:`function<functions>` for the :ref:`if statement<if statements>` to practice making a decorator :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def reject_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! Numbers only! try again...'
            else:
                return function(first_input, second_input)
        return wrapper


    def only_takes_numbers(function):

* then use it to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 37

    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):

  the test is still green

* I remove the :ref:`if statement<if statements>` from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions` have parts that are the same

  .. code-block:: python

        def wrapper(first_input, second_input):
            ...
            return 'Excuse me?! Numbers only! try again...'
            ...
            return function(first_input, second_input)
        return wrapper

  I make a new :ref:`function<functions>` that has the :ref:`if statement<if statements>` from ``reject_strings`` and the :ref:`exception handler<how to use try...except...else>` from ``only_takes_numbers``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-10

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! Numbers only! try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! Numbers only! try again...'
        return wrapper


    def reject_strings(function):

* I use the new :ref:`function<functions>` to wrap the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 1

    @only_takes_numbers_and_rejects_strings
    @reject_strings
    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* I remove the other wrappers from the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 49

    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

  still green

* I wrap the other :ref:`functions<functions>` with ``only_takes_numbers_and_reject_strings``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1, 7, 13

    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):

  the terminal_ shows green

* I remove ``only_takes_numbers`` from each :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 31

    @only_takes_numbers_and_rejects_strings
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* I remove the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions`

  .. code-block:: python
    :linenos:

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! Numbers only! try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! Numbers only! try again...'
        return wrapper


    @only_takes_numbers_and_rejects_strings
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers_and_rejects_strings
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers_and_rejects_strings
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

* I change the name of the new decorator :ref:`function<functions>` to make it easier

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 13, 18, 23, 31

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'Excuse me?! Numbers only! try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'Excuse me?! Numbers only! try again...'
        return wrapper


    @only_takes_numbers
    def subtract(first_input, second_input):
        return first_input - second_input


    @only_takes_numbers
    def multiply(first_input, second_input):
        return first_input * second_input


    @only_takes_numbers
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'undefined: I cannot divide by 0'


    @only_takes_numbers
    def add(first_input, second_input):
        return first_input + second_input

  still green

* There is also duplication of the error message. I add a :ref:`variable<what is a variable?>` to remove it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 6, 11

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            error_message = 'Excuse me?! Numbers only! try again...'

            if isinstance(first_input, str) or isinstance(second_input, str):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  and all the tests are still passing. The world is my oyster!

----

=================================================================================
close the project
=================================================================================

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/calculator

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<TypeError: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment part 1>`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`how to make the calculator check if its inputs are numbers<test_calculator_sends_message_when_input_is_not_a_number>`

:ref:`Would you like to test Lists?<lists>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->