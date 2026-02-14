.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

#################################################################################
how to make a calculator 5
#################################################################################

I want to practice using :ref:`lists` with the :ref:`calculator project<how to make a calculator>`

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_lists.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 5 items

    tests/test_calculator.py ....                                        [100%]

    ======================== 5 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_sends_message_when_input_is_a_list
*********************************************************************************

I want to see what happens when I send a :ref:`list<lists>` as input to the :ref:`calculator program<how to make a calculator>`, will it send a message or raise :ref:`TypeError`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to see what happens when I send a :ref:`list<lists>` as input

.. code-block:: python
  :lineno-start: 88
  :emphasize-lines: 6-7, 9-12

          self.assertEqual(
              src.calculator.subtract('1', '1'),
              error_message
          )

      def test_calculator_sends_message_when_input_is_a_list(self):
          a_list = [0, 1, 2, 3]

          self.assertEqual(
              src.calculator.add(a_list, 0),
              'BOOM!!!'
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to match

.. code-block:: python
  :lineno-start: 96
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(a_list, 0),
              'brmph?! Numbers only. Try again...'
          )

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` for the next :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(a_list, 0),
                'brmph?! Numbers only. Try again...'
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                'BAP!!!'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'brmph?! Numbers only. Try again...' != 'BAP!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(a_list, 1),
                'brmph?! Numbers only. Try again...'
            )

  the test passes. Wait a minute! I just wrote the same thing twice, and I did it 8 times before in :ref:`test_calculator_sends_message_when_input_is_not_a_number` and 2 times in the ``only_takes_numbers`` :ref:`function<what is a function?>`. Never again

* I add a :ref:`variable<what is a variable?>` to remove the repetition

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3, 7, 11

        def test_calculator_sends_message_when_input_is_a_list(self):
            a_list = [0, 1, 2, 3]
            error_message = 'brmph?! Numbers only. Try again...'

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )

  the test is still green

---------------------------------------------------------------------------------
how to multiply a list
---------------------------------------------------------------------------------

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                'BOOM!!!'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 3, 0, 1, 2, 3] != 'BOOM!!!'

  :ref:`I know how to multiply a list<how to multiply a list>`

* I change the expectation of the test to the error message

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3] != 'brmph?! Numbers only. Try again...'

* I open ``calculator.py`` in the :ref:`editor<2 editors>`

* I add an :ref:`if statement<if statements>` to the ``only_takes_numbers`` :ref:`function<what is a function?>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-13

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            error_message = 'brmph?! Numbers only. Try again...'

            if isinstance(first_input, str) or isinstance(second_input, str):
                return error_message
            if isinstance(first_input, list) or isinstance(second_input, list):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  the test passes. The ``only_takes_numbers`` :ref:`function<what is a function?>` looks ugly now, there has to be a better way

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>` to ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                'BOOM!!!'
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )

  the test passes

* I remove the name of the test to move the new :ref:`assertions<what is an assertion?>` to ``test_calculator_sends_message_when_input_is_not_a_number``

  .. code-block:: python
    :lineno-start: 88

            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

            a_list = [0, 1, 2, 3]
            error_message = 'brmph?! Numbers only. Try again...'

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )
            self.assertEqual(
                src.calculator.divide(a_list, 1),
                error_message
            )
            self.assertEqual(
                src.calculator.multiply(a_list, 2),
                error_message
            )
            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )


    # Exceptions seen

  the tests are still green

* I remove the duplication of the ``error_message`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 88

            self.assertEqual(
                src.calculator.subtract('1', '1'),
                error_message
            )

            a_list = [0, 1, 2, 3]

            self.assertEqual(
                src.calculator.add(a_list, 0),
                error_message
            )

  still green. This test is long, there has to be :ref:`a better way to test the calculator with inputs that are NOT numbers<a better way to test the calculator with inputs that are NOT numbers>`

----

*********************************************************************************
how to test if something is an instance of more than one type
*********************************************************************************

The `isinstance function`_ can take a tuple_ as the second input, which allows me to check if the first input is an instance of any of the :ref:`objects<what is a class?>` in the tuple_

* I add a :ref:`variable<what is a variable?>` to the ``only_takes_numbers`` :ref:`function<what is a function?>` in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 5-8, 11-12

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            bad_types = (str, list)
            error_message = 'brmph?! Numbers only. Try again...'

            # if isinstance(first_input, str) or isinstance(second_input, str):
            #     return error_message
            # if isinstance(first_input, list) or isinstance(second_input, list):
            #     return error_message

            if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  the tests are still green

* I remove the comments

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            bad_types = (str, list)
            error_message = 'brmph?! Numbers only. Try again...'

            if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
                return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  still green

* I can use :ref:`Logical Negation (NOT)<test_logical_negation>` to make the :ref:`if statement<if statements>` allow only the types of numbers (integers_ and floats_) that I want the :ref:`calculator<how to make a calculator>` to work with

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3, 7-8, 10-16

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            bad_types = (str, list)
            error_message = 'brmph?! Numbers only. Try again...'

            # if isinstance(first_input, bad_types) or isinstance(second_input, bad_types):
            #     return error_message

            if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still green

* I remove the comments and the ``bad_types`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'brmph?! Numbers only. Try again...'

            if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  the tests are still passing

* ":ref:`not<test_logical_negation>`" happens twice in the :ref:`if statement<if statements>`, I change the line to use it for every symbol

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

            # if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
            if (not isinstance(first_input, good_types)) (not and) (not isinstance(second_input, good_types)):
                return error_message

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 7

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError
    # SyntaxError

* I fix the `if statement<if statement>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

            # if not isinstance(first_input, good_types) or not isinstance(second_input, good_types):
            # if (not isinstance(first_input, good_types)) (not and) ((not isinstance(second_input, good_types))):
            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
                return error_message

  the test is green again

* I remove the comments

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'brmph?! Numbers only. Try again...'

            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
                return error_message
            else:
                try:
                    return function(first_input, second_input)
                except TypeError:
                    return error_message
        return wrapper

  all the tests are still passing. I wonder if there is a way to write this :ref:`function<what is a function?>` with only one `return statement`_ for the error message

----

*********************************************************************************
test_calculator_w_list_items
*********************************************************************************

I can use a :ref:`list<lists>` to test the :ref:`calculator functions<how to make a calculator>` as long as its items are numbers

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to use the :ref:`index of the items in the list<test_index_returns_first_position_of_item_in_a_list>` to test the :ref:`calculator<how to make a calculator>`

.. code-block:: python
  :lineno-start: 107
  :emphasize-lines: 6-7, 9-12

            self.assertEqual(
                src.calculator.subtract(a_list, 3),
                error_message
            )

        def test_calculator_w_list_items(self):
            two_numbers = [self.random_first_number, self.random_second_number]

            self.assertEqual(
                src.calculator.add(two_numbers[0], two_numbers[1]),
                self.random_first_number-self.random_second_number
            )


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: ABC.DEFGHIJKLMNOPQ != RST.UVWXYZABCDEFG

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to the right calculation

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(two_numbers[0], two_numbers[1]),
              self.random_first_number+self.random_second_number
          )

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(two_numbers[0], two_numbers[1]),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(two_numbers[-2], two_numbers[-1]),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: D.EFGHIJKLMNOPQRST != UVWXY.ZABCDEFGHIJ

* I change the calculation

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3

          self.assertEqual(
              src.calculator.divide(two_numbers[-2], two_numbers[-1]),
              self.random_first_number/self.random_second_number
          )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(two_numbers[-2], two_numbers[-1]),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(two_numbers[1], two_numbers[-1]),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: EFGHIJ.KLMNOPQRSTU != VWXYZ.ABCDEFGHIJKL

* I change the expectation

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(two_numbers[1], two_numbers[-1]),
                self.random_second_number*self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(two_numbers[1], two_numbers[-1]),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(two_numbers[-2], two_numbers[0]),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 != FGH.IJKLMNOPQRSTU

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(two_numbers[-2], two_numbers[0]),
                self.random_first_number-self.random_first_number
            )

  the test passes

* Python_ allows me use a star expression like I did in :ref:`test_functions_w_unknown_arguments`. I add an :ref:`assertion<what is an assertion?>` with it

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.subtract(two_numbers[-2], two_numbers[0]),
                self.random_first_number-self.random_first_number
            )
            self.assertEqual(
                src.calculator.add(*two_numbers),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: GHI.JKLMNOPQRSTUVW != XYZ.ABCDEFGHIJKLMN

* I change the expectation

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(*two_numbers),
                self.random_first_number+self.random_second_number
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(*two_numbers),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(*two_numbers),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: H.IJKLMNOPQRSTUVWX != YZABCD.EFGHIJKLMNO

* I change the calculation

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(*two_numbers),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(*two_numbers),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(*two_numbers),
                self.random_first_number/self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: IJKLMN.OPQRSTUVWX != Y.ZABCDEFGHIJKLMNOP

* I change the calculation

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(*two_numbers),
                self.random_first_number*self.random_second_number
            )

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(*two_numbers),
                self.random_first_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(*two_numbers),
                self.random_first_number+self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: JKL.MNOPQRSTUVWXYZ != ABC.DEFGHIJKLMNOP

* I change the expectation

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(*two_numbers),
                self.random_first_number-self.random_second_number
            )

  the test passes

----

*********************************************************************************
test_calculator_raises_type_error_when_given_more_than_two_inputs
*********************************************************************************

It is important to note that the star expression always gives the items from the list in order, and I cannot use a :ref:`list<lists>` that has more than 2 numbers with these :ref:`calculator functions<how to make a calculator>` since they only take 2 inputs

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to show the problem when I have more than 2 inputs and use a star expression

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 6-7, 9

          self.assertEqual(
              src.calculator.subtract(*a_list),
              self.random_first_number-self.random_second_number
          )

      def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
          not_two_numbers = [0, 1, 2]

          src.calculator.add(*not_two_numbers)


  # Exceptions seen

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the `assertRaises method`_ to handle the :ref:`Exception<errors>`

.. code-block:: python
  :lineno-start: 148
  :emphasize-lines: 4-5

      def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
          not_two_numbers = [0, 1, 2]

          with self.assertRaises(TypeError):
              src.calculator.add(*not_two_numbers)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a failing line for :ref:`division<test_division>` with the new :ref:`list<lists>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.add(*not_two_numbers)
            src.calculator.divide(*not_two_numbers)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.add(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.divide(*not_two_numbers)

    the test passes

* I add a line for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.divide(*not_two_numbers)
            src.calculator.multiply(*not_two_numbers)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3-4

            with self.assertRaises(TypeError):
                src.calculator.divide(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.multiply(*not_two_numbers)

  the test passes

* I add the last line

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 3

            with self.assertRaises(TypeError):
                src.calculator.multiply(*not_two_numbers)
            src.calculator.subtract(*not_two_numbers)

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

* I handle the :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 10-11

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            not_two_numbers = [0, 1, 2]

            with self.assertRaises(TypeError):
                src.calculator.add(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.divide(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.multiply(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.subtract(*not_two_numbers)

  the test passes

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editors<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I added these tests to the :ref:`calculator program<how to make a calculator 3>` after testing :ref:`lists<what is a list?>`

* :ref:`test_calculator_sends_message_when_input_is_not_a_number`
* :ref:`add more instance tests to the only_takes_numbers function<how to test if something is an instance of more than one type>`
* :ref:`test_calculator_w_list_items`
* :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<lists: tests and solutions>`

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
* :ref:`what None is<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`how to make the calculator check if its inputs are numbers<test_calculator_sends_message_when_input_is_not_a_number>`
* :ref:`what you can do with Lists<lists>`

:ref:`would you like to test list comprehensions?<list comprehensions>` They are a quick way to make :ref:`lists`

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