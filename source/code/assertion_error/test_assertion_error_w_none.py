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
        self.assertIsNone(None)
        self.assertIsNotNone(False)
        self.assertIsNotNone(True)
        self.assertIsNotNone(self.an_integer)
        self.assertIsNotNone(self.a_float)
        self.assertIsNotNone(self.a_string)
        self.assertNotNone(self.a_tuple)
        self.assertIsNotNone(self.a_list)
        self.assertIsNoneNone(self.a_set)
        self.assertIsNotNone(self.a_dictionary)

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
# None is not False and NOT equal to True
# None is None and equal to None


# Exceptions seen
# AssertionError
# AttributeError
# NameError
# TypeError