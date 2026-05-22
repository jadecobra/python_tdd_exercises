import datetime
import random
import src.person
import unittest


def choose(*choices):
    return random.choice(choices)


class TestPerson(unittest.TestCase):

    def test_factory_w_keyword_arguments(self):
        a_person = dict(
            first_name=choose('jane', 'joe', 'john', 'person'),
            last_name=choose('doe', 'smith', 'blow', 'public'),
            sex=choose('F', 'M')
        )

        this_year = datetime.datetime.now().year
        year_of_birth = random.randint(
            this_year-120, this_year
        )

        reality = src.person.factory(
            **a_person,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(
            **a_person,
            age=this_year-year_of_birth,
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_w_optional_arguments(self):
        first_name = choose('jane', 'joe', 'john', 'person')

        this_year = datetime.datetime.now().year
        year_of_birth = random.randint(
            this_year-120, this_year
        )

        reality = src.person.factory(
            first_name=first_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(

            first_name=first_name,
            last_name='doe',
            sex='M',
            age=this_year-year_of_birth,
        )
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError