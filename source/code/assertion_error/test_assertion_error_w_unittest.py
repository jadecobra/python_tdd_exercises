import unittest


class TestAssertionError(unittest.TestCase):

    an_integer = 0
    a_float = 0.0
    a_string = ''
    a_tuple = ()
    a_list = []
    a_set = set()
    a_dictionary = {}

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

        assert self.an_integer is not None
        self.assertIsNot(self.an_integer, None)

        assert self.a_float is not None
        self.assertIsNot(self.a_float, None)

        assert self.a_string is not None
        self.assertIsNot(self.a_string, None)

        assert self.a_tuple is not None
        self.assertIsNot(self.a_tuple, None)

        assert self.a_list is not None
        self.assertIsNot(self.a_list, None)

        assert self.a_set is not None
        self.assertIsNot(self.a_set, None)

        assert self.a_dictionary is not None
        self.assertIsNot(self.a_dictionary, None)

    def test_assertion_error_w_false(self):
        assert None is not False
        self.assertIsNot(None, False)

        assert False is False
        self.assertIs(False, False)

        assert True is not False
        self.assertIsNot(True, False)

        assert self.an_integer is not False
        self.assertIsNot(self.an_integer, False)

        assert self.a_float is not False
        self.assertIsNot(self.a_float, False)

        assert self.a_string is not False
        self.assertIsNot(self.a_string, False)

        assert self.a_tuple is not False
        self.assertIsNot(self.a_tuple, False)

        assert self.a_list is not False
        self.assertIsNot(self.a_list, False)

        assert self.a_set is not False
        self.assertIsNot(self.a_set, False)

        assert self.a_dictionary is not False
        self.assertIsNot(self.a_dictionary, False)

    def test_assertion_error_w_true(self):
        assert None is not True
        self.assertIsNot(None, True)

        assert False is not True
        self.assertIsNot(False, True)

        assert True is True
        self.assertIs(True, True)

        assert self.an_integer is not True
        self.assertIsNot(self.an_integer, True)

        assert self.a_float is not True
        self.assertIsNot(self.a_float, True)

        assert self.a_string is not True
        self.assertIsNot(self.a_string, True)

        assert self.a_tuple is not True
        self.assertIsNot(self.a_tuple, True)

        assert self.a_list is not True
        self.assertIsNot(self.a_list, True)

        assert self.a_set is not True
        self.assertIsNot(self.a_set, True)

        assert self.a_dictionary is not True
        self.assertIsNot(self.a_dictionary, True)

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

    def will_not_run():
        assert False == True
        self.assertEqual(False, True)

    def test_failure(self):
        assert False == False
        self.assertEqual(False, False)


# NOTES
# a dictionary is not the same object as True
# a dictionary is not the same object as False
# a dictionary is not the same object as None
# a set is not the same object as True
# a set is not the same object as False
# a set is not the same object as None
# a list is not the same object as True
# a list is not the same object as False
# a list is not the same object as None
# a tuple is not the same object as True
# a tuple is not the same object as False
# a tuple is not the same object as None
# a string is not the same object as True
# a string is not the same object as False
# a string is not the same object as None
# a float is not the same object as True
# a float is not the same object as False
# a float is not the same object as None
# an integer is not the same object as True
# an integer is not the same object as False
# an integer is not the same object as None
# True is True and equal to True
# True is not the same object as False and NOT equal to False
# True is not the same object as None and NOT equal to None
# False is not the same object as True and NOT equal to True
# False is False and equal to False
# False is not the same object as None and NOT equal to None
# None is not the same object as True and NOT equal to True
# None is not the same object as False and NOT equal to False
# None is None and equal to None


# Exceptions seen
# AssertionError
# AttributeError
# NameError
# TypeError