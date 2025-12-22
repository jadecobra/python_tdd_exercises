import unittest


class TestModuleNotFoundError(unittest.TestCase):

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02
        import src.module_03


# Exceptions seen
# AssertionError
# ModuleNotFoundError