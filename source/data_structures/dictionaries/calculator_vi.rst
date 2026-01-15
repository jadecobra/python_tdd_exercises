.. meta::
  :description: Master Python dictionaries with TDD! Learn :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s, methods, and testing techniques in this hands-on guide. Start coding now!
  :keywords: Jacob Itegboje, Python dictionaries, Test-Driven Development, Python programming, data structures, unit testing, Python tutorial, coding guide

.. include:: ../../links.rst

#################################################################################
how to make a calculator part 6
#################################################################################

I can use a dictionary_ to test the :ref:`calculator functions<how to make a calculator part 1>` as long as its values are numbers

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

* I activate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: Powershell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/calculator

* I use ``pytest-watch`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 7 items

    tests/test_calculator.py .......                                     [100%]

    ============================ 7 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_w_dictionary_items
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test to use a dictionary_ to test the :ref:`calculator<how to make a calculator part 1>`

.. code-block:: python
  :lineno-start: 119
  :emphasize-lines: 6-10, 12-15

            self.assertEqual(
                src.calculator.subtract(*a_list),
                self.random_first_number-self.random_second_number
            )

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'x': self.random_first_number,
                'y': self.random_second_number,
            }

            self.assertEqual(
                src.calculator.add(two_numbers['x'], two_numbers['y']),
                self.random_first_number+self.random_first_number
            )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            not_two_numbers = [0, 1, 2]

the terminal_ shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: ABC.DEFGHIJKLMNOPQ != RST.UVWXYZABCDEFG

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to the right calculation

.. code-block:: python
  :lineno-start: 130
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(two_numbers['x'], two_numbers['y']),
              self.random_first_number+self.random_second_number
          )

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(two_numbers['x'], two_numbers['y']),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(two_numbers['x'], two_numbers['y']),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: D.EFGHIJKLMNOPQRST != UVWXY.ZABCDEFGHIJ

* I change the calculation

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(two_numbers['x'], two_numbers['y']),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(two_numbers['x'], two_numbers['y']),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(two_numbers['y'], two_numbers['y']),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: EFGHIJ.KLMNOPQRSTU != VWXYZ.ABCDEFGHIJKL

* I change the expectation

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(two_numbers['y'], two_numbers['y']),
                self.random_second_number*self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(two_numbers['y'], two_numbers['y']),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(two_numbers['x'], two_numbers['x']),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 0.0 != FGH.IJKLMNOPQRSTU

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(two_numbers['x'], two_numbers['x']),
                self.random_first_number-self.random_first_number
            )

  the test passes

* Python_ allows me use a double starred expression like I did in :ref:`test_functions_w_unknown_arguments`. I add an :ref:`assertion<what is an assertion?>` with it

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.subtract(two_numbers['x'], two_numbers['x']),
                self.random_first_number-self.random_first_number
            )
            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: only_takes_numbers.<locals>.wrapper() got an unexpected keyword argument 'x'

* the names of the :ref:`keys<test_keys_of_a_dictionary>` in the ``two_numbers`` dictionary_ must be the same as the names of the arguments the :ref:`calculator functions<how to make a calculator part 1>` receive - ``first_input`` and ``second_input`` not ``x`` and ``y``. I change ``x`` and ``y`` to ``first_input`` and ``second_input`` in the test

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3-4, 9-10, 16-17, 23-24, 30-31

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'first_input': self.random_first_number,
                'second_input': self.random_second_number,
            }

            self.assertEqual(
                src.calculator.add(
                    two_numbers['first_input'],
                    two_numbers['second_input']
                ),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(
                    two_numbers['first_input'],
                    two_numbers['second_input']
                ),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['second_input'],
                    two_numbers['second_input']
                ),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['first_input'],
                    two_numbers['first_input']
                ),
                self.random_first_number-self.random_first_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: VWX.YZABCDEFGHIJK != LMN.OPQRSTUVWXYZABC

* I change the calculation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number+self.random_second_number
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: H.IJKLMNOPQRSTUVWX != YZABCD.EFGHIJKLMNO

* I change the calculation

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number/self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: IJKLMN.OPQRSTUVWX != Y.ZABCDEFGHIJKLMNOP

* I change the calculation

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(**two_numbers),
                self.random_first_number+self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: JKL.MNOPQRSTUVWXYZ != ABC.DEFGHIJKLMNOP

* I change the expectation

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.subtract(**two_numbers),
                self.random_first_number-self.random_second_number
            )

  the test passes

* I can use the :ref:`values method<test_values_of_a_dictionary>` to make a :ref:`list<lists>` to test the :ref:`calculator<how to make a calculator part 1>` in ``test_calculator_w_list_items``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2-7

        def test_calculator_w_list_items(self):
            # two_numbers = [self.random_first_number, self.random_second_number]
            a_dictionary = {
                'x': self.random_first_number,
                'y': self.random_second_number
            }
            two_numbers = list(a_dictionary.values())

            self.assertEqual(
                src.calculator.add(two_numbers[0], two_numbers[1]),
                self.random_first_number+self.random_second_number
            )

  the test is still green

* I can also use a dictionary_ with a `for loop`_ to make ``test_calculator_sends_message_when_input_is_not_a_number`` more complex and simpler at the same time

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-9, 21-25

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'brmph?! Numbers only. Try again...'

            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for data in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                with self.subTest(i=data):
                    for operation in arithmetic:
                        self.assertEqual(
                            arithmetic[operation](data, a_random_number()),
                            'BOOM!!!'
                        )
                    self.assertEqual(
                        src.calculator.add(data, a_random_number()),
                        error_message
                    )

  the terminal_ shows :ref:`AssertionError` for every case in the :ref:`iterable<what is an iterable?>`

  .. code-block:: python

    SUBFAILED(i=None) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=True) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=False) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i='') tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i='text') tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=()) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=(0, 1, 2, 'n')) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=[]) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=[0, 1, 2, 'n']) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=set()) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={0, 1, 2, 'n'}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={'key': 'value'}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM'

  the test works

  .. NOTE::

    ``arithmetic[operation](data, a_random_number())`` represents every operation in the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` and every item in the :ref:`iterable<what is an iterable?>` for example

    .. code-block:: python

      arithmetic['addition'](None, a_random_number())
      arithmetic['subtraction']((0, 1, 2, 'n'), a_random_number())
      arithmetic['division'](dict(), a_random_number())
      arithmetic['multiplication']('text', a_random_number())

    these 4 examples are translated by the computer to

    .. code-block:: python

      src.calculator.add(None, a_random_number())
      src.calculator.subtract((0, 1, 2, 'n'), a_random_number())
      src.calculator.divide(dict(), a_random_number())
      src.calculator.multiply('text', a_random_number())

    If I had to write a test for each operation and each data item, I would end up with a total of 52 tests. Too much

* I change the expectation

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 5

                with self.subTest(i=data):
                    for operation in arithmetic:
                        self.assertEqual(
                            arithmetic[operation](data, a_random_number),
                            error_message
                        )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 58

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'brmph?! Numbers only. Try again...'

            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for data in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                with self.subTest(i=data):
                    for operation in arithmetic:
                        self.assertEqual(
                            arithmetic[operation](data, a_random_number()),
                            error_message
                        )
                    self.assertEqual(
                        src.calculator.add(data, a_random_number()),
                        error_message
                    )

        def test_calculator_w_list_items(self):

  this solution is not as easy to read as what was there before especially for someone new to Python_. :ref:`There has to be a better way<test_calculator_functions>`

----

*********************************************************************************
test_calculator_functions
*********************************************************************************

I want to use a dictionary_ to write one test that covers all the :ref:`4 calculator functions: addition, subtraction, division and multiplication<how to make a calculator part 1>`

=================================================================================
:green:`RED`: make it pass
=================================================================================

* I add a new test

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7-13, 15-23

            except ZeroDivisionError:
                self.assertEqual(
                    src.calculator.divide(self.random_first_number, 0),
                    'brmph?! cannot divide by 0. Try again...'
                )

        def test_calculator_functions(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'division': src.calculator.divide,
                'multiplication': src.calculator.multiply,
            }

            for operation in arithmetic:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic[operation](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        'BOOM!!!'
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the terminal_ shows :ref:`AssertionError` for the 4 arithmetic operations

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: QRS.TUVWXYZABCDEF != 'BOOM!!!'
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: GHI.JKLMNOPQRSTUVWX != 'BOOM!!!'
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: Y.ABCDEFGHIJKLMNOP != 'BOOM!!!'
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: QRSTUV.WXYZABCDEFG != 'BOOM!!!'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I need a way to add the calculations for each operation to the :ref:`assertion<what is an assertion?>`. I add another dictionary_

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-16

                'multiplication': src.calculator.multiply,
            }
            expectations = {
                'addition': (
                    self.random_first_number+self.random_second_number
                ),
                'subtraction': (
                    self.random_first_number-self.random_second_number
                ),
                'division': (
                    self.random_first_number/self.random_second_number
                ),
                'multiplication': (
                    self.random_first_number*self.random_second_number
                )
            }

            for operation in arithmetic:

* I use the new dictionary_ for the calculation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 8

            for operation in arithmetic:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic[operation](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        expectations[operation]
                    )

  the test passes.

This test goes through every operation in the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` then calls the :ref:`function<what is a function?>` that is its :ref:`value<test_values_of_a_dictionary>` with ``self.random_first_number`` and ``self.random_second_number`` as input, and checks if the result is the :ref:`value<test_values_of_a_dictionary>` for the :ref:`key<test_keys_of_a_dictionary>` in the ``expectations`` :ref:`dictionary<what is a dictionary?>`

* In other words

  .. code-block:: python

    arithmetic['addition'](self.first_random_number, self.second_random_number)
    arithmetic['subtraction'](self.first_random_number, self.second_random_number)
    arithmetic['division'](self.first_random_number, self.second_random_number)
    arithmetic['multiplication'](self.first_random_number, self.second_random_number)

* these four statements get translated by the computer to

  .. code-block:: python

    src.calculator.add(self.first_random_number, self.second_random_number)
    src.calculator.subtract(self.first_random_number, self.second_random_number)
    src.calculator.divide((self.first_random_number, self.second_random_number)
    src.calculator.multiply(self.first_random_number, self.second_random_number)

* then the computer checks if the results of the operations are the same as

  .. code-block:: python

    expectations['addition']
    expectations['subtraction']
    expectations['division']
    expectations['multiplication']

  which are

  .. code-block:: python

    self.random_first_number+self.random_second_number
    self.random_first_number-self.random_second_number
    self.random_first_number/self.random_second_number
    self.random_first_number*self.random_second_number

* the test is checking if these statements are equal

  for :ref:`addition<test_addition>`

  .. code-block:: python

    src.calculator.add(self.first_random_number, self.second_random_number)
    self.random_first_number+self.random_second_number

  for :ref:`subtraction<test_subtraction>`

  .. code-block:: python

    src.calculator.subtract(self.first_random_number, self.second_random_number)
    self.random_first_number-self.random_second_number

  for :ref:`division<test_division>`

  .. code-block:: python

    src.calculator.divide((self.first_random_number, self.second_random_number)
    self.random_first_number/self.random_second_number

  for :ref:`multiplication<test_multiplication>`

  .. code-block:: python

    src.calculator.multiply(self.first_random_number, self.second_random_number)
    self.random_first_number*self.random_second_number

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* the two dictionaries_ in this test have the same :ref:`keys<test_keys_of_a_dictionary>`, I can put them together

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 6-31

                'multiplication': (
                    self.random_first_number*self.random_second_number
                )
            }

            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': (
                        self.random_first_number+self.random_second_number
                    ),
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': (
                        self.random_first_number-self.random_second_number
                    ),
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': (
                        self.random_first_number/self.random_second_number
                    ),
                },
                'multiplication': {
                    'function': src.calculator.divide,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                }
            }

            for operation in arithmetic:

* I add a new :ref:`assertion<what is an assertion?>` in a `for loop`_ with the `subTest method`_

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 11-19

            for operation in arithmetic:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic[operation](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        expectations[operation]
                    )

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        'BOOM!!!'
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the terminal_ shows :ref:`AssertionError`:

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: HIJ.KLMNOPQRSTUVW != 'BOOM!!!'
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: XYZA.BCDEFGHIJKLMN != 'BOOM!!!'
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: NO.PQRSTUVWXYZABCDE != 'BOOM!!!'
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: FGHIJKLM.NOPQRSTUVW != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 8

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        arithmetic_tests[operation]['expectation']
                    )

  the test passes

* I remove the other dictionaries_ and `for loop`_

  .. code-block:: python
    :lineno-start: 58

        def test_calculator_functions(self):
            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': (
                        self.random_first_number+self.random_second_number
                    ),
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': (
                        self.random_first_number-self.random_second_number
                    ),
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': (
                        self.random_first_number/self.random_second_number
                    ),
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                }
            }

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        arithmetic_tests[operation]['expectation']
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

* I remove the ``test_addition``, ``test_subtraction`` and ``test_multiplication`` :ref:`methods<what is a function?>`

  .. code-block:: python

    class TestCalculator(unittest.TestCase):

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

        def test_division(self):

* I need a way to handle :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` in ``test_calculator_functions`` for the :ref:`divide function<test_division>`. I change ``random_second_number`` to ``0`` in the `setUp method`_ to make :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` happen in the tests

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-4

        def setUp(self):
            self.random_first_number = a_random_number()
            # self.random_second_number = a_random_number()
            self.random_second_number = 0

        def test_division(self):

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` for 3 tests

  .. code-block:: python

    FAILED tests/test_calculator.py::TestCalculator::test_calculator_functions - ZeroDivisionError: float division by zero
    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - ZeroDivisionError: float division by zero
    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - ZeroDivisionError: float division by zero

* I use an :ref:`exception handler<how to use try...except...else>` to add a new :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` to the `setUp method`_ for the result of :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 15

            self.random_second_number = 0
            try:
                self.division_result = (
                    self.random_first_number / self.random_second_number
                )
            except ZeroDivisionError:
                self.division_result = 'brmph?! cannot divide by 0. Try again...'

* I use the new :ref:`class attribute (variable) <test_attribute_error_w_class_attributes>` in ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3-6

                'division': {
                    'function': src.calculator.divide,
                    # 'expectation': (
                    #     self.random_first_number/self.random_second_number
                    # ),
                    'expectation': self.division_result,
                },

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` for 2 tests

  .. code-block:: python

    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - ZeroDivisionError: float division by zero
    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - ZeroDivisionError: float division by zero

  progress

* I add the :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` to ``test_calculator_w_list_items``

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(two_numbers[-2], two_numbers[-1]),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  and

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(*two_numbers),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` for 1 test

  .. code-block:: python

    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - ZeroDivisionError: float division by zero

* I add the :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` to ``test_calculator_w_dictionary_items``

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 6-7

            self.assertEqual(
                src.calculator.divide(
                    two_numbers['first_input'],
                    two_numbers['second_input']
                ),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  and

  .. code-block:: python
    :lineno-start: 189
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  the terminal_ shows green again. Lovely!

* I remove the lines I commented out to replace with ``self.division_result``

* I remove ``test_division``

  .. code-block:: python
    :lineno-start: 12

        def setUp(self):
            self.random_first_number = a_random_number()
            # self.random_second_number = a_random_number()
            self.random_second_number = 0
            try:
                self.division_result = (
                    self.random_first_number / self.random_second_number
                )
            except ZeroDivisionError:
                self.division_result = 'brmph?! cannot divide by 0. Try again...'

        def test_calculator_functions(self):

* I change ``self.random_second_number`` back to a random float_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()

  all tests are still green

* the dictionaries_ in ``test_calculator_functions`` and ``test_calculator_sends_message_when_input_is_not_a_number`` are similar, I add a new dictionary_ in the `setUp method`_ to replace them

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-27

            except ZeroDivisionError:
                self.division_result = 'brmph?! cannot divide by 0. Try again...'

            self.arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': (
                        self.random_first_number+self.random_second_number
                    ),
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': (
                        self.random_first_number-self.random_second_number
                    ),
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': self.division_result,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                }
            }

        def test_calculator_functions(self):

* then I use it in ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 1-2, 5-6, 10-11

            # for operation in arithmetic_tests:
            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        # arithmetic_tests[operation]['function'](
                        self.arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        # arithmetic_tests[operation]['expectation']
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test is still green

* I remove the commented lines and ``arithemtic_tests`` dictionary_ from ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 47

        def test_calculator_functions(self):
            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  still green

* I use the new :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` in ``test_calculator_sends_message_when_input_is_not_a_number``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3, 5-8

                with self.subTest(i=data):
                    # for operation in arithmetic:
                    for operation in self.arithmetic_tests:
                        self.assertEqual(
                            # arithmetic[operation](data, a_random_number()),
                            self.arithmetic_tests[operation]['function'](
                                data, a_random_number()
                            ),
                            error_message
                        )

  the test is still green

* I remove the commented lines and the ``arithmetic`` dictionary_

  .. code-block:: python
    :lineno-start: 58

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'brmph?! Numbers only. Try again...'

            for data in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                with self.subTest(i=data):
                    for operation in self.arithmetic_tests:
                        self.assertEqual(
                            self.arithmetic_tests[operation]['function'](
                                data, a_random_number()
                            ),
                            error_message
                        )

        def test_calculator_w_list_items(self):

  still green

* I add a `for loop`_ to use the ``arithmetic_tests`` dictionary_ in :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

  .. code-block:: python
    :lineno-start: 180
    :emphasize-lines: 4-8

            with self.assertRaises(TypeError):
                src.calculator.subtract(*not_two_numbers)

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.arithmetic_tests[operation]['function'](
                        **not_two_numbers
                    )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError` for all 4 cases

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...

* I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 3-6

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](
                            *not_two_numbers
                        )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 171

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            not_two_numbers = [0, 1, 2]

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](
                            *not_two_numbers
                        )


    # Exceptions seen

  still green

* I no longer need the :ref:`variable<what is a variable?>`, I remove it and use the :ref:`list<lists>` directly in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 5-7

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](
                            *[0, 1, 2]
                        )

  the test is still green

* Python_ allows me to put the 2 `with statements`_ together as one

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 3-11

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                # with self.subTest(operation=operation):
                #     with self.assertRaises(TypeError):
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](
                        *[0, 1, 2]
                    )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 171

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](
                        *[0, 1, 2]
                    )

* I add a `for loop`_ to ``test_calculator_w_list_items``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 6-13

            self.assertEqual(
                src.calculator.subtract(*two_numbers),
                self.random_first_number-self.random_second_number
            )

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            *two_numbers
                        ),
                        'BOOM!!!'
                    )

        def test_calculator_w_dictionary_items(self):

  the terminal_ shows :ref:`AssertionError` for the 4 operations

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - AssertionError: YZA.BCDEFGHIJKLMNO != 'BOOM!!!'
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - AssertionError: PQR.STUVWXYZABCDE != 'BOOM!!!'
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - AssertionError: F.GHIJKLMNOPQRSTUV != 'BOOM!!!'
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - AssertionError: WXYABC.DEFGHIJKLMN != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 7

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            *two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test passes

* I remove all the :ref:`assertions<what is an assertion?>` for the starred expression

  .. code-block:: python
    :lineno-start: 99

            self.assertEqual(
                src.calculator.subtract(two_numbers[-2], two_numbers[0]),
                self.random_first_number-self.random_first_number
            )

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            *two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

        def test_calculator_w_dictionary_items(self):

  still green

* I add a `for loop`_ to ``test_calculator_w_dictionary_items``

  .. code-block:: python
    :lineno-start: 159

            self.assertEqual(
                src.calculator.subtract(**two_numbers),
                self.random_first_number-self.random_second_number
            )

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            **two_numbers
                        ),
                        'BOOM!!!'
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the terminal_ shows :ref:`AssertionError` for the 4 operations

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - AssertionError: OPQ.RSTUVWXYZABCDEF != 'BOOM!!!'
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - AssertionError: GHI.JKLMNOPQRSTUVWX != 'BOOM!!!'
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - AssertionError: Y.ZABCDEFGHIJKLMNOP != 'BOOM!!!'
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - AssertionError: -QRSTU.VWXYZABCDEF != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 7

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            **two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>` for the double starred expression

  .. code-block:: python
    :lineno-start: 140

            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['first_input'],
                    two_numbers['first_input']
                ),
                self.random_first_number-self.random_first_number
            )

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            **two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  still green

----

*********************************************************************************
test squares
*********************************************************************************

Since I am using a :ref:`dictionary<what is a dictionary?>` adding a new test is easy. I want to add a test for using the :ref:`calculator<how to make a calculator part 1>` to square numbers like I did in :ref:`test_making_a_list_w_processes`

=================================================================================
:red:`RED`: make it fail
=================================================================================

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

=================================================================================
:refactor:`REFACTOR`: make it better
=================================================================================



I think it is time to take nap. That was a lot.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/calculator

* I deactivate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: python

    .../pumping_python/calculator

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

I added the following tests for the :ref:`calculator program<how to make a calculator part 5>` with :ref:`dictionaries` which made testing the program easier

* :ref:`test_calculator_w_dictionary_items`
* :ref:`test_calculator_functions` which replaced

  - :ref:`test_addition`
  - :ref:`test_subtraction`
  - :ref:`test_multiplication`
  - :ref:`test_division`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: dictionaries: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment part 1>`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator part 1>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`what you can do with dictionaries<dictionaries>`

I keep editing ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` when I start a new project. I want to automate the process so that I call the program and it does all the steps for me when I give it the name of the project, so I never have to edit the file again.

:ref:`Would you like to know how to make a Python Test Driven Development environment automatically with variables?<how to make a test driven development environment part 3>`

----

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