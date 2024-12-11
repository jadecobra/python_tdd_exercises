import unittest


class TestAssertionError(unittest.TestCase):

    def test_assertion_error_w_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNone(None)

    def test_assertion_error_w_false(self):
        assert True is not False
        self.assertFalse(False)

    def test_assertion_error_w_true(self):
        assert False is not True
        self.assertTrue(True)

    def test_assertion_error_w_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert None == None
        self.assertEqual(None, None)

        assert False == False
        self.assertEqual(False, False)

        assert True != False
        self.assertNotEqual(True, False)

        assert True == True
        self.assertEqual(True, True)

        assert False != True
        self.assertNotEqual(False, True)


# NOTES
# False is not True and is not equal to True
# True is True and is equal to True
# True is not False and is not equal to False
# False is False and is equal to False
# None is None and is equal to None
# True is not None is not equal to None
# False is not None is not equal to None


# Exceptions Encountered
# AssertionError
