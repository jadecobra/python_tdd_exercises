.. include:: calculator_links.rst

#################################################################################
how to make a calculator 10: part 4
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_streamlit_calculator_4.py
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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 16 items

    tests/test_calculator.py .....                                [ 31%]
    tests/test_calculator_website.py ...                          [ 50%]
    tests/test_streamlit_calculator.py ........                   [100%]

    ======================== 16 passed in X.YZs =========================

* I open another terminal_ then use uv_ in the ``calculator`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    uv run streamlit run src/streamlit_calculator.py

  the terminal_ shows

  .. code-block:: shell

    Collecting usage statistics.
    To deactivate, set browser.gatherUsageStats to false.


      You can now view your Streamlit app in your browser.

      Local URL: http://localhost:8501
      Network URL: http://ABC.DEF.GHI.JKL:8501
      External URL: http://MNO.PQR.STU.VWX:8501

  I use :kbd:`ctrl/option` on the keyboard and click on ``http://localhost:8501`` with the mouse to open the browser and it shows

  .. image:: /_static/calculator/streamlit/primary_buttons.png
    :width: 600
    :align: left
    :alt: Calculator Streamlit Primary Buttons

----

*********************************************************************************
test_streamlit_calculator_reset
*********************************************************************************

I want the ``C`` and ``AC`` buttons to change the number the Calculator shows back to ``0``, they should reset the calculator.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I hold :kbd:`ctrl/command` on the keyboard and click on ``tests/test_streamlit_calculator.py`` with the mouse to open it in the :ref:`editor<2 editors>`

* I add a test to ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 19-20, 22-26, 28-31

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '963.0258741'
            for key in a_number:
                self.press_button(key)
            self.assertEqual(
                self.tester.session_state['number'], a_number
            )

            self.press_button('+/-')
            self.assertEqual(
                self.tester.session_state['number'], f'-{a_number}'
            )

            self.press_button('+/-')
            self.assertEqual(
                self.tester.session_state['number'], a_number
            )

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            number = random.choice(numbers)
            self.press_button(number)
            self.assertEqual(
                self.tester.session_state['number'], number
            )

            self.press_button('C')
            self.assertEqual(
                self.tester.session_state['number'], '0'
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X' != '0'

  - where ``'X'`` is a random number
  - ``number = random.choice(numbers)`` picks a random number from ``'123456789'`` (the ``numbers`` :ref:`variable<what is a variable?>`)
  - ``self.press_button(number)`` presses the random number
  - ``self.assertEqual(self.tester.session_state['number'], number)`` checks that the value of the ``number`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_ is the same as the number that was pressed
  - ``self.press_button('C')`` presses the ``C`` button
  - ``self.assertEqual(self.tester.session_state['number'], '0')`` checks that the the ``number`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_ is set back to ``0`` after the ``C`` button is pressed

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    def show_number(display):
        display.write(streamlit.session_state['number'])


    def reset_number():
        streamlit.session_state['number'] = 0


    def plus_minus():

* I add the ``on_click`` and ``args`` parameters to the ``C`` button in the ``add_buttons_to_column_2`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def add_buttons_to_column_2(column_2, display):
        column_2.button(
            label='C', key='C', width='stretch', on_click=on_click,
            args=[reset_number, display], type='primary',
        )
        column_2.button(
            label='8', key='8', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '8'],
        )
        column_2.button(
            label='5', key='5', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '5'],
        )
        column_2.button(
            label='2', key='2', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '2'],
        )
        column_2.button(
            label='0', key='0', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '0'],
        )


    def add_buttons_to_column_3(column_3, display):

  the terminal shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 != '0'

  I forgot that all the values have been strings_ so far

* I change ``0`` to ``'0'`` in the ``reset_number`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

    def reset_number():
        streamlit.session_state['number'] = '0'

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I refresh the browser, click on number buttons and when I click on ``C`` it clears the numbers I type

* I add an :ref:`assertion<what is an assertion?>` for the ``AC`` button in :ref:`test_streamlit_calculator_reset` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 15-19, 21-24

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            number = random.choice(numbers)
            self.press_button(number)
            self.assertEqual(
                self.tester.session_state['number'], number
            )

            self.press_button('C')
            self.assertEqual(
                self.tester.session_state['number'], '0'
            )

            number = random.choice(numbers)
            self.press_button(number)
            self.assertEqual(
                self.tester.session_state['number'], number
            )

            self.press_button('AC')
            self.assertEqual(
                self.tester.session_state['number'], '0'
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X' != '0'

* I add the ``on_click`` and ``args`` parameters to the ``AC`` button in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

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

* I add a :ref:`for loop<what is a for loop?>` to :ref:`test_streamlit_calculator_reset` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 4-5, 7-12,14-18

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            for key in ('C', 'AC'):
                with self.subTest(key=key):

                    number = random.choice(numbers)
                    self.press_button(number)
                    self.assertEqual(
                        self.tester.session_state['number'],
                        number
                    )

                    self.press_button(key)
                    self.assertEqual(
                        self.tester.session_state['number'],
                        'BOOM!!!'
                    )

            number = random.choice(numbers)
            self.press_button(number)
            self.assertEqual(
                self.tester.session_state['number'], number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(key='C') ... - AssertionError: '0' != 'BOOM!!!'
    SUBFAILED(key='AC') ... - AssertionError: '0' != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4

                    self.press_button(key)
                    self.assertEqual(
                        self.tester.session_state['number'],
                        '0'
                    )

  the test passes

* I remove the other statements from :ref:`test_streamlit_calculator_reset`

  .. code-block:: python
    :lineno-start: 132

        def test_streamlit_calculator_reset(self):
            numbers = '123456789'

            for key in ('C', 'AC'):
                with self.subTest(key=key):

                    number = random.choice(numbers)
                    self.press_button(number)
                    self.assertEqual(
                        self.tester.session_state['number'],
                        number
                    )

                    self.press_button(key)
                    self.assertEqual(
                        self.tester.session_state['number'],
                        '0'
                    )


    # Exceptions seen


on to the arithmetic operations

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
  :lineno-start: 145
  :emphasize-lines: 7-9, 11-14, 16-19

                  self.press_button(key)
                  self.assertEqual(
                      self.tester.session_state['number'],
                      '0'
                  )

      def test_streamlit_calculator_operations(self):
          first_number = '1'
          second_number = '2'

          self.press_button(first_number)
          self.press_button('+')
          self.press_button(second_number)
          self.press_button('=')

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
    :lineno-start: 155
    :emphasize-lines: 2
    :emphasize-text: \+

            self.press_button(first_number)
            self.press_button(r'\+')
            self.press_button(second_number)
            self.press_button('=')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ... - AssertionError: '12' != 3.0

* The calculator is putting the two numbers together since they are strings_. I want it to take the numbers separately then add them as numbers not strings_. I add an :ref:`assertion<what is an assertion?>` to check the value of the first number after the ``+`` button is pressed

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 7-10

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            self.press_button(first_number)
            self.press_button(r'\+')
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.press_button(second_number)
            self.press_button('=')

            self.assertEqual(
                self.tester.session_state['number'],
                float(first_number)+float(second_number)
            )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "first_number".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I use the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>` to add a default value for the ``first_number`` :ref:`key<test_keys_of_a_dictionary>` in the ``main`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 4

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', '0')
        streamlit.session_state.setdefault('first_number', '0')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations)


    if __name__ == '__main__':

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0' != '1'

* I make a :ref:`function<what is a function?>` to change the ``first_number`` :ref:`key<test_keys_of_a_dictionary>` of the `session state object`_ when the ``+`` button is pressed

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-8

    def reset_number():
        streamlit.session_state['number'] = '0'


    def first_number():
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        reset_number()


    def plus_minus():

* I add the ``on_click`` and ``args`` parameters to the ``+`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 15-16

    def add_buttons_to_column_4(column_4):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display],
        )


    def main():

  the terminal_ shows :ref:`KeyError<test_key_error>` and :ref:`TypeError<what causes TypeError?>`

* I add ``display`` as a :ref:`positional argument<test_functions_w_positional_arguments>` of the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 1

    def add_buttons_to_column_4(column_4, display):

  the terminal_ shows :ref:`KeyError<test_key_error>` for more sub tests

* I add ``display`` to the call to the ``add_buttons_to_column_4`` :ref:`function<what is a function?>` from the ``main`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 11

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', '0')
        streamlit.session_state.setdefault('first_number', '0')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations, display)


    if __name__ == '__main__':

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != 3.0

  Okay! The calculator is no longer adding the strings_, the error shows only the second number

* I add an :ref:`assertion<what is an assertion?>` for the second number after the ``=`` button is pressed, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 14-17

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            self.press_button(first_number)
            self.press_button(r'\+')
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.press_button(second_number)
            self.press_button('=')
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

    KeyError: 'st.session_state has no key "second_number".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I use the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>` to add a default value for the ``first_number`` :ref:`key<test_keys_of_a_dictionary>` in the ``main`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 5

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', '0')
        streamlit.session_state.setdefault('first_number', '0')
        streamlit.session_state.setdefault('second_number', '0')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations, display)


    if __name__ == '__main__':

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0' != '2'

* I make a new :ref:`function<what is a function?>` for the result of the calculation, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7-10

    def first_number():
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        reset_number()


    def calculate():
        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        reset_number()


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

  awesome! The ``number`` :ref:`key<test_keys_of_a_dictionary>` of the `session state object`_ now resets after the ``+`` and ``=`` buttons are pressed

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


    def plus_minus():

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

  the result is correct but the number looks different from the others I have seen so far

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* when I try another number, the browser and the terminal_ for the application show :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: unsupported operand type(s) for +=: 'float' and 'str'


* I want the result to look the same as the other numbers. I change it to a string_ in the ``calculate`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 4
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

  closer

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_streamlit_calculator_operations` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 169
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
    :lineno-start: 151
    :emphasize-lines: 24-31

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            self.press_button(first_number)
            self.press_button(r'\+')
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            self.press_button(first_number)
            self.press_button(r'\-')
            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)-float(second_number))
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '4.0120000000000005' != '-1.0'

  I need a way to handle the operations

* I add a :ref:`variable<what is a variable?>` then an :ref:`assertion<what is an assertion?>` for an ``'operation'`` :ref:`key<test_keys_of_a_dictionary>` in the `session state object`_

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 5, 7-8, 13-16

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = r'\+'
            self.press_button(first_number)
            # self.press_button(r'\+')
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            self.press_button(first_number)
            self.press_button(r'\-')
            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)-float(second_number))
            )

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "operation".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

* I use the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>` to add a default value for the ``operation`` :ref:`key<test_keys_of_a_dictionary>` in the ``main`` :ref:`function<what is a function?>`, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 146
    :emphasize-lines:

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', '0')
        streamlit.session_state.setdefault('first_number', '0')
        streamlit.session_state.setdefault('second_number', '0')
        streamlit.session_state.setdefault('operation', '=')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations, display)


    if __name__ == '__main__':

  the terminal_ shows :ref:`AssertionError<test_assertion_error>`

  .. code-block:: python

    AssertionError: '=' != '\\+'

* I change the value of the ``operation``:ref:`key<test_keys_of_a_dictionary>` in the ``first_number`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1, 4
    :emphasize-text: operation

    def first_number(operation):
        first_number = streamlit.session_state['number']
        streamlit.session_state['first_number'] = first_number
        streamlit.session_state['operation'] = operation
        reset_number()


    def calculate():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0' != '1'

  I broke the test for the ``'first_number'`` :ref:`key<test_keys_of_a_dictionary>` that was passing before

* I add the value for ``operation`` to the ``args`` :ref:`list<what is a list?>` for the ``r'\+'`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 13

    def add_buttons_to_column_4(column_4, display):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\+'],
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
            on_click=on_click, args=[calculate, display],
        )


    def main():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '4.0120000000000005' != '-1.0'

* I add an :ref:`assertion<what is an assertion?>` for the ``operation`` :ref:`key<test_keys_of_a_dictionary>` after the ``-`` button is pressed, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 30, 32-33, 37-40

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = r'\+'
            self.press_button(first_number)
            # self.press_button(r'\+')
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            operation = r'\-'
            self.press_button(first_number)
            # self.press_button(r'\-')
            self.press_button(operation)
            self.press_button(second_number)
            self.press_button('=')

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

* I add values for the ``on_click`` and ``args`` parameters for the ``r'\-'`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 10

    def add_buttons_to_column_4(column_4, display):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\-'],
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\+'],
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
            on_click=on_click, args=[calculate, display],
        )


    def main():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '5.01' != '-1.0'

  alright! Time to add the calculation for :ref:`subtraction<test_subtraction>`


* I use the operation in a :ref:`dictionary<what is a dictionary?>` in the ``calculate`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-4

    def calculate():
        arithmetic = {
            r'\+': 'add',
        }

        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        streamlit.session_state['number'] = str(
            float(streamlit.session_state['first_number'])
          + float(streamlit.session_state['second_number'])
        )


    def plus_minus():

* I use the ``__getattribute__`` :ref:`method<what is a function?>` to get the :ref:`add function<test_addition>` from the :ref:`calculator module<how to make a calculator>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8-18

    def calculate():
        arithmetic = {
            r'\+': 'add',
        }

        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        # streamlit.session_state['number'] = str(
        #     float(streamlit.session_state['first_number'])
        #   + float(streamlit.session_state['second_number'])
        # )
        operation = arithmetic[streamlit.session_state['operation']]
        first_number = float(streamlit.session_state['first_number'])
        second_number = float(streamlit.session_state['second_number'])
        result = calculator.__getattribute__(operation)(
            first_number, second_number
        )
        streamlit.session_state['number'] = str(result)


    def plus_minus():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != '3.0'

  and :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'calculator' is not defined. Did you mean: 'calculate'?

* I add an `import statement`_ for the :ref:`calculator module<how to make a calculator>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import calculator
    import streamlit


    def show_number(display):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '2' != '-1.0'

  and :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '\\-'

* I add a :ref:`key<test_keys_of_a_dictionary>` for ``r'\-'`` to the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` in the ``calculate`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

    def calculate():
        arithmetic = {
            r'\+': 'add',
            r'\-': 'subtract',
        }

        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        # streamlit.session_state['number'] = str(
        #     float(streamlit.session_state['first_number'])
        #   + float(streamlit.session_state['second_number'])
        # )
        operation = arithmetic[streamlit.session_state['operation']]
        first_number = float(streamlit.session_state['first_number'])
        second_number = float(streamlit.session_state['second_number'])
        result = calculator.__getattribute__(operation)(
            first_number, second_number
        )
        streamlit.session_state['number'] = str(result)


    def plus_minus():

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '1.0099999999999998' != '-1.0'

  the calculation is wrong

* I add an :ref:`assertion<what is an assertion?>` for the value of the first number in the :ref:`subtraction<test_subtraction>` operation in :ref:`test_streamlit_calculator_operations` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 34-37

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = r'\+'
            self.press_button(first_number)
            # self.press_button(r'\+')
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            operation = r'\-'
            self.press_button(first_number)
            # self.press_button(r'\-')
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.press_button(second_number)
            self.press_button('=')

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

    AssertionError: '3.01' != '1'

  ah! the calculation is correct, I have to reset the :ref:`calculator<how to make a calculator>` after it shows the result

* I reset the :ref:`calculator<how to make a calculator>` after the first operation :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 30

    def test_streamlit_calculator_operations(self):
        first_number = '1'
        second_number = '2'

        operation = r'\+'
        self.press_button(first_number)
        # self.press_button(r'\+')
        self.press_button(operation)
        self.assertEqual(
            self.tester.session_state['first_number'],
            first_number
        )
        self.assertEqual(
            self.tester.session_state['operation'],
            operation
        )

        self.press_button(second_number)
        self.press_button('=')
        self.assertEqual(
            self.tester.session_state['second_number'],
            second_number
        )

        self.assertEqual(
            self.tester.session_state['number'],
            str(float(first_number)+float(second_number))
        )

        self.press_button('AC')

        operation = r'\-'
        self.press_button(first_number)
        # self.press_button(r'\-')
        self.press_button(operation)
        self.assertEqual(
            self.tester.session_state['first_number'],
            first_number
        )

        self.press_button(second_number)
        self.press_button('=')

        self.assertEqual(
            self.tester.session_state['operation'],
            operation
        )

        self.assertEqual(
            self.tester.session_state['number'],
            str(float(first_number)-float(second_number))
        )

  the test passes. Wow!

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 151

        def test_streamlit_calculator_operations(self):
            first_number = '1'
            second_number = '2'

            operation = r'\+'
            self.press_button(first_number)
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )
            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.press_button(second_number)
            self.press_button('=')
            self.assertEqual(
                self.tester.session_state['second_number'],
                second_number
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)+float(second_number))
            )

            self.press_button('AC')

            operation = r'\-'
            self.press_button(first_number)
            self.press_button(operation)
            self.assertEqual(
                self.tester.session_state['first_number'],
                first_number
            )

            self.press_button(second_number)
            self.press_button('=')

            self.assertEqual(
                self.tester.session_state['operation'],
                operation
            )

            self.assertEqual(
                self.tester.session_state['number'],
                str(float(first_number)-float(second_number))
            )

  this test is long and will get longer when I add the other two operations

* I make a :ref:`dictionary<what is a dictionary?>` for the operations in :ref:`test_streamlit_calculator_operations`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 2-7

    def test_streamlit_calculator_operations(self):
        arithmetic_operations = {
            r'\+': 'add',
            r'\-': 'subtract',
            'X': 'multiply',
            '/': 'divide'
        }

        first_number = '1'
        second_number = '2'

* I use a :ref:`for loop<what is a for loop?>` with the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 12-15, 17-20

        def test_streamlit_calculator_operations(self):
            arithmetic_operations = {
                r'\+': 'add',
                r'\-': 'subtract',
                'X': 'multiply',
                '/': 'divide'
            }

            first_number = '1'
            second_number = '2'

            for operation in arithmetic_operations:
                with self.subTest(operation=operation):
                    self.press_button(first_number)
                    self.press_button(operation)

                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        'BOOM!!!'
                    )

            operation = r'\+'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='\\+') ... - AssertionError: '1' != 'BOOM!!!'
    SUBFAILED(operation='\\-') ... - AssertionError: '1' != 'BOOM!!!'
    SUBFAILED(operation='X') ... - AssertionError: '1' != 'BOOM!!!'
    SUBFAILED(operation='/') ... - AssertionError: '1' != 'BOOM!!!'
    FAILED ... - AssertionError: '111' != '1'

* I change the expectation

  .. code-block:: python
    :lineno-start: 166
    :emphasize-lines: 3

                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '111' != '1'

* I reset the calculator with the ``AC`` button

  .. code-block:: python
    :lineno-start: 167
    :emphasize-lines: 6

                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

                    self.press_button('AC')

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the operation

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 22-25

        def test_streamlit_calculator_operations(self):
            arithmetic_operations = {
                r'\+': 'add',
                r'\-': 'subtract',
                'X': 'multiply',
                '/': 'divide'
            }

            first_number = '1'
            second_number = '2'

            for operation in arithmetic_operations:
                with self.subTest(operation=operation):
                    self.press_button(first_number)
                    self.press_button(operation)

                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

                    self.assertEqual(
                        self.tester.session_state['operation'],
                        'BOOM!!!'
                    )

                    self.press_button('AC')

            operation = r'\+'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='\\+') ... - AssertionError: '\\+' != 'BOOM!!!'
    SUBFAILED(operation='\\-') ... - AssertionError: '\\-' != 'BOOM!!!'
    SUBFAILED(operation='X') ... - AssertionError: '\\-' != 'BOOM!!!'
    SUBFAILED(operation='/') ... - AssertionError: '\\-' != 'BOOM!!!'
    FAILED ... - AssertionError: '111' != '1'

* I change the expectation

  .. code-block:: python
    :lineno-start: 171
    :emphasize-lines: 3

                    self.assertEqual(
                        self.tester.session_state['operation'],
                        operation
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='X') ... - AssertionError: '\\-' != 'X'
    SUBFAILED(operation='/') ... - AssertionError: '\\-' != '/'
    FAILED ... - AssertionError: '111' != '1'

* I add values for the ``on_click`` and ``args`` parameters to the ``X`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 7

    def add_buttons_to_column_4(column_4, display):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, 'X'],
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\-'],
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\+'],
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
            on_click=on_click, args=[calculate, display],
        )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='/') ... - AssertionError: 'X' != '/'
    FAILED ... - AssertionError: '11' != '1'

* I add values for the ``on_click`` and ``args`` parameters to the ``/`` button in the ``add_buttons_to_column_4`` :ref:`function<what is a function?>`

  .. code-block:: python

    def add_buttons_to_column_4(column_4, display):
        column_4.button(
            label='/', key='/', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, '/'],
        )
        column_4.button(
            label='X', key='X', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, 'X'],
        )
        column_4.button(
            label=r'\-', key=r'\-', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\-'],
        )
        column_4.button(
            label=r'\+', key=r'\+', width='stretch', type='primary',
            on_click=on_click, args=[first_number, display, r'\+'],
        )
        column_4.button(
            label='=', key='=', width='stretch', type='primary',
            on_click=on_click, args=[calculate, display],
        )


    def main():

  the test passes

* I add a button press for the second number and ``=``, then an :ref:`assertion<what is an assertion?>` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 29-32

        def test_streamlit_calculator_operations(self):
            arithmetic_operations = {
                r'\+': 'add',
                r'\-': 'subtract',
                'X': 'multiply',
                '/': 'divide'
            }

            first_number = '1'
            second_number = '2'

            for operation in arithmetic_operations:
                with self.subTest(operation=operation):
                    self.press_button(first_number)
                    self.press_button(operation)
                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

                    self.assertEqual(
                        self.tester.session_state['operation'],
                        operation
                    )

                    self.press_button(second_number)
                    self.press_button('=')

                    self.assertEqual(
                        self.tester.session_state['second_number'],
                        'BOOM!!!'
                    )

                    self.press_button('AC')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='\\+') ... - AssertionError: '2' != 'BOOM!!!'
    SUBFAILED(operation='\\-') ... - AssertionError: '3.01' != '1'
    SUBFAILED(operation='X') ... - AssertionError: '2' != 'BOOM!!!'

  and :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(operation='/') t... - KeyError: '1'
    FAILED ... - KeyError: '1'

* I change the expectation

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 3

                    self.assertEqual(
                        self.tester.session_state['second_number'],
                        second_number
                    )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` and :ref:`KeyError<test_key_error>`

* I add ``X`` to the ``arithmetic`` :ref:`dictionary<what is a dictionary?>` in the ``calculate`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5

    def calculate():
        arithmetic = {
            r'\+': 'add',
            r'\-': 'subtract',
            'X': 'multiply',
        }

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    SUBFAILED(operation='/') ... - KeyError: 'AC'
    FAILED ... - KeyError: '1'

* I add ``/`` to the ``arithmetic`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 6

    def calculate():
        arithmetic = {
            r'\+': 'add',
            r'\-': 'subtract',
            'X': 'multiply',
            '/': 'divide',
        }

        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number
        # streamlit.session_state['number'] = str(
        #     float(streamlit.session_state['first_number'])
        #   + float(streamlit.session_state['second_number'])
        # )
        operation = arithmetic[streamlit.session_state['operation']]
        first_number = float(streamlit.session_state['first_number'])
        second_number = float(streamlit.session_state['second_number'])
        result = calculator.__getattribute__(operation)(
            first_number, second_number
        )
        streamlit.session_state['number'] = str(result)


    def plus_minus():

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the calculation in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 151
    :emphasize-lines: 34-40

        def test_streamlit_calculator_operations(self):
            arithmetic_operations = {
                r'\+': 'add',
                r'\-': 'subtract',
                'X': 'multiply',
                '/': 'divide'
            }

            first_number = '1'
            second_number = '2'

            for operation in arithmetic_operations:
                with self.subTest(operation=operation):
                    self.press_button(first_number)
                    self.press_button(operation)
                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

                    self.assertEqual(
                        self.tester.session_state['operation'],
                        operation
                    )

                    self.press_button(second_number)
                    self.press_button('=')

                    self.assertEqual(
                        self.tester.session_state['second_number'],
                        second_number
                    )

                    function = arithmetic_operations[operation]
                    self.assertEqual(
                        self.tester.session_state['number'],
                        src.calculator.__getattribute__(function)(
                            first_number, second_number
                        )
                    )

                    self.press_button('AC')


  the terminal_ shows :ref:`Exceptions<errors>`

  .. code-block:: python
    :emphasize-lines: NameError

    SUBFAILED(operation='\\+') ... - NameError: name 'src' is not defined
    SUBFAILED(operation='\\-') ... - AssertionError: '3.01' != '1'
    SUBFAILED(operation='X') ... - NameError: name 'src' is not defined
    SUBFAILED(operation='/') ... - AssertionError: '2.01' != '1'

* I add an `import statement`_ at the top of ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :empasize-lines: 2

    import random
    import src.calculator
    import streamlit.testing.v1
    import tests.test_calculator
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='\\+') ... - AssertionError: '3.0' != 'brmph?! Numbers only. Try again...'
    SUBFAILED(operation='\\-') ... - AssertionError: '3.01' != '1'
    SUBFAILED(operation='X') ... - AssertionError: '2.0' != 'brmph?! Numbers only. Try again...'
    SUBFAILED(operation='/') ... - AssertionError: '2.01' != '1'

* I change ``first_number`` and ``second_number`` to floats_ in the calculation in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 5-6

                    function = arithmetic_operations[operation]
                    self.assertEqual(
                        self.tester.session_state['number'],
                        src.calculator.__getattribute__(function)(
                            float(first_number),
                            float(second_number)
                        )
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(operation='\\+') ... - AssertionError: '3.0' != 3.0
    SUBFAILED(operation='\\-') ... - AssertionError: '3.01' != '1'
    SUBFAILED(operation='X') ... - AssertionError: '2.0' != 2.0
    SUBFAILED(operation='/') ... - AssertionError: '2.01' != '1'

* I change the expectation to a string_

  .. code-block:: python
    :emphasize-lines: 4-9

                    function = arithmetic_operations[operation]
                    self.assertEqual(
                        self.tester.session_state['number'],
                        str(
                            src.calculator.__getattribute__(function)(
                                float(first_number),
                                float(second_number)
                            )
                        )
                    )

  the test passes

* I remove the other statements from :ref:`test_streamlit_calculator_operations`

  .. code-block:: python
    :lineno-start: 151

        def test_streamlit_calculator_operations(self):
            arithmetic_operations = {
                r'\+': 'add',
                r'\-': 'subtract',
                'X': 'multiply',
                '/': 'divide'
            }

            first_number = '1'
            second_number = '2'

            for operation in arithmetic_operations:
                with self.subTest(operation=operation):
                    self.press_button(first_number)
                    self.press_button(operation)

                    self.assertEqual(
                        self.tester.session_state['first_number'],
                        first_number
                    )

                    self.assertEqual(
                        self.tester.session_state['operation'],
                        operation
                    )

                    self.press_button(second_number)
                    self.press_button('=')

                    self.assertEqual(
                        self.tester.session_state['second_number'],
                        second_number
                    )

                    function = arithmetic_operations[operation]
                    self.assertEqual(
                        self.tester.session_state['number'],
                        str(
                            src.calculator.__getattribute__(function)(
                                float(first_number),
                                float(second_number)
                            )
                        )
                    )

                    self.press_button('AC')


    # Exceptions seen

* I remove the commented lines from the ``calculate`` :ref:`function<what is a function>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 20

    def calculate():
        arithmetic = {
            r'\+': 'add',
            r'\-': 'subtract',
            'X': 'multiply',
            '/': 'divide',
        }

        second_number = streamlit.session_state['number']
        streamlit.session_state['second_number'] = second_number

        operation = arithmetic[streamlit.session_state['operation']]
        first_number = float(streamlit.session_state['first_number'])
        second_number = float(streamlit.session_state['second_number'])

        result = calculator.__getattribute__(operation)(
            first_number, second_number
        )

        streamlit.session_state['number'] = str(result)


    def plus_minus():

----

All tests are green and when I try calculations, they work. But ... there is a problem - When I press a new number after I get the result, If I do not press ``C`` or ``AC`` to reset the number, it adds the number to the end of the result instead of replacing it

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_streamlit_calculator.py``, ``streamlit_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the first terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I click in the second terminal_, then use :kbd:`ctrl+c` on the keyboard to close the web server. The terminal_ goes back to the command line

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

I made a website using Streamlit_ with a

* :ref:`title<test_streamlit_calculator_title>`
* :ref:`display<test_streamlit_calculator_display>`
* :ref:`buttons<test_streamlit_calculator_columns_and_buttons>`

I used :ref:`while loops<what is a while loop?>` and added tests for

* :ref:`the session state object<test_streamlit_session_state>`
* :ref:`decimals<test_streamlit_calculator_w_decimals>`
* :ref:`backspace<test_streamlit_calculator_w_backspace>`
* :ref:`+/-<test_streamlit_calculator_w_plus_minus>`
* :ref:`resetting with 'C' and 'AC'<test_streamlit_calculator_reset>`
* :ref:`calculator operatiosn<test_streamlit_calculator_operations>`

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 10: part 4: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You have completed an amazing journey from pure functions to a real web application! Celebrate it

You now know how to:

* Build a program with Test-Driven Development
* Turn it into a Flask_ website
* Turn it into a Streamlit_ app

:ref:`Would you like to see how to make a Calculator with a Large Language Model?<calculator 11>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->