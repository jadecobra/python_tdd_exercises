import unittest

import streamlit as st


class TestCalculatorStreamlit(unittest.TestCase):

    def test_streamlit_can_be_imported(self):
        """Make sure Streamlit is installed and importable"""
        self.assertIsNotNone(st)

    def test_streamlit_calculator_app(self):
        """The main function in our Streamlit app exists and is callable"""
        from src.streamlit_app import main
        self.assertTrue(callable(main))

    def test_calculator_error_messages_still_work(self):
        """Our original calculator error messages are still working"""
        import src.calculator

        self.assertEqual(
            src.calculator.divide(10, 0),
            'brmph?! I cannot divide by 0. Try again...'
        )

        self.assertEqual(
            src.calculator.add(None, 5),
            'brmph?! Numbers only. Try again...'
        )

        self.assertEqual(
            src.calculator.multiply('hello', 3),
            'brmph?! Numbers only. Try again...'
        )


# Exceptions seen
# (none new - we reuse everything from chapters 1-8)