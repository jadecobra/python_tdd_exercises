.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../../links.rst

#################################################################################
how to make a calculator 8
#################################################################################

I can use the ``__getattribute__`` :ref:`method<what is a function?>` that comes with every Python_ :ref:`object<what is a class?>` in the :ref:`calculator<how to make a calculator>` tests

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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now --delay 0 .

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 6 items

    tests/test_calculator.py ......                                      [100%]

    ============================ 6 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_w_getattribute
*********************************************************************************


----

=================================================================================
:red:`RED`: make it fail
----

=================================================================================

----

* I add a test with a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 9-14

                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                },
            }

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }

        def test_calculator_functions(self):

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7-10

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }
            self.assertEqual(
                src.calculator.__getattribute__('add'),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: <function only_takes_numbers.<locals>.wrapper at 0xffff1a2bc3d4> != ABCD.EFGHIJKLMN

  I have to call the :ref:`function<what is a function?>` after ``__getattribute__`` returns it

----

=================================================================================
:green:`GREEN`: make it pass
----

=================================================================================

----

* I add parentheses after to make it a call

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 2
    :emphasize-text: ( )

            self.assertEqual(
                src.calculator.__getattribute__('add')(),
                calculator_tests['add']
            )

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: only_takes_numbers.<locals>.wrapper() missing 2 required positional arguments: 'first_input' and 'second_input'

  I have to give the inputs to the :ref:`function<what is a function?>`

* I add inputs in the parentheses

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 8-11

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }
            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the test passes

  - ``src.calculator.__getattribute__('add')`` returns ``src.calculator.add``
  - ``calculator_tests['add']`` returns ``self.random_first_number + self.random_second_number``
  - ``object.__getattribute__(something)`` checks if ``something`` is in ``object`` and returns it

----

=================================================================================
:green:`GREEN`: make it pass
----

=================================================================================

----

* I add another operation to the ``calculator_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines:

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                )
            }
            self.assertEqual(

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-14

            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )
            self.assertEqual(
                src.calculator.__getattribute__('subtract')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: OPQ.RSTUVWXYZABCDE != FGH.IJKLMNOPQRSTUV

* I change the expectation

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 6

                self.assertEqual(
                    src.calculator.__getattribute__('subtract')(
                        self.random_first_number,
                        self.random_second_number
                    ),
                    calculator_tests['subtract']
                )

  the test passes

* I add a `for loop`_

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 9-17

            self.assertEqual(
                src.calculator.__getattribute__('subtract')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['subtract']
            )

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        1
                    )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: operation add subtract

    SUBFAILED(operation='add') tests/test_calculator.py::TestCalculator::test_calculator_w_getattribute - AssertionError: WXY.ZABCDEFGHIJKL != 1
    SUBFAILED(operation='subtract') tests/test_calculator.py::TestCalculator::test_calculator_w_getattribute - AssertionError: MNO.PQRSTUVWXYZAB != 1

* I change the expectation

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 8

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        calculator_tests[operation]
                    )

  the test passes

* I remove the other :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                )
            }

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        calculator_tests[operation]
                    )

        def test_calculator_functions(self):

  the test is still green

* I add a :ref:`key<test_keys_of_a_dictionary>` for the next operation

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 9

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'division': self.division_result,
            }

            for operation in calculator_tests:

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'division'

* I used a name that is not in ``calculator.py``. I change the name

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines:

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
            }

  the test passes

* I add another operation

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 9-11

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiplication': (
                    self.random_first_number*self.random_second_number
                ),
            }

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiplication'

* I change the name

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 9

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

  the test passes

----

* I add the new :ref:`dictionary<what is a dictionary?>` to the `setUp method`_

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 8-19

                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                },
            }
            self.calculator_tests_a = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

        def test_calculator_w_getattribute(self):

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in ``test_calculator_w_getattribute``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-13

        def test_calculator_w_getattribute(self):
            # calculator_tests = {
            #     'add': (
            #         self.random_first_number+self.random_second_number
            #     ),
            #     'subtract': (
            #         self.random_first_number-self.random_second_number
            #     ),
            #     'divide': self.division_result,
            #     'multiply': (
            #         self.random_first_number*self.random_second_number
            #     ),
            # }
            calculator_tests = self.calculator_tests_a

            for operation in calculator_tests:

  the test is still green

* I use ``self.calculator_tests_a`` in the `for loop`_

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 1-2

            # for operation in calculator_tests:
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(

  still green

* I use it in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 9-10

            # for operation in calculator_tests:
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        # calculator_tests[operation]
                        self.calculator_tests_a[operation]
                    )

  green

* I remove the commented lines and the ``calculator_tests`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 60

        def test_calculator_w_getattribute(self):
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_functions(self):

  still green

* I no longer need ``test_calculator_functions`` since it is covered by ``test_calculator_w_getattribute``, they have the same tests. I remove ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 60

        def test_calculator_w_getattribute(self):
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the tests are still green

* I change the name of ``test_calculator_w_getattribute`` to ``test_calculator_functions``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

        def test_calculator_functions(self):
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  still green

----

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_calculator_sends_message_when_input_is_not_a_number` in a new `for loop`_

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 8-14

                    for operation in self.calculator_tests:
                        self.assertEqual(
                            self.calculator_tests[operation]['function'](
                                data, a_random_number()
                            ),
                            error_message
                        )
                    for operation in self.calculator_tests_a:
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                data, a_random_number()
                            ),
                            'BOOM!!!'
                        )

        def test_calculator_w_list_items(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for 13 tests

  .. code-block:: python

    AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'

* I change the expectation to the error message

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 6

                    for operation in self.calculator_tests_a:
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                data, a_random_number()
                            ),
                            error_message
                        )

  the test passes

* I remove the other `for loop`_

  .. code-block:: python
    :lineno-start: 74

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
                    for operation in self.calculator_tests_a:
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                data, a_random_number()
                            ),
                            error_message
                        )

        def test_calculator_w_list_items(self):

  the test is still green

* I forgot to remove the ``error_message`` :ref:`variable<what is a variable?>`. I remove it because I do not need it anymore

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 17

        def test_calculator_sends_message_when_input_is_not_a_number(self):
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
                    for operation in self.calculator_tests_a:
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                data, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

        def test_calculator_w_list_items(self):

  still green

----

* I use the ``__getattribute__`` :ref:`method<what is a function?>` with ``self.calculator_tests_a`` in a new `for loop`_ in :ref:`test_calculator_w_list_items`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 9-16

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.calculator_tests[operation]['function'](
                            *two_numbers
                        ),
                        self.calculator_tests[operation]['expectation']
                    )
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        1
                    )

        def test_calculator_w_dictionary_items(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the 4 operations

  .. code-block:: python

    AssertionError: CDEF.GHIJKLMNOPQRS != 1

* I change the expectation

  .. code-block:: python
    :lineno-start: 123

            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_w_dictionary_items(self):

  the test passes

* I remove the other `for loop`_

  .. code-block:: python
    :lineno-start: 110

            self.assertEqual(
                src.calculator.subtract(two_numbers[-2], two_numbers[0]),
                self.random_first_number-self.random_first_number
            )

            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_w_dictionary_items(self):

  the test is still green

----

* I do the same thing in :ref:`test_calculator_w_dictionary_items`

  .. code-block:: python
    :lineno-start: 159
    :emphasize-lines: 9-16

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        self.calculator_tests[operation]['function'](
                            **two_numbers
                        ),
                        self.calculator_tests[operation]['expectation']
                    )
            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        1
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the 4 operations

  .. code-block:: python

    AssertionError: TUVW.XYZABCDEFGHI != 1

* I change the expectation

  .. code-block:: python
    :lineno-start: 167

            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the test passes

* I remove the `for loop`_

  .. code-block:: python
    :lineno-start: 151

            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['first_input'],
                    two_numbers['first_input']
                ),
                self.random_first_number-self.random_first_number
            )

            for operation in self.calculator_tests_a:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        self.calculator_tests_a[operation]
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the test is still green

----

* I use the ``__getattribute__`` :ref:`method<what is a function?>` with ``self.calculator_tests_a`` in a new `for loop`_ in :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

  .. code-block:: python
    :lineno-start: 168
    :emphasize-lines: 10-17

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.calculator_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.calculator_tests[operation]['function'](
                        *[0, 1, 2]
                    )
            for operation in self.calculator_tests_a:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(ZeroDivisionError),
                ):
                    src.calculator.__getattribute__(operation)(
                        *[0, 1, 2]
                    )


    # Exceptions seen

  the terminal_ shows :ref:`TypeError<what causes TypeError?>` for each operation

  .. code-block:: python

    TypeError: only_takes_numbers.<locals>.wrapper() takes 2 positional arguments but 3 were given

  good, the tests work

* I change the :ref:`Exception<errors>` to match

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 4
    :emphasize-text: TypeError

            for operation in self.calculator_tests_a:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    src.calculator.__getattribute__(operation)(
                        *[0, 1, 2]
                    )


    # Exceptions seen

  the test passes

* I remove the other `for loop`_

  .. code-block:: python
    :lineno-start: 168

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.calculator_tests_a:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    src.calculator.__getattribute__(operation)(
                        *[0, 1, 2]
                    )


    # Exceptions seen

  the test is still green

----

* I remove ``self.calculator_tests`` from the `setUp method`_ because it is no longer used

  .. code-block:: python
    :lineno-start: 12

        def setUp(self):
            self.history = {}
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()
            try:
                self.division_result = (
                    self.random_first_number / self.random_second_number
                )
            except ZeroDivisionError:
                self.division_result = 'brmph?! cannot divide by 0. Try again...'

            self.calculator_tests_a = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

        def test_calculator_functions(self):

  the tests are still green

* I use the ``Rename Symbol`` feature to change ``self.calculator_tests_a`` to ``self.calculator_tests``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 12
    :emphasize-text: calculator_tests

        def setUp(self):
            self.history = {}
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()
            try:
                self.division_result = (
                    self.random_first_number / self.random_second_number
                )
            except ZeroDivisionError:
                self.division_result = 'brmph?! cannot divide by 0. Try again...'

            self.calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

        def test_calculator_functions(self):

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2, 9
    :emphasize-text: calculator_tests

        def test_calculator_functions(self):
            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests[operation]
                    )

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 12
    :emphasize-text: calculator_tests

        def test_calculator_sends_message_when_input_is_not_a_number(self):
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
                    for operation in self.calculator_tests:
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                data, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

        def test_calculator_w_list_items(self):

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 1, 7
    :emphasize-text: calculator_tests

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        self.calculator_tests[operation]
                    )

        def test_calculator_w_dictionary_items(self):

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 1, 7
    :emphasize-text: calculator_tests

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        self.calculator_tests[operation]
                    )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 2
    :emphasize-text: calculator_tests

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.calculator_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    src.calculator.__getattribute__(operation)(
                        *[0, 1, 2]
                    )


    # Exceptions seen

all the tests are passing and I feel like magic

----

*********************************************************************************
test calculator tests again
*********************************************************************************

I want to write the solution that will make all the tests in ``test_calculator.py`` pass without looking at them

----

=================================================================================
:red:`RED`: make it fail
----

=================================================================================

----

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`

* I delete all the text in ``calculator.py``, the terminal_ shows 3 passing tests and :ref:`AttributeError<what causes AttributeError?>` for 23 failing tests, I start with the last one

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize

    add

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'add' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
----

=================================================================================

----

* I point ``add`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:

    add = None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change it to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def add():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

* I add a name to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def add(x):
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add() takes 1 positional argument but 2 were given

* I add a second name to the parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(x, y):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != TUV.WXYZABCDEFGHIJ

* I change the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(x, y):
        return x + y

  the terminal shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def add(x, y):
        return x + y


    def divide(x, y):
        return x / y

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiply'

* I add a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def divide(x, y):
        return x / y


    def multiply(x, y):
        return x * y

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def multiply(x, y):
        return x * y


    def subtract(x, y):
        return x - y

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    TypeError: multiply() got an unexpected keyword argument 'first_input'

* I add a name to the ``multiply`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def multiply(x, y, first_input):
        return x * y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: multiply() missing 1 required positional argument: 'first_input'

* I add a default argument to make it a choice

  .. code-block:: python
    :lineno-start: 9

    def multiply(x, y, first_input=None):
        return x * y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: multiply() got an unexpected keyword argument 'second_input'

* I add ``second_input`` with a default value to the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def multiply(x, y, first_input=None, second_input=None):
        return x * y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: multiply() missing 2 required positional arguments: 'x' and 'y'

* my solution makes no sense, I remove ``x`` and ``y`` from the parentheses

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def multiply(first_input=None, second_input=None):
        return x * y

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'x' is not defined

* I change the names in the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    def multiply(first_input=None, second_input=None):
        return first_input * second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() got an unexpected keyword argument 'first_input'

* I use ``Rename Symbol`` to change the name

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def divide(first_input, y):
        return first_input / y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() got an unexpected keyword argument 'second_input'

* I do the same thing to ``y``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def divide(first_input, second_input):
        return first_input / second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: subtract() got an unexpected keyword argument 'first_input'

  same problem, same solution

* I change the names

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1-2

    def subtract(first_input, second_input):
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: add() got an unexpected keyword argument 'first_input'

* I change the names in the ``add`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def add(first_input, second_input):
        return first_input + second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +: 'dict' and 'float'

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3
    :emphasize-text: dict

    def add(first_input, second_input):
        if isinstance(first_input, dict):
            return None
        return first_input + second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'brmph?! Numbers only. Try again...'

* I change the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3
    :emphasize-text: dict

    def add(first_input, second_input):
        if isinstance(first_input, dict):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'dict' and 'float'

* I add an :ref:`if statement<if statements>` to the ``subtract`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-3
    :emphasize-text: dict

    def subtract(first_input, second_input):
        if isinstance(first_input, dict):
            return None
        return first_input - second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'brmph?! Numbers only. Try again...'

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3
    :emphasize-text: dict

    def subtract(first_input, second_input):
        if isinstance(first_input, dict):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for /: 'dict' and 'float'

  same problem, same solution

* I add an :ref:`if statement<if statements>` with the same message in the ``divide`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3
    :emphasize-text: dict

    def divide(first_input, second_input):
        if isinstance(first_input, dict):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for *: 'dict' and 'float'

* I add the same :ref:`if statement<if statements>` to the ``multiply`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3
    :emphasize-text: dict

    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, dict):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +: 'set' and 'float'

* I add to the :ref:`if statement<if statements>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2
    :emphasize-text: set

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'set' and 'float'

* I change the :ref:`if statement<if statements>` in the ``subtract`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2
    :emphasize-text: set

    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: unsupported operand type(s) for *: 'set' and 'float'

* I change the :ref:`if statement<if statements>` in the ``multiply`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-text: set

    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: can only concatenate list (not "float") to list

* I add another :ref:`data type<data structures>` to the :ref:`if statement<if statements>` of the ``add`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2
    :emphasize-text: list

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set, list)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'list' and 'float'

  it looks I will have to do this for all the other operations

* I add the :ref:`list<what is a list?>` to the :ref:`if statement<if statements>` in the other :ref:`functions<what is a function?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2, 8, 14
    :emphasize-text: list

    def divide(first_input, second_input):
        if isinstance(first_input, (dict, set, list)):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set, list)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set, list)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: can only concatenate tuple (not "float") to tuple

  another :ref:`data type<data structures>`, there has to be a better way

* I add tuple_ to the `isinstance method`_ in the :ref:`if statement<if statements>` of the ``add`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2
    :emphasize-text: tuple

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for -: 'tuple' and 'float'

  same problem, same solution

* I add tuple_ to the :ref:`if statement<if statements>` of the other :ref:`functions<what is a function?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2, 8, 14
    :emphasize-text: tuple

    def divide(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple)):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set, list, tuple)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: can only concatenate str (not "float") to str

* I add str_ to the :ref:`if statements` of the 4 :ref:`functions`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2, 8, 14, 20
    :emphasize-text: str

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input


    def divide(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str)):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set, list, tuple, str)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(i=True) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: 404.40333818765737 != 'brmph?! Numbers on...
    SUBFAILED(i=False) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: JKL.MNOPQRSTUVWXYZ != 'brmph?! Numbers on...

  2 of the failures are for :ref:`booleans<what are booleans?>`

* I add bool_ to the :ref:`if statements` of the :ref:`functions<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2, 8, 14, 20
    :emphasize-text: bool

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input


    def divide(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool)):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set, list, tuple, str, bool)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +: 'NoneType' and 'float'

* I add :ref:`None<what is None?>` to the call to the `isinstance method`_ in the :ref:`if statements` of the :ref:`functions<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2, 8, 14, 20
    :emphasize-text: None

    def add(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool, None)):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input


    def divide(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool, None)):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if isinstance(first_input, (dict, set, list, tuple, str, bool, None)):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if isinstance(first_input, (dict, set, list, tuple, str, bool, None)):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

  that change made things worse. I cannot use :ref:`None<what is None?>` in the `isinstance method`_

* I undo the change then add a new condition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5, 11-14, 20-23, 29-32

    def add(first_input, second_input):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input


    def divide(first_input, second_input):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input


    def multiply(first_input=None, second_input=None):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input * second_input


    def subtract(first_input, second_input):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input - second_input

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
----

=================================================================================

----

* I add a :ref:`decorator function<how to make a decorator function>` to remove the repetition of the :ref:`if statements` because they are all the same

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-12

    def check_input(function):
        def wrapper(first_input, second_input):
            if (
                isinstance(
                    first_input,
                    (dict, set, list, tuple, str, bool)
                ) or
                first_input is None
            ):
                return 'brmph?! Numbers only. Try again...'
            return function(first_input, second_input)
        return wrapper


    def add(first_input, second_input):

* I use the new :ref:`function<what is a function?>` to :ref:`wrap<how to make a decorator function>` the ``add`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

    @check_input
    def add(first_input, second_input):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input + second_input

  the test is still green

* I remove the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 15

    @check_input
    def add(first_input, second_input):
        return first_input + second_input


    def divide(first_input, second_input):

  still green

* I do the same thing with the ``divide`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1

    @check_input
    def divide(first_input, second_input):
        if (
            isinstance(first_input, (dict, set, list, tuple, str, bool))
            or first_input is None
        ):
            return 'brmph?! Numbers only. Try again...'
        return first_input / second_input

  green

* I remove the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 20

    @check_input
    def divide(first_input, second_input):
        return first_input / second_input


    def multiply(first_input=None, second_input=None):

  the test is still green

* I make the same change to the other 2 :ref:`functions<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 25-27, 30-32

    def check_input(function):
        def wrapper(first_input, second_input):
            if (
                isinstance(
                    first_input,
                    (dict, set, list, tuple, str, bool)
                ) or
                first_input is None
            ):
                return 'brmph?! Numbers only. Try again...'
            return function(first_input, second_input)
        return wrapper


    @check_input
    def add(first_input, second_input):
        return first_input + second_input


    @check_input
    def divide(first_input, second_input):
        return first_input / second_input


    @check_input
    def multiply(first_input=None, second_input=None):
        return first_input * second_input


    @check_input
    def subtract(first_input, second_input):
        return first_input - second_input

  still green

----

All the tests are passing, but there is a problem. What happens when the :ref:`functions<what is a function?>` receive a bad input as the second input or something that is not a :ref:`dictionary<what is a dictionary?>`, set_, :ref:`list<what is a list?>`, string_ or :ref:`boolean<what are booleans?>`? I need a better test. I am still learning

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests, the terminal_ shows

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

I used the ``__getattribute__`` built-in :ref:`function<what is a function?>` to make the calculator tests simpler.

I rewrote the solution after rewriting the tests and found that I did not add a test for bad second inputs

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 8: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`

:ref:`Would you like to know what causes ModuleNotFoundError?<what is a module?>`

----

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