import src.attribute_error


def test_attribute_error_w_variables():
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


def test_attribute_error_w_functions():
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


def test_attribute_error_w_class_attributes():
    src.attribute_error.AClass.attribute_00
    src.attribute_error.AClass().attribute_01
    src.attribute_error.AClass.attribute_02
    src.attribute_error.AClass().attribute_03
    src.attribute_error.AClass.attribute_04
    src.attribute_error.AClass().attribute_05
    src.attribute_error.AClass().attribute_06
    src.attribute_error.AClass.attribute_07
    src.attribute_error.AClass.attribute_08
    src.attribute_error.AClass().attribute_09


def test_attribute_error_w_class_methods():
    src.attribute_error.AClass().method_00()
    src.attribute_error.AClass().method_01()
    src.attribute_error.AClass().method_02()
    src.attribute_error.AClass().method_03()
    src.attribute_error.AClass().method_04()
    src.attribute_error.AClass().method_05()
    src.attribute_error.AClass().method_06()
    src.attribute_error.AClass().method_07()
    src.attribute_error.AClass().method_08()
    src.attribute_error.AClass().method_09()


# Exceptions seen
# AssertionError
# ModuleNotFoundError
# AttributeError
# NameError
# TypeError
# SyntaxError