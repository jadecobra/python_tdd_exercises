import exceptions
import module
import unittest


class TestExceptions(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module

    def test_catching_attribute_error_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
            module.non_existent_function()
            module.NonExistentClass()

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception()

    def test_catching_failures(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.raises_exception
            ),
            'failed'
        )

    def test_catching_successes(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.does_not_raise_exception
            ),
            'succeeded'
        )

    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(
                exceptions.does_not_raise_exception
            ),
            'always returns this'
        )
        self.assertEqual(
            exceptions.always_returns(
                exceptions.raises_exception
            ),
            'always returns this'
        )

# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError