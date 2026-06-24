import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_a_string(self):
        a_string = 'hello'
        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        self.assertEqual(reality, my_expectation)

        a_string = 'yes'
        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        self.assertEqual(reality, my_expectation)

    def test_passing_none(self):
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        self.assertEqual(reality, my_expectation)

    def test_passing_booleans(self):
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(True)
        my_expectation = 'I got: True'
        self.assertEqual(reality, my_expectation)

    def test_passing_an_integer(self):
        an_integer = 1234
        reality = src.telephone.text(an_integer)
        my_expectation = f'I got: {an_integer}'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_float(self):
        a_float = 1.234
        reality = src.telephone.text(a_float)
        my_expectation = f'I got: {a_float}'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_tuple(self):
        a_tuple = (0, 1, 2, 'n')
        reality = src.telephone.text(a_tuple)
        my_expectation = f"I got: {a_tuple}"
        self.assertEqual(reality, my_expectation)

    def test_passing_a_list(self):
        a_list = [0, 1, 2, 'n']
        reality = src.telephone.text(a_list)
        my_expectation = f"I got: {a_list}"
        self.assertEqual(reality, my_expectation)

    def test_passing_a_dictionary(self):
        a_dictionary = {
            'key1': 'value1',
            'keyN': [0, 1, 2, 'n'],
        }
        reality = src.telephone.text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_class(self):
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(TestTelephone)
        my_expectation = (
            "I got: <class"
            f" 'tests.test_telephone.TestTelephone'>"
        )
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(self)
        my_expectation = (
            "I got: test_passing_a_class"
            " (tests.test_telephone.TestTelephone"
            ".test_passing_a_class)"
        )
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(bool)
        my_expectation = "I got: <class 'bool'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(int)
        my_expectation = "I got: <class 'int'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(float)
        my_expectation = "I got: <class 'float'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(str)
        my_expectation = "I got: <class 'str'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(tuple)
        my_expectation = "I got: <class 'tuple'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(list)
        my_expectation = "I got: <class 'list'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(set)
        my_expectation = "I got: <class 'set'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(dict)
        my_expectation = "I got: <class 'dict'>"
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError