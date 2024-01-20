import unittest
import module


class TestAttributeErrors(unittest.TestCase):

    def test_defining_variables_to_solve_attribute_errors(self):
        module.variable_0
        module.variable_1
        module.variable_2
        module.variable_3

    def test_defining_functions_to_solve_attribute_errors(self):
        module.function_0()
        module.function_1()
        module.function_2()
        module.function_3()

    def test_defining_classes_to_solve_attribute_errors(self):
        module.Class0()
        module.Class1()
        module.Class2()
        module.Class3()

    def test_defining_attributes_in_classes_to_solve_attribute_errors(self):
        module.Class.attribute_0
        module.Class.attribute_1
        module.Class.attribute_2
        module.Class.attribute_3

    def test_defining_functions_in_classes_to_solve_attribute_errors(self):
        module.Class.method_0()
        module.Class.method_1()
        module.Class.method_2()
        module.Class.method_3()

# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# AttributeError
# NameError
# TypeError
# SyntaxError