import unittest


class WPass: pass


class WParentheses(self): pass


class WObject(object): pass


class TestClass(unittest.TestCase):

    def test_making_a_class_w_pass(self):
        assert isinstance(WPass(), object)
        self.assertIsInstance(WPass(), object)
        assert issubclass(WPass, object)
        self.assertIsSubclass(WPass, object)
        self.assertIsSubclass(WPass, object)

    def test_making_a_class_w_parentheses(self):
        assert isinstance(WParentheses(), object)
        self.assertIsInstance(WParentheses(), object)
        assert issubclass(WParentheses, object)
        self.assertIsSubclass(WParentheses, object)

    def test_making_a_class_w_object(self):
        assert isinstance(WObject(), object)
        self.assertIsInstance(WObject(), object)
        assert issubclass(WObject, object)
        self.assertIsSubclass(WObject, object)

    def test_is_none_an_object(self):
        assert isinstance(None, object)
        self.assertIsInstance(None, object)
        # assert issubclass(None, object)
        # fails because None is not a class
        # self.assertIsSubclass(None, object)

    def test_is_a_boolean_an_object(self):
        assert isinstance(bool, object)
        self.assertIsInstance(bool, object)
        assert issubclass(bool, object)
        self.assertIsSubclass(bool, object)

    def test_is_an_integer_an_object(self):
        assert isinstance(int, object)
        self.assertIsInstance(int, object)
        assert issubclass(int, object)
        self.assertIsSubclass(int, object)

    def test_is_a_float_an_object(self):
        assert isinstance(float, object)
        self.assertIsInstance(float, object)
        assert issubclass(float, object)
        self.assertIsSubclass(float, object)

    def test_is_a_string_an_object(self):
        assert isinstance(str, object)
        self.assertIsInstance(str, object)
        assert issubclass(str, object)
        self.assertIsSubclass(str, object)

    def test_is_a_tuple_an_object(self):
        assert isinstance(tuple, object)
        self.assertIsInstance(tuple, object)
        assert issubclass(tuple, object)
        self.assertIsSubclass(tuple, object)

    def test_is_a_list_an_object(self):
        assert isinstance(list, object)
        self.assertIsInstance(list, object)
        assert issubclass(list, object)
        self.assertIsSubclass(list, object)

    def test_is_a_set_an_object(self):
        assert isinstance(set, object)
        self.assertIsInstance(set, object)
        assert issubclass(set, object)
        self.assertIsSubclass(set, object)

    def test_is_a_dictionary_an_object(self):
        assert isinstance(dict, object)
        self.assertIsInstance(dict, object)
        assert issubclass(dict, object)
        self.assertIsSubclass(dict, object)

    def test_dir_object(self):
        reality = dir(object)
        my_expectation = [
            '__class__', '__delattr__', '__dir__',
            '__doc__', '__eq__', '__format__', '__ge__',
            '__getattribute__', '__getstate__', '__gt__',
            '__hash__', '__init__', '__init_subclass__',
            '__le__', '__lt__', '__ne__', '__new__',
            '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__'
        ]
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# TypeError