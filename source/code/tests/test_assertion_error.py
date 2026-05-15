import unittest


class TestAssertionError(unittest.TestCase):

    def test_what_is_an_assertion(self):
        reality = 1 + 1
        my_expectation = 2
        assert reality == my_expectation

        reality = '1' + '1'
        my_expectation = '11'
        assert reality == my_expectation

        reality = 'I am' + ' alive'
        my_expectation = 'I am alive'
        assert reality == my_expectation

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert 0 is not None
        self.assertIsNotNone(0)

        assert 0.0 is not None
        self.assertIsNotNone(0.0)

        assert 'a string' is not None
        self.assertIsNotNone('a string')

        assert (1, 2, 3, 'n') is not None
        self.assertIsNotNone((1, 2, 3, 'n'))

        assert [1, 2, 3, 'n'] is not None
        self.assertIsNotNone([1, 2, 3, 'n'])

        assert {1, 2, 3, 'n'} is not None
        self.assertIsNotNone({1, 2, 3, 'n'})

        assert {'key': 'value'} is not None
        self.assertIsNotNone({'key': 'value'})

    def test_assertion_error_w_false(self):
        assert True is not False
        self.assertFalse(False)

    def test_assertion_error_w_true(self):
        assert False is not True
        self.assertTrue(True)

    def test_assertion_error_w_equality(self):
        assert None == None
        self.assertEqual(None, None)

        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True != False
        self.assertNotEqual(True, False)

        assert False == False
        self.assertEqual(False, False)

        assert False != True
        self.assertNotEqual(False, True)

        assert True == True
        self.assertEqual(True, True)


# NOTES
# True is True and equal to True
# False is not True and not equal to True
# False is False and equal to False
# True is not False and not equal to False
# True is not None and not equal to None
# False is not None and not equal to None
# None is None and equal to None


# Exceptions seen
# AssertionError