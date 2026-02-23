import src.website
import tests.test_calculator
import unittest


class TestCalculatorWebsite(unittest.TestCase):

    def setUp(self):
        self.client = src.website.app.test_client()
        self.x = tests.test_calculator.a_random_number()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'<h1>Calculator</h1>',
            response.data
        )

    def test_calculations(self):
        y = tests.test_calculator.a_random_number()

        operations = {
            'add': '+',
            'subtract': '-',
            'divide': '/',
            'multiply': '*',
        }

        for operation in operations:
            with self.subTest(operation=operation):
                response = self.client.post(
                    '/calculate',
                    data={
                        'first_input': self.x,
                        'second_input': y,
                        'operation': operation,
                    }
                )
                self.assertEqual(response.status_code, 200)

                function = src.calculator.__getattribute__(
                    operation
                )
                result = function(self.x, y)
                self.assertEqual(
                    response.data.decode(),
                    (
                        f'<h2>{self.x} {operations[operation]} {y} '
                        f'= {result}</h2>'
                    )
                )

    def test_website_handling_zero_division_error(self):
        response = self.client.post(
            '/calculate',
            data={
                'first_input': self.x,
                'second_input': 0,
                'operation': 'divide',
            }
        )
        self.assertEqual(
            response.data.decode(),
            (
                f'<h2>{self.x} / 0.0 = '
                'brmph?! I cannot divide by 0. Try again...</h2>'
            )
        )


# Exceptions seen
# NameError
# ModuleNotFoundError
# AttributeError
# AssertionError
# jinja2.exceptions.TemplateNotFound
# SyntaxError