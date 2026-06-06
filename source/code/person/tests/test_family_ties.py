import src.classes
import unittest


class TestClasses(unittest.TestCase):

    def test_making_a_class_w_inheritance(self):
        a_class = src.classes.Doe

        assert not isinstance(a_class, src.person.Person)
        self.assertNotIsInstance(
            a_class, src.person.Person
        )

        assert issubclass(a_class, src.person.Person)
        self.assertIsSubclass(
            a_class, src.person.Person
        )

        assert not isinstance(a_class, a_class)
        self.assertNotIsInstance(a_class, a_class)

        an_instance = src.classes.Doe('first_name')
        assert isinstance(
            an_instance, src.person.Person
        )
        self.assertIsInstance(
            an_instance, src.person.Person
        )

        self.assertEqual(
            dir(a_class),
            dir(src.person.Person)
        )

    def test_classes_w_one_parent(self):
        doe = src.classes.Doe('doe')
        self.assertEqual(doe.last_name, 'doe')

        joe = src.classes.Blow('joe')
        self.assertEqual(joe.last_name, 'blow')

        blow = src.person.Person('joe', last_name='blow')
        self.assertEqual(blow.last_name, joe.last_name)

        jane = src.person.Person('jane')
        self.assertEqual(jane.last_name, doe.last_name)

        john = src.classes.Smith('john')
        self.assertEqual(john.last_name, 'smith')

        smith = src.person.Person('john', 'smith')
        self.assertEqual(smith.last_name, john.last_name)

    def test_classes_w_multiple_parents(self):
        joe = src.classes.Joe()
        self.assertEqual(joe.first_name, 'joe')
        self.assertEqual(joe.last_name, 'blow')
        assert issubclass(
            src.classes.Joe, src.classes.Blow
        )
        # self.assertNotIsSubclass(
        self.assertIsSubclass(
            src.classes.Joe, src.classes.Blow
        )

        jane = src.classes.Jane()
        self.assertEqual(jane.first_name, 'jane')
        self.assertEqual(jane.last_name, 'doe')
        self.assertEqual(jane.eye_color, 'brown')
        self.assertIsSubclass(
            src.classes.Jane, src.classes.Doe
        )

        # mary = src.classes.Jane('mary')
        mary = src.classes.Mary()
        self.assertEqual(mary.first_name, 'mary')
        # self.assertEqual(mary.last_name, mary.first_name)
        # self.assertEqual(mary.last_name, jane.last_name)
        self.assertEqual(mary.last_name, joe.last_name)
        # self.assertEqual(mary.eye_color, jane.eye_color)
        self.assertEqual(mary.eye_color, 'red')
        # assert not issubclass(
        assert issubclass(
            src.classes.Mary, src.classes.Jane
        )
        # self.assertNotIsSubclass(
        self.assertIsSubclass(
            src.classes.Mary, src.classes.Jane
        )
        assert issubclass(
            src.classes.Mary, src.classes.Joe
        )
        # self.assertNotIsSubclass(
        self.assertIsSubclass(
            src.classes.Mary, src.classes.Joe
        )

        john = src.classes.John()
        self.assertEqual(john.first_name, 'john')
        self.assertEqual(john.last_name, 'smith')
        self.assertEqual(john.eye_color, 'orange')
        assert issubclass(
            src.classes.John, src.classes.Smith
        )
        # self.assertNotIsSubclass(
        self.assertIsSubclass(
            src.classes.John, src.classes.Smith
        )

        lil = src.classes.Lil()
        self.assertEqual(lil.first_name, 'lil')
        self.assertEqual(lil.last_name, mary.last_name)
        # self.assertEqual(lil.last_name, john.last_name)
        # self.assertEqual(lil.eye_color, '')
        # self.assertEqual(lil.eye_color, jane.eye_color)
        self.assertEqual(lil.eye_color, mary.eye_color)
        assert issubclass(
            src.classes.Lil, src.classes.John
        )
        # self.assertNotIsSubclass(
        self.assertIsSubclass(
            src.classes.Lil, src.classes.John
        )
        assert issubclass(
            src.classes.Lil, src.classes.Mary
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# ModuleNotFoundError
# TypeError