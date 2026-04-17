.. include:: calculator_links.rst

#################################################################################
how to make a calculator 10: part 3
#################################################################################

I want the numbers to stay when I press a button so that I can make numbers that have more than one digit.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_streamlit_calculator_3.py
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

  the terminal_ is your friend, and shows

  .. code-block:: shell

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 12 items

    tests/test_calculator.py .....                                [ 41%]
    tests/test_calculator_website.py ...                          [ 66%]
    tests/test_streamlit_calculator.py ....                       [100%]

    ======================== 12 passed in X.YZs =========================

* I open another terminal_ then use uv_ in the ``calculator`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    uv run streamlit run src/streamlit_calculator.py

  the terminal_ is your friend, and shows

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
test_streamlit_session_state
*********************************************************************************

streamlit_ has a `session state object`_ that I can use to keep values in between button presses. They work the same as :ref:`class attributes<test_attribute_error_w_class_attributes>` and they are :ref:`dictionaries<what is a dictionary?>` - I can add :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` to them

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I hold :kbd:`ctrl/command` on the keyboard and click on ``tests/test_streamlit_calculator.py`` with the mouse to open it in the :ref:`editor<2 editors>`

* I add a test for the `session state object`_, I want it to hold the number when I click the buttons, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 9-10

        def test_streamlit_calculator_operations_buttons(self):
            for key in ('/', 'X', r'\-', r'\+', '=', 'C', 'AC'):
                with self.subTest(key=key):
                    self.assertEqual(
                        self.tester.button(key).proto.type,
                        'primary'
                    )

        def test_streamlit_session_state(self):
            self.assertIsNone(self.tester.session_state['number'])


    # Exceptions seen

  the terminal_ is your friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'st.session_state has no key "number".
    Did you forget to initialize it?
    More info: https://docs.streamlit.io/develop/concepts/architecture/session-state#initialization'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the :ref:`setdefault method<test_setdefault_adds_given_key_to_a_dictionary>` to add a :ref:`key<test_keys_of_a_dictionary>` that will hold the numbers to show in the Calculator, in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3

    def main():
        streamlit.title('Calculator')
        streamlit.session_state.setdefault('number', '0')
        display = streamlit.container(border=True)

        column_1, column_2, column_3, operations = streamlit.columns(4)
        add_buttons_to_column_1(column_1, display)
        add_buttons_to_column_2(column_2, display)
        add_buttons_to_column_3(column_3, display)
        add_buttons_to_column_4(operations)

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I add ``0`` as the expectation in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_streamlit_session_state(self):
            self.assertIsNone(self.tester.session_state['number'], '0')

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0' is not None : 0

* I change the assertIsNone_ to assertEqual_

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 1

            self.assertEqual(self.tester.session_state['number'], '0')

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the `session state object`_ to the ``show`` :ref:`function<what is a function?>` so that when a button is clicked, it will be added to the `session state object`_ then shown in the disply

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-4

    def show(display, number):
        # display.write(number)
        streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])


    def add_buttons_to_column_1(column_1, display):

  the test passes

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    def show(display, number):
        streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

* I add an :ref:`assertion<what is an assertion?>` to test what happens to the `session state object`_ when I press a button for a number

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3-4

        def test_streamlit_session_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')
            self.tester.button('1').click().run()
            self.assertEqual(self.tester.session_state['number'], '0')

  - ``.click()`` presses the button
  - ``.run()`` runs the program - ``streamlit_calculator.py``, which is what happens when a person uses the application in the browser

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01' != '0'

  this is a problem

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 1

            self.assertEqual(self.tester.session_state['number'], '01')

  the test passes

* I add more button presses and another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 5-8

        def test_streamlit_session_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')
            self.tester.button('1').click().run()
            self.assertEqual(self.tester.session_state['number'], '01')
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('4').click().run()
            self.assertEqual(self.tester.session_state['number'], '01')

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01234' != '01'

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 1-3

            self.assertEqual(
                self.tester.session_state['number'], '01234'
            )

  the test passes

* I refresh the browser and click on all the numbers

  .. image:: /_static/calculator/streamlit/many_numbers.png
    :width: 600
    :align: left
    :alt: Many Numbers

  the calculator keeps numbers when I press the buttons and the number starts with ``0`` like the test

* I want the calculator to remove ``0`` when it is the first number after I click on other numbers. I change the :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4, 8-10

        def test_streamlit_session_state(self):
            self.assertEqual(self.tester.session_state['number'], '0')
            self.tester.button('1').click().run()
            self.assertEqual(self.tester.session_state['number'], '1')
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('4').click().run()
            self.assertEqual(
                self.tester.session_state['number'], '1234'
            )

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '01' != '1'

* I add a :ref:`condition<if statements>` to the ``show`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-5

    def show(display, number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

  the test passes

* I refresh the browser and try all the numbers

  .. image:: /_static/calculator/streamlit/many_numbers_no_zero_first.png
    :width: 600
    :align: left
    :alt: Many Numbers Without 0 first

  the number no longer starts with ``0``

* I import the `random module`_ to use random numbers for the test, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import streamlit.testing.v1
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

* I use it in :ref:`test_streamlit_session_state`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2, 4-6
    :emphasize-text: x

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            self.tester.button(x).click().run()
            self.assertEqual(self.tester.session_state['number'], '1')

  - ``numbers = '0123456789'`` makes a string_ with ten numbers
  - ``x = random.choice(numbers)`` picks a random number from the ten numbers and points ``x`` to it

  the terminal_ is your friend, and shows. :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X' != '1'

  where ``X`` is a random number

* I change the expectation

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            self.tester.button(x).click().run()
            self.assertEqual(self.tester.session_state['number'], x)
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('4').click().run()
            self.assertEqual(
                self.tester.session_state['number'], '1234'
            )

  when ``x`` is not ``1``, the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'X234' != '1234'

* I use random numbers for the other button presses

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2-10

            self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()
            # self.tester.button('3').click().run()
            # self.tester.button('4').click().run()
            y = random.choice(numbers)
            self.tester.button(y).click().run()
            z = random.choice(numbers)
            self.tester.button(z).click().run()
            a = random.choice(numbers)
            self.tester.button(a).click().run()
            self.assertEqual(
                self.tester.session_state['number'], '1234'
            )

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'XYZA' != '1234'

* I use the random numbers in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2

            self.assertEqual(
                self.tester.session_state['number'], f'{x}{y}{z}{a}'
            )

  when ``x`` is ``0``, the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YZA' != '0YZA'

----

*********************************************************************************
what is a while loop?
*********************************************************************************

* I can use a `while loop`_ to make sure that ``x`` is never ``0``, since the ``session_state['number']`` is always ``0`` at the beginning. I add a `while loop`_ to :ref:`test_streamlit_session_state`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 6-9

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            while x == '0':
                x = random.choice(numbers)
            else:
                self.tester.button(x).click().run()

            self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()

  - ``x = random.choice(numbers)`` points ``x`` to a random number from the ``numbers`` :ref:`variable<what is a variable?>`

    * if ``x`` is not equal to ``'0'`` it goes to the next block which is ``else: self.tester.button(x).click().run()``

    * if ``x`` is equal to ``'0'`` it goes to ``while x == '0':`` which makes a loop that will continue to run as long as ``x`` is equal to ``'0'``

      - inside the loop ``x = random.choice(numbers)`` points ``x`` to a random number from the ``numbers`` string_ then checks again to see if ``x`` is equal to ``'0'``

        * if ``x`` is equal to ``0`` the loop runs again
        * if ``x`` is not equal to ``0`` in the loop, it leaves the loop and goes to the next block which is ``else: self.tester.button(x).click().run()``

  I use :kbd:`ctrl+s` on the keyboard a few times and there are no more random failures

* I add a :ref:`for loop<what is a for loop?>` to test with a 10 digit number

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 25-31, 33-36

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            while x == '0':
                x = random.choice(numbers)
            else:
                self.tester.button(x).click().run()

            self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()
            # self.tester.button('3').click().run()
            # self.tester.button('4').click().run()
            y = random.choice(numbers)
            self.tester.button(y).click().run()
            z = random.choice(numbers)
            self.tester.button(z).click().run()
            a = random.choice(numbers)
            self.tester.button(a).click().run()
            self.assertEqual(
                self.tester.session_state['number'], f'{x}{y}{z}{a}'
            )

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                (
                    self.tester.button(a_random_number)
                        .click().run()
                )
                x += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                x
            )


    # Exceptions seen

  ``for _ in range(0, 10):`` uses ``_`` because I do not need a name for each number from the `range object`_ in the :ref:`for loop<what is a for loop?>` since I do not use it

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'XYZABCDEFGHIJK' != 'XBCDEFGHIJK'

  the first number and the last 10 numbers are the same in the two strings_

* I comment out the other lines

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 15-23

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')
            # self.tester.button('1').click().run()
            x = random.choice(numbers)
            while x == '0':
                x = random.choice(numbers)
            else:
                self.tester.button(x).click().run()

            self.assertEqual(self.tester.session_state['number'], x)
            # self.tester.button('2').click().run()
            # self.tester.button('3').click().run()
            # self.tester.button('4').click().run()
            # y = random.choice(numbers)
            # self.tester.button(y).click().run()
            # z = random.choice(numbers)
            # self.tester.button(z).click().run()
            # a = random.choice(numbers)
            # self.tester.button(a).click().run()
            # self.assertEqual(
            #     self.tester.session_state['number'], f'{x}{y}{z}{a}'
            # )

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                (
                    self.tester.button(a_random_number)
                        .click().run()
                )
                x += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                x
            )


  I use :kbd:`ctrl+s` on the keyboard to run the tests a few times and the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')

            x = random.choice(numbers)
            while x == '0':
                x = random.choice(numbers)
            else:
                self.tester.button(x).click().run()

            self.assertEqual(self.tester.session_state['number'], x)

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                (
                    self.tester.button(a_random_number)
                        .click().run()
                )
                x += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                x
            )

* I use the ``Rename Symbol`` feature of the `Integrated Development Environment (IDE)`_ to change ``x`` to ``expectation`` because I like the name better

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 5-7, 9, 11-13, 21, 25
    :emphasize-text: expectation

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')

            expectation = random.choice(numbers)
            while expectation == '0':
                expectation = random.choice(numbers)
            else:
                self.tester.button(expectation).click().run()

            self.assertEqual(
                self.tester.session_state['number'], expectation
            )

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                (
                    self.tester.button(a_random_number)
                        .click().run()
                )
                expectation += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )


    # Exceptions seen

----

*********************************************************************************
test_streamlit_calculator_w_decimals
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for decimal numbers

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 6-23

            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )

        def test_streamlit_calculator_w_decimals(self):
            self.tester.button('0').click().run()
            self.tester.button('.').click().run()
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('.').click().run()
            self.tester.button('5').click().run()
            self.tester.button('.').click().run()
            self.tester.button('6').click().run()
            self.tester.button('.').click().run()
            self.tester.button('7').click().run()
            self.tester.button('.').click().run()
            self.tester.button('8').click().run()
            self.tester.button('9').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )


    # Exceptions seen

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '.23.5.6.7.89' != '0.2356789'

* I refresh the browser and do the same thing

  .. image:: /_static/calculator/streamlit/many_decimals.png
    :width: 600
    :align: left
    :alt: Many Decimals

  the Calculator allows me add many decimal points

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` for decimals in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 1
    :emphasize-lines: 4-9

    import streamlit


    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') >= 1:
            return None
        else:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])


    def show(display, number):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the ``on_click`` parameter for the ``.`` button in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>` to use the new :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-4
    :emphasize-text: handle_decimals

        column_3.button(
            label='.', key='.', width='stretch',
            # on_click=show, args=[display, '.'],
            on_click=handle_decimals, args=[display, '.'],
        )

  the test passes

* I remove the commented line

  .. code-block:: python
    :lineno-start: 62

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch',
            on_click=show, args=[display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch',
            on_click=show, args=[display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch',
            on_click=show, args=[display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch',
            on_click=handle_decimals, args=[display, '.'],
        )


    def add_buttons_to_column_4(column_4):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the `else clause`_ to an :ref:`if statement<if statements>` to make it simpler

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') >= 1:
            return None
        # else:
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])

  the test is still green

* I remove the other :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 4

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        display.write(streamlit.session_state['number'])


    def show(display, number):

  still green

  - ``if streamlit.session_state['number'].count('.') == 0:`` checks if ``.`` is in ``session_state['number']``

    * ``streamlit.session_state['number'].count('.')`` counts how many times ``.`` shows up in ``session_state['number']``
    * if ``.`` is NOT in ``session_state['number']``, then ``.`` gets added to ``session_state['number']`` and the program runs the next line, which is ``display.write(streamlit.session_state['number'])``
    * if ``.`` is in ``session_state['number']``, then the program runs the next line, which is  ``display.write(streamlit.session_state['number'])``

* I refresh the browser and try many decimals again

  .. image:: /_static/calculator/streamlit/one_decimal.png
    :width: 600
    :align: left
    :alt: One Decimal

  Yes! I can only do one decimal in a number

* I add a :ref:`for loop<what is a for loop?>` to :ref:`test_streamlit_calculator_w_decimals` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-6

        def test_streamlit_calculator_w_decimals(self):
            for key in ('0.23.5.6.7.89'):
                (
                    self.tester.button(key)
                        .click().run()
                )

            self.tester.button('0').click().run()
            self.tester.button('.').click().run()
            self.tester.button('2').click().run()
            self.tester.button('3').click().run()
            self.tester.button('.').click().run()
            self.tester.button('5').click().run()
            self.tester.button('.').click().run()
            self.tester.button('6').click().run()
            self.tester.button('.').click().run()
            self.tester.button('7').click().run()
            self.tester.button('.').click().run()
            self.tester.button('8').click().run()
            self.tester.button('9').click().run()
            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )


  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '0.235678902356789' != '0.2356789'

* I remove the other button presses

  .. code-block:: python
    :lineno-start: 83

        def test_streamlit_calculator_w_decimals(self):
            for key in ('0.23.5.6.7.89'):
                (
                    self.tester.button(key)
                        .click().run()
                )

            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )


    # Exceptions seen

  the test passes

----

* I keep writing ``self.tester.button(key).click().run()``, time to add a :ref:`method<what is a function?>` for button presses

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-4

    class TestStreamlitCalculator(unittest.TestCase):

        def press_button(self, key):
            self.tester.button(key).click().run()

        def setUp(self):

* I use the new :ref:`method<what is a function?>` in :ref:`test_streamlit_session_state`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 9-10 ,18-22
    :emphasize-text: press_button

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')

            expectation = random.choice(numbers)
            while expectation == '0':
                expectation = random.choice(numbers)
            else:
                # self.tester.button(expectation).click().run()
                self.press_button(expectation)

            self.assertEqual(
                self.tester.session_state['number'], expectation
            )

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                # (
                #     self.tester.button(a_random_number)
                #         .click().run()
                # )
                self.press_button(a_random_number)
                expectation += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )

  the tests are still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 59

        def test_streamlit_session_state(self):
            numbers = '0123456789'
            self.assertEqual(self.tester.session_state['number'], '0')

            expectation = random.choice(numbers)
            while expectation == '0':
                expectation = random.choice(numbers)
            else:
                self.press_button(expectation)

            self.assertEqual(
                self.tester.session_state['number'], expectation
            )

            for _ in range(0, len(numbers)):
                a_random_number = random.choice(numbers)
                self.press_button(a_random_number)
                expectation += a_random_number

            self.assertEqual(
                self.tester.session_state['number'],
                expectation
            )

        def test_streamlit_calculator_w_decimals(self):

* I use the ``press_button`` :ref:`method<what is a function?>` in :ref:`test_streamlit_calculator_w_decimals`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3-7

        def test_streamlit_calculator_w_decimals(self):
            for key in ('0.23.5.6.7.89'):
                # (
                #     self.tester.button(key)
                #         .click().run()
                # )
                self.press_button(key)

            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 83

        def test_streamlit_calculator_w_decimals(self):
            for key in ('0.23.5.6.7.89'):
                self.press_button(key)

            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )


    # Exceptions seen

----

*********************************************************************************
test_streamlit_calculator_backspace
*********************************************************************************

I want to be able to remove the last digit of a number with the ``<-`` button

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 6-15

            self.assertEqual(
                self.tester.session_state['number'],
                '0.2356789'
            )

        def test_streamlit_calculator_backspace(self):
            self.press_button('1')
            self.press_button('2')
            self.press_button('3')
            self.press_button('4')
            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                '123'
            )


    # Exceptions seen

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '1234' != '123'

* I try the same thing in the browser and it clears the screen

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-7

    import streamlit


    def backspace(display):
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        display.write(streamlit.session_state['number'])


    def handle_decimals(display, number):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I add the ``on_click`` parameter to the ``<-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-5
    :emphasize-text: backspace

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display],
        )
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=show, args=[display, '+/-'],
        )


    def add_buttons_to_column_2(column_2, display):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an `import statement`_ for ``tests/test_calculator.py`` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    import random
    import streamlit.testing.v1
    import tests.test_calculator
    import unittest


    class TestStreamlitCalculator(unittest.TestCase):

* I add a :ref:`variable<what is a variable?>` with a :ref:`for loop<what is a for loop?>` for a random number in :ref:`test_streamlit_calculator_backspace`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 2-3, 5-7, 9-12

        def test_streamlit_calculator_backspace(self):
            a_random_number = tests.test_calculator.a_random_number()
            a_random_number = str(a_random_number)

            for key in a_random_number:
                self.press_button(key)
            self.press_button('<-')

            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number
            )

            self.press_button('1')
            self.press_button('2')
            self.press_button('3')
            self.press_button('4')
            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                '123'
            )

  - ``a_random_number = tests.test_calculator.a_random_number()`` uses the ``a_random_number`` :ref:`function<what is a function?>` from ``test_calculator.py`` that I made in :ref:`how to use random numbers`
  - ``a_random_number = str(a_random_number)`` changes the random number to a string_ since all the tests of the calculator have been done with strings_ so far

  I use :kbd:`ctrl+s` on the keyboard to run the test a few times because I am using random numbers. If the number is positive, the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'LMN.OPQRSTUVWXYZ' != 'LMN.OPQRSTUVWXYZA'

  the last number was not removed

  If the random number is negative, the terminal_ is your friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '-'

  I need :ref:`a test for the '+/-' button<test_streamlit_calculator_w_plus_minus>`

* I add a :ref:`while loop<what is a while loop?>` to make sure ``a_random_number`` is never negative

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3-4

        def test_streamlit_calculator_backspace(self):
            a_random_number = tests.test_calculator.a_random_number()
            while a_random_number < 0:
                a_random_number = tests.test_calculator.a_random_number()
            a_random_number = str(a_random_number)

            for key in a_random_number:

  I use :kbd:`ctrl+s` on the keyboard to run the tests a few times and the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'BCD.EFGHIJKLMNOP' != 'BCD.EFGHIJKLMNOPQ'

  I remove this :ref:`while statement<what is a while loop?>` when :ref:`I test the '+/-' button<test_streamlit_calculator_w_plus_minus>`

* I change the expectation to remove the last digit from the random number

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 3

            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-1]
            )

  the terminal shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RS.TUVWXYZABCDEF123' != '123'

  because I have button presses after the test. I need :ref:`a way to reset the numbers back to 0<test_streamlit_calculator_reset>`

* I comment out the other button presses

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 16-19

        def test_streamlit_calculator_backspace(self):
            a_random_number = tests.test_calculator.a_random_number()
            while a_random_number < 0:
                a_random_number = tests.test_calculator.a_random_number()
            a_random_number = str(a_random_number)

            for key in a_random_number:
                self.press_button(key)
            self.press_button('<-')

            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-1]
            )

            # self.press_button('1')
            # self.press_button('2')
            # self.press_button('3')
            # self.press_button('4')
            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                '123'
            )

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GHI.JKLMNOPQRS' != '123'

* I change the expectation

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 23-24

        def test_streamlit_calculator_backspace(self):
            a_random_number = tests.test_calculator.a_random_number()
            while a_random_number < 0:
                a_random_number = tests.test_calculator.a_random_number()
            a_random_number = str(a_random_number)

            for key in a_random_number:
                self.press_button(key)
            self.press_button('<-')

            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-1]
            )

            # self.press_button('1')
            # self.press_button('2')
            # self.press_button('3')
            # self.press_button('4')
            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                # '123'
                a_random_number[:-2]
            )

  the test passes

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 93

        def test_streamlit_calculator_backspace(self):
            a_random_number = tests.test_calculator.a_random_number()
            while a_random_number < 0:
                a_random_number = tests.test_calculator.a_random_number()
            a_random_number = str(a_random_number)

            for key in a_random_number:
                self.press_button(key)
            self.press_button('<-')

            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-1]
            )

            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-2]
            )


    # Exceptions seen

* I go to the browser and click on a few numbers, then click on ``<-`` and it removes the last number. Fantastic!

----

*********************************************************************************
test_streamlit_calculator_w_plus_minus
*********************************************************************************

Nothing happens when I click ``+/-`` in the calculator. I want it to

* change positive numbers to negative numbers
* change negative numbers to positive numbers

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for the ``+/-`` button

.. code-block:: python
  :lineno-start: 108
  :emphasize-lines: 7-11, 13-16

            self.press_button('<-')
            self.assertEqual(
                self.tester.session_state['number'],
                a_random_number[:-2]
            )

        def test_streamlit_calculator_w_plus_minus(self):
            self.press_button('9')
            self.assertEqual(
                self.tester.session_state['number'], '9'
            )

            self.press_button('+/-')
            self.assertEqual(
                self.tester.session_state['number'], '-9'
            )


    # Exceptions seen

the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: '9' != '-9'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``+/-`` button in ``streamlit_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-8

    import streamlit


    def plus_minus(display):
        if not streamlit.session_state['number'].startswith('-'):
            number = '-' + streamlit.session_state['number']
            streamlit.session_state['number'] = number
            display.write(streamlit.session_state['number'])


    def backspace(display):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I add the ``on_click`` parameter for the ``+/-`` button in the ``add_buttons_to_column_1``  :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 18-21
    :emphasize-text: plus_minus

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display],
        )
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display],
        )


    def add_buttons_to_column_2(column_2, display):

  the test passes. I can turn a positive number to a negative number with the ``+/-`` button. Can I turn a negative number to a positive number with the ``+/-`` button?

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a button press and :ref:`assertion<what is an assertion?>` to make sure I can turn a negative number to a positive number with the ``+/-`` button, in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 12-15

        def test_streamlit_calculator_w_plus_minus(self):
            self.press_button('9')
            self.assertEqual(
                self.tester.session_state['number'], '9'
            )

            self.press_button('+/-')
            self.assertEqual(
                self.tester.session_state['number'], '-9'
            )

            self.press_button('+/-')
            self.assertEqual(
                self.tester.session_state['number'], '9'
            )


    # Exceptions seen

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '-9' != '9'

* I add another :ref:`if statement<if statements>` to the ``plus_minus`` :ref:`function<what is a function?>` in ``streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-3, 6

    def plus_minus(display):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        if not streamlit.session_state['number'].startswith('-'):
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        display.write(streamlit.session_state['number'])

  the test passes

* I use else_ for the second :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    def plus_minus(display):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        # if not streamlit.session_state['number'].startswith('-'):
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        display.write(streamlit.session_state['number'])

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    def plus_minus(display):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        display.write(streamlit.session_state['number'])


    def backspace(display):

* I add a :ref:`variable<what is a variable?>` to remove repetition from :ref:`test_streamlit_calculator_w_plus_minus` in ``test_streamlit_calculator.py``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2
    :emphasize-text: a_number

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '9'
            self.press_button('9')
            self.assertEqual(

* I use the :ref:`variable<what is a variable?>` in the :ref:`assertions<what is an assertion?>` and button presses

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 3-4, 6-7, 12-13, 18-19
    :emphasize-text: a_number

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '9'
            # self.press_button('9')
            self.press_button(a_number)
            self.assertEqual(
                # self.tester.session_state['number'], '9'
                self.tester.session_state['number'], a_number
            )

            self.press_button('+/-')
            self.assertEqual(
                # self.tester.session_state['number'], '-9'
                self.tester.session_state['number'], f'-{a_number}'
            )

            self.press_button('+/-')
            self.assertEqual(
                # self.tester.session_state['number'], '9'
                self.tester.session_state['number'], a_number
            )

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 114

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '9'
            self.press_button(a_number)
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

* I try a bigger number

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '96'
            self.press_button(a_number)

  the terminal_ is your friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    KeyError: '96'

  I need separate button presses for the two numbers

* I add a :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 3-4

        def test_streamlit_calculator_w_plus_minus(self):
            a_number = '96'
            for key in a_number:
                self.press_button(key)
            self.assertEqual(
                self.tester.session_state['number'], a_number
            )

            self.press_button('+/-')

  the test passes

* I try a number with all the digits and decimals

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 2

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


    # Exceptions seen

  the test is still green

* I refresh the browser and try to make a negative number

  .. image:: /_static/calculator/streamlit/negative_number.png
    :width: 600
    :align: left
    :alt: Negative Number

  when I click on the ``+/-`` button it turns a positive number negative

* I try the ``+/-`` button again

  .. image:: /_static/calculator/streamlit/positive_number.png
    :width: 600
    :align: left
    :alt: Negative Number

  the ``-`` is removed from the number to make it a positive number. Progress!

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* The last 4 :ref:`functions<what is a function?>` in ``streamlit_calculator.py`` - ``plus_minus``, ``backspace``, ``handle_decimals`` and ``show`` look the same. 2 of the :ref:`functions<what is a function?>` have ``number`` in the :ref:`function<what is a function?>` signature, all 4 have ``display`` in the :ref:`function<what is a function?>` signature

  .. code-block:: python

    def function_name(display):
    def function_name(display, number):
        statements
        display.write(streamlit.session_state['number'])

* I add ``number`` in the parentheses for the ``plus_minus`` :ref:`function<what is a function?>` to make it have the same signature as the ``show`` and ``handle_decimals`` :ref:`functions<what is a function?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    def plus_minus(display, number):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        display.write(streamlit.session_state['number'])


    def backspace(display):

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    '963.0258741' != '-963.0258741'

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: plus_minus() missing 1 required positional argument: 'number'

* I add a second argument to the ``args`` parameter for the ``+/-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 20
    :emphasize-text: +/-

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display],
        )
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display, '+/-'],
        )


    def add_buttons_to_column_2(column_2, display):

  the test is green again

* I add ``number`` in the parentheses for the ``backspace`` :ref:`function<what is a function?>` to make it have the same signature as the ``show``, ``handle_decimals`` and ``plus_minus`` :ref:`functions<what is a function?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

    def backspace(display, number):
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        display.write(streamlit.session_state['number'])


    def handle_decimals(display, number):

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RST.UVWXYZABCDEFGH' != 'RST.UVWXYZABCDEFG'

  it also shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: backspace() missing 1 required positional argument: 'number'

* I add a second argument to the ``args`` parameter for the ``<-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display, '<-'],
        )
        column_1.button(
            label='7', key='7', width='stretch',
            on_click=show, args=[display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display, '+/-'],
        )


    def add_buttons_to_column_2(column_2, display):

  the test is green again

* I add a new :ref:`function<what is a function?>` for showing the ``number`` :ref:`key<test_keys_of_a_dictionary>` of the `session state object`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import streamlit


    def show_number(display):
        display.write(streamlit.session_state['number'])


    def plus_minus(display, number):

* I use the new :ref:`function<what is a function?>` in the ``plus_minus`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 8-9

    def plus_minus(display, number):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        # display.write(streamlit.session_state['number'])
        show_number(display)

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 8

    def plus_minus(display, number):
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        show_number(display)


    def backspace(display, number):

