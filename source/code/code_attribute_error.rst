
#####################################
AttributeError: Tests and Solutions
#####################################

**********
tests
**********

Here is the code in ``tests/test_attribute_error.py``

.. code-block:: python

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

**********
solutions
**********

Here are the solutions in ``module.py``

.. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None
    variable_3 = None

    def function_0():
        return None

    def function_1():
        return None

    def function_2():
        return None

    def function_3():
        return None


    class Class0():
        pass


    class Class1():
        pass


    class Class2():
        pass


    class Class3():
        pass


    class Class():
        attribute_0 = None
        attribute_1 = None
        attribute_2 = None
        attribute_3 = None

        def method_0():
            return None

        def method_1():
            return None

        def method_2():
            return None

        def method_3():
            return None