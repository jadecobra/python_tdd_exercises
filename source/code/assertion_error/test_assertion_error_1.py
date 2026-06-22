import unittest


class TestAssertionError(unittest.TestCase):

    def test_assert_keyword(self):
        reality = 1 + 1
        my_expectation = 2
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = '1' + '1'
        my_expectation = '11'
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = 'I am' + ' alive'
        my_expectation = 'I am alive'
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIs(None, None)

        assert False is not None
        self.assertIsNot(False, None)

        assert True is not None
        self.assertIsNot(True, None)

        an_integer = 0
        assert an_integer is not None
        self.assertIsNot(an_integer, None)

        a_float = 0.0
        assert a_float is not None
        self.assertIsNot(a_float, None)

        a_string = 'a string'
        assert a_string is not None
        self.assertIsNot(a_string, None)

        a_tuple = (1, 2, 3, 'n')
        assert a_tuple is not None
        self.assertIsNot(a_tuple, None)

        a_list = [1, 2, 3, 'n']
        assert a_list is not None
        self.assertIsNot(a_list, None)

        a_set = {1, 2, 3, 'n'}
        assert a_set is not None
        self.assertIsNot(a_set, None)

        a_dictionary = {'key': 'value'}
        assert a_dictionary is not None
        self.assertIsNot(a_dictionary, None)

    def test_assertion_error_w_false(self):
        assert None is not False
        self.assertIsNot(None, False)

        assert False is False
        self.assertIs(False, False)

        assert True is not False
        self.assertIsNot(True, False)

        an_integer = 0
        assert an_integer is not False
        self.assertIsNot(an_integer, False)

        a_float = 0.0
        assert a_float is not False
        self.assertIsNot(a_float, False)

        a_string = 'a string'
        assert a_string is not False
        self.assertIsNot(a_string, False)

        a_tuple = (1, 2, 3, 'n')
        assert a_tuple is not False
        self.assertIsNot(a_tuple, False)

        a_list = [1, 2, 3, 'n']
        assert a_list is not False
        self.assertIsNot(a_list, False)

        a_set = {1, 2, 3, 'n'}
        assert a_set is not False
        self.assertIsNot(a_set, False)

        a_dictionary = {'key': 'value'}
        assert a_dictionary is not False
        self.assertIsNot(a_dictionary, False)

    def test_assertion_error_w_true(self):
        assert None is not True
        self.assertIsNot(None, True)

        assert False is not True
        self.assertIsNot(False, True)

        assert True is True
        self.assertIs(True, True)

        an_integer = 0
        assert an_integer is not True
        self.assertIsNot(an_integer, True)

        a_float = 0.0
        assert a_float is not True
        self.assertIsNot(a_float, True)

        a_string = 'a string'
        assert a_string is not True
        self.assertIsNot(a_string, True)

        a_tuple = (1, 2, 3, 'n')
        assert a_tuple is not True
        self.assertIsNot(a_tuple, True)

        a_list = [1, 2, 3, 'n']
        assert a_list is not True
        self.assertIsNot(a_list, True)

        a_set = {1, 2, 3, 'n'}
        assert a_set is not True
        self.assertIsNot(a_set, True)

        a_dictionary = {'key': 'value'}
        assert a_dictionary is not True
        self.assertIsNot(a_dictionary, True)

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

    def test_assertion_error_w_is_vs_equal(self):
        assert 0 is not 0.0
        self.assertIsNot(0, 0.0)

        assert 0 == 0.0
        self.assertEqual(0, 0.0)


# NOTES
# a dictionary is not True
# a dictionary is not False
# a dictionary is not None
# a set is not True
# a set is not False
# a set is not None
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