import unittest


class TestAssertionError(unittest.TestCase):

    def test_what_is_an_assertion(self):
        reality = 1 + 1
        my_expectation = 2
        assert reality == my_expectation
        self.assertEqual(
            reality, my_expectation
        )

        reality = '1' + '1'
        my_expectation = '11'
        assert reality == my_expectation
        self.assertEqual(
            reality, my_expectation
        )

        reality = 'I am' + ' alive'
        my_expectation = 'I am alive'
        assert reality == my_expectation
        self.assertEqual(
            reality, my_expectation
        )

    def test_assertion_error_w_none(self):
        assert None is None
        assert False is not None
        assert True is not None
        assert 0 is not None
        assert 0.0 is not None
        assert 'a string' is not None
        assert (1, 2, 3, 'n') is not None
        assert [1, 2, 3, 'n'] is not None
        assert {1, 2, 3, 'n'} is not None
        assert {'key': 'value'} is not None

    def test_assertion_error_w_false(self):
        assert None is not False
        assert False is False
        assert True is not False
        assert 0 is not False
        assert 0.0 is not False
        assert 'a string' is not False
        assert (1, 2, 3, 'n') is not False
        assert [1, 2, 3, 'n'] is not False
        assert {1, 2, 3, 'n'} is not False
        assert {'key': 'value'} is not False

    def test_assertion_error_w_true(self):
        assert None is not True
        assert False is not True
        assert True is True
        assert 0 is not True
        assert 0.0 is not True
        assert 'a string' is not True
        assert (1, 2, 3, 'n') is not True
        assert [1, 2, 3, 'n'] is not True
        assert {1, 2, 3, 'n'} is not True
        assert {'key': 'value'} is not True

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False != None
        self.assertNotEqual(False, None)

        assert False != True
        self.assertNotEqual(False, True)

        assert False == False
        self.assertEqual(False, False)

        assert True != None
        self.assertNotEqual(True, None)

        assert True == True
        self.assertEqual(True, True)


# NOTES
# a dictionary is not True
# a dictionary is not False
# a dictionary is not None
# a set is not False
# a set is not None
# a list is not False
# a list is not True
# a list is not False
# a list is not None
# a tuple is not True
# a tuple is not False
# a tuple is not None
# a string is not True
# a string is not False
# a string is not None
# a float is not True
# a float is not False
# a float is not None
# an integer is not True
# an integer is not False
# an integer is not None
# True is True and equal to True
# True is not False and NOT equal to False
# True is not None and NOT equal to None
# False is not True and NOT equal to True
# False is False and equal to False
# False is not None and NOT equal to None
# None is not True and NOT equal to True
# None is not False and NOT equal to False
# None is None and equal to None

# Exceptions seen
# AssertionError