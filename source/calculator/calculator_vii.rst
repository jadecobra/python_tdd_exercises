.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

#################################################################################
how to make a calculator 7
#################################################################################

I want to test the :ref:`calculator<how to make a calculator>` with a :ref:`dictionary<what is a dictionary?>`

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
    collected 7 items

    tests/test_calculator.py .......                              [100%]

    ======================== 7 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_w_dictionary_items
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 52-56, 58-64

      def test_calculator_w_list_items(self):
          two_numbers = [
              self.random_first_number,
              self.random_second_number
          ]

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
          self.assertEqual(
              src.calculator.add(*two_numbers),
              self.random_first_number+self.random_second_number
          )
          self.assertEqual(
              src.calculator.divide(*two_numbers),
              self.random_first_number/self.random_second_number
          )
          self.assertEqual(
              src.calculator.multiply(*two_numbers),
              self.random_first_number*self.random_second_number
          )
          self.assertEqual(
              src.calculator.subtract(*two_numbers),
              self.random_first_number-self.random_second_number
          )

      def test_calculator_w_dictionary_items(self):
          two_numbers = {
              'x': self.random_first_number,
              'y': self.random_second_number,
          }

          self.assertEqual(
              src.calculator.add(
                  two_numbers['x'],
                  two_numbers['y']
              ),
              self.random_first_number+self.random_first_number
          )

      def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: ABC.DEFGHIJKLMNOPQ != RST.UVWXYZABCDEFG

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to the right calculation

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 6

          self.assertEqual(
              src.calculator.add(
                  two_numbers['x'],
                  two_numbers['y']
              ),
              self.random_first_number+self.random_second_number
          )

the test passes. ``two_numbers`` is a :ref:`dictionary<what is a dictionary?>` with two :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`

- ``'x': self.random_first_number``
- ``'y': self.random_second_number``

this means

- ``two_numbers['x']`` is ``self.random_first_number``
- ``two_numbers['y']`` is ``self.random_second_number``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 8-14

            self.assertEqual(
                src.calculator.add(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: D.EFGHIJKLMNOPQRST != UVWXY.ZABCDEFGHIJ

* I change the calculation to :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 6

            self.assertEqual(
                src.calculator.divide(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 8-14

            self.assertEqual(
                src.calculator.divide(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['y'],
                    two_numbers['y']
                ),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: EFGHIJ.KLMNOPQRSTU != VWXYZ.ABCDEFGHIJKL

* I change the expectation to use the correct :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 6

            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['y'],
                    two_numbers['y']
                ),
                self.random_second_number*self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 8-14

            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['y'],
                    two_numbers['y']
                ),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['x'],
                    two_numbers['x'],
                ),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 != FGH.IJKLMNOPQRSTU

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 33

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'first_input': self.random_first_number,
                'second_input': self.random_second_number,
            }

            self.assertEqual(
                src.calculator.add(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['y'],
                    two_numbers['y']
                ),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['x'],
                    two_numbers['x'],
                ),
                self.random_first_number-self.random_first_number
            )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the test passes

----

*********************************************************************************
test calculator with ** expression
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I use ``**`` like I did for the :ref:`keyword arguments<test_functions_w_keyword_arguments>` in :ref:`test_functions_w_unknown_arguments`

.. code-block:: python
  :lineno-start: 136
  :emphasize-lines: 8-11

          self.assertEqual(
              src.calculator.subtract(
                  two_numbers['x'],
                  two_numbers['x'],
              ),
              self.random_first_number-self.random_first_number
          )
          self.assertEqual(
              src.calculator.add(**two_numbers),
              self.random_first_number-self.random_second_number
          )

the terminal_ shows :ref:`TypeError`

.. code-block:: python

  TypeError: numbers_only.<locals>.wrapper() got an unexpected keyword argument 'x'

the names of the :ref:`keys<test_keys_of_a_dictionary>` in the ``two_numbers`` :ref:`dictionary<what is a dictionary?>` must be the same as the names of the arguments the :ref:`calculator functions<how to make a calculator>` receive - ``first_input`` and ``second_input`` not ``x`` and ``y``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``x`` and ``y`` to ``first_input`` and ``second_input`` in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3-6

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                # 'x': self.random_first_number,
                'first_input': self.random_first_number,
                # 'y': self.random_second_number,
                'second_input': self.random_second_number,
            }

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: 'x'

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 214
    :emphasize-lines: 6
    :emphasize-text: KeyError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # KeyError

* I remove the comments to put ``x`` and ``y`` back as :ref:`keys<test_keys_of_a_dictionary>` in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3, 5

        def test_calculator_w_dictionary_items(self):
            two_numbers = {
                'x': self.random_first_number,
                'first_input': self.random_first_number,
                'y': self.random_second_number,
                'second_input': self.random_second_number,
            }

            self.assertEqual(
                src.calculator.add(
                    two_numbers['x'],
                    two_numbers['y']
                ),
                self.random_first_number+self.random_second_number
            )

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: numbers_only.<locals>.decorator() got an unexpected keyword argument 'x'

  the same :ref:`Exception<errors>` I had before I added the :ref:`keys<test_keys_of_a_dictionary>` to the :ref:`dictionary<what is a dictionary?>`

* I change ``two_numbers['x']`` to ``two_numbers['first_input']`` to use the new :ref:`keys<test_keys_of_a_dictionary>` in the :ref:`assertions<What is an assertion?>` for :ref:`addition<test_addition>`

  .. code-block:: python
    :lineno-start: 117

            self.assertEqual(
                src.calculator.add(
                    # two_numbers['x'],
                    two_numbers['first_input'],
                    two_numbers['y']
                ),
                self.random_first_number+self.random_second_number
            )

  .. code-block:: python

    TypeError: numbers_only.<locals>.decorator() got an unexpected keyword argument 'x'

  the same :ref:`Exception<errors>` I had before I added the :ref:`keys<test_keys_of_a_dictionary>` to the :ref:`dictionary<what is a dictionary?>`

* I comment out the :ref:`assertion<what is an assertion?>` with ``**two_numbers``

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 8-11

            self.assertEqual(
                src.calculator.subtract(
                    two_numbers['x'],
                    two_numbers['x'],
                ),
                self.random_first_number-self.random_first_number
            )
            # self.assertEqual(
            #     src.calculator.add(**two_numbers),
            #     self.random_first_number-self.random_second_number
            # )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the test is green again

* I use ``two_numbers['second_input']`` for ``two_numbers['y']``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 5-6

            self.assertEqual(
                src.calculator.add(
                    # two_numbers['x'],
                    two_numbers['first_input'],
                    # two_numbers['y']
                    two_numbers['second_input']
                ),
                self.random_first_number+self.random_second_number
            )

  the test is still green

* I remove the commented lines then make the same change for :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 10-13

            self.assertEqual(
                src.calculator.add(
                    two_numbers['first_input'],
                    two_numbers['second_input']
                ),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(
                    # two_numbers['x'],
                    two_numbers['first_input'],
                    # two_numbers['y']
                    two_numbers['second_input']
                ),
                self.random_first_number/self.random_second_number
            )

  still green

* I do the same thing for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 10-13

            self.assertEqual(
                src.calculator.divide(
                    two_numbers['first_input'],
                    two_numbers['second_input']
                ),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(
                    # two_numbers['y'],
                    two_numbers['second_input'],
                    # two_numbers['y']
                    two_numbers['second_input']
                ),
                self.random_second_number*self.random_second_number
            )

  green

* I do it in the :ref:`assertions<what is an assertion?>` for the :ref:`subtract function<test_subtraction>`

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 10-13

            self.assertEqual(
                src.calculator.multiply(
                    two_numbers['second_input'],
                    two_numbers['second_input']
                ),
                self.random_second_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(
                    # two_numbers['x'],
                    two_numbers['first_input'],
                    # two_numbers['x'],
                    two_numbers['first_input']
                ),
                self.random_first_number-self.random_first_number
            )

  still green

* I remove the ``x`` and ``y`` :ref:`keys<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 109

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
            # self.assertEqual(
            #     src.calculator.add(**two_numbers),
            #     self.random_first_number-self.random_second_number
            # )

  the tests are still green

* I remove the comments from the :ref:`assertion<what is an assertion?>` with ``**two_numbers``

  .. code-block:: python
    :lineno-start: 143

            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number-self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: VWX.YZABCDEFGHIJK != LMN.OPQRSTUVWXYZABC

* I change the calculation in the :ref:`assertion<what is an assertion?>` to :ref:`addition<test_addition>`

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(**two_numbers),
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
    :lineno-start: 143
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number*self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: H.IJKLMNOPQRSTUVWX != YZABCD.EFGHIJKLMNO

* I change the calculation to use :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the :ref:`multiply function<test_multiplication>`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number/self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: IJKLMN.OPQRSTUVWX != Y.ZABCDEFGHIJKLMNOP

* I change the calculation to :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )

  the test passes

* I add the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(**two_numbers),
                self.random_first_number+self.random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: JKL.MNOPQRSTUVWXYZ != ABC.DEFGHIJKLMNOP

* I change the expectation

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 49

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
            self.assertEqual(
                src.calculator.add(**two_numbers),
                self.random_first_number+self.random_second_number
            )
            self.assertEqual(
                src.calculator.divide(**two_numbers),
                self.random_first_number/self.random_second_number
            )
            self.assertEqual(
                src.calculator.multiply(**two_numbers),
                self.random_first_number*self.random_second_number
            )
            self.assertEqual(
                src.calculator.subtract(**two_numbers),
                self.random_first_number-self.random_second_number
            )

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):

  the test passes

----

*********************************************************************************
test calculator with dictionary values
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I can use the :ref:`values method of dictionaries<test_values_of_a_dictionary>` to make a :ref:`list<lists>` to test the :ref:`calculator<how to make a calculator>` in :ref:`test_calculator_w_list_items`

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 2-9

      def test_calculator_w_list_items(self):
          # two_numbers = [
          #     self.random_first_number,
          #     self.random_second_number
          # ]
          a_dictionary = {
              'x': self.random_first_number,
              'y': self.random_second_number
          }

          self.assertEqual(
              src.calculator.add(
                  two_numbers[0],
                  two_numbers[1]
              ),
              self.random_first_number+self.random_second_number
          )

the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'two_numbers' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a new :ref:`variable<what is a variable?>` and make a :ref:`list<what is a list?>` from the :ref:`values<test_values_of_a_dictionary>` of the :ref:`dictionary<what is a dictionary?>`

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 10

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
          self.assertEqual(
              src.calculator.add(*two_numbers),
              self.random_first_number+self.random_second_number
          )
          self.assertEqual(
              src.calculator.divide(*two_numbers),
              self.random_first_number/self.random_second_number
          )
          self.assertEqual(
              src.calculator.multiply(*two_numbers),
              self.random_first_number*self.random_second_number
          )
          self.assertEqual(
              src.calculator.subtract(*two_numbers),
              self.random_first_number-self.random_second_number
          )

      def test_calculator_w_dictionary_items(self):

the test is green again

----

*********************************************************************************
test_calculator_w_for_loops_and_dictionaries
*********************************************************************************

I can use a :ref:`dictionary<what is a dictionary?>` with a :ref:`for loop<what is a for loop?>` in :ref:`test_calculator_sends_message_when_input_is_not_a_number`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test with a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 54-60

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'brmph?! Numbers only. Try again...'

            [
                self.assertEqual(
                    src.calculator.add(data_type, a_random_number()),
                    error_message
                ) for data_type in (
                    None,
                    True, False,
                    str(), 'text',
                    tuple(), (0, 1, 2, 'n'),
                    list(), [0, 1, 2, 'n'],
                    set(), {0, 1, 2, 'n'},
                    dict(), {'key': 'value'},
                )
            ]

            for data_type in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                with self.subTest(data_type=data_type):
                    self.assertEqual(
                        src.calculator.add(
                            data_type, a_random_number()
                        ),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.divide(
                            data_type, a_random_number()
                        ),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.multiply(
                            data_type, a_random_number()
                        ),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.subtract(
                            data_type, a_random_number()
                        ),
                        error_message
                    )

        def test_calculator_w_for_loops_and_dictionaries(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }


    # Exceptions seen

  ``arithmetic`` is a :ref:`dictionary<what is a dictionary?>` with the names of the Arithmetic_ operations as :ref:`keys<test_keys_of_a_dictionary>`, this means

  .. code-block:: python

    arithmetic['addition'] is src.calculator.add
    arithmetic['subtract'] is src.calculator.subtract
    arithmetic['multiplication'] is src.calculator.multiply
    arithmetic['division'] is src.calculator.divide

  it also means that

  .. code-block:: python

    arithmetic['addition'](x, y) is src.calculator.add(x, y)
    arithmetic['subtract'](x, y) is src.calculator.subtract(x, y)
    arithmetic['multiplication'](x, y) is src.calculator.multiply(x, y)
    arithmetic['division'](x, y) is src.calculator.divide(x, y)

* I add :ref:`for loops<what is a for loop?>` with the `subTest method`_

  .. code-block:: python
    :lineno-start: 230
    :emphasize-lines: 9-28

        def test_calculator_w_for_loops_and_dictionaries(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                for operation in arithmetic:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            arithmetic[operation](
                                bad_input, a_random_number()
                            ),
                            'BOOM!!!'
                        )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='addition', bad_input=None) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='subtraction', bad_input=None) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='multiplication', bad_input=None) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='division', bad_input=None) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    ...
    SUBFAILED(operation='addition', bad_input={'key': 'value'}) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='subtraction', bad_input={'key': 'value'}) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='multiplication', bad_input={'key': 'value'}) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    SUBFAILED(operation='division', bad_input={'key': 'value'}) ... - AssertionError: 'brmph?! Numbers only. Try again...' != 'BOOM!!!'
    =================== 52 failed, 9 passed in R.STs ===================

  The second :ref:`for loop<what is a for loop?>` goes over the :ref:`keys<test_keys_of_a_dictionary>` of the :ref:`dictionary<what is a dictionary?>` and runs 4 tests for every bad input in the ``bad_inputs`` tuple_. The two :ref:`for loops<what is a for loop?>` together go every combination of operations and bad inputs

  .. code-block:: python

    (addition, None)
    (subtraction, None)
    (multiplication, None)
    (division, None)
    ...
    (addition, tuple())
    (subtraction, tuple())
    (multiplication, tuple())
    (division, tuple())
    ...
    (addition, {'key': 'value'})
    (subtraction, {'key': 'value'})
    (multiplication, {'key': 'value'})
    (division, {'key': 'value'})

  this means I do not have to write 52 tests

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation to the error message

.. code-block:: python
  :lineno-start: 252
  :emphasize-lines: 5

                  self.assertEqual(
                      arithmetic[operation](
                          bad_input, a_random_number()
                      ),
                      'brmph?! Numbers only. Try again...'
                  )

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove :ref:`test_calculator_sends_message_when_input_is_not_a_number` because :ref:`test_calculator_sends_message_when_input_is_not_a_number` covers all its :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 165

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

        def test_calculator_w_for_loops_and_dictionaries(self):

* I change the name of :ref:`test_calculator_w_for_loops_and_dictionaries` to :ref:`test_calculator_sends_message_when_input_is_not_a_number` to say what it does

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 1

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                for operation in arithmetic:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            arithmetic[operation](
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )


    # Exceptions seen

  this solution is not as easy to read as what was there before. :ref:`Is there a better way?<test_calculator_functions>`

----

*********************************************************************************
test_calculator_functions
*********************************************************************************

I want to use a :ref:`dictionary<what is a dictionary?>` to write one test that covers all the :ref:`4 arithmetic functions: addition, subtraction, division and multiplication<how to make a calculator>` and check their results are correct

----

=================================================================================
:green:`RED`: make it pass
=================================================================================

----

* I add a new test

  .. code-block:: python
    :lineno-start: 177
    :emphasize-lines: 30-36, 38-46

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                for operation in arithmetic:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            arithmetic[operation](
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the 4 arithmetic operations

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - AssertionError: QRS.TUVWXYZABCDEF != 'BOOM!!!'
    SUBFAILED(operation='subtraction') ...    - AssertionError: GHI.JKLMNOPQRSTUVWX != 'BOOM!!!'
    SUBFAILED(operation='division') ...       - AssertionError: Y.ABCDEFGHIJKLMNOP != 'BOOM!!!'
    SUBFAILED(operation='multiplication') ... - AssertionError: QRSTUV.WXYZABCDEFG != 'BOOM!!!'

  how do I add the results?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`dictionary<what is a dictionary?>` for the calculations of each operation

  .. code-block:: python
    :lineno-start: 206
    :emphasize-lines: 9-22

        def test_calculator_functions(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'division': src.calculator.divide,
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

* I use the new :ref:`dictionary<what is a dictionary?>` for the calculation in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 229
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

This test goes through every operation in the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` then calls the :ref:`function<what is a function?>` that is its :ref:`value<test_values_of_a_dictionary>` with ``self.random_first_number`` and ``self.random_second_number`` as input, and checks if the result is the :ref:`value<test_values_of_a_dictionary>` for the :ref:`operation key<test_keys_of_a_dictionary>` in the ``expectations`` :ref:`dictionary<what is a dictionary?>`. I think of it as

.. code-block:: python

  self.assertEqual(
      arithmetic[operation](x, y),
      expectations[operation]
  )

- ``operation`` can be ``addition``, ``subtraction``, ``multiplication`` or ``division``
- in this case ``x`` is ``self.first_random_number``
- in this case ``y`` is ``self.second_random_number``

this means all these statements are the same

* for :ref:`addition<test_addition>`

  .. code-block:: python

    arithmetic['addition'](x, y)
    src.calculator.add(x, y)
    expectations['addition']
    x + y

* for :ref:`subtraction<test_subtraction>`

  .. code-block:: python

    arithmetic['subtraction'](x, y)
    src.calculator.add(x, y)
    expectations['subtraction']
    x - y

* for :ref:`multiplication<test_multiplication>`

  .. code-block:: python

    arithmetic['multiplication'](x, y)
    src.calculator.add(x, y)
    expectations['multiplication']
    x * y

* for :ref:`division<test_division>`

  .. code-block:: python

    arithmetic['division'](x, y)
    src.calculator.add(x, y)
    expectations['division']
    x / y

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can put the two :ref:`dictionaries<what is a dictionary?>` in this test together because they have the same :ref:`keys<test_keys_of_a_dictionary>`

  .. code-block:: python
    :lineno-start: 214
    :emphasize-lines: 16-35

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

            x = self.random_first_number
            y = self.random_second_number
            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': x+y,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': x-y,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': x/y,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': x*y,
                },
            }

            for operation in arithmetic:

* I add a new :ref:`assertion<what is an assertion?>` in a :ref:`for loop<what is a for loop?>` with the `subTest method`_

  .. code-block:: python
    :lineno-start: 250
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
                        arithmetic_tests[operation]['function'](x, y),
                        'BOOM!!!'
                    )


    # Exceptions seen

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`:

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - AssertionError: HIJ.KLMNOPQRSTUVW != 'BOOM!!!'
    SUBFAILED(operation='subtraction') ...    - AssertionError: XYZA.BCDEFGHIJKLMN != 'BOOM!!!'
    SUBFAILED(operation='division') ...       - AssertionError: NO.PQRSTUVWXYZABCDE != 'BOOM!!!'
    SUBFAILED(operation='multiplication') ... - AssertionError: FGHIJKLM.NOPQRSTUVW != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 260
    :emphasize-lines: 5

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](x, y),
                        arithmetic_tests[operation]['expectation']
                    )

  the test passes

* I remove the other :ref:`dictionaries<what is a dictionary?>` and :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 206

        def test_calculator_functions(self):
            x = self.random_first_number
            y = self.random_second_number
            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': x+y,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': x-y,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': x/y,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': x*y,
                },
            }

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](x, y),
                        arithmetic_tests[operation]['expectation']
                    )


    # Exceptions seen

  much better

----

* I remove :ref:`test_addition`, :ref:`test_subtraction` and :ref:`test_multiplication`

  .. code-block:: python
    :lineno-start: 10

    class TestCalculator(unittest.TestCase):

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

        def test_division(self):

  I have to handle :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` in :ref:`test_calculator_functions` before I can remove :ref:`test_division`

* I change ``y`` to ``0`` in :ref:`test_calculator_functions`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 2-3

        def test_calculator_functions(self):
            x = self.random_first_number
            # y = self.random_second_number
            y = 0

            arithmetic_tests = {

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: python

    ZeroDivisionError: float division by zero

  good

* I add an :ref:`exception handler<how to use try...except...else>` to make a :ref:`variable<what is a variable?>` for the result of :ref:`division<test_division>`

  .. code-block:: python
    :lineno-start: 179

        def test_calculator_functions(self):
            x = self.random_first_number
            # y = self.random_second_number
            y = 0

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'BOOM!!!'

            arithmetic_tests = {

  here is what the :ref:`exception handler<how to use try...except...else>` does

  .. code-block:: python

    try:
        division_result = x / y

  try to point ``division_result`` to the result of dividing ``x`` by ``y``

  .. code-block:: python

    except ZeroDivisionError:
        division_result = 'BOOM!!!'

  if :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` is raised when trying to divide ``x`` by ``y``, point ``division_result`` to ``'BOOM!!!'``

* I use ``division_result`` in the ``arithmetic_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 189
    :emphasize-lines: 12-13

            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': x+y,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': x-y,
                },
                'division': {
                    'function': src.calculator.divide,
                    # 'expectation': x/y,
                    'expectation': division_result,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': x*y,
                },
            }

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'brmph?! I cannot divide by 0. Try again...' != 'BOOM!!!'

* I change ``'BOOM!!!'`` to the error message

  .. code-block:: python
    :lineno-start: 184
    :emphasize-lines: 3

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

  the test passes. Progress

* I change ``y`` back to ``self.random_second_number``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 3

        def test_calculator_functions(self):
            x = self.random_first_number
            y = self.random_second_number

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': x+y,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': x-y,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': division_result,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': x*y,
                },
            }

            for operation in arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](x, y),
                        arithmetic_tests[operation]['expectation']
                    )


    # Exceptions seen

  the test is still green

----

I can put the ``arithmetic_tests`` :ref:`dictionary<what is a dictionary?>` from :ref:`test_calculator_functions` and the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` from :ref:`test_calculator_sends_message_when_input_is_not_a_number` together because they have the same :ref:`keys<test_keys_of_a_dictionary>`.

* I add the :ref:`variables<what is a variable?>` from :ref:`test_calculator_functions` to the `setUp method`_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5-6, 8-11, 13-30

        def setUp(self):
            self.random_first_number = a_random_number()
            self.random_second_number = a_random_number()

            x = self.random_first_number
            y = self.random_second_number

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            self.arithmetic_tests = {
                'addition': {
                    'function': src.calculator.add,
                    'expectation': x+y,
                },
                'subtraction': {
                    'function': src.calculator.subtract,
                    'expectation': x-y,
                },
                'division': {
                    'function': src.calculator.divide,
                    'expectation': division_result,
                },
                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': x*y,
                }
            }

* I use the new :ref:`class attribute<test_attribute_error_w_class_attributes>` in the :ref:`for loop<what is a for loop?>` in :ref:`test_calculator_functions`

  .. code-block:: python
    :lineno-start: 219
    :emphasize-lines: 1-2

            # for operation in arithmetic_tests:
            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        arithmetic_tests[operation]['function'](x, y),
                        arithmetic_tests[operation]['expectation']
                    )

  the test is still green

* I use it in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 222
    :emphasize-lines: 2-3

                    self.assertEqual(
                        # arithmetic_tests[operation]['function'](x, y),
                        self.arithmetic_tests[operation]['function'](
                            x, y
                        ),
                        arithmetic_tests[operation]['expectation']
                    )

  still green

* I use it for the expectation

  .. code-block:: python
    :lineno-start: 222
    :emphasize-lines: 6-7

                    self.assertEqual(
                        # arithmetic_tests[operation]['function'](x, y),
                        self.arithmetic_tests[operation]['function'](
                            x, y
                        ),
                        # arithmetic_tests[operation]['expectation']
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test is still green

* I comment out the ``arithmetic_tests`` :ref:`dictionary<what is a dictionary?>` in :ref:`test_calculator_functions`

  .. code-block:: python
    :lineno-start: 195

            try:
                division_result = x / y
            except ZeroDivisionError:
                division_result = 'brmph?! I cannot divide by 0. Try again...'

            # arithmetic_tests = {
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
            #     },
            # }

            # for operation in arithmetic_tests:

  still green

* I comment out the :ref:`exception handler<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 191

        def test_calculator_functions(self):
            x = self.random_first_number
            y = self.random_second_number

            # try:
            #     division_result = x / y
            # except ZeroDivisionError:
            #     division_result = 'brmph?! I cannot divide by 0. Try again...'

  green

* I comment out the ``x`` and ``y`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 191

        def test_calculator_functions(self):
            # x = self.random_first_number
            # y = self.random_second_number

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - NameError: name 'x' is not defined
    SUBFAILED(operation='subtraction') ...    - NameError: name 'x' is not defined
    SUBFAILED(operation='division') ...       - NameError: name 'x' is not defined
    SUBFAILED(operation='multiplication') ... - NameError: name 'x' is not defined

* I undo the change

  .. code-block:: python
    :lineno-start: 191

        def test_calculator_functions(self):
            x = self.random_first_number
            y = self.random_second_number

  the test is green again

* I change the inputs in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 222
    :emphasize-lines: 4-6

                    self.assertEqual(
                        # arithmetic_tests[operation]['function'](x, y),
                        self.arithmetic_tests[operation]['function'](
                            # x, y
                            self.random_first_number,
                            self.random_second_number
                        ),
                        # arithmetic_tests[operation]['expectation']
                        self.arithmetic_tests[operation]['expectation']
                    )

  the test is still green

* I comment out ``x`` and ``y`` again

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 2-3

        def test_calculator_functions(self):
            # x = self.random_first_number
            # y = self.random_second_number

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 191

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


    # Exceptions seen

  the test is still green

----

* I use the new :ref:`class attribute <test_attribute_error_w_class_attributes>` in the :ref:`for loop<what is a for loop?>` in :ref:`test_calculator_sends_message_when_input_is_not_a_number`

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 18-19

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            arithmetic = {
                'addition': src.calculator.add,
                'subtraction': src.calculator.subtract,
                'multiplication': src.calculator.multiply,
                'division': src.calculator.divide,
            }

            for bad_input in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                # for operation in arithmetic:
                for operation in self.arithmetic_tests:
                    with self.subTest(
                        operation=operation,
                        bad_input=bad_input,
                    ):
                        self.assertEqual(
                            arithmetic[operation](
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

        def test_calculator_functions(self):

  still green

* I use it in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 2-3

                        self.assertEqual(
                            # arithmetic[operation](
                            self.arithmetic_tests[operation]['function'](
                                bad_input, a_random_number()
                            ),
                            'brmph?! Numbers only. Try again...'
                        )

  green

* I remove the commented lines and the ``arithmetic`` :ref:`variable<what is a variable?>` because it is no longer used

  .. code-block:: python
    :lineno-start: 162

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

        def test_calculator_functions(self):

  green around the roses

----

* I add a :ref:`for loop<what is a for loop?>` to use the ``self.arithmetic_tests`` :ref:`dictionary<what is a dictionary?>` in :ref:`test_calculator_raises_type_error_when_given_more_than_two_inputs`

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 4-8

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            not_two_numbers = [0, 1, 2]

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    self.arithmetic_tests[operation]['function'](
                        **not_two_numbers
                    )

            with self.assertRaises(TypeError):
                src.calculator.add(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.divide(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.multiply(*not_two_numbers)
            with self.assertRaises(TypeError):
                src.calculator.subtract(*not_two_numbers)

  the terminal_ shows :ref:`TypeError` for all 4 cases

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - TypeError: src.calculator.numbers_only.<locals>.decorator() argument after ** must be a m...
    SUBFAILED(operation='subtraction') ...    - TypeError: src.calculator.numbers_only.<locals>.decorator() argument after ** must be a m...
    SUBFAILED(operation='division') ...       - TypeError: src.calculator.numbers_only.<locals>.decorator() argument after ** must be a m...
    SUBFAILED(operation='multiplication') ... - TypeError: src.calculator.numbers_only.<locals>.decorator() argument after ** must be a m...

  lovely! The test works

* I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 3-6

            for operation in self.arithmetic_tests:
                with self.subTest(operation=operation):
                    with self.assertRaises(TypeError):
                        self.arithmetic_tests[operation]['function'](
                            **not_two_numbers
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
                            **not_two_numbers
                        )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  the test is still green

* I use the :ref:`list<what is a list?>` for the :ref:`variable<what is a variable?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 2-3

                        self.arithmetic_tests[operation]['function'](
                            # **not_two_numbers
                            [0, 1, 2]
                        )

  still green

* I put the two `with statements`_ together

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 2-7

            for operation in self.arithmetic_tests:
                # with self.subTest(operation=operation):
                #     with self.assertRaises(TypeError):
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](
                        # **not_two_numbers
                        [0, 1, 2]
                    )

  green

* I remove the commented lines and ``not_two_numbers`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 150

        def test_calculator_raises_type_error_when_given_more_than_two_inputs(self):
            for operation in self.arithmetic_tests:
                with (
                    self.subTest(operation=operation),
                    self.assertRaises(TypeError),
                ):
                    self.arithmetic_tests[operation]['function'](
                        [0, 1, 2]
                    )

        def test_calculator_sends_message_when_input_is_not_a_number(self):

  still green

----

* I add a :ref:`for loop<what is a for loop?>` to ``test_calculator_w_list_items``

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the 4 operations

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - AssertionError: YZA.BCDEFGHIJKLMNO != 'BOOM!!!'
    SUBFAILED(operation='subtraction') ...    - AssertionError: PQR.STUVWXYZABCDE != 'BOOM!!!'
    SUBFAILED(operation='division') ...       - AssertionError: F.GHIJKLMNOPQRSTUV != 'BOOM!!!'
    SUBFAILED(operation='multiplication') ... - AssertionError: WXYABC.DEFGHIJKLMN != 'BOOM!!!'

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

* I add a :ref:`for loop<what is a for loop?>` to ``test_calculator_w_dictionary_items``

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the 4 operations

  .. code-block:: python

    SUBFAILED(operation='addition') ...       - AssertionError: OPQ.RSTUVWXYZABCDEF != 'BOOM!!!'
    SUBFAILED(operation='subtraction') ...    - AssertionError: GHI.JKLMNOPQRSTUVWX != 'BOOM!!!'
    SUBFAILED(operation='division') ...       - AssertionError: Y.ZABCDEFGHIJKLMNOP != 'BOOM!!!'
    SUBFAILED(operation='multiplication') ... - AssertionError: -QRSTU.VWXYZABCDEF != 'BOOM!!!'

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

I think it is time to take nap. That was a lot.

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

I added these tests for the :ref:`calculator program<how to make a calculator 5>` with :ref:`dictionaries` which made testing the program easier

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

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
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
* :ref:`what you can do with dictionaries<dictionaries>`

I edited ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` for the last few projects. I want to automate the process so that I can call the program and it does all the steps for me when I give it the name of the project.

:ref:`Would you like to know how to make a Python Test Driven Development environment automatically with variables?<how to make a test driven development environment 3>`

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