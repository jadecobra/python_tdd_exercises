import random
import streamlit.testing.v1
import tests.test_calculator
import unittest


class TestStreamlitCalculator(unittest.TestCase):

    def setUp(self):
        self.tester = streamlit.testing.v1.AppTest.from_file(
            'src/streamlit_calculator.py'
        )
        self.tester.run()

    def test_streamlit_calculator_title(self):
        self.assertEqual(self.tester.title[0].value, 'Calculator')

    def test_streamlit_calculator_display(self):
        self.assertEqual(
            self.tester.main.children[1].type,
            'flex_container'
        )

    def test_streamlit_calculator_columns(self):
        self.assertEqual(len(self.tester.columns), 4)
        self.assertEqual(
            self.tester.columns[0].button('<-').label,
            '<-'
        )
        self.assertEqual(
            self.tester.columns[0].button('7').label,
            '7'
        )
        self.assertEqual(
            self.tester.columns[0].button('4').label,
            '4'
        )
        self.assertEqual(
            self.tester.columns[0].button('1').label,
            '1'
        )
        self.assertEqual(
            self.tester.columns[0].button('+/-').label,
            '+/-'
        )
        self.assertEqual(
            self.tester.columns[1].button('C').label,
            'C'
        )
        self.assertEqual(
            self.tester.columns[1].button('8').label,
            '8'
        )
        self.assertEqual(
            self.tester.columns[1].button('5').label,
            '5'
        )
        self.assertEqual(
            self.tester.columns[1].button('2').label,
            '2'
        )
        self.assertEqual(
            self.tester.columns[1].button('0').label,
            '0'
        )

        self.assertEqual(
            self.tester.columns[2].button('AC').label,
            'AC'
        )
        self.assertEqual(
            self.tester.columns[2].button('9').label,
            '9'
        )
        self.assertEqual(
            self.tester.columns[2].button('6').label,
            '6'
        )
        self.assertEqual(
            self.tester.columns[2].button('3').label,
            '3'
        )
        self.assertEqual(
            self.tester.columns[2].button('.').label,
            '.'
        )

        self.assertEqual(
            self.tester.columns[3].button('/').label,
            '/'
        )
        self.assertEqual(
            self.tester.columns[3].button('X').label,
            'X'
        )
        self.assertEqual(
            self.tester.columns[3].button('-').label,
            r'\-'
        )
        self.assertEqual(
            self.tester.columns[3].button('+').label,
            r'\+'
        )
        self.assertEqual(
            self.tester.columns[3].button('=').label,
            '='
        )

    def test_streamlit_calculator_state(self):
        expectation = '0'
        for _ in range(0, 10):
            number = random.choice('0123456789')
            (
                self.tester.button(number)
                .click().run()
            )
            if expectation == '0':
                expectation = number
            else:
                expectation += number
        self.assertEqual(
            self.tester.session_state['number'],
            expectation
        )

    def test_streamlit_calculator_w_decimals(self):
        for button in ('0.23.5.6.7.8.9'):
            (
                self.tester.button(button)
                .click().run()
            )
        self.assertEqual(
            self.tester.session_state['number'],
            '.2356789'
        )

    def test_streamlit_calculator_w_plus_minus(self):
        number = '963.0258741'
        for button in number:
            (
                self.tester.button(button)
                .click().run()
            )
        self.tester.button('+/-').click().run()
        self.assertEqual(
            self.tester.session_state['number'],
            f'-{number}'
        )

        self.tester.session_state['number'] = '0'
        number = '-963.0258741'
        for button in number:
            (
                self.tester.button(button)
                .click().run()
            )

        self.tester.button('+/-').click().run()
        self.assertEqual(
            self.tester.session_state['number'],
            number[1:]
        )

    def test_streamlit_calculator_reset_state(self):
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

    @unittest.skip
    def test_streamlit_calculator_operations(self):
        # first_number = '1'
        first_number = tests.test_calculator.a_random_number()
        first_number = str(first_number)
        second_number = '2'

        for character in first_number:
            if character == '-':
                self.tester.button('+/-').click().run()
            else:
                self.tester.button(character).click().run()
        self.tester.button('+').click().run()
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
            str(float(first_number) + float(second_number))
        )


# Exceptions seen
# NameError
# AttributeError
# AssertionError
# SyntaxError
# KeyError
# streamlit.errors.StreamlitDuplicateElementKey
# TypeError