import datetime
import random
import src.person
import unittest


def this_year():
    return datetime.datetime.now().year


def get_age(year_of_birth):
    return this_year() - year_of_birth


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.random_first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        self.random_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.random_new_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.age = get_age(self.random_year_of_birth)
        self.random_last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        self.random_sex = random.choice(('F', 'M'))
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

    def test_function_w_default_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.random_first_name,
            ),
            dict(
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                age=this_year()-this_year(),
            )
        )

    def test_factory_person_introduction(self):
        self.assertEqual(
            src.person.introduce(self.random_factory_person),
            (
                f'Hi! My name is {self.random_first_name} '
                f'{self.random_last_name} '
                f'and I am {get_age(self.random_year_of_birth)}'
            )
        )

    def test_classy_person_introduction(self):
        self.assertEqual(
            self.random_classy_person.introduce(),
            (
                f'Hi! My name is {self.random_first_name} '
                f'{self.random_last_name} '
                f'and I am {get_age(self.random_year_of_birth)}'
            )
        )

    def test_update_factory_person_year_of_birth(self):
        with self.assertRaises(KeyError):
            self.random_factory_person['year_of_birth']
        self.assertEqual(
            self.random_factory_person.get('age'), self.age
        )
        self.random_factory_person['year_of_birth'] = self.random_new_year_of_birth
        self.assertEqual(
            self.random_factory_person.get('age'), self.age
        )
        self.assertEqual(
            src.person.update_year_of_birth(
                self.random_factory_person,
                self.random_new_year_of_birth
            ),
            {
                'first_name': self.random_factory_person.get('first_name'),
                'last_name': self.random_factory_person.get('last_name'),
                'sex': self.random_factory_person.get('sex'),
                'age': this_year()-self.random_new_year_of_birth,
            }
        )

    def test_update_classy_person_year_of_birth(self):
        self.assertEqual(
            self.random_classy_person.get_age(), self.age
        )
        self.random_classy_person.year_of_birth = self.random_new_year_of_birth
        self.assertEqual(
            self.random_classy_person.get_age(),
            this_year()-self.random_new_year_of_birth
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError
