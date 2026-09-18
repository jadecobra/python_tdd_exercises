import src.telephone
import unittest


text = src.telephone.text


class TestTelephone(unittest.TestCase):

    def test_passing_none(self):
        self.assertEqual(text(None), 'I got: None')

    def test_passing_booleans(self):
        self.assertEqual(text(False), 'I got: False')
        self.assertEqual(text(True), 'I got: True')

    def test_passing_an_integer(self):
        an_integer = 1234
        self.assertEqual(
            text(an_integer), f'I got: {an_integer}'
        )

    def test_passing_a_float(self):
        a_float = 5.678
        self.assertEqual(
            text(a_float), f'I got: {a_float}'
        )

    def test_passing_a_string(self):
        a_string = 'hello'
        self.assertEqual(
            text('hello'), f'I got: {a_string}'
        )

    def test_passing_a_tuple(self):
        a_tuple = (0, 1, 2, 'n')
        self.assertEqual(
            text(a_tuple), f"I got: {a_tuple}"
        )

    def test_passing_a_list(self):
        a_list = [0, 1, 2, 'n']
        self.assertEqual(
            text(a_list), f'I got: {a_list}'
        )

    def test_passing_a_set(self):
        a_set = {0, 1, 2, 'n'}
        self.assertEqual(text(a_set), f'I got: {a_set}')

    def test_passing_a_dictionary(self):
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        reality = text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_class(self):
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