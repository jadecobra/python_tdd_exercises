import unittest


class WPass: pass


class WParentheses(): pass


class WObject(object): pass


class TestObjects(unittest.TestCase):

    def test_what_is_an_object(self):
        for an_object in (
            WPass, WParentheses, WObject,
            bool, int, float, str,
            tuple, list, set, dict
        ):
            with self.subTest(an_object):
                assert isinstance(an_object(), object)
                self.assertIsInstance(an_object(), object)
                assert issubclass(an_object, object)
                self.assertIsSubclass(an_object, object)

    def test_is_none_an_object(self):
        assert isinstance(None, object)
        self.assertIsInstance(None, object)

        # fails because None is not a class
        # assert issubclass(None, object)
        # self.assertIsSubclass(None, object)

    def test_dir_object(self):
        reality = dir(object)
        my_expectation = [
            '__class__', '__delattr__', '__dir__',
            '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__',
            '__getstate__', '__gt__', '__hash__',
            '__init__', '__init_subclass__', '__le__',
            '__lt__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__str__', '__subclasshook__'
        ]
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError