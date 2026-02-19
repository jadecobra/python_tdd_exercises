.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

.. _isinstance built-in function: https://docs.python.org/3/library/functions.html#isinstance

#################################################################################
how to make a calculator 8
#################################################################################

I can use the ``__getattribute__`` :ref:`method<what is a function?>` that comes with every :ref:`Python object<what is a class?>` in the :ref:`calculator tests<how to make a calculator>`

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

    tests/test_calculator.py .....                                [100%]

    ======================== 5 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_w_getattribute
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 168
  :emphasize-lines: 12-16

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

      def test_calculator_w_getattribute(self):
          self.assertEqual(
              src.calculator.__getattribute__('BOOM!!!'),
              src.calculator.add
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'BOOM!!!'

* ``__getattribute__`` is a :ref:`method<what is a function?>` that takes a name and checks if the name is an :ref:`attribute<what is an attribute?>` of the :ref:`object<what is a class?>`

  - if the name is NOT an :ref:`attribute<what is an attribute?>` it raises :ref:`AttributeError<what causes AttributeError?>`
  - if the name is an :ref:`attribute<what is an attribute?>` it returns the object it points to

* ``src.calculator.__getattribute__('BOOM!!!')`` checks if the ``calculator.py`` :ref:`module<what is a module?>` in the ``src`` folder_ has anything named ``BOOM!!!``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``'BOOM!!!'`` to ``'add'``

.. code-block:: python
  :lineno-start: 179
  :emphasize-lines: 4

        def test_calculator_w_getattribute(self):
            self.assertEqual(
                src.calculator.__getattribute__('add'),
                src.calculator.add
            )

the test passes because the :ref:`add function<test_addition>` is an :ref:`attribute<what is an attribute?>` of ``src.calculator``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to the :ref:`add function<test_addition>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 4-7

        def test_calculator_w_getattribute(self):
            self.assertEqual(
                src.calculator.__getattribute__('add'),
                src.calculator.add(
                    self.random_first_number,
                    self.random_second_number
                )
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: <function numbers_only.<locals>.decorator at 0xffffa1234bc0> != DEF.GHIJKLMNOPQRS


  I have to call the :ref:`add function<test_addition>` after ``__getattribute__`` returns it

* I add parentheses at the end of the line to make it a call

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 3-6
    :emphasize-text: ( )

        def test_calculator_w_getattribute(self):
            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                src.calculator.add(
                    self.random_first_number,
                    self.random_second_number
                )
            )

  the test passes

* I add a :ref:`variables<what is a variable?>` and a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 2-4

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {'add': x+y}

            self.assertEqual(


* I use the :ref:`dictionary<what is a dictionary?>` to change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 6-10

            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                # src.calculator.add(
                #     self.random_first_number,
                #     self.random_second_number
                # )
                calculator_tests['add']
            )

  the test is still green

* I use the :ref:`variables<what is a variable?>` for ``self.random_first_number`` and ``self.random_second_number`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 3-5

            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    # self.random_first_number,
                    # self.random_second_number
                    x, y
                ),
                # src.calculator.add(
                #     self.random_first_number,
                #     self.random_second_number
                # )
                calculator_tests['add']
            )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 184

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {'add': x+y}

            self.assertEqual(
                src.calculator.__getattribute__('add')(x, y),
                calculator_tests['add']
            )

  green

----

* I add :ref:`subtraction<test_subtraction>` to the ``calculator_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 4-7

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
            }

* then I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.__getattribute__('add')(x, y),
                calculator_tests['add']
            )
            self.assertEqual(
                src.calculator.__getattribute__('subtract')(x, y),
                calculator_tests['add']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: OPQ.RSTUVWXYZABCDE != FGH.IJKLMNOPQRSTUV

* I change the expectation

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.__getattribute__('subtract')(x, y),
                calculator_tests['subtract']
            )

  the test passes

----

* I add :ref:`multiplication<test_multiplication>` to the ``calculator_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 7

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
            }

* then I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 192
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.__getattribute__('subtract')(x, y),
                calculator_tests['subtract']
            )
            self.assertEqual(
                src.calculator.__getattribute__('multiply')(x, y),
                calculator_tests['subtract']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: WXYZA.BCDEFGHIJKLMNO != PQ.RSTUVWXYZABCDE

* I change the expectation

  .. code-block:: python
    :lineno-start: 196
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.__getattribute__('multiply')(x, y),
                calculator_tests['multiply']
            )

  the test passes

----

* I add :ref:`division<test_division>` to the ``calculator_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 8

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': x/y,
            }

* then I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 197
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.__getattribute__('multiply')(x, y),
                calculator_tests['multiply']
            )
            self.assertEqual(
                src.calculator.__getattribute__('divide')(x, y),
                calculator_tests['multiply']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: F.GHIJKLMNOPQRST != UVWXY.ZABCDEFGH

* I change the expectation

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 25

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': x/y,
            }

            self.assertEqual(
                src.calculator.__getattribute__('add')(x, y),
                calculator_tests['add']
            )
            self.assertEqual(
                src.calculator.__getattribute__('subtract')(x, y),
                calculator_tests['subtract']
            )
            self.assertEqual(
                src.calculator.__getattribute__('multiply')(x, y),
                calculator_tests['multiply']
            )
            self.assertEqual(
                src.calculator.__getattribute__('divide')(x, y),
                calculator_tests['divide']
            )


    # Exceptions seen

  the test passes

----

* I add a :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 11-18

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': x/y,
            }

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            x, y
                        ),
                        'BOOM!!!'
                    )

            self.assertEqual(
                src.calculator.__getattribute__('add')(x, y),
                calculator_tests['add']
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: add subtract multiply divide

    SUBFAILED(operation='add') ...      - AssertionError: FGH.IJKLMNOPQRSTU != 'BOOM!!!'
    SUBFAILED(operation='subtract') ... - AssertionError: VWX.YZABCDEFGHIJKL != 'BOOM!!!'
    SUBFAILED(operation='multiply') ... - AssertionError: MNOP.QRSTUVWXYZAB != 'BOOM!!!'
    SUBFAILED(operation='divide') ...   - AssertionError: CD.EFGHIJKLMNOPQR != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 5

                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            x, y
                        ),
                        calculator_tests[operation]
                    )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 179

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': x/y,
            }

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            x, y
                        ),
                        calculator_tests[operation]
                    )


    # Exceptions seen

  is this simpler than :ref:`test_calculator_functions`?

----

* I add ``calculator_tests`` to the `setUp method`_ to make it a :ref:`class attribute<test_attribute_error_w_class_attributes>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 13-18

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

            x = self.random_first_number
            y = self.random_second_number

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            self.calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': division_result
            }

            self.arithmetic_tests = {

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in :ref:`test_calculator_w_getattribute`

  .. code-block:: python
    :lineno-start: 186
    :emphasize-lines: 4-10

        def test_calculator_w_getattribute(self):
            x = self.random_first_number
            y = self.random_second_number
            # calculator_tests = {
            #     'add': x+y,
            #     'subtract': x-y,
            #     'multiply': x*y,
            #     'divide': x/y,
            # }
            calculator_tests = self.calculator_tests

            for operation in calculator_tests:

  the test is still green

* I use ``self.calculator_tests`` in the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 197
    :emphasize-lines: 1-2

            # for operation in calculator_tests:
            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            x, y
                        ),
                        calculator_tests[operation]
                    )

  still green

* I use it in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 200
    :emphasize-lines: 8-9

                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            x, y
                        ),
                        # calculator_tests[operation]
                        self.calculator_tests[operation]
                    )

  green

* I use ``self.random_first_number`` for ``x`` and ``self.random_second_number`` for ``y`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 200
    :emphasize-lines: 3-5

                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            # x, y
                            self.random_first_number,
                            self.random_second_number
                        ),
                        # calculator_tests[operation]
                        self.calculator_tests[operation]
                    )

  still green

* I remove the commented lines and the :ref:`variables<what is a variable?>` because they are no longer used

  .. code-block:: python
    :lineno-start: 186

        def test_calculator_w_getattribute(self):
            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests[operation]
                    )


    # Exceptions seen

  the test is still green

----

* I remove :ref:`test_calculator_functions` because :ref:`test_calculator_w_getattribute` has the same tests

  .. code-block:: python
    :lineno-start: 153

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                for operation in self.arithmetic_tests:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            self.arithmetic_tests[operation]['function'](
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

        def test_calculator_w_getattribute(self):
            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        self.calculator_tests[operation]
                    )


    # Exceptions seen

  the tests are still green

* I change the name of :ref:`test_calculator_w_getattribute` to :ref:`test_calculator_functions`

  .. code-block:: python
    :lineno-start: 175
    :emphasize-lines: 1

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


    # Exceptions seen

----

* I use ``self.calculator_tests`` in the :ref:`for loop<what is a for loop?>` of  :ref:`test_calculator_sends_message_when_input_is_not_a_number`

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 11-12

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                # for operation in self.arithmetic_tests:
                for operation in self.calculator_tests:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):

  the terminal_ shows :ref:`KeyError<test_key_error>` for all 52 sub tests

* I use the ``__getattribute__`` :ref:`method<what is a function?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 169
    :emphasize-lines: 2-3

                        self.assertEqual(
                            # self.arithmetic_tests[operation]['function'](
                            src.calculator.__getattribute__(operation)(
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 153

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                for operation in self.calculator_tests:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            src.calculator.__getattribute__(operation)(
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

        def test_calculator_functions(self):

----

* I use ``self.calculator_tests`` in the :ref:`for loop<what is a for loop?>` of  :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 2-3

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            # for operation in self.arithmetic_tests:
            for operation in self.calculator_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](
                        [0, 1, 2]
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the terminal_ shows :ref:`KeyError<test_key_error>` for all 4 sub tests

* I use the ``__getattribute__`` :ref:`method<what is a function?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 1-2

                    # self.arithmetic_tests[operation]['function'](
                    src.calculator.__getattribute__(operation)(
                        [0, 1, 2]
                    )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 143

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.calculator_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    src.calculator.__getattribute__(operation)(
                        [0, 1, 2]
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the test is still green

----

* I use ``self.calculator_tests`` in the :ref:`for loop<what is a for loop?>` of  :ref:`test_calculator_w_dictionary_items`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 7-8

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'first_input': self.random_first_number,
                'second_input': self.random_second_number,
            }

            # for operation in self.arithmetic_tests:
            for operation in self.calculator_tests:
                with self.subTest(operation=operation):

  the terminal_ shows :ref:`KeyError<test_key_error>` for the 4 tests

* I use the ``__getattribute__`` :ref:`method<what is a function?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 2-3

                    self.assertEqual(
                        # self.arithmetic_tests[operation]['function'](
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

  the terminal_ shows :ref:`KeyError<test_key_error>` for the 4 sub tests

* I use ``self.calculator_tests`` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 6-7

                    self.assertEqual(
                        # self.arithmetic_tests[operation]['function'](
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        # self.arithmetic_tests[operation]['expectation']
                        self.calculator_tests[operation]
                    )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 99

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'first_input': self.random_first_number,
                'second_input': self.random_second_number,
            }

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            **two_numbers
                        ),
                        self.calculator_tests[operation]
                    )

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

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

----

* I use ``self.calculator_tests`` in the :ref:`for loop<what is a for loop?>` of  :ref:`test_calculator_w_list_items`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 12-13

      def test_calculator_w_list_items(self):
          # two_numbers = [
          #     self.random_first_number,
          #     self.random_second_number
          # ]
          a_dictionary = {
              'x': self.random_first_number,
              'y': self.random_second_number
          }
          two_numbers = list(a_dictionary.values())

          # for operation in self.arithmetic_tests:
          for operation in self.calculator_tests:
              with self.subTest(operation=operation):

  the terminal_ shows :ref:`KeyError<test_key_error>` for the 4 sub tests

* I use the ``__getattribute__`` :ref:`method<what is a function?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2-3

                    self.assertEqual(
                        # self.arithmetic_tests[operation]['function'](
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        self.arithmetic_tests[operation]['expectation']
                    )

  the terminal_ shows :ref:`KeyError<test_key_error>` for the sub tests

* I use ``self.calculator_tests`` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 6-7

                    self.assertEqual(
                        # self.arithmetic_tests[operation]['function'](
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        # self.arithmetic_tests[operation]['expectation']
                        self.calculator_tests[operation]
                    )

  the test passes

* I remove the new commented lines

  .. code-block:: python
    :lineno-start: 50

        def test_calculator_w_list_items(self):
            # two_numbers = [
            #     self.random_first_number,
            #     self.random_second_number
            # ]
            a_dictionary = {
                'x': self.random_first_number,
                'y': self.random_second_number
            }
            two_numbers = list(a_dictionary.values())

            for operation in self.calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            *two_numbers
                        ),
                        self.calculator_tests[operation]
                    )

            self.assertEqual(
                src.calculator.add(
                    two_numbers[0],
                    two_numbers[1]
                ),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(
                    two_numbers[-2],
                    two_numbers[-1]
                ),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(
                    two_numbers[1],
                    two_numbers[-1]
                ),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(
                    two_numbers[-2],
                    two_numbers[0]
                ),
                self.random_first_number-self.random_first_number
            )

        def test_calculator_w_dictionary_items(self):

----

* I comment out ``self.arithmetic_tests`` in the `setUp method`_ to see if there are any tests that still use it

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 20-37

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

            x = self.random_first_number
            y = self.random_second_number

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            self.calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': division_result
            }

            # self.arithmetic_tests = {
            #     'addition': {
            #         'function': src.calculator.add,
            #         'expectation': x+y,
            #     },
            #     'subtraction': {
            #         'function': src.calculator.subtract,
            #         'expectation': x-y,
            #     },
            #     'division': {
            #         'function': src.calculator.divide,
            #         'expectation': division_result,
            #     },
            #     'multiplication': {
            #         'function': src.calculator.multiply,
            #         'expectation': x*y,
            #     }
            # }

        def test_calculator_w_list_items(self):

  the tests are still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

            x = self.random_first_number
            y = self.random_second_number

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            self.calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                'divide': division_result
            }

        def test_calculator_w_list_items(self):

----

* I make a :ref:`function<what is a function?>` for the :ref:`division result<test_division>` because I can

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-7

    class TestCalculator(unittest.TestCase):

        def get_division_result(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return 'brmph?! I cannot divide by 0. Try again...'

        def setUp(self):

* I use the new :ref:`function<what is a function?>` in ``self.calculator_tests``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines:

            self.calculator_tests = {
                'add': x+y,
                'subtract': x-y,
                'multiply': x*y,
                # 'divide': division_result
                'divide': self.get_division_result(x, y)
            }

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCalculator.get_division_result() takes 2 positional arguments but 3 were given

  I forgot to make ``get_division_result`` a staticmethod_ since it does not do anything with the rest of the :ref:`class<what is a class?>`

* I :ref:`wrap<what is a decorator function?>` ``get_division_result`` with the `staticmethod decorator`_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    class TestCalculator(unittest.TestCase):

        @staticmethod
        def get_division_result(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return 'brmph?! I cannot divide by 0. Try again...'

        def setUp(self):

  the test passes

* I remove the commented line and the :ref:`exception handler<how to use try...except...else>` from the `setUp method`_

  .. code-block:: python
    :lineno-start: 19

    def setUp(self):
        self.random_first_number = a_random_number()
        self.random_second_number = a_random_number()

        x = self.random_first_number
        y = self.random_second_number

        self.calculator_tests = {
            'add': x+y,
            'subtract': x-y,
            'multiply': x*y,
            'divide': self.get_division_result(x, y)
        }

    def test_calculator_w_list_items(self):

all the tests are passing and I feel like magic

----

*********************************************************************************
test calculator tests again
*********************************************************************************

I want to write the solution that will make all the tests in ``test_calculator.py`` pass without looking at them

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
* I open ``calculator.py`` from the ``src`` folder in the :ref:`editor<2 editors>`
* then I delete everything in ``calculator.py``, the terminal_ shows 3 passing tests and :ref:`AttributeError<what causes AttributeError?>` for 70 failing tests, I start with the last one

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'add' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I point ``add`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add = None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change it to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

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

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() got an unexpected keyword argument 'first_input'

* I add a name to the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def divide(x, y, first_input):
        return x / y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() missing 1 required positional argument: 'first_input'

* I add a default argument to make it a choice

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def divide(x, y, first_input=None):
        return x / y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() got an unexpected keyword argument 'second_input'

* I add ``second_input`` with a default value to the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def divide(x, y, first_input=None, second_input=None):
        return x / y

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() missing 2 required positional arguments: 'x' and 'y'

* the test must be calling :ref:`divide<test_division>` with :ref:`positional arguments<test_functions_w_positional_arguments>` in some cases and with :ref:`keyword arguments<test_functions_w_keyword_arguments>` in others. My solution does not work, I remove ``x`` and ``y`` from the parentheses

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def divide(first_input=None, second_input=None):
        return x / y

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'x' is not defined

* I change the names in the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def divide(first_input=None, second_input=None):
        return first_input / second_input

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: divide() got an unexpected keyword argument 'first_input'

* I use the ``Rename Symbol`` feature to change the name

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

* I add tuple_ to the `isinstance built-in function`_ in the :ref:`if statement<if statements>` of the ``add`` :ref:`function<what is a function?>`

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

    SUBFAILED(i=True) ...  - AssertionError: TUV.VWXYZABCDEFGHI != 'brmph?! Numbers on...
    SUBFAILED(i=False) ... - AssertionError: JKL.MNOPQRSTUVWXYZ != 'brmph?! Numbers on...

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

* I add :ref:`None<what is None?>` to the call to the `isinstance built-in function`_ in the :ref:`if statements` of the :ref:`functions<what is a function?>`

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

  that change made things worse. I cannot use :ref:`None<what is None?>` in the `isinstance built-in function`_

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
=================================================================================

----

* I add a :ref:`decorator function<what is a decorator function?>` to remove the repetition of the :ref:`if statements` because they are all the same

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

* I use the new :ref:`function<what is a function?>` to :ref:`wrap<what is a decorator function?>` the ``add`` :ref:`function<what is a function?>`

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
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line, the terminal_ shows

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