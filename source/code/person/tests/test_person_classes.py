import datetime
import random
import src.person
import unittest


def pick_one(*choices):
    return random.choice(choices)


def get_random_name():
    return pick_one(
        'jane', 'joe', 'john', 'person',
        'doe', 'smith', 'blow', 'public',
    )


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.random_first_name = get_random_name()
        self.random_last_name = get_random_name()
        this_year = datetime.datetime.now().year
        self.random_year_of_birth = random.randint(
            this_year-120, this_year
        )
        self.age = this_year - self.random_year_of_birth

    def test_factory_w_keyword_arguments(self):
        a_person = dict(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            sex=pick_one('F', 'M'),
        )

        reality = src.person.factory(
            **a_person,
            year_of_birth=self.random_year_of_birth,
        )
        my_expectation = dict(
            **a_person,
            age=self.age,
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_w_optional_arguments(self):
        reality = src.person.factory(
            first_name=self.random_first_name,
            year_of_birth=self.random_year_of_birth,
        )
        my_expectation = dict(
            first_name=self.random_first_name,
            last_name='doe',
            sex='M',
            age=self.age,
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_person_says_hello(self):
        a_random_person = src.person.factory(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
        )

        reality = src.person.say_hello(a_random_person)
        my_expectation = (
            f'Hi, my name is {self.random_first_name}'
            f' {self.random_last_name}'
            f' and I am {self.age}'
        )
        self.assertEqual(reality, my_expectation)

    def test_classy_person_says_hello(self):
        a_random_person = src.person.Person(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
        )

        reality = a_random_person.say_hello()
        my_expectation = (
            f'Hi, my name is {self.random_first_name}'
            f' {self.random_last_name}'
            f' and I am {self.age}'
        )
        self.assertEqual(reality, my_expectation)

    def test_attributes_and_methods_of_person_class(self):
        reality = dir(src.person.Person)
        my_expectation = [
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
            'say_hello',
        ]
        self.assertEqual(reality, my_expectation)

    def test_attributes_and_methods_of_person_instance(self):
        an_instance_of_person = src.person.Person(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
            sex=pick_one('F', 'M')
        )

        reality = dir(an_instance_of_person)
        my_expectation = [
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
            'first_name',
            'last_name',
            'say_hello',
            'sex',
            'year_of_birth',
        ]
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError