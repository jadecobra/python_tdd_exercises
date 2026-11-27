import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    this_year = datetime.date.today().year
    not_younger_than_18 = this_year - 18
    younger_than_18 = this_year - 17

    years_of_birth = (
        not_younger_than_18,
        younger_than_18,
        None, 2027.0, '2027', (2027,),
    )

    first_name = 'first_name'
    last_name = 'last_name'
    sex = 'M'

    def calculate_age(self, year_of_birth):
        return self.this_year - year_of_birth

    def test_person_object(self):
        self.maxDiff = None

        booleans = (False, True)
        people = []
        for year_of_birth in self.years_of_birth:
            row = []
            for is_citizen in booleans:
                for passed_test in booleans:
                    is_not_younger_than_18 = (
                        year_of_birth == self.not_younger_than_18
                    )
                    row.append((
                        is_citizen, passed_test,
                        is_citizen and is_not_younger_than_18,
                        passed_test and is_not_younger_than_18,
                    ))
            people.append((year_of_birth, row))

        for (
            year_of_birth, inputs_outputs
        ) in people:
            for (
                is_citizen, passed_test,
                can_vote, can_get_license,
            ) in inputs_outputs:
                with self.subTest(
                    a_person=(
                        self.first_name, self.last_name,
                        self.sex, year_of_birth,
                        is_citizen, passed_test,
                        can_vote, can_get_license,
                    )
                ):
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
                            an_instance.can_vote(), can_vote
                        )
                        self.assertEqual(
                            an_instance.can_get_license(),
                            can_get_license
                        )

    def test_say_hello_function(self):
        for year_of_birth in self.years_of_birth:
            with self.subTest(
                first_name=self.first_name,
                year_of_birth=year_of_birth,
            ):
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
        for number in (1, -121):
            year_of_birth = self.this_year + number
            age = self.calculate_age(year_of_birth)

            with (
                self.subTest(year_of_birth),
                self.assertRaisesRegex(
                    ValueError,
                    f'a {age} year old person is not alive.'
                )
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
                    year_of_birth=self.this_year,
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