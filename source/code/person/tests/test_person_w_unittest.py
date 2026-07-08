import unittest
import src.person


class TestPerson(unittest.TestCase):

    def test_joe(self):
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        reality = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        joe = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = joe.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_jane(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        reality = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        jane = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = jane.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_john(self):
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1580

        reality = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = john.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_mary(self):
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        reality = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        reality = src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am'
            f' {2026-year_of_birth}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = mary.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_dir_person_class(self):
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
            'say_hello'
        ]
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_dir_person_instance(self):
        an_instance_of_person = src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            year_of_birth=2026,
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
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError
# SyntaxError