* I use the new :ref:`function<what is a function?>` in the ``backspace`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 4-5

    def backspace(display, number):
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        # display.write(streamlit.session_state['number'])
        show_number(display)

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 18

    def backspace(display, number):
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        show_number(display)


    def handle_decimals(display, number):

* I use the new :ref:`function<what is a function?>` in the ``handle_decimals`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4-5

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        # display.write(streamlit.session_state['number'])
        show_number(display)

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 24

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        show_number(display)


    def show(display, number):

* I use the new :ref:`function<what is a function?>` in the ``show`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-7

    def show(display, number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        # display.write(streamlit.session_state['number'])
        show_number(display)

  the test is still green

* I remove the commented line

  .. code-block:: python
    :lineno-start: 30

    def show(display, number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        show_number(display)


    def add_buttons_to_column_1(column_1, display):

* I add a new :ref:`function<what is a function?>` for adding the number to the `session state object`_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-11

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        show_number(display)


    def add_number_to_state(number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number


    def show(display, number):

* I add a :ref:`function<what is a function?>` to handle all the button clicks

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9-11

    def show(display, number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number
        show_state(display)


    def on_click(function, display, value):
        function(value)
        show_state(display)


    def add_buttons():

* I try the ``on_click`` :ref:`function<what is a function?>` with the ``7`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 7-9

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display, '<-'],
        )
        column_1.button(
            label='7', key='7', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '7'],
            args=[add_number_to_state, display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch',
            on_click=show, args=[display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch',
            on_click=show, args=[display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display, '+/-'],
        )

  the tests are still green! Yes!!

* I use the ``on_click`` :ref:`function<what is a function?>` with all the other number buttons in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 12-14, 17-19

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display, '<-'],
        )
        column_1.button(
            label='7', key='7', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '7'],
            args=[add_number_to_state, display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '4'],
            args=[add_number_to_state, display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '1'],
            args=[add_number_to_state, display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display, '+/-'],
        )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch',
            on_click=backspace, args=[display, '<-'],
        )
        column_1.button(
            label='7', key='7', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch',
            on_click=plus_minus, args=[display, '+/-'],
        )


    def add_buttons_to_column_2(column_2, display):

* I use the ``on_click`` :ref:`function<what is a function?>` with all the number buttons in the ``add_buttons_to_column_2`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 6-8, 11-13, 16-18, 21-23

    def add_buttons_to_column_2(column_2, display):
        column_2.button(
            label='C', key='C', width='stretch', type='primary',
        )
        column_2.button(
            label='8', key='8', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '8'],
            args=[add_number_to_state, display, '8'],
        )
        column_2.button(
            label='5', key='5', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '5'],
            args=[add_number_to_state, display, '5'],
        )
        column_2.button(
            label='2', key='2', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '2'],
            args=[add_number_to_state, display, '2'],
        )
        column_2.button(
            label='0', key='0', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '0'],
            args=[add_number_to_state, display, '0'],
        )

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 73

    def add_buttons_to_column_2(column_2, display):
        column_2.button(
            label='C', key='C', width='stretch', type='primary',
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

* I use the ``on_click`` :ref:`function<what is a function?>` with all the number buttons in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 6-8, 11-13, 16-18

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '9'],
            args=[add_number_to_state, display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '6'],
            args=[add_number_to_state, display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch', on_click=on_click,
            # on_click=show, args=[display, '3'],
            args=[add_number_to_state, display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch',
            on_click=handle_decimals, args=[display, '.'],
        )

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 95

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch',
            on_click=handle_decimals, args=[display, '.'],
        )


    def add_buttons_to_column_4(column_4):

* I remove the ``show`` :ref:`function<what is a function?>` because it is no longer used

  .. code-block:: python
    :lineno-start: 30

    def add_number_to_state(number):
        if streamlit.session_state['number'] == '0':
            streamlit.session_state['number'] = number
        else:
            streamlit.session_state['number'] += number


    def on_click(function, display, value):

----

* I add a new :ref:`function<what is a function?>` to make decimal numbers

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-9

    def handle_decimals(display, number):
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += number
        show_number(display)


    def add_decimal():
        if streamlit.session_state['number'].count('.') == 0:
            streamlit.session_state['number'] += '.'


    def add_number_to_state(number):

* I use the new :ref:`function<what is a function?>` with the ``.`` button in the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 18-20

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch', on_click=on_click,
            # on_click=handle_decimals, args=[display, '.'],
            args=[add_decimal, display]
        )

  the terminal_ is your friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: python

    FAILED ... - KeyError: 'I'
    FAILED ... - KeyError: '2'
    FAILED ... - KeyError: '0'

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: on_click() missing 1 required positional argument: 'value'

* I make the ``value`` parameter a choice in the ``on_click`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1-2

    def on_click(function, display, *value):
        function(*value)
        show_number(display)


    def add_buttons_to_column_1(column_1, display):

  the test passes

* I remove the commented line from the ``add_buttons_to_column_3`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 92

    def add_buttons_to_column_3(column_3, display):
        column_3.button(
            label='AC', key='AC', width='stretch', type='primary',
        )
        column_3.button(
            label='9', key='9', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '9'],
        )
        column_3.button(
            label='6', key='6', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '6'],
        )
        column_3.button(
            label='3', key='3', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '3'],
        )
        column_3.button(
            label='.', key='.', width='stretch', on_click=on_click,
            args=[add_decimal, display]
        )


    def add_buttons_to_column_4(column_4):

* I remove the ``handle_decimals`` :ref:`function<what is a function?>` because it is no longer used

  .. code-block:: python
    :lineno-start: 18

    def backspace(display, number):
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        show_number(display)


    def add_decimal():

----

* I change the ``on_click`` and ``args`` parameters for the ``<-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-5

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch', on_click=on_click,
            # on_click=backspace, args=[display, '<-'],
            args=[backspace, display],
        )

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'MNO.PQRSTUVWXYZABCD' != 'MNO.PQRSTUVWXYZABC'

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: backspace() missing 2 required positional arguments: 'display' and 'number'

* I change the ``backspace`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1-2, 5

    # def backspace(display, number):
    def backspace():
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number
        # show_number(display)

  the test passes

