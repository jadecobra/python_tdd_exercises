.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
how to make a calculator 4
#################################################################################

I want to use TypeError_ with :ref:`exception handlers<how to use try...except...else>` to make sure that the :ref:`calculator program<how to make a calculator>` only works with numbers, like a Calculator in the real world.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_type_error.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: python

    .../pumping_python/calculator

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 5

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 4 items

    tests/test_calculator.py ....                                        [100%]

    ======================== 4 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_raises_type_error_w_none
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new failing test to show that the :ref:`calculator<how to make a calculator>` raises TypeError_ when one of the inputs is :ref:`None<what is None?>`, just like in :ref:`test_type_error_w_objects_that_do_not_mix`

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
                  'brmph?! I cannot divide by 0. Try again...'
              )

      def test_calculator_raises_type_error_w_none(self):
          src.calculator.add(None, None)


  # Exceptions seen

the terminal_ shows TypeError_

.. code-block:: python

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add assertRaises_

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2-3

      def test_calculator_raises_type_error_w_none(self):
          with self.assertRaises(TypeError):
              src.calculator.add(None, None)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a failing line for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

        def test_calculator_raises_type_error_w_none(self):
            with self.assertRaises(TypeError):
                src.calculator.add(None, None)
            src.calculator.divide(None, None)

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'

* I add assertRaises_

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

  .. code-block:: python

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

* I add assertRaises_

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

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

* I add the `assertRaises method`_

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

:ref:`The calculator raises TypeError when None is given as input<test_calculator_raises_type_error_w_none>`.

What does it do if the input is a :ref:`boolean<what are booleans?>`, string_, tuple_, :ref:`list<lists>`, set_ or :ref:`a dictionary<dictionaries>`?

----

*********************************************************************************
test_calculator_raises_type_error_w_strings
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test with an :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_an_assertion`, to test the :ref:`add function<test_addition>` with strings_

.. code-block:: python
  :lineno-start: 64
  :emphasize-lines: 4-5

          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

      def test_calculator_with_strings(self):
          self.assertEqual(src.calculator.add('1', '1'), '2')


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: '11' != '2'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 1

          self.assertEqual(src.calculator.add('1', '1'), '11')

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            self.assertEqual(src.calculator.divide('1', '1'), '11')

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

* I change assertEqual_ to assertRaises_

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

* I add assertRaises_

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

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 7-8

        def test_calculator_with_strings(self):
            self.assertEqual(src.calculator.add('1', '1'), '11')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.multiply('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.subtract('1', '1')

  the test passes

----

*********************************************************************************
how to test if something is an instance of an object in a program
*********************************************************************************

I want the :ref:`add function<test_addition>` to raise TypeError_ when it gets a string_, the same way the other :ref:`functions<what is a function?>` raise TypeError_ when one of the inputs is a string_. I can use the `isinstance function`_ which is like the `assertIsInstance method`_ from when I tested :ref:`None<what is None?>`, it checks if one thing is an instance or child of a :ref:`class<what is a class?>`

* I change the assertEqual_ to assertRaises_ in :ref:`test_calculator_with_strings<test_calculator_raises_type_error_w_strings>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

        def test_calculator_with_strings(self):
            with self.assertRaises(TypeError):
                src.calculator.add('1', '1')
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: TypeError not raised

* I open ``calculator.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add an :ref:`if statement<if statements>` to the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-6

    def add(first_input, second_input):
        if (
            isinstance(first_input, str)
            or
            isinstance(second_input, str)
        ):
            raise TypeError
        else:
            return first_input + second_input

  the test passes

  .. NOTE::

    - the `isinstance function`_ like the `assertIsInstance method`_ checks if the first input it is given is an instance (child) of the :ref:`class<what is a class?>` it is given as the second input. It is part of `Python's Built-in Functions`_
    - the :ref:`if statement<if statements>` ``if isinstance(first_input, str) or isinstance(second_input, str):`` is :ref:`True<test_what_is_true>` if

      * ``first_input`` is a string_ and ``second_input`` is NOT a string_
      * ``first_input`` is NOT a string_ and ``second_input`` is a string_
      * ``first_input`` is a string_ and ``second_input`` is a string_

      the statement is only :ref:`False<test_what_is_false>` if ``first_input`` is NOT a string_ and ``second_input`` is NOT a string_.

    This is :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`, which only returns :ref:`False<test_what_is_false>`, if the two inputs are :ref:`False<test_what_is_false>`

* I change the name of the test to say what it does

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

I want the :ref:`calculator functions<how to make a calculator>` to send a message when it gets something that is not a number, not raise TypeError_ which causes the program to stop. I want the user to be able to try again with different input.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in :ref:`test_calculator_raises_type_error_w_none`

.. code-block:: python
  :lineno-start: 57
  :emphasize-lines: 2,4-5

      def test_calculator_raises_type_error_w_none(self):
          self.assertEqual(
              src.calculator.add(None, None),
              'brmph?! Numbers only. Try again...'
          )
          with self.assertRaises(TypeError):
              src.calculator.divide(None, None)
          with self.assertRaises(TypeError):
              src.calculator.multiply(None, None)
          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

the terminal_ shows TypeError_

.. code-block:: python

  TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`exception handler<how to use try...except...else>` to the `else clause`_ of the :ref:`add function<test_addition>` in ``calculator.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 8-12

  def add(first_input, second_input):
      if (
          isinstance(first_input, str)
          or
          isinstance(second_input, str)
      ):
          raise TypeError
      else:
          try:
              return first_input + second_input
          except TypeError:
              return 'brmph?! Numbers only. Try again...'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6,8-9

        def test_calculator_raises_type_error_w_none(self):
            self.assertEqual(
                src.calculator.add(None, None),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.divide(None, None),
                'brmph?! Numbers only. Try again...'
            )
            with self.assertRaises(TypeError):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'

* I add another :ref:`except clause<how to use try...except...else>` to the :ref:`exception handler<how to use try...except...else>` in the :ref:`divide function<test_division>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7

    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'
        except TypeError:
            return 'brmph?! Numbers only. Try again...'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: TypeError not raised

  my change made the :ref:`assertion<what is an assertion?>` in :ref:`test_calculator_raises_type_error_w_strings` fail

* I undo the change, then add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-3

    def divide(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'


    def add(first_input, second_input):

  the test passes

----

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in :ref:`test_calculator_raises_type_error_w_none` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 5,7-8

          self.assertEqual(
              src.calculator.divide(None, None),
              'brmph?! Numbers only. Try again...'
          )
          self.assertEqual(
              src.calculator.multiply(None, None),
              'brmph?! Numbers only. Try again...'
          )
          with self.assertRaises(TypeError):
              src.calculator.subtract(None, None)

      def test_calculator_raises_type_error_w_strings(self):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

* I add an :ref:`if statement<if statements>` to the :ref:`multiply function<test_multiplication>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

    def multiply(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def divide(first_input, second_input):

  the test passes

----

* I change the assertRaises_ for the :ref:`subtract function<test_subtraction>` to assertEqual_ in :ref:`test_calculator_raises_type_error_w_none` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 5, 7-8

            self.assertEqual(
                src.calculator.multiply(None, None),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                'brmph?! Numbers only. Try again...'
            )

        def test_calculator_raises_type_error_w_strings(self):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'

* I add an :ref:`if statement<if statements>` to the :ref:`subtract function<test_subtraction>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def subtract(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input


    def multiply(first_input, second_input):

  the test passes

----

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

        def test_calculator_raises_type_error_w_none(self):
            error_message = 'brmph?! Numbers only. Try again...'
            self.assertEqual(
                src.calculator.add(None, None),
                'brmph?! Numbers only. Try again...'
            )

* I use it to remove the repetition of the error message

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 5,9,13,17

        def test_calculator_raises_type_error_w_none(self):
            error_message = 'brmph?! Numbers only. Try again...'
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

        def test_calculator_raises_type_error_w_strings(self):

  the test is still green

----

*********************************************************************************
how to make a decorator function
*********************************************************************************

3 of the :ref:`functions<what is a function?>` in the :ref:`calculator program<how to make a calculator>` have the same :ref:`if statement<if statements>`. How can I remove this repetition?

.. code-block:: python

  if first_input is None or second_input is None:
      return 'brmph?! Numbers only. Try again...'

The only difference between the 3 :ref:`functions<what is a function?>` is in what they do with the inputs


.. code-block:: python

  return first_input - second_input
  return first_input * second_input
  return first_input / second_input

I can use a decorator/wrapper :ref:`function<what is a function?>` to remove the repetition from those 3 :ref:`functions<what is a function?>`. It is a :ref:`function<what is a function?>` that takes another :ref:`function<what is a function?>` as input.

* I add a :ref:`decorator function<what is a function?>` to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-6

    def input_is_not_none(function):
        def wrapper(first_input, second_input):
            if first_input is None or second_input is None:
                return 'brmph?! Numbers only. Try again...'
            return function(first_input, second_input)
        return wrapper


    def subtract(first_input, second_input):

  The ``input_is_not_none`` :ref:`function<what is a function?>`

  - takes a :ref:`given function<what is a function?>` as input
  - uses :ref:`logical disjunction<test_logical_disjunction>` to check the inputs

    * if the first input is :ref:`None<what is None?>` or the second input is :ref:`None<what is None?>` it returns an error message
    * if the two inputs are both NOT :ref:`None<what is None?>` it returns the result of calling the :ref:`given function<what is a function?>` with the inputs

* I use it with the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    @input_is_not_none
    def subtract(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the tests are still green

* I remove the :ref:`if statement<if statements>` from the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 9

    @input_is_not_none
    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):

  still green

* I use ``input_is_not_none`` with the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

    @input_is_not_none
    def multiply(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input

  green

* I remove the :ref:`if statement<if statements>` from the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 14

    @input_is_not_none
    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):

  still green

* I wrap the :ref:`divide function<test_division>` with ``input_is_not_none``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

    @input_is_not_none
    def divide(first_input, second_input):
        if first_input is None or second_input is None:
            return 'brmph?! Numbers only. Try again...'
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'

  the tests are still green

* I remove the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 19

    @input_is_not_none
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'


    def add(first_input, second_input):

  still green

* I try it with the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 1

    @input_is_not_none
    def add(first_input, second_input):
        if (
            isinstance(first_input, str)
            or
            isinstance(second_input, str)
        ):
            raise TypeError
        else:
            try:
                return first_input + second_input
            except TypeError:
                return 'brmph?! Numbers only. Try again...'

  the tests are still green

* I remove the :ref:`exception handler<how to use try...except...else>` from the :ref:`add function<test_addition>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 32

    def input_is_not_none(function):
        def wrapper(first_input, second_input):
            if first_input is None or second_input is None:
                return 'brmph?! Numbers only. Try again...'
            return function(first_input, second_input)
        return wrapper


    @input_is_not_none
    def subtract(first_input, second_input):
        return first_input - second_input


    @input_is_not_none
    def multiply(first_input, second_input):
        return first_input * second_input


    @input_is_not_none
    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! I cannot divide by 0. Try again...'


    @input_is_not_none
    def add(first_input, second_input):
        if (
            isinstance(first_input, str)
            or
            isinstance(second_input, str)
        ):
            raise TypeError
        else:
            return first_input + second_input


  still green

----

* I

----

----

----

* I  change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in :ref:`test_calculator_raises_type_error_w_strings`

  .. code-block:: python
    :lineno-start: 76


----

* I want the same thing to happen if the :ref:`add function<test_addition>` gets a string_ as input. I change the assertRaises_ to assertEqual_ for the :ref:`add function<test_addition>` in :ref:`test_calculator_raises_type_error_w_strings` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2,4-5

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            with self.assertRaises(TypeError):
                src.calculator.divide('1', '1')

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError

* I change the `raise statement`_ to a `return statement`_ in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'brmph?! Numbers only. Try again...'
        else:
            try:
                return first_input + second_input
            except TypeError:
                return 'brmph?! Numbers only. Try again...'

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in :ref:`test_calculator_raises_type_error_w_strings` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 6-9

        def test_calculator_raises_type_error_w_strings(self):
            self.assertEqual(
                src.calculator.add('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'brmph?! Numbers only. Try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

----

----

----

----

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: TypeError not raised

  :ref:`test_calculator_raises_type_error_w_none` fails because it expects TypeError_ if the inputs are not numbers

* I change the assertRaises_ to assertEqual_ for the :ref:`divide function<test_division>` in :ref:`test_calculator_raises_type_error_w_none` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6-9

    def test_calculator_raises_type_error_w_none(self):
        self.assertEqual(
            src.calculator.add(None, None),
            'brmph?! Numbers only. Try again...'
        )
        self.assertEqual(
            src.calculator.divide(None, None),
            'brmph?! Numbers only. Try again...'
        )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in :ref:`test_calculator_raises_type_error_w_none`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 5-8


            self.assertEqual(
                src.calculator.divide(None, None),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.multiply(None, None),
                'brmph?! Numbers only. Try again...'
            )

  the terminal_ shows TypeError_

  .. code-block:: python

    TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'

* I add an :ref:`exception handler<how to use try...except...else>` to the :ref:`multiply function<test_multiplication>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-5

    def multiply(first_input, second_input):
        try:
            return first_input * second_input
        except TypeError:
            return 'brmph?! Numbers only. Try again...'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`multiply function<test_multiplication>` in :ref:`test_calculator_raises_type_error_w_strings` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'brmph?! Numbers only. Try again...'
            )

  the test passes

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in :ref:`test_calculator_raises_type_error_w_strings`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'brmph?! Numbers only. Try again...'
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
            return 'brmph?! Numbers only. Try again...'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: TypeError not raised

* I change the assertRaises_ to assertEqual_ for the :ref:`subtract function<test_subtraction>` in :ref:`test_calculator_raises_type_error_w_none` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(None, None),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.subtract(None, None),
                'brmph?! Numbers only. Try again...'
            )


        def test_calculator_raises_type_error_w_strings(self):

  the test passes

  That was a lot of doing the same thing over and over again.

  - :ref:`test_calculator_raises_type_error_w_none` and :ref:`test_calculator_raises_type_error_w_strings` both look the same
  - the :ref:`calculator<how to make a calculator>` no longer raises TypeError_ when any of the inputs are NOT a number

