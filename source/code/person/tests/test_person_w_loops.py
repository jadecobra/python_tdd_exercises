import datetime
import src.person
import unittest


class TestPerson(unittest.TestCase):

    this_year = datetime.date.today().year
    not_younger_than_18 = this_year - 18
    younger_than_18 = this_year - 17

    first_name = 'first_name'
    last_name = 'last_name'
    sex = 'M'

    people = (
        (
            not_younger_than_18,
            # is_citizen, passed_test
            True, True, True, True,
        ),
        (
            not_younger_than_18,
            # is_citizen, not passed_test
            True, False, True, False,
        ),
        (
            not_younger_than_18,
            # not is_citizen, passed_test
            False, True, False, True,
        ),
        (
            not_younger_than_18,
            # not is_citizen, not passed_test
            False, False, False, False,
        ),
        (
            younger_than_18,
            # is_citizen, passed_test
            True, True, False, False,
        ),
        (
            # not is_citizen, passed_test
            younger_than_18,
            False, True, False, False,
        ),
        (
            younger_than_18,
            # is_citizen, not passed_test
            True, False, False, False,
        ),
        (
            # not is_citizen, not passed_test
            younger_than_18,
            False, False, False, False,
        ),
        # year_of_birth is not an integer
        (
            None,
            False, False, False, False,
        ),
        (
            2026.0,
            False, False, False, False,
        ),
        (
            '2026',
            False, False, False, False,
        ),
        (
            (2026,),
            False, False, False, False,
        ),
    )

    def calculate_age(self, year_of_birth):
        return self.this_year - year_of_birth

    def test_person_object(self):
        for (
            year_of_birth,
            is_citizen, passed_test,
            can_vote, can_get_license,
        ) in self.people:
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
        for a_person in self.people:
            year_of_birth = a_person[0]
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
        for a_person in self.people:
            year_of_birth = a_person[0]
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
                    year_of_birth=self.this_year,
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