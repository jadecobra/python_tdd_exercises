import src.classes
import unittest


class TestClasses(unittest.TestCase):

    def test_make_a_class_w_pass(self):
        self.assertIsInstance(src.classes.WithPass, object)

    def test_make_a_class_w_parentheses(self):
        self.assertIsInstance(
            src.classes.WithParentheses, object
        )

    def test_make_a_class_w_object(self):
        self.assertIsInstance(
            src.classes.WithObject, object
        )

    def test_make_a_class_w_attributes(self):
        self.assertEqual(
            src.classes.WithAttributes.attribute,
            'attribute'
        )

    def test_make_a_class_w_methods(self):
        self.assertEqual(
            src.classes.WithMethods.method(),
            'You called method'
        )

    def test_make_a_class_w_attributes_and_methods(self):
        self.assertEqual(
            src.classes.WithAttributesAndMethods.attribute,
            'attribute'
        )
        self.assertEqual(
            src.classes.WithAttributesAndMethods.method(),
            'You called method'
        )

    def test_make_a_class_w_an_initializer(self):
        boy_a = src.classes.Human()
        boy_b = src.classes.Boy()
        self.assertEqual(boy_b.sex, 'M')
        self.assertEqual(boy_b.sex, boy_a.sex)

        girl_a = src.classes.Human('F')
        girl_b = src.classes.Girl('F')
        self.assertEqual(girl_b.sex, 'F')
        self.assertEqual(girl_b.sex, girl_a.sex)

        other_a = src.classes.Human('?')
        other_b = src.classes.Other('?')
        self.assertEqual(other_b.sex, '?')
        self.assertEqual(other_b.sex, other_a.sex)

        self.assertNotEqual(boy_a, boy_b)
        self.assertNotIsInstance(boy_a, src.classes.Boy)
        self.assertIsInstance(boy_b, src.classes.Human)

    def test_attributes_and_methods_of_classes(self):
        self.assertEqual(
            dir(src.classes.WithAttributesAndMethods),
            [
                '__class__',
                '__delattr__',
                '__dict__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__firstlineno__',
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
                '__module__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__setattr__',
                '__sizeof__',
                '__static_attributes__',
                '__str__',
                '__subclasshook__',
                '__weakref__',
                'attribute',
                'method'
            ]
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError