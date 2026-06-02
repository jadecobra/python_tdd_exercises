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

    def test_making_a_class_w_inheritance(self):
        a_class = src.classes.Doe

        assert not isinstance(a_class, src.person.Person)
        self.assertNotIsInstance(
            a_class, src.person.Person
        )

        assert not isinstance(a_class, a_class)
        self.assertNotIsInstance(a_class, a_class)

        an_instance = src.classes.Doe('doe')
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

    def test_family_ties(self):
        doe = src.classes.Doe('first')
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
        self.assertIsInstance(joe, src.classes.Blow)

        jane = src.classes.Jane()
        self.assertEqual(jane.first_name, 'jane')
        self.assertEqual(jane.last_name, 'doe')
        self.assertIsInstance(jane, src.classes.Doe)

        mary = src.classes.Mary()
        self.assertEqual(mary.first_name, 'mary')
        self.assertEqual(mary.last_name, joe.last_name)
        self.assertIsInstance(mary, src.classes.Jane)
        self.assertIsInstance(mary, src.classes.Doe)
        self.assertIsInstance(mary, src.classes.Joe)

        john = src.classes.John()
        self.assertEqual(john.first_name, 'john')
        self.assertEqual(john.last_name, 'smith')
        self.assertIsInstance(john, src.classes.Smith)

        lil = src.classes.Lil()
        self.assertIsInstance(lil, src.classes.John)
        self.assertIsInstance(lil, src.classes.Mary)
        self.assertEqual(lil.first_name, 'lil')
        self.assertEqual(lil.last_name, john.last_name)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError