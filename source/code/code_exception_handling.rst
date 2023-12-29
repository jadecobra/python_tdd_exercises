
################################################
How to handle Exceptions: Tests and Solutions
################################################


tests
-----

Here is the code in ``tests/test_exception_handling.py``

.. code-block:: python

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
                "always_returns_this"
            )
            self.assertEqual(
                exceptions.always_returns(
                    exceptions.raises_exception_error
                ),
                'always_returns_this'
            )

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

solutions
---------

Here are the solutions in ``exceptions.py``

.. code-block:: python

    def raises_exception_error():
        raise Exception

    def does_not_raise_exception_error():
        return None

    def exception_handler(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

    def always_returns(function):
        try:
            function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'
        finally:
            return 'always_returns_this'