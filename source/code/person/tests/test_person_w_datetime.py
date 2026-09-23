import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    def assert_person_factory_works(
            self, first_name, last_name,
            sex, year_of_birth
        ):
        self.assertEqual(
            src.person.person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ),
            (
                f'{first_name}, {last_name},'
                f' {sex}, {year_of_birth}'
            )
        )

    @staticmethod
    def calculate_age(year_of_birth):
        return (
            datetime.date.today().year
          - year_of_birth
        )

    def assert_say_hello_works(
            self, first_name, last_name,
            year_of_birth,
        ):
        self.assertEqual(
            src.person.say_hello(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth
            ),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
        )

    def assert_person_can_say_hello(
            self,first_name, last_name,
            sex, year_of_birth,
        ):
        self.assertEqual(
            src.person.Person(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ).say_hello(),
            (
                f'Hello, my name is {first_name}'
                f' {last_name} and I am'
                f' {self.calculate_age(year_of_birth)}.'
            )
        )

    def test_joe(self):
        first_name = 'joe'
        last_name = 'blow'
        sex = 'M'
        year_of_birth = 1996

        self.assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

        self.assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth
        )

    def test_jane(self):
        first_name = 'jane'
        last_name = 'doe'
        sex = 'F'
        year_of_birth = 1991

        self.assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        self.assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

    def test_john(self):
        first_name = 'john'
        last_name = 'smith'
        sex = 'M'
        year_of_birth = 1980

        self.assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        self.assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

    def test_mary(self):
        first_name = 'mary'
        last_name = 'public'
        sex = 'F'
        year_of_birth = 2000

        self.assert_person_factory_works(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        self.assert_say_hello_works(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        self.assert_person_can_say_hello(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

    def test_when_person_is_older_than_120(self):
        src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            year_of_birth=datetime.date.today().year-121
        )
        # ).say_hello() fails
        # because person is older than 120

    def test_when_year_of_birth_is_the_future(self):
        src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='F',
            year_of_birth=datetime.date.today().year+1,
        )
        # ).say_hello() fails
        # because year_of_birth is in the future

    def test_when_year_of_birth_is_not_an_integer(self):
        src.person.Person(
            first_name='first_name',
            last_name='last_name',
            sex='M',
            # year_of_birth=None,     # fails
            # year_of_birth=2026.0,   # fails
            # year_of_birth='2026',   # fails
            # year_of_birth=(2026,),  # fails
        )
        # ).say_hello() fails
        # because year_of_birth is not an integer

    def test_dir_person_class(self):
        self.assertEqual(
            dir(src.person.Person),
            [
                '__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'say_hello'
            ]
        )

    def test_dir_person_instance(self):
        self.assertEqual(
            dir(
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=2026,
                )
            ),
            [
                '__class__', '__delattr__', '__dict__',
                '__dir__', '__doc__', '__eq__',
                '__firstlineno__', '__format__', '__ge__',
                '__getattribute__', '__getstate__', '__gt__',
                '__hash__', '__init__', '__init_subclass__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__new__', '__reduce__', '__reduce_ex__',
                '__repr__', '__setattr__', '__sizeof__',
                '__static_attributes__', '__str__',
                '__subclasshook__', '__weakref__', 'first_name',
                'last_name', 'say_hello', 'sex', 'year_of_birth',
            ]
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError
# SyntaxError