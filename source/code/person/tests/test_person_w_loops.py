import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    this_year = datetime.date.today().year
    younger_than_18 = this_year - 17
    not_younger_than_18 = this_year - 18

    first_name = 'first_name'
    last_name = 'last_name'
    sex = 'M'

    people = (
        (
            # is_citizen, passed_test
            not_younger_than_18, True, True,
            True, True,
        ),
        (
            # is_citizen, not passed_test
            not_younger_than_18, True, False,
            True, False,
        ),
        (
            # not is_citizen, passed_test
            not_younger_than_18, False, True,
            False, True,
        ),
        (
            # not is_citizen, not passed_test
            not_younger_than_18, False, False,
            False, False,
        ),
        (
            # underage, is_citizen, passed_test
            younger_than_18, True, True,
            False, False,
        ),
        (
            # underage, not is_citizen, passed_test
            younger_than_18, False, True,
            False, False,
        ),
        (
            # underage, is_citizen, not passed_test
            younger_than_18, True, False,
            False, False,
        ),
        (
            # underage, not is_citizen, not passed_test
            younger_than_18, False, False,
            False, False,
        ),
        # year_of_birth is not an integer
        (None, False, False,),
        (2026.0, False, False,),
        ('2026', False, False,),
        ((2026,), False, False,),
    )

    def calculate_age(self, year_of_birth):
        return self.this_year - year_of_birth

    def test_person_class(self):
        for a_person in self.people:
            year_of_birth = a_person[0]

            with self.subTest(a_person):
                try:
                    an_instance = src.person.Person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                        is_citizen=a_person[1],
                        passed_test=a_person[2],
                    )
                except TypeError as error:
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:
                    self.assertEqual(
                        an_instance.say_hello(),
                        (
                            f'Hello, my name is {self.first_name}'
                            f' {self.last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )
                    self.assertEqual(an_instance.can_vote(), a_person[3])
                    self.assertEqual(
                        an_instance.can_get_license(), a_person[4]
                    )

    def test_say_hello_function(self):
        for a_person in self.people:
            year_of_birth = a_person[0]

            with self.subTest(a_person):
                try:
                    reality = src.person.say_hello(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        year_of_birth=year_of_birth,
                    )
                except TypeError as error:
                    self.assertEqual(
                        error.args[0],
                        f"'{year_of_birth}' is not an integer"
                    )
                else:
                    self.assertEqual(
                        reality,
                        (
                            f'Hello, my name is {self.first_name}'
                            f' {self.last_name} and I am'
                            f' {self.calculate_age(year_of_birth)}.'
                        )
                    )

    def test_person_factory(self):
        for a_person in self.people:
            year_of_birth = a_person[0]

            with self.subTest(a_person):
                self.assertEqual(
                    src.person.person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                    ),
                    (
                        f'{self.first_name}, {self.last_name},'
                        f' {self.sex}, {year_of_birth}'
                    )
                )

    def test_if_person_is_not_alive(self):
        for year_of_birth in (
            self.this_year+1,
            self.this_year-121,
        ):
            age = self.calculate_age(year_of_birth)

            with (
                self.subTest(year_of_birth),
                self.assertRaisesRegex(
                    ValueError,
                    f'a {age} year old person is not alive.'
                ),
            ):
                src.person.Person(
                    first_name=self.first_name,
                    last_name=self.last_name,
                    sex=self.sex,
                    year_of_birth=year_of_birth,
                )

    def test_when_person_is_older_than_120(self):
        year_of_birth = self.this_year - 121
        age = self.calculate_age(year_of_birth)

        with self.assertRaisesRegex(
            ValueError,
            f'a {age} year old person is not alive.'
        ):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='M',
                year_of_birth=self.this_year-121
            )

    def test_when_year_of_birth_is_the_future(self):
        year_of_birth = self.this_year + 1
        age = self.calculate_age(year_of_birth)

        with self.assertRaisesRegex(
            ValueError,
            f'a {age} year old person is not alive.'
        ):
            src.person.Person(
                first_name='first_name',
                last_name='last_name',
                sex='F',
                year_of_birth=year_of_birth,
            )

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
                '__subclasshook__', '__weakref__',
                'can_get_license', 'can_vote', 'check_age',
                'say_hello',
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
                '__subclasshook__', '__weakref__',
                'age', 'can_get_license', 'can_vote',
                'check_age', 'first_name', 'is_citizen',
                'last_name', 'passed_test', 'say_hello',
                'sex', 'year_of_birth',
            ]
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError
# SyntaxError