import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    people = (
        ('jane', 'doe', 'F', 1991, True, True, True, True),
        ('joe', 'blow', 'M', 1996, True, False, True, False),
        ('mary', 'public', 'F', 2000, False, True, False, True),
        ('john', 'smith', 'M', 1980, False, False, False, False),
    )

    @staticmethod
    def calculate_age(year_of_birth):
        return (
            datetime.date.today().year
          - year_of_birth
        )

    def test_factory_function(self):
        for a_person in self.people:
            with self.subTest(first_name=a_person[0]):
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
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

    def test_say_hello_function(self):
        for a_person in self.people:
            with self.subTest(first_name=a_person[0]):
                first_name = a_person[0]
                last_name = a_person[1]
                year_of_birth = a_person[3]

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

    def test_say_hello_method(self):
        for a_person in self.people:
            with self.subTest(first_name=a_person[0]):
                first_name = a_person[0]
                last_name = a_person[1]
                sex = a_person[2]
                year_of_birth = a_person[3]
                is_citizen = a_person[4]
                passed_test = a_person[5]

                person = src.person.Person(
                    first_name=first_name,
                    last_name=last_name,
                    sex=sex,
                    year_of_birth=year_of_birth,
                    is_citizen=is_citizen,
                    passed_test=passed_test,
                )

                reality = person.say_hello()
                my_expectation = (
                    f'Hello, my name is {first_name}'
                    f' {last_name} and I am'
                    f' {self.calculate_age(year_of_birth)}.'
                )
                assert reality == my_expectation
                self.assertEqual(reality, my_expectation)
                self.assertEqual(person.can_vote(), is_citizen)
                self.assertEqual(person.can_get_license(), passed_test)

    def test_person_can_vote(self):

    def test_person_can_get_license(self):

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

    def test_when_person_is_too_old_to_be_alive(self):
        with self.assertRaises(ValueError):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=datetime.date.today().year-121,
            )

    def test_when_year_of_birth_is_not_an_integer(self):
        for year_of_birth in (
            datetime.date.today().year-121,
            None,
            2026.0,
            '2026',
            (2026,),
        ):
            with self.subTest(i=year_of_birth):
                with self.assertRaises(TypeError):
                    src.person.Person(
                        first_name='first_name',
                        last_name='last_name',
                        sex='M',
                        year_of_birth=year_of_birth,
                    )

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