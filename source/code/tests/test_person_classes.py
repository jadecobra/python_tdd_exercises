import datetime
import random
import src.person
import unittest


def choose(*choices):
    return random.choice(choices)


def this_year():
    return datetime.datetime.now().year


def random_year_of_birth():
    return random.randint(
        this_year()-120, this_year()
    )


def get_age(year_of_birth):
    return this_year() - year_of_birth


class TestPerson(unittest.TestCase):

    RANDOM_NAMES = (
        'jane', 'joe', 'john', 'person',
        'doe', 'smith', 'blow', 'public',
    )

    def setUp(self):
        self.random_year_of_birth = random_year_of_birth()
        self.random_new_year_of_birth = random_year_of_birth()
        self.original_age = get_age(self.random_year_of_birth)
        self.new_age = get_age(self.random_new_year_of_birth)
        self.random_first_name = choose(*self.RANDOM_NAMES)
        self.random_last_name = choose(*self.RANDOM_NAMES)
        self.random_sex = choose('M', 'F')
        self.random_factory_person = src.person.factory(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            sex=self.random_sex,
            year_of_birth=self.random_year_of_birth,
        )
        self.random_classy_person = src.person.Person(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            sex=self.random_sex,
            year_of_birth=self.random_year_of_birth,
        )

    def test_factory_takes_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            ),
            self.random_factory_person
        )

    def test_factory_w_default_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.random_first_name,
                year_of_birth=self.random_year_of_birth,
            ),
            dict(
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                age=self.original_age,
            )
        )

    def expected_greeting(self):
        return (
            f'Hi, my name is {self.random_first_name} '
            f'{self.random_last_name} '
            f'and I am {self.original_age}'
        )

    def test_factory_person_greeting(self):
        self.assertEqual(
            src.person.hello(self.random_factory_person),
            self.expected_greeting()
        )

    def test_classy_person_greeting(self):
        self.assertEqual(
            self.random_classy_person.hello(),
            self.expected_greeting()
        )

    def test_update_factory_person_year_of_birth(self):
        self.assertEqual(
            self.random_factory_person.get('age'),
            self.original_age
        )

        with self.assertRaises(KeyError):
            self.random_factory_person['year_of_birth']
        self.assertEqual(
            self.random_factory_person.setdefault(
                'year_of_birth', self.random_new_year_of_birth
            ),
            self.random_new_year_of_birth
        )
        self.assertEqual(
            self.random_factory_person.get('age'),
            self.original_age
        )

        self.assertEqual(
            src.person.update_year_of_birth(
                self.random_factory_person,
                self.random_new_year_of_birth
            ),
            dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                age=self.new_age
            )
        )

    def test_update_classy_person_year_of_birth(self):
        self.assertEqual(
            self.random_classy_person.get_age(),
            self.original_age
        )

        self.random_classy_person.year_of_birth = self.random_new_year_of_birth
        self.assertEqual(
            self.random_classy_person.get_age(),
            self.new_age
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError