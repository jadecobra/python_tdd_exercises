import unittest
import src.classes
import src.person


class TestClasses(unittest.TestCase):

    def test_making_a_class_w_pass(self):
        self.assertIsInstance(src.classes.WPass(), object)

    def test_making_a_class_w_parentheses(self):
        self.assertIsInstance(src.classes.WParentheses(), object)

    def test_making_a_class_w_object(self):
        self.assertIsInstance(src.classes.WObject(), object)

    def test_attributes_and_methods_of_objects(self):
        self.assertEqual(
            dir(object),
            [
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
        )

    def test_making_classes_w_inheritance(self):
        self.assertIsInstance(
            src.classes.Doe('doe'),
            src.person.Person
        )
        self.assertEqual(
            dir(src.classes.Doe),
            dir(src.person.Person)
        )

    def test_family_ties(self):
        doe = src.classes.Doe('doe')
        jane = src.classes.Doe('jane')
        john = src.classes.Doe('john')
        mary = src.classes.Smith('mary')
        joe = src.classes.Blow('joe')
        baby = src.classes.Baby('baby')
        lil = src.classes.Lil('lil')

        self.assertEqual(doe.last_name, 'doe')
        self.assertEqual(jane.last_name, 'doe')
        self.assertEqual(john.last_name, 'doe')
        self.assertEqual(mary.last_name, 'smith')
        self.assertEqual(joe.last_name, 'blow')
        self.assertEqual(baby.last_name, 'blow')
        self.assertEqual(lil.last_name, 'doe')


# Exceptions seen
# AssertionError