* I remove the commented lines from the ``backspace`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18

    def backspace():
        number = streamlit.session_state['number'][:-1]
        streamlit.session_state['number'] = number


    def add_decimal():

----

* I change the ``on_click`` and ``args`` parameters for the ``+/-`` button in the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 20-22

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch', on_click=on_click,
            # on_click=backspace, args=[display, '<-'],
            args=[backspace, display],
        )
        column_1.button(
            label='7', key='7', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch', on_click=on_click,
            # on_click=plus_minus, args=[display, '+/-'],
            args=[plus_minus, display],
        )

  the terminal_ is your friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: -

    AssertionError: '963.0258741' != '-963.0258741'

  and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: plus_minus() missing 2 required positional arguments: 'display' and 'number'

* I change the ``plus_minus`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1-2, 9

    # def plus_minus(display, number):
    def plus_minus():
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number

        # show_number(display)

  the test passes

* I remove the commented lines from the ``plus_minus`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 8

    def plus_minus():
        if streamlit.session_state['number'].startswith('-'):
            number = streamlit.session_state['number'][1:]
        else:
            number = '-' + streamlit.session_state['number']
        streamlit.session_state['number'] = number


    def backspace():

* I remove the commented lines from the ``add_buttons_to_column_1`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 42

    def add_buttons_to_column_1(column_1, display):
        column_1.button(
            label='<-', key='<-', width='stretch', on_click=on_click,
            args=[backspace, display],
        )
        column_1.button(
            label='7', key='7', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '7'],
        )
        column_1.button(
            label='4', key='4', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '4'],
        )
        column_1.button(
            label='1', key='1', width='stretch', on_click=on_click,
            args=[add_number_to_state, display, '1'],
        )
        column_1.button(
            label='+/-', key='+/-', width='stretch', on_click=on_click,
            args=[plus_minus, display],
        )


    def add_buttons_to_column_2(column_2, display):

That was a lot! I am going to take a nap. I will work on the operations after that.

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

  the terminal_ is your friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

* I click in the second terminal_, then use :kbd:`ctrl+c` on the keyboard to close the web server. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ is your friend, and shows

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
* :ref:`backspace<test_streamlit_calculator_backspace>`
* :ref:`+/-<test_streamlit_calculator_w_plus_minus>`

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator 10: part 3: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know how to:

* build a website with streamlit_
* how to test the parts of the website
* :ref:`how to add a title to the streamlit website<test_streamlit_calculator_title>`
* :ref:`how to add a display to the streamlit website<test_streamlit_calculator_display>`
* :ref:`how to add buttons to the streamlit website<test_streamlit_calculator_columns_and_buttons>`
* :ref:`how to change the colors of the buttons<test_streamlit_calculator_operations_buttons>`
* :ref:`how to show something when a button is pressed<how to show the numbers when I click on them>`
* :ref:`how to use the session state object<test_streamlit_session_state>`
* how to add :ref:`functions<what is a function?>` to `streamlit buttons`_ to make them do things from

  - :ref:`test_streamlit_calculator_w_decimals`
  - :ref:`test_streamlit_calculator_backspace`
  - :ref:`test_streamlit_calculator_w_plus_minus`

:ref:`Would you like to continue with the operation buttons of the calculator?<how to make a calculator 10: part 4>`

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