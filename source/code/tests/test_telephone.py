import src.telephone
import unittest


class TestTelephone(unittest.TestCase):

    def test_passing_a_string(self):
        reality = src.telephone.text('hello')
        my_expectation = 'I got: hello'
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text('yes')
        my_expectation = 'I got: yes'
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
        reality = src.telephone.text(1234)
        my_expectation = 'I got: 1234'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_float(self):
        reality = src.telephone.text(1.234)
        my_expectation = 'I got: 1.234'
        self.assertEqual(reality, my_expectation)

    def test_passing_a_tuple(self):
        reality = src.telephone.text((1, 2, 3, 'n'))
        my_expectation = "I got: (1, 2, 3, 'n')"
        self.assertEqual(reality, my_expectation)

    def test_passing_a_list(self):
        reality = src.telephone.text([1, 2, 3, "n"])
        my_expectation = "I got: [1, 2, 3, 'n']"
        self.assertEqual(reality, my_expectation)

    def test_passing_a_dictionary(self):
        reality = src.telephone.text(
            {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
        )
        my_expectation = (
            "I got: "
            "{'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
        )
        self.assertEqual(reality, my_expectation)

    def test_passing_a_class(self):
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        self.assertEqual(reality, my_expectation)

        reality = src.telephone.text(TestTelephone)
        my_expectation = (
            "I got: <class "
            "'tests.test_telephone.TestTelephone'>"
        )
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError