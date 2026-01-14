.. meta::
  :description: Master Python dictionaries with TDD! Learn :ref:`key-value pair<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`s, methods, and testing techniques in this hands-on guide. Start coding now!
  :keywords: Jacob Itegboje, Python dictionaries, Test-Driven Development, Python programming, data structures, unit testing, Python tutorial, coding guide

.. include:: ../../links.rst

.. _clear: https://docs.python.org/3/library/stdtypes.html#dict.clear
.. _clear method: clear_
.. _copy: https://docs.python.org/3/library/stdtypes.html#dict.copy
.. _copy method: copy_
.. _fromkeys: https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
.. _fromkeys method: fromkeys_
.. _get: https://docs.python.org/3/library/stdtypes.html#dict.get
.. _get method: get_
.. _items: https://docs.python.org/3/library/stdtypes.html#dict.items
.. _items method: items_
.. _keys: https://docs.python.org/3/library/stdtypes.html#dict.keys
.. _keys method: keys_
.. _pop: https://docs.python.org/3/library/stdtypes.html#dict.pop
.. _pop method: pop_
.. _popitem: https://docs.python.org/3/library/stdtypes.html#dict.popitem
.. _popitem method: popitem_
.. _setdefault: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
.. _setdefault method: setdefault_
.. _update: https://docs.python.org/3/library/stdtypes.html#dict.update
.. _update method: update_
.. _values: https://docs.python.org/3/library/stdtypes.html#dict.values
.. _dict: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
.. _dict class: dict_
.. _dictionary: dict_
.. _dictionaries: dictionary_

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done

#################################################################################
how to make a calculator part 6
#################################################################################

*********************************************************************************
test_calculator_w_dictionary_items
*********************************************************************************

I can use a dictionary_ to test the :ref:`calculator functions<how to make a calculator part 1>` as long as its values are numbers

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
    collected 7 items

    tests/test_calculator.py .......                                     [100%]

    ============================ 7 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

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

.. code-block:: shell

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

  .. code-block:: shell

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

  .. code-block:: shell

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

  .. code-block:: shell

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
    :emphasize-lines: 3-4, 8, 12, 16, 20

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'first_input': self.random_first_number,
                'second_input': self.random_second_number,
            }

            self.assertEqual(
                src.calculator.add(two_numbers['first_input'], two_numbers['second_input']),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(two_numbers['first_input'], two_numbers['second_input']),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(two_numbers['second_input'], two_numbers['second_input']),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(two_numbers['first_input'], two_numbers['first_input']),
                self.random_first_number-self.random_first_number
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: VWX.YZABCDEFGHIJK != LMN.OPQRSTUVWXYZABC

* I change the calculation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 146
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number+self.random_second_number
            )

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 146
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

  .. code-block:: shell

    AssertionError: H.IJKLMNOPQRSTUVWX != YZABCD.EFGHIJKLMNO

* I change the calculation

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 150
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

  .. code-block:: shell

    AssertionError: IJKLMN.OPQRSTUVWX != Y.ZABCDEFGHIJKLMNOP

* I change the calculation

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 154
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

  .. code-block:: shell

    AssertionError: JKL.MNOPQRSTUVWXYZ != ABC.DEFGHIJKLMNOP

* I change the expectation

  .. code-block:: python
    :lineno-start: 158
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

* I can also use a dictionary_ with a `for loop`_ to make ``test_calculator_sends_message_when_input_is_not_a_number`` more complex and simpler

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-9, 21-25

    def test_calculator_sends_message_when_input_is_not_a_number(self):
        error_message = 'Excuse me?! Numbers only. Try again...'

        arithmetic = {
            'add': src.calculator.add,
            'subtract': src.calculator.subtract,
            'multiply': src.calculator.multiply,
            'divide': src.calculator.divide
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
                        arithmetic[operation](data, a_random_number),
                        'BOOM'
                    )
                self.assertEqual(
                    src.calculator.add(data, a_random_number()),
                    error_message
                )

  the terminal_ shows :ref:`AssertionError` for every case in the :ref:`iterable<what is an iterable?>`

  .. code-block:: python

    SUBFAILED(i=None) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=True) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=False) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i='') tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i='text') tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=()) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=(0, 1, 2, 'n')) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=[]) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=[0, 1, 2, 'n']) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i=set()) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={0, 1, 2, 'n'}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'
    SUBFAILED(i={'key': 'value'}) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 'Excuse me?! Numbers only. Try again...' != 'BOOM'

  the test works

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
            error_message = 'Excuse me?! Numbers only. Try again...'

            arithmetic = {
                'add': src.calculator.add,
                'subtract': src.calculator.subtract,
                'multiply': src.calculator.multiply,
                'divide': src.calculator.divide
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
                            arithmetic[operation](data, a_random_number),
                            error_message
                        )

        def test_calculator_w_list_items(self):

  this solution is not as easy to read as what was there before especially for someone new to Python_

----

*********************************************************************************
test_calculator_functions
*********************************************************************************

I want to use a dictionary_ to write one test that covers all the :ref:`4 calculator functions<how to make a calculator part 1>`

=================================================================================
:green:`RED`: make it pass
=================================================================================

* I add a new test

  .. code-block:: python
    :lineno-start: 173
    :emphasize-lines: 4-10, 12-17

            with self.assertRaises(TypeError):
                src.calculator.subtract(*not_two_numbers)

        def test_calculator_functions(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'division': src.calculator.divide,
                'multiplication': src.calculator.multiply
            }

            for operation in arithmetic:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic[operation](self.random_first_number, self.random_second_number),
                        'BOOM!!!'
                    )


    # Exceptions seen

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
    :lineno-start: 181
    :emphasize-lines: 3-8

                'multiplication': src.calculator.multiply
            }
            data = {
                'addition': self.random_first_number+self.random_second_number,
                'subtraction': self.random_first_number-self.random_second_number,
                'division': self.random_first_number/self.random_second_number,
                'multiplication': self.random_first_number*self.random_second_number,
            }

            for operation in arithmetic:

* I use the new dictionary_ in the calculation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5

            for operation in arithmetic:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic[operation](self.random_first_number, self.random_second_number),
                        data[operation]
                    )

  the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* the two dictionaries_ in this test have the same :ref:`keys<test_keys_of_a_dictionary>`. I put the dictionaries_ together

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 4-21

                'multiplication': self.random_first_number*self.random_second_number,
            }

            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': self.random_first_number+self.random_second_number,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': self.random_first_number-self.random_second_number,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': self.random_first_number/self.random_second_number,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': self.random_first_number*self.random_second_number,
                }
            }

            for operation in arithmetic:

* I add a new :ref:`assertion<what is an assertion?>` in a `for loop`_ with the `subTest method`_

  .. code-block:: python
    :lineno-start: 213
    :emphasize-lines: 4-12

                        data[operation]
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


    def test_addition(self):

  the terminal_ shows :ref:`AssertionError`:

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: HIJ.KLMNOPQRSTUVW != 'BOOM!!!'
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: XYZA.BCDEFGHIJKLMN != 'BOOM!!!'
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: NOP.QRSTUVWXYZABCDEF != 'BOOM!!!'
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_functions - AssertionError: GHIJKLM.NOPQRSTUVWX != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 216
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
    :lineno-start: 176

        def test_calculator_functions(self):
            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': self.random_first_number+self.random_second_number,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': self.random_first_number-self.random_second_number,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': self.random_first_number/self.random_second_number,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': self.random_first_number*self.random_second_number,
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

* I remove the ``test_addition``, ``test_subtraction``, ``test_multiplication``

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

* I use an :ref:`exception handler<how to use try...except...else>` to add a new :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` for the result of :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 15

            self.random_second_number = 0
            try:
                self.division_result = self.random_first_number / self.random_second_number
            except ZeroDivisionError:
                self.division_result = 'undefined: I cannot divide by 0'

* I use the new :ref:`class attribute (variable) <test_attribute_error_w_class_attributes>` in ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-4

                'division': {
                    'function': src.calculator.divide,
                    # 'expectation': self.random_first_number/self.random_second_number,
                    'expectation': self.division_result,
                },

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` for 2 tests

  .. code-block:: python

    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_dictionary_items - ZeroDivisionError: float division by zero
    FAILED tests/test_calculator.py::TestCalculator::test_calculator_w_list_items - ZeroDivisionError: float division by zero

  progress

* I add the :ref:`class attribute (variable)<test_attribute_error_w_class_attributes>` to ``test_calculator_w_list_items``

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(two_numbers[-2], two_numbers[-1]),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  and

  .. code-block:: python
    :lineno-start: 122
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
    :lineno-start: 146
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(two_numbers['first_input'], two_numbers['second_input']),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  and

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 3-4

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                # self.random_first_number/self.random_second_number
                self.division_result
            )

  the terminal_ shows green. Lovely!

* I remove the commented lines I added

* I remove ``test_division``

  .. code-block:: python

        def setUp(self):
            self.random_first_number = a_random_number()
            # self.random_second_number = a_random_number()
            self.random_second_number = 0
            try:
                self.division_result = self.random_first_number / self.random_second_number
            except ZeroDivisionError:
                self.division_result = 'undefined: I cannot divide by 0'

        def test_calculator_functions(self):

* I change ``self.random_second_number`` back to a random float_

  .. code-block:: python
    :lineno-start: 12

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()
        try:
            self.division_result = self.random_first_number / self.random_second_number
        except ZeroDivisionError:
            self.division_result = 'undefined: I cannot divide by 0'

  all tests are passing

* the dictionaries_ in ``test_calculator_functions`` and ``test_calculator_sends_message_when_input_is_not_a_number`` are similar, I add a new dictionary_ in the `setUp method`_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-21

            except ZeroDivisionError:
                self.division_result = 'undefined: I cannot divide by 0'

            self.arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': self.random_first_number+self.random_second_number,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': self.random_first_number-self.random_second_number,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': self.division_result,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': self.random_first_number*self.random_second_number,
                }
            }

        def test_calculator_functions(self):

* I use it in ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 1, 4, 8

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.arithmetic_tests[operation]['function'](
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test is green

* I remove the ``arithemtic_tests`` dictionary_ from ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 39

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
    :lineno-start: 69
    :emphasize-lines: 2-3, 5-6

                with self.subTest(i=data):
                    # for operation in arithmetic:
                    for operation in self.arithmetic_tests:
                        self.assertEqual(
                            # arithmetic[operation](data, a_random_number),
                            self.arithmetic_tests[operation]['function'](data, a_random_number),
                            error_message
                        )

  the test is still green

* I remove the commented lines and the ``arithmetic`` dictionary_

  .. code-block:: python
    :lineno-start: 50

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'Excuse me?! Numbers only. Try again...'

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
                            self.arithmetic_tests[operation]['function'](data, a_random_number),
                            error_message
                        )

        def test_calculator_w_list_items(self):

  still green

* I add a `for loop`_ to use the ``arithmetic_tests`` dictionary_ in :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 4-6

            with self.assertRaises(TypeError):
                src.calculator.subtract(*not_two_numbers)

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.arithmetic_tests[operation]['function'](*not_two_numbers)


    # Exceptions seen

  the terminal_ shows :ref:`TypeError` for all 4 cases

  .. code-block:: python

    SUBFAILED(operation='addition') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='subtraction') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='division') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...
    SUBFAILED(operation='multiplication') tests/test_calculator.py::TestCalculator::test_calculator_raises_type_error_when_given_more_than_two_inputs - TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were ...

* I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 3-4

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](*not_two_numbers)

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 149

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            not_two_numbers = [0, 1, 2]

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](*not_two_numbers)


    # Exceptions seen

  still green

* I no longer need the :ref:`variable<what is a variable?>`, I remove it and use the :ref:`list<lists>` directly in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 5

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](*[0, 1, 2])

  the test is still green

* Python_ allows me to put the 2 with contexts together in one statement

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 3-8

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                # with self.subTest(operation=operation):
                #     with self.assertRaises(TypeError):
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](*[0, 1, 2])

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 137

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](*[0, 1, 2])

* I add a `for loop`_ to ``test_calculator_w_list_items``

  .. code-block:: python
    :lineno-start: 105
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
    :lineno-start: 1
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
    :lineno-start: 89

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
    :lineno-start: 137

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
    :lineno-start: 142
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

* I remove the other :ref:`assertions<what is an assertion?>` for the starred expression

  .. code-block:: python
    :lineno-start: 121

            self.assertEqual(
                src.calculator.subtract(two_numbers['first_input'], two_numbers['first_input']),
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

=================================================================================
close the project
=================================================================================

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
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

*********************************************************************************
review
*********************************************************************************

Dictionaries_ are also known as Mappings, they contain :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` and any :ref:`object<what is a class?>` can be used as values.

I ran tests to show that I can make a dictionary_ with ``dict()`` or curly braces ``{}``, then I ran the following tests to see what :ref:`Python basic data types<data structures>` I can use as :ref:`keys in a dictionary<test_keys_of_a_dictionary>`

* :ref:`test_making_a_dictionary_w_none_as_a_key`
* :ref:`test_making_a_dictionary_w_a_boolean_as_a_key`
* :ref:`test_making_a_dictionary_w_a_number_as_a_key`
* :ref:`test_making_a_dictionary_w_a_tuple_as_a_key`
* :ref:`test_making_a_dictionary_w_a_list_as_a_key`
* :ref:`test_making_a_dictionary_w_a_set_as_a_key`
* :ref:`test_making_a_dictionary_w_a_dictionary_as_a_key`

I also ran these tests for the :ref:`methods of dictionaries<test_attributes_and_methods_of_dictionaries>`

* :ref:`test_clear_empties_a_dictionary`
* :ref:`test_copy_a_dictionary`
* :ref:`test_fromkeys_makes_a_dictionary_from_an_iterable`
* :ref:`test_get_value_of_a_key_in_a_dictionary`
* :ref:`test_items_returns_iterable_of_key_value_pairs_of_a_dictionary`
* :ref:`test_keys_of_a_dictionary`
* :ref:`test_pop_removes_given_key_from_a_dictionary_and_returns_its_value`
* :ref:`test_popitem_removes_and_returns_last_key_value_pair_from_a_dictionary`
* :ref:`test_setdefault_adds_given_key_to_a_dictionary`
* :ref:`test_update_a_dictionary`
* :ref:`test_values_of_a_dictionary`

and finally a test for the :ref:`Exception<errors>` to know when working with dictionaries_ - :ref:`KeyError<test_key_error>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about dictionaries>`

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
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator part 1>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`

:ref:`Would you like to put it all together in Classes?<what is a class?>`

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