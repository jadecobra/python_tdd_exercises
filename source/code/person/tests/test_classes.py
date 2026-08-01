import src.classes
import unittest


class TestClasses(unittest.TestCase):

    def test_making_a_class_w_pass(self):
        an_instance = src.classes.WPass()
        assert isinstance(an_instance, object)
        self.assertIsInstance(an_instance, object)

        a_class = src.classes.WPass
        assert issubclass(a_class, object)
        self.assertIsSubclass(a_class, object)

    def test_making_a_class_w_parentheses(self):
        an_instance = src.classes.WParentheses()
        assert isinstance(an_instance, object)
        self.assertIsInstance(an_instance, object)

        a_class = src.classes.WParentheses
        assert issubclass(a_class, object)
        self.assertIsSubclass(a_class, object)

    def test_making_a_class_w_object(self):
        an_instance = src.classes.WObject()
        assert isinstance(an_instance, object)
        self.assertIsInstance(an_instance, object)

        a_class = src.classes.WObject
        assert issubclass(a_class, object)
        self.assertIsSubclass(a_class, object)

    def test_is_none_an_object(self):
        assert isinstance(None, object)
        self.assertIsInstance(None, object)

    def test_is_a_boolean_an_object(self):
        assert issubclass(bool, object)
        self.assertIsSubclass(bool, object)

    def test_is_an_integer_an_object(self):
        assert issubclass(int, object)
        self.assertIsSubclass(int, object)

    def test_is_a_float_an_object(self):
        assert issubclass(float, object)
        self.assertIsSubclass(float, object)

    def test_is_a_string_an_object(self):
        assert issubclass(str, object)
        self.assertIsSubclass(str, object)

    def test_is_a_tuple_an_object(self):
        assert issubclass(tuple, object)
        self.assertIsSubclass(tuple, object)

    def test_is_a_list_an_object(self):
        assert issubclass(list, object)
        self.assertIsSubclass(list, object)

    def test_is_a_set_an_object(self):
        assert issubclass(set, object)
        self.assertIsSubclass(set, object)

    def test_is_a_dictionary_an_object(self):
        assert issubclass(dict, object)
        self.assertIsSubclass(dict, object)

    def test_dir_object(self):
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