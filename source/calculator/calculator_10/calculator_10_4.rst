.. include:: calculator_links.rst

#################################################################################
how to make a calculator 10: part 4
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_streamlit_calculator_4.py
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

* I make a new test file_ for the Streamlit_ website

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_streamlit_calculator.py

* I add streamlit_ to the ``requirements.txt`` file_

  .. code-block:: shell
    :emphasize-lines: 1

    echo "streamlit" >> requirements.txt

  Streamlit_ is a Python_ library that is used for making websites, it is not part of `The Python Standard Library`_

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I use ``pytest-watcher`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 8 items

    tests/test_calculator.py .....                                [ 62%]
    tests/test_calculator_website.py ...                          [100%]

    ======================== 5 passed in X.YZs =========================

----

*********************************************************************************
test_streamlit_calculator_reset
*********************************************************************************

I want the ``C`` and ``AC`` buttons to change the number the Calculator shows back to ``0``

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test

.. code-block:: python
  :lineno-start: 111
  :emphasize-lines: 19-20, 22-27, 29-33

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '963.0258741'
            for number in a_number:
                self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'], a_number
            )

            self.tester.button('+/-').click().run()
            self.assertEqual(
                self.tester.session_state['number'], f'-{a_number}'
            )

            self.tester.button('+/-').click().run()
            self.assertEqual(
                self.tester.session_state['number'], a_number
            )

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )

            self.tester.button('C').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )


    # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'C' != '0'

* ``number = random.choice(numbers)`` picks a random number from ``'123456789'`` (the ``numbers`` :ref:`variable<what is a variable?>`)
* ``self.tester.button(number).click().run()`` presses the random number
* ``self.assertEqual(self.tester.session_state['number'], number)`` checks that the value of the ``number`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_ is the same as the number that was pressed
* ``self.tester.button('C').click().run()`` presses the ``C`` button
* ``self.assertEqual(self.tester.session_state['number'], '0')`` checks that the the ``number`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_ is set back to ``0`` after the ``C`` button is pressed

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    def show_state(display):
        display.write(streamlit.session_state['number'])


    def reset():
        streamlit.session_state['number'] = '0'


    def plus_minus():

* I add the ``on_click`` and ``args`` parameters to the ``C`` button in the ``add_buttons_to_column_2`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def add_buttons_to_column_2(column_2, display):
        column_2.button(
            'C', key='C', width='stretch', on_click=on_click,
            args=[reset, display], type='primary',
        )
        column_2.button(
            '8', key='8', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '8'],
        )
        column_2.button(
            '5', key='5', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '5'],
        )
        column_2.button(
            '2', key='2', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '2'],
        )
        column_2.button(
            '0', key='0', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '0'],
        )


    def add_buttons_to_column_3(column_3, display):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I refresh the browser, click on number buttons and when I click on ``C`` it clears the numbers I type

* I add an :ref:`assertion<what is an assertion?>` for the ``AC`` button in :ref:`test_streamlit_calculator_reset`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 17-22, 24-28

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )

            self.tester.button('C').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )

            number = random.choice(numbers)
            self.tester.button(number).click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                number
            )

            self.tester.button('AC').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0'
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'D' != '0'

* I add the ``on_click`` and ``args`` parameters to the ``AC`` button in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            'AC', key='AC', width='stretch', on_click=on_click,
            args=[reset, display], type='primary',
        )
        column_3.button(
            '9', key='9', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '9'],
        )
        column_3.button(
            '6', key='6', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '6'],
        )
        column_3.button(
            '3', key='3', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '3'],
        )
        column_3.button(
            '.', key='.', width='stretch', on_click=on_click,
            args=[add_decimal, display],
        )


    def add_buttons_to_column_4(column_4):

  the test passes

* I refresh the browser, click on number buttons and when I click on ``AC`` it clears the numbers

On to the arithmetic operations

----

*********************************************************************************
test_streamlit_calculator_operations
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for a calculation in ``test_streamlit_calculator.py``

.. code-block:: python
  :lineno-start: 152
  :emphasize-lines: 7-9, 11-14, 16-19

          self.tester.button('AC').click().run()
          self.assertEqual(
              self.tester.session_state['number'],
              '0'
          )

      def test_streamlit_calculator_operations(self):
          first_number = '1'
          second_number = '2'

          self.tester.button(first_number).click().run()
          self.tester.button('+').click().run()
          self.tester.button(second_number).click().run()
          self.tester.button('=').click().run()

          self.assertEqual(
              self.tester.session_state['number'],
              float(first_number)+float(second_number)
          )


  # Exceptions seen

the terminal_ shows :ref:`KeyError<test_key_error>`

.. code-block:: python

  KeyError: '+'

I forgot that I used ``r'\+'`` as the :ref:`key<test_keys_of_a_dictionary>` for :ref:`addition<test_addition>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the key in the test

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 2
    :emphasize-text: \+

            self.tester.button(first_number).click().run()
            self.tester.button(r'\+').click().run()
            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()

* I add an :ref:`assertion<what is an assertion?>` to check the value of the first number

  .. code-block:: python
    :lineno-start: 162
    :emphasize-lines: 3-6

            self.tester.button(first_number).click().run()
            self.tester.button('\+').click().run()
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "first_number". Did you forget to initialize it? More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I make a :ref:`function<what is a function?>` to add the first number as a :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_ when the ``+`` button is pressed, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-8

    def reset():
        streamlit.session_state['number'] = '0'


    def first_number():
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        reset()


    def plus_minus():

* I add the ``on_click`` and ``args`` parameters to the ``+`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 12-13

    def add_buttons_to_column_4(column_4):
        column_4.button(
            '/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            'X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            r'\-', key=r'\-', width='stretch', type='primary',
        )
        column_4.button(
            r'\+', key=r'\+', width='stretch', on_click=on_click,
            args=[first_number], type='primary',
        )
        column_4.button(
            '=', key='=', width='stretch', type='primary',
        )

  the terminal_ shows :ref:`KeyError<test_key_error>` again and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: on_click() missing 1 required positional argument: 'display'

* I add ``display`` to the ``args`` :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 3
    :emphasize-text: display

        column_4.button(
            r'\+', key=r'\+', width='stretch', on_click=on_click,
            args=[first_number, display], type='primary',
        )

  the terminal_ shows :ref:`KeyError<test_key_error>`

* I add ``display`` as a :ref:`positional argument<test_functions_w_positional_arguments>` of the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 116
    :emphasize-lines: 1

    def add_buttons_to_column_4(column_4, display):

  the terminal_ shows :ref:`AssertionError<test_key_error>` for more tests

* I add ``display`` in the call to the ``add_buttons_to_column_4`` :ref:`function<what is a function?>` from the ``add_buttons`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 8

    def add_buttons():
        display = streamlit.container(border=True)
        column_1, column_2, column_3, operations = streamlit.columns(4)

        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations, display)


    def main():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != 3.0

* I add an :ref:`assertion<what is an assertion?>` for the second number after the ``=`` button is pressed, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 14-17

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            self.tester.button(first_number).click().run()
            self.tester.button('\+').click().run()
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                float(first_number)+float(second_number)
            )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "second_number". Did you forget to initialize it? More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I make a new :ref:`function<what is a function?>` for the result of the calculation, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7-10

    def first_number():
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        reset()


    def calculate():
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        reset()


    def plus_minus():

* I add the ``on_click`` and ``args`` parameters to the ``=`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 16-17

    def add_buttons_to_column_4(column_4, display):
        column_4.button(
            '/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            'X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            r'\-', key=r'\-', width='stretch', type='primary',
        )
        column_4.button(
            r'\+', key=r'\+', width='stretch', on_click=on_click,
            args=[first_number, display], type='primary',
        )
        column_4.button(
            '=', key='=', width='stretch', on_click=on_click,
            args=[calculate, display], type='primary',
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0' != 3.0

* I add a calculation to the ``calculate`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 4-7

    def calculate():
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        streamlit.session_state['number'] = (
            streamlit.session_state['first_number']
          + streamlit.session_state['second_number']
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '12' != 3.0

* I change the numbers to floats_

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6
    :emphasize-text: float

    def calculate():
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        streamlit.session_state['number'] = (
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )

  the test passes

* I refresh the browser and try the same calculation

  .. image:: /_static/calculator/streamlit/addition.png
    :width: 600
    :align: left
    :alt: Addition Result

  the result is correct but the number looks different from the others

* when I try another number, the browser shows :ref:`TypeError<what causes TypeError?>`

  .. image:: /_static/calculator/streamlit/type_error_after_addition.png
    :width: 600
    :align: left
    :alt: TypeError after Addition

  the terminal_ for the browser also shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +=: 'float' and 'str'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the result to look the same as the other numbers. I change it to a string_ in the ``calculate`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 1
    :emphasize-lines:
    :emphasize-text: str

    def calculate():
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        streamlit.session_state['number'] = str(
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )


    def plus_minus():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '3.0' != 3.0

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_streamlit_calculator_operations` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 3
    :emphasize-text: str

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

  the test passes

* I refresh the browser and try the calculation again

  .. image:: /_static/calculator/streamlit/addition_string_result.png
    :width: 600
    :align: left
    :alt: Addition with String Result

  I like it, though I do not need the ``.0`` after the ``3``

* I add an :ref:`assertion<what is an assertion?>` for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 176
    :emphasize-lines: 6-13

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            self.tester.button(first_number).click().run()
            self.tester.button('\-').click().run()
            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)-float(second_number))
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '4.0120000000000005' != '-1.0'

  I need to handle the operations

* I add an :ref:`assertion<what is an assertion?>` for an ``'operation'`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 5, 7, 12-15

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = '\+'
            self.tester.button(first_number).click().run()
            self.tester.button(operation).click().run()
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "operation".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I add a :ref:`key<test_keys_of_a_dictionary>` to the ``first_number`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1, 4
    :emphasize-text: operation

    def first_number(operation):
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        streamlit.session_state['operation'] = operation
        reset()

  the terminal_ still shows :ref:`KeyError<test_key_error>`

* I add the value for ``operation`` to the ``args`` :ref:`list<what is a list?>` for the ``r'\+'`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 3

        column_4.button(
            r'\+', key=r'\+', width='stretch', on_click=on_click,
            args=[first_number, display, r'\+'], type='primary',
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '4.0120000000000005' != '-1.0'

* I add an :ref:`assertion<what is an assertion?>` for the ``operation`` :ref:`key<test_keys_of_a_dictionary>` after the ``-`` button is pressed, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 29, 31, 34-37

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = '\+'
            self.tester.button(first_number).click().run()
            self.tester.button(operation).click().run()
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            operation = r'\-'
            self.tester.button('AC').click().run()
            self.tester.button(first_number).click().run()
            self.tester.button(operation).click().run()
            self.tester.button(second_number).click().run()
            self.tester.button('=').click().run()
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )
            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)-float(second_number))
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '\\+' != '\\-'

* I use the operation in a :ref:`dictionary<what is a dictionary?>` in the ``calculate`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1-4

    def calculate():
        arithmetic = {
            r'\+': calculator.add,
        }
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        streamlit.session_state['number'] = str(
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "second_number".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

  the terminal_ also shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'calculator' is not defined. Did you mean: 'calculate'?

* I add an `import statement`_ for the :ref:`calculator module<how to make a calculator>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import calculator
    import streamlit


    def show_state(display):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '\\+' != '\\-'

* I add the ``on_click`` and ``args`` parameters to the ``-`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 2-3

        column_4.button(
            r'\-', key=r'\-', width='stretch', on_click=on_click,
            args=[first_number, display, r'\-'], type='primary',
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '5.01' != '-1.0'

* I add the ``operation`` for :ref:`subtraction<test_subtraction>` to the ``calculate`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 20

    def calculate():
        arithmetic = {
            r'\+': calculator.add,
            r'\-': calculator.subtract,
        }

* I use the operation for the calculation

  .. code-block:: python
    :lineno-start: 20

    def calculate():
        arithmetic = {
            r'\+': calculator.add,
            r'\-': calculator.subtract,
        }
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number

        # streamlit.session_state['number'] = str(
        #     float(streamlit.session_state['first_number'])
        #   + float(streamlit.session_state['second_number'])
        # )
        operation = streamlit.session_state['operation']
        result = arithmetic[operation](
            float(streamlit.session_state['first_number']),
            float(streamlit.session_state['second_number'])
        )
        streamlit.session_state['number'] = str(result)

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 20

    def calculate():
        arithmetic = {
            r'\+': calculator.add,
            r'\-': calculator.subtract,
        }
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number

        operation = streamlit.session_state['operation']
        result = arithmetic[operation](
            float(streamlit.session_state['first_number']),
            float(streamlit.session_state['second_number'])
        )
        streamlit.session_state['number'] = str(result)


    def plus_minus():

----

* I add a dictionary for operations to :ref:`test_streamlit_calculator_operations` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 2-7

        def test_streamlit_calculator_operations(self):
            arithmetic = {
                r'\+': src.calculator.add,
                r'\-': src.calculator.subtract,
                '/': src.calculator.divide,
                'X': src.calculator.multiply,
            }
            first_number = '1'
            second_number = '2'

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import random
    import src.calculator
    import streamlit.testing.v1
    import tests.test_calculator
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

  the test is green again

* I use the :ref:`dictionary<what is a dictionary?>` in a new :ref:`assertion<what is an assertion?>`

  .. code-block:: python




* I use the ``a_random_number`` :ref:`function<what is a function?>` from ``test_calculator.py`` to add randomness to :ref:`test_streamlit_calculator_operations`

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 2-3

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            second_number = '2'

            self.tester.button(first_number).click().run()

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: ABC.DEFGHIJKLMNOP

* I have to change the number to button presses. I change the number to a string_

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 4

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)
            second_number = '2'

  the terminal_ shows :ref:`KeyError<test_key_error>`

    KeyError: 'QRS.TUVWXYZABCDEF'

* I add a :ref:`for loop<what is a for loop?>` for the button presses

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 7-9

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)
            second_number = '2'

            for character in first_number:
                self.tester.button(character).click().run()
            # self.tester.button(first_number).click().run()
            self.tester.button('+').click().run()

  I use :kbd:`ctrl+s` on the keyboard to run the test a few times, sometimes it passes and sometimes it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GH.IJKLMNOPQRSTUVW' != '-GH.IJKLMNOPQRSTUVW'

  there is no button for ``-`` it is ``+/-``

* I add a :ref:`condition<if statements>` to the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 2-3

            for character in first_number:
                if character == '-':
                    character = '+/-'
                self.tester.button(character).click().run()
            self.tester.button('+').click().run()

* I do the same thing with the second number

  .. code-block:: python
    :lineno-start: 181
    :emphasize-lines: 6-8

        def test_streamlit_calculator_operations(self):
            # first_number = '1'
            first_number = tests.test_calculator.a_random_number()
            first_number = str(first_number)

            # second_number = '2'
            second_number = tests.test_calculator.a_random_number()
            second_number = str(second_number)

            for character in first_number:

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

----

----

*********************************************************************************
test_error_messages_in_streamlit
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add

.. code-block:: python
  :lineno-start: 20

      def test_error_messages_in_streamlit(self):
          self.assertEqual(
              src.calculator.divide(10, 0),
              'brmph?! I cannot divide by 0. Try again...'
          )

the test already passes (thanks to chapters 3–4).

----

*********************************************************************************
how to run the app
*********************************************************************************

In the terminal I type:

.. code-block:: shell
  :emphasize-lines: 1

  uv run streamlit run src/streamlit_app.py

A browser window opens automatically with my beautiful calculator!

----

*********************************************************************************
close the project
*********************************************************************************

* I close all files
* I click in the terminal_, then use :kbd:`q` to leave the tests
* I `change directory`_ to the parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I now have **three** different versions of the same calculator:

* Pure Python (chapters 1–8)
* Flask website (chapter 9)
* **Streamlit web app** (chapter 10) — the fastest and most beautiful version

The core calculator code never changed. All my tests still protect it.
This is the real power of Test-Driven Development.

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 10: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You have completed an amazing journey from pure functions to real web applications!

You now know how to:

* Build programs with Test-Driven Development
* Turn them into Flask websites
* Turn them into beautiful Streamlit apps

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