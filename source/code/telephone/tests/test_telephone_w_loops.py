import src.telephone
import unittest


text = src.telephone.text


class TestTelephone(unittest.TestCase):

    def test_passing_values(self):
        for value in (
            None, False, True,
            1234, 5.678, 'hello',
            (0, 1, 2, 'n'), [0, 1, 2, 'n'],
            {0, 1, 2, 'n'},
            {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
        ):
            with self.subTest(value):
                self.assertEqual(
                    text(value),
                    f'I got: {value}'
                )

    def test_passing_an_object(self):
        self.assertEqual(
            text(object), "I got: <class 'object'>"
        )
        self.assertEqual(
            text(bool), "I got: <class 'bool'>"
        )
        self.assertEqual(text(int), "I got: <class 'int'>")
        self.assertEqual(
            text(float), "I got: <class 'float'>"
        )
        self.assertEqual(text(str), "I got: <class 'str'>")
        self.assertEqual(
            text(tuple), "I got: <class 'tuple'>"
        )
        self.assertEqual(
            text(list), "I got: <class 'list'>"
        )
        self.assertEqual(text(set), "I got: <class 'set'>")
        self.assertEqual(
            text(dict), "I got: <class 'dict'>"
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError