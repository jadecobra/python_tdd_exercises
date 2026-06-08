import src.family_ties
import unittest


class TestFamilyTies(unittest.TestCase):

    def test_making_a_class_w_inheritance(self):
        person_class = src.person.Person
        doe_class = src.family_ties.Doe
        doe_instance = doe_class('the_first')

        self.assertNotIsInstance(
            doe_class, person_class
        )

        self.assertNotIsInstance(
            doe_class, doe_class
        )

        self.assertIsSubclass(
            doe_class, person_class
        )

        self.assertIsInstance(
            doe_instance, person_class
        )

        self.assertEqual(
            dir(doe_class), dir(person_class)
        )

    def test_classes_w_one_parent(self):
        doe = src.family_ties.Doe('the_first')
        self.assertEqual(doe.last_name, 'doe')

        joe = src.family_ties.Blow('joe')
        self.assertEqual(joe.last_name, 'blow')

        blow = src.person.Person('joe', last_name='blow')
        self.assertEqual(blow.last_name, joe.last_name)

        jane = src.person.Person('jane')
        self.assertEqual(jane.last_name, doe.last_name)

        john = src.family_ties.Smith('john')
        self.assertEqual(john.last_name, 'smith')

        smith = src.person.Person('john', 'smith')
        self.assertEqual(smith.last_name, john.last_name)

    def test_classes_w_multiple_parents(self):
        joe = src.family_ties.Joe()
        self.assertEqual(joe.first_name, 'joe')
        self.assertEqual(joe.last_name, 'blow')
        self.assertEqual(joe.eye_color, 'blue')
        self.assertIsSubclass(
            src.family_ties.Joe, src.family_ties.Blow
        )

        jane = src.family_ties.Jane()
        self.assertEqual(jane.first_name, 'jane')
        self.assertEqual(jane.last_name, 'doe')
        self.assertEqual(jane.eye_color, 'green')
        self.assertIsSubclass(
            src.family_ties.Jane, src.family_ties.Doe
        )

        mary = src.family_ties.Mary()
        self.assertEqual(mary.first_name, 'mary')
        self.assertEqual(mary.last_name, jane.last_name)
        self.assertEqual(mary.eye_color, joe.eye_color)
        self.assertIsSubclass(
            src.family_ties.Mary, src.family_ties.Jane
        )
        self.assertIsSubclass(
            src.family_ties.Mary, src.family_ties.Joe
        )

        john = src.family_ties.John()
        self.assertEqual(john.first_name, 'john')
        self.assertEqual(john.last_name, 'smith')
        self.assertEqual(john.eye_color, 'brown')
        self.assertIsSubclass(
            src.family_ties.John, src.family_ties.Smith
        )

        lil = src.family_ties.Lil()
        self.assertEqual(lil.first_name, 'lil')
        self.assertEqual(lil.last_name, john.last_name)
        self.assertEqual(lil.eye_color, mary.eye_color)
        self.assertIsSubclass(
            src.family_ties.Lil, src.family_ties.John
        )
        self.assertIsSubclass(
            src.family_ties.Lil, src.family_ties.Mary
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# ModuleNotFoundError
# TypeError