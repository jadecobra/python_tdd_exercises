import datetime
import random
import src.person
import unittest


def choose(*choices):
    return random.choice(choices)


def this_year():
    return datetime.datetime.now().year


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.random_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.random_first_name = choose('jane', 'joe', 'john', 'person')

    def test_factory_takes_keyword_arguments(self):
        a_person = dict(
            first_name=self.random_first_name,
            last_name=choose('doe', 'smith', 'blow', 'public'),
            sex=choose('F', 'M'),
        )

        self.assertEqual(
            src.person.factory(
                **a_person,
                year_of_birth=self.random_year_of_birth,
            ),
            dict(
                **a_person,
                age=this_year()-self.random_year_of_birth,
            )
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
                age=this_year()-self.random_year_of_birth,
            )
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError