import unittest


class TestAssertionError(unittest.TestCase):

    def test_what_is_an_assertion(self):
        assert 1 + 1 == 2
        self.assertEqual(1+1, 2)

        assert '1' + '1' == '11'
        self.assertEqual('1'+'1', '11')

        assert 'I am' + ' a programmer' == 'I am a programmer'
        self.assertEqual('I am'+' a programmer', 'I am a programmer')

    def test_assertion_error_w_none(self):
        assert None is None
        self.assertIsNone(None)

        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

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