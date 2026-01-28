import unittest


class TestModuleNotFoundError(unittest.TestCase):

    def test_module_not_found_error(self):
        import src.module_00
        import src.module_01
        import src.module_02
        import src.module_03
        import src.module_04
        import src.module_05
        import src.module_06
        import src.module_07
        import src.module_08
        import src.module_09


# Exceptions seen
# AssertionError
# ModuleNotFoundError