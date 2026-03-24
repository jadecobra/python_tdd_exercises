import random
import streamlit.testing.v1
import tests.test_calculator
import unittest


class TestStreamlitCalculator(unittest.TestCase):

    def press_button(self, key):
        self.tester.button(key).click().run()

    def setUp(self):
        self.tester = streamlit.testing.v1.AppTest.from_file(
            'src/streamlit_calculator.py'
        )
        self.tester.run()

    def test_streamlit_calculator_title(self):
        self.assertEqual(self.tester.title[0].value, 'Calculator')

    def test_streamlit_calculator_display(self):
        display = (
            self.tester.main.children[1].proto
                .flex_container
        )
        self.assertEqual(display.gap_config.gap_size, 1)
        self.assertEqual(display.direction, 1)
        self.assertEqual(display.justify, 1)
        self.assertEqual(display.align, 1)
        self.assertTrue(display.border)

    def test_streamlit_calculator_columns_and_buttons(self):
        self.assertEqual(len(self.tester.columns), 4)

        for column, keys in (
            (0, ('<-', '7', '4', '1', '+/-')),
            (1, ('C', '8', '5', '2', '0')),
            (2, ('AC', '9', '6', '3', '.')),
            (3, ('/', 'X', r'\-', r'\+', '=')),
        ):
            for key in keys:
                with self.subTest(key=key):
                    self.assertEqual(
                        (
                            self.tester.columns[column]
                                .button(key)
                                .label
                        ),
                        key
                    )

    def test_streamlit_calculator_operations_buttons(self):
        for key in ('/', 'X', r'\-', r'\+', '=', 'C', 'AC'):
            with self.subTest(key=key):
                self.assertEqual(
                    self.tester.button(key).proto.type,
                    'primary'
                )

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
        for key in ('0.23.5.6.7.89'):
            self.press_button(key)

        self.assertEqual(
            self.tester.session_state['number'],
            '0.2356789'
        )

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
# NameError
# AttributeError
# AssertionError
# SyntaxError
# KeyError
# streamlit.errors.StreamlitDuplicateElementKey