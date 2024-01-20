import unittest


class TestAssertionErrors(unittest.TestCase):

    def test_assertion_errors_with_none(self):
        assert False is not None
        self.assertIsNotNone(False)

        assert True is not None
        self.assertIsNotNone(True)

        assert None is None
        self.assertIsNone(None)

    def test_assertion_errors_with_false(self):
        assert False is False
        self.assertFalse(False)

    def test_assertion_errors_with_true(self):
        assert True is True
        self.assertTrue(True)

    def test_assertion_errors_with_equality(self):
        assert False != None
        self.assertNotEqual(False, None)

        assert True != None
        self.assertNotEqual(True, None)

        assert True == True
        self.assertEqual(True, True)

        assert True != False
        self.assertNotEqual(True, False)

        assert False == False
        self.assertEqual(False, False)

        assert False != True
        self.assertNotEqual(False, True)

        assert None == None
        self.assertEqual(None, None)

# Exceptions Encountered
# AssertionError