* I remove the name of :ref:`test_calculator_raises_type_error_w_strings` to make its :ref:`assertions<what is an assertion?>` part of :ref:`test_calculator_raises_type_error_w_none`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 5-20

            self.assertEqual(
                src.calculator.subtract(None, None),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.add('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.divide('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.multiply('1', '1'),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.subtract('1', '1'),
                'brmph?! Numbers only. Try again...'
            )


    # Exceptions seen

* I change the name from :ref:`test_calculator_raises_type_error_w_none` to ``test_calculator_sends_message_when_input_is_not_a_number`` to be clearer

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
            error_message = 'brmph?! Numbers only. Try again...'

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

  still green. All these :ref:`assertions<what is an assertion?>` look the same, they check that the :ref:`calculator<how to make a calculator>` :ref:`functions<what is a function?>` return an error message if they get input that is NOT a number

  .. code-block:: python

    self.assertEqual(
        src.calculator.function(NOT_A_NUMBER, ALSO_NOT_A_NUMBER),
        error_message
    )

  there has to be :ref:`a better way to test the calculator with inputs that are NOT numbers`

----
----
----
----
the :ref:`divide function<test_division>` is different because it has another :ref:`except clause<how to use try...except...else>`

.. code-block:: python

  except ZeroDivisionError:
      return 'brmph?! I cannot divide by 0. Try again...'

the other part that is different for all the :ref:`functions<what is a function?>` are the calculations

.. code-block:: python

  return first_input - second_input
  return first_input * second_input
  return first_input / second_input
  return first_input + second_input

----

=================================================================================
what is a decorator function?
=================================================================================

----

A decorator or wrapper :ref:`function<what is a function?>` takes another :ref:`function<what is a function?>` as input and returns a :ref:`function<what is a function?>`. I can use it to remove the :ref:`exception handler<how to use try...except...else>` that is the same in all of the :ref:`calculator functions<how to make a calculator>`

* I add a new :ref:`function<what is a function?>` add the top of ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            try:
                return function(first_input, second_input)
            except TypeError:
                return 'brmph?! Numbers only. Try again...'
        return wrapper


    def subtract(first_input, second_input):

  The ``only_takes_numbers`` :ref:`function<what is a function?>` takes a :ref:`function<what is a function?>` as input

  - it tries to return the result of the :ref:`function<what is a function?>` working on the two inputs
  - if TypeError_ is raised it returns the error message

* I use it to wrap the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

    @only_takes_numbers
    def subtract(first_input, second_input):
        try:

  the test is still green

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<what is a function?>`

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

  the test is green again

* I remove the parts that are also in the ``only_takes_numbers`` :ref:`function<what is a function?>`

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
            return 'brmph?! I cannot divide by 0. Try again...'


    def add(first_number, second_input):

  all the tests are still green

* one more to go, I wrap the :ref:`add function<test_addition>` with the ``only_takes_numbers`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):

  the test is still green

* I remove the :ref:`exception handler<how to use try...except...else>` from the `else clause`_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    @only_takes_numbers
    def add(first_input, second_input):
        if isinstance(first_input, str) or isinstance(second_input, str):
            return 'brmph?! Numbers only. Try again...'
        else:
            return first_input + second_input

  green! Lovely!

* I can make a :ref:`function<what is a function?>` for the condition in the :ref:`if statement<if statements>` in the :ref:`add function<test_addition>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def is_string(something):
        return isinstance(something, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if is_string(first_input) or is_string(second_input):
            return 'brmph?! Numbers only. Try again...'
        else:
            return first_input + second_input

  the test is still green

  - This removes the duplication of ``str`` in the call to the `isinstance function`_

    .. code-block:: python

      isinstance(first_input, str)
      isinstance(second_input, str):

  - it also adds 2 lines of code to remove 6 characters. WOW!

* I can make a :ref:`function<what is a function?>` for the whole :ref:`if statement<if statements>` in the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2, 7

    def one_input_is_a_string(first_input, second_input):
        return isinstance(first_input, str) or isinstance(second_input, str)


    @only_takes_numbers
    def add(first_input, second_input):
        if one_input_is_a_string(first_input, second_input):
            return 'brmph?! Numbers only. Try again...'
        else:
            return first_input + second_input

  the test is still green.

  - the ``one_input_is_a_string`` :ref:`function<what is a function?>` looks the same as :ref:`Logical Disjunction from the Truth Table<test_logical_disjunction>`
  - this makes it easier to change the :ref:`condition<if statements>` later without touching the :ref:`add function<test_addition>`
  - it still adds 2 lines of code

* I can also make a decorator :ref:`function<what is a function?>` for the :ref:`if statement<if statements>` to practice making a decorator :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-7

    def reject_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'brmph?! Numbers only. Try again...'
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

* the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions<what is a function?>` have parts that are the same

  .. code-block:: python

        def wrapper(first_input, second_input):
            ...
            return 'brmph?! Numbers only. Try again...'
            ...
            return function(first_input, second_input)
        return wrapper

  I make a new :ref:`function<what is a function?>` that has the :ref:`if statement<if statements>` from ``reject_strings`` and the :ref:`exception handler<how to use try...except...else>` from ``only_takes_numbers``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-10

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'brmph?! Numbers only. Try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'brmph?! Numbers only. Try again...'
        return wrapper


    def reject_strings(function):

* I use the new :ref:`function<what is a function?>` to wrap the :ref:`add function<test_addition>`

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

* I wrap the other :ref:`functions<what is a function?>` with ``only_takes_numbers_and_reject_strings``

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
            return 'brmph?! I cannot divide by 0. Try again...'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):

  the test is green again

* I remove ``only_takes_numbers`` from each :ref:`function<what is a function?>`

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
            return 'brmph?! I cannot divide by 0. Try again...'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

  the test is still green

* I remove the ``reject_strings`` and ``only_takes_numbers`` :ref:`functions<what is a function?>`

  .. code-block:: python
    :linenos:

    def only_takes_numbers_and_rejects_strings(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'brmph?! Numbers only. Try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'brmph?! Numbers only. Try again...'
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
            return 'brmph?! I cannot divide by 0. Try again...'


    @only_takes_numbers_and_rejects_strings
    def add(first_input, second_input):
        return first_input + second_input

* I change the name of the new decorator :ref:`function<what is a function?>` to make it easier

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 13, 18, 23, 31

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            if isinstance(first_input, str) or isinstance(second_input, str):
                return 'brmph?! Numbers only. Try again...'
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return 'brmph?! Numbers only. Try again...'
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
            return 'brmph?! I cannot divide by 0. Try again...'


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
            error_message = 'brmph?! Numbers only. Try again...'

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

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

The :ref:`calculator program<how to make a calculator>` can take 2 inputs and :ref:`check if they are both numbers<test_calculator_sends_message_when_input_is_not_a_number>`, then :ref:`add<test_addition>`, :ref:`subtract<test_subtraction>`, :ref:`multiply<test_multiplication>` or :ref:`divide<test_division>` them

Even though the program_ says it only works with numbers, I did not add tests for tuples_, :ref:`lists`, sets_, and :ref:`dictionaries`, though they are touched in :ref:`test_type_error_w_objects_that_do_not_mix`, Do you want to add them or do we already have enough tests to know what would happen?


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

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
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

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->