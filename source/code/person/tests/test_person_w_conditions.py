import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    @staticmethod
    def calculate_age(year_of_birth):
        return (
            datetime.date.today().year
          - year_of_birth
        )

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
            f' {self.calculate_age(year_of_birth)}.'
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
        self.assertEqual(joe.can_vote(), True)
        self.assertEqual(joe.can_get_license(), False)

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
            f' {self.calculate_age(year_of_birth)}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        jane = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
            passed_test=True,
        )

        reality = jane.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)
        self.assertEqual(jane.can_vote(), True)
        self.assertEqual(jane.can_get_license(), True)

    def test_john(self):
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1980
        # year_of_birth = 1580
        # raises AssertionError
        # because older than 120

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
            f' {self.calculate_age(year_of_birth)}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        john = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
            is_citizen=False,
        )

        reality = john.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)
        self.assertEqual(john.can_vote(), False)
        self.assertEqual(john.can_get_license(), False)

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
            f' {self.calculate_age(year_of_birth)}.'
        )
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

        mary = src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
            is_citizen=False,
            passed_test=True,
        )

        reality = mary.say_hello()
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)
        self.assertEqual(mary.can_vote(), False)
        self.assertEqual(mary.can_get_license(), True)

    def test_underage_citizen(self):
        person = src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            year_of_birth=datetime.date.today().year-17,
            is_citizen=True,
            passed_test=True,
        )
        self.assertEqual(person.can_vote(), False)
        self.assertEqual(
            person.can_get_license(), False
        )

    @unittest.skip('will always fail')
    def test_when_year_of_birth_is_not_an_integer(self):
        person = src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            # year_of_birth=None,    # fails
            # year_of_birth=False,   # fails
            # year_of_birth=2026.0,  # fails
            # year_of_birth='2026',  # fails
            # year_of_birth=(2026,), # fails
        )
        # person.say_hello()
        # fails if year_of_birth is not an integer

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
            'can_get_license',
            'can_vote',
            'check_age',
            'say_hello',
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
            'age',
            'can_get_license',
            'can_vote',
            'check_age',
            'first_name',
            'is_citizen',
            'last_name',
            'passed_test',
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