import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_values(self):
        for value in (
            'hello',
            'yes',
            None,
            1234,
            1.234,
            (1, 2, 3, 'n'),
            [1, 2, 3, 'n'],
            {
                'key1': 'value1',
                'keyN': 'valueN'
            },
        ):
            self.assertEqual(
                src.telephone.text(value),
                f"I received this message: {value}"
            )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError