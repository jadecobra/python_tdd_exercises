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

    years_of_birth = (
        not_younger_than_18, younger_than_18,
        None, 2026.0, '2026', (2026,),
    )

    def calculate_age(self, year_of_birth):
        return self.this_year - year_of_birth

    def test_person_object(self):
        booleans = (True, False)
        people = []
        for year_of_birth in self.years_of_birth:
            for is_citizen in booleans:
                for passed_test in booleans:
                    if year_of_birth == self.not_younger_than_18:
                        people.append((
                            year_of_birth, is_citizen, passed_test,
                            is_citizen, passed_test,
                        ))
                    else:
                        people.append((
                            year_of_birth, is_citizen, passed_test,
                            False, False
                        ))

        for (
            year_of_birth, is_citizen, passed_test,
            can_vote_result, can_get_license_result,
        ) in people:

            with self.subTest((
                year_of_birth, is_citizen, passed_test,
                can_vote_result, can_get_license_result,
            )):
                try:
                    an_instance = src.person.Person(
                        first_name=self.first_name,
                        last_name=self.last_name,
                        sex=self.sex,
                        year_of_birth=year_of_birth,
                        is_citizen=is_citizen,
                        passed_test=passed_test,
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
                    self.assertEqual(
                        an_instance.can_vote(),
                        can_vote_result
                    )
                    self.assertEqual(
                        an_instance.can_get_license(),
                        can_get_license_result
                    )

    def test_say_hello_function(self):
        for year_of_birth in self.years_of_birth:
            with self.subTest(year_of_birth):
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
        for year_of_birth in self.years_of_birth:
            with self.subTest(year_of_birth):
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

    def test_when_person_is_not_alive(self):
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

    def test_dir_person_object(self):
        dir_person = dir(object)
        dir_person.extend((
            '__dict__', '__firstlineno__',
            '__module__', '__static_attributes__',
            '__weakref__',
            'can_get_license', 'can_vote',
            'check_age', 'say_hello',
        ))
        dir_person.sort()
        self.assertEqual(
            dir(src.person.Person),
            dir_person
        )

    def test_dir_person_instance(self):
        self.maxDiff = None
        dir_person_instance = dir(src.person.Person)
        dir_person_instance.extend((
            'age', 'first_name', 'is_citizen',
            'last_name', 'passed_test',
            'sex', 'year_of_birth',
        ))
        dir_person_instance.sort()
        self.assertEqual(
            dir(
                src.person.Person(
                    first_name='first_name',
                    last_name='last_name',
                    sex='M',
                    year_of_birth=2026,
                )
            ),
            dir_person_instance
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError
# SyntaxError