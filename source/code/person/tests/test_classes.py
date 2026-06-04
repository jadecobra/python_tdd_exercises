import src.classes
import unittest


class TestClasses(unittest.TestCase):

    def test_making_a_class_w_pass(self):
        assert isinstance(
            src.classes.WPass, object
        )
        self.assertIsInstance(
            src.classes.WPass, object
        )

    def test_making_a_class_w_parentheses(self):
        assert isinstance(
            src.classes.WParentheses, object
        )
        self.assertIsInstance(
            src.classes.WParentheses, object
        )

    def test_making_a_class_w_object(self):
        assert isinstance(
            src.classes.WObject, object
        )
        self.assertIsInstance(
            src.classes.WObject, object
        )

        assert isinstance(None, object)
        self.assertIsInstance(None, object)

        assert isinstance(bool, object)
        self.assertIsInstance(bool, object)

        assert isinstance(int, object)
        self.assertIsInstance(int, object)

        assert isinstance(float, object)
        self.assertIsInstance(float, object)

        assert isinstance(str, object)
        self.assertIsInstance(str, object)

        assert isinstance(tuple, object)
        self.assertIsInstance(tuple, object)

        assert isinstance(list, object)
        self.assertIsInstance(list, object)

        assert isinstance(set, object)
        self.assertIsInstance(set, object)

        assert isinstance(dict, object)
        self.assertIsInstance(dict, object)

    def test_attributes_and_methods_of_objects(self):
        reality = dir(object)
        my_expectation = [
            '__class__',
            '__delattr__',
            '__dir__',
            '__doc__',
            '__eq__',
            '__format__',
            '__ge__',
            '__getattribute__',
            '__getstate__',
            '__gt__',
            '__hash__',
            '__init__',
            '__init_subclass__',
            '__le__',
            '__lt__',
            '__ne__',
            '__new__',
            '__reduce__',
            '__reduce_ex__',
            '__repr__',
            '__setattr__',
            '__sizeof__',
            '__str__',
            '__subclasshook__'
        ]
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError