import src.attribute_error
import unittest


class TestAttributeError(unittest.TestCase):

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03
        src.attribute_error.variable_04
        src.attribute_error.variable_05
        src.attribute_error.variable_06
        src.attribute_error.variable_07
        src.attribute_error.variable_08
        src.attribute_error.variable_09

    def test_attribute_error_w_functions(self):
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()
        src.attribute_error.function_07()
        src.attribute_error.function_08()
        src.attribute_error.function_09()

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.AnObject.attribute_00
        src.attribute_error.AnObject.attribute_01
        src.attribute_error.AnObject.attribute_02
        src.attribute_error.AnObject.attribute_03
        src.attribute_error.AnObject.attribute_04
        src.attribute_error.AnObject().attribute_05
        src.attribute_error.AnObject().attribute_06
        src.attribute_error.AnObject().attribute_07
        src.attribute_error.AnObject().attribute_08
        src.attribute_error.AnObject().attribute_09

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.AnObject.method_00()
        src.attribute_error.AnObject.method_01
        src.attribute_error.AnObject().method_02()
        src.attribute_error.AnObject().method_03
        src.attribute_error.AnObject().method_04()
        src.attribute_error.AnObject.method_05
        src.attribute_error.AnObject.method_06()
        src.attribute_error.AnObject.method_07
        src.attribute_error.AnObject().method_08()
        src.attribute_error.AnObject().method_09


# Exceptions seen
# AssertionError
# AttributeError
# NameError
# TypeError
# SyntaxError