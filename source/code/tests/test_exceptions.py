import exceptions
import module
import unittest


class TestExceptionHandling(unittest.TestCase):

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import non_existent_module

    def test_catching_attribute_errors_in_tests(self):
        with self.assertRaises(AttributeError):
            module.non_existent_attribute
            module.non_existent_function()
            module.NonExistentClass()

    def test_catching_exceptions(self):
        with self.assertRaises(Exception):
            exceptions.raises_exception_error()

    def test_catching_things_that_fail(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.raises_exception_error
            ),
            'failed'
        )

    def test_catching_things_that_succeed(self):
        self.assertEqual(
            exceptions.exception_handler(
                exceptions.does_not_raise_exception_error
            ),
            'succeeded'
        )

    def test_finally_always_returns(self):
        self.assertEqual(
            exceptions.always_returns(
                exceptions.does_not_raise_exception_error
            ),
            'always returns this'
        )
        self.assertEqual(
            exceptions.always_returns(
                exceptions.raises_exception_error
            ),
            'always returns this'
        )

# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# NameError
# AttributeError
# TypeError