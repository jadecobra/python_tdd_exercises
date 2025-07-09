import src.classes
import unittest


class TestClasses(unittest.TestCase):

    def test_make_a_class_w_pass(self):
        self.assertIsInstance(src.classes.WithPass(), object)

    def test_make_a_class_w_parentheses(self):
        self.assertIsInstance(src.classes.WithParentheses(), object)

    def test_make_a_class_w_object(self):
        self.assertIsInstance(src.classes.WithObject(), object)

    def test_make_a_class_w_attributes(self):
        self.assertEqual(src.classes.WithAttributes.attribute_a, 'attribute_a')
        self.assertEqual(src.classes.WithAttributes.attribute_b, 'attribute_b')
        self.assertEqual(src.classes.WithAttributes.attribute_c, 'attribute_c')
        self.assertEqual(src.classes.WithAttributes.attribute_d, 'attribute_d')

    def test_make_a_class_w_methods(self):
        self.assertEqual(src.classes.WithMethods.method_a(), 'You called method_a')
        self.assertEqual(src.classes.WithMethods.method_b(), 'You called method_b')
        self.assertEqual(src.classes.WithMethods.method_c(), 'You called method_c')
        self.assertEqual(src.classes.WithMethods.method_d(), 'You called method_d')

    def test_make_a_class_w_attributes_and_methods(self):
        self.assertEqual(
            src.classes.WithAttributesAndMethods.attribute, 'attribute'
        )
        self.assertEqual(
            src.classes.WithAttributesAndMethods.method(), 'You called method'
        )

    def test_make_a_class_w_an_initializer(self):
        boy_a = src.classes.Human()
        boy_b = src.classes.Boy()
        girl_a = src.classes.Human(sex='F')
        girl_b = src.classes.Girl(sex='F')
        other_a = src.classes.Human(sex='?')
        other_b = src.classes.Human(sex='?')

        self.assertEqual(boy_a.sex, 'M')
        self.assertEqual(boy_b.sex, boy_a.sex)
        self.assertEqual(girl_a.sex, 'F')
        self.assertEqual(girl_b.sex, girl_a.sex)
        self.assertEqual(other_a.sex, '?')
        self.assertEqual(other_b.sex, other_a.sex)

        self.assertNotEqual(boy_a, boy_b)
        self.assertNotIsInstance(boy_a, src.classes.Boy)
        self.assertIsInstance(boy_b, src.classes.Human)

    def test_attributes_and_methods_of_objects(self):
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