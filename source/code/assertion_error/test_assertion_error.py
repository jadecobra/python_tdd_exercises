import unittest


class TestAssertionError(unittest.TestCase):

    def test_what_is_an_assertion(self):
        reality = 1 + 1
        my_expectation = 2
        # my_expectation = 11
        # reality == my_expectation
        assert reality == my_expectation
        # self.assertNotEqual(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

        reality = '1' + '1'
        # my_expectation = '2'
        my_expectation = '11'
        # reality == my_expectation
        assert reality == my_expectation
        # self.assertNotEqual(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

        reality = 'I am' + ' alive'
        # my_expectation = '11'
        my_expectation = 'I am alive'
        # reality == my_expectation
        assert reality == my_expectation
        # self.assertNotEqual(reality, my_expectation)
        self.assertEqual(reality, my_expectation)

    def test_assertion_error_w_none(self):
        # assert None is not None
        assert None is None
        # self.assertIsNot(None, None)
        self.assertIs(None, None)

        # assert False is None
        assert False is not None
        # self.assertIs(False, None)
        self.assertIsNot(False, None)

        # assert True is None
        assert True is not None
        # self.assertIs(True, None)
        self.assertIsNot(True, None)

        # assert 0 is None
        assert 0 is not None
        # self.assertIs(0, None)
        self.assertIsNot(0, None)

        # assert 0.0 is None
        assert 0.0 is not None
        # self.assertIs(0.0, None)
        self.assertIsNot(0.0, None)

        # assert 'a string' is None
        assert 'a string' is not None
        # self.assertIs('a string', None)
        self.assertIsNot('a string', None)

        # assert (1, 2, 3, 'n') is None
        assert (1, 2, 3, 'n') is not None
        # self.assertIs((1, 2, 3, 'n'), None)
        self.assertIsNot((1, 2, 3, 'n'), None)

        # assert [1, 2, 3, 'n'] is None
        assert [1, 2, 3, 'n'] is not None
        # self.assertIs([1, 2, 3, 'n'], None)
        self.assertIsNot([1, 2, 3, 'n'], None)

        # assert {1, 2, 3, 'n'} is None
        assert {1, 2, 3, 'n'} is not None
        # self.assertIs({1, 2, 3, 'n'}, None)
        self.assertIsNot({1, 2, 3, 'n'}, None)

        # assert {'key': 'value'} is None
        assert {'key': 'value'} is not None
        # self.assertIs({'key': 'value'}, None)
        self.assertIsNot({'key': 'value'}, None)

    def test_assertion_error_w_false(self):
        # assert None is False
        assert None is not False
        # self.assertIs(None, False)
        self.assertIsNot(None, False)

        # assert False is not False
        assert False is False
        # self.assertIsNot(False, False)
        self.assertIs(False, False)

        # assert True is False
        assert True is not False
        # self.assertIs(True, False)
        self.assertIsNot(True, False)

        # assert 0 is False
        assert 0 is not False
        # self.assertIs(0, False)
        self.assertIsNot(0, False)

        # assert 0.0 is False
        assert 0.0 is not False
        # self.assertIs(0.0, False)
        self.assertIsNot(0.0, False)

        # assert 'a string' is False
        assert 'a string' is not False
        # self.assertIs('a string', False)
        self.assertIsNot('a string', False)

        # assert (1, 2, 3, 'n') is False
        assert (1, 2, 3, 'n') is not False
        # self.assertIs((1, 2, 3, 'n'), False)
        self.assertIsNot((1, 2, 3, 'n'), False)

        # assert [1, 2, 3, 'n'] is False
        assert [1, 2, 3, 'n'] is not False
        # self.assertIs([1, 2, 3, 'n'], False)
        self.assertIsNot([1, 2, 3, 'n'], False)

        # assert {1, 2, 3, 'n'} is False
        assert {1, 2, 3, 'n'} is not False
        # self.assertIs({1, 2, 3, 'n'}, False)
        self.assertIsNot({1, 2, 3, 'n'}, False)

        # assert {'key': 'value'} is False
        assert {'key': 'value'} is not False
        # self.assertIs({'key': 'value'}, False)
        self.assertIsNot({'key': 'value'}, False)

    def test_assertion_error_w_true(self):
        # assert None is True
        assert None is not True
        # self.assertIs(None, True)
        self.assertIsNot(None, True)

        # assert False is True
        assert False is not True
        # self.assertIs(False, True)
        self.assertIsNot(False, True)

        # assert True is not True
        assert True is True
        # self.assertIsNot(True, True)
        self.assertIs(True, True)

        # assert 0 is True
        assert 0 is not True
        # self.assertIs(0, True)
        self.assertIsNot(0, True)

        # assert 0.0 is True
        assert 0.0 is not True
        # self.assertIs(0.0, True)
        self.assertIsNot(0.0, True)

        # assert 'a string' is True
        assert 'a string' is not True
        # self.assertIs('a string', True)
        self.assertIsNot('a string', True)

        # assert (1, 2, 3, 'n') is True
        assert (1, 2, 3, 'n') is not True
        # self.assertIs((1, 2, 3, 'n'), True)
        self.assertIsNot((1, 2, 3, 'n'), True)

        # assert [1, 2, 3, 'n'] is True
        assert [1, 2, 3, 'n'] is not True
        # self.assertIs([1, 2, 3, 'n'], True)
        self.assertIsNot([1, 2, 3, 'n'], True)

        # assert {1, 2, 3, 'n'} is True
        assert {1, 2, 3, 'n'} is not True
        # self.assertIs({1, 2, 3, 'n'}, True)
        self.assertIsNot({1, 2, 3, 'n'}, True)

        # assert {'key': 'value'} is True
        assert {'key': 'value'} is not True
        # self.assertIs({'key': 'value'}, True)
        self.assertIsNot({'key': 'value'}, True)

    def test_assertion_error_w_equality(self):
        # assert None != None
        assert None == None
        # self.assertNotEqual(None, None)
        self.assertEqual(None, None)

        # assert False == None
        assert False != None
        # self.assertEqual(False, None)
        self.assertNotEqual(False, None)

        # assert False == True
        assert False != True
        # self.assertEqual(False, True)
        self.assertNotEqual(False, True)

        # assert False != False
        assert False == False
        # self.assertNotEqual(False, False)
        self.assertEqual(False, False)

        # assert True == None
        assert True != None
        # self.assertEqual(True, None)
        self.assertNotEqual(True, None)

        # assert True != True
        assert True == True
        # self.assertNotEqual(True, True)
        self.assertEqual(True, True)


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