import unittest
import module


class TestAttributeError(unittest.TestCase):

    def test_attribute_error_w_variables(self):
        src.module.variable_00
        src.module.variable_01
        src.module.variable_02
        src.module.variable_03

    def test_attribute_error_w_functions(self):
        src.module.function_00()
        src.module.function_01()
        src.module.function_02()
        src.module.function_03()

    def test_attribute_error_w_classes(self):
        src.module.Class00()
        src.module.Class01()
        src.module.Class02()
        src.module.Class03()

    def test_attribute_error_w_class_attributes(self):
        src.module.Class.attribute_00
        src.module.Class.attribute_01
        src.module.Class.attribute_02
        src.module.Class.attribute_03

    def test_attribute_error_w_class_methods(self):
        src.module.Class.method_0()
        src.module.Class.method_1()
        src.module.Class.method_2()
        src.module.Class.method_3()

# Exceptions Encountered
# AssertionError
# ModuleNotFoundError
# AttributeError
# NameError
# TypeError
# SyntaxError