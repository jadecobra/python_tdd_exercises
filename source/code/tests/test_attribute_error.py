import unittest
import src.attribute_error


class TestAttributeError(unittest.TestCase):

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03

    def test_attribute_error_w_functions(self):
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.Class.attribute_00
        src.attribute_error.Class.attribute_01
        src.attribute_error.Class.attribute_02
        src.attribute_error.Class.attribute_03

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.Class.method_00()
        src.attribute_error.Class.method_01()
        src.attribute_error.Class.method_02()
        src.attribute_error.Class.method_03()


# Exceptions Encountered
# AssertionError
# AttributeError
# NameError
# TypeError
# SyntaxError