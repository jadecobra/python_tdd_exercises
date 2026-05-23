import datetime
import random
import src.person
import unittest


def choose(*choices):
    return random.choice(choices)


def calculate_age(year_of_birth):
    return (
        datetime.datetime.now().year
      - year_of_birth
    )


def random_year_of_birth():
    this_year = datetime.datetime.now().year
    return random.randint(
        this_year-120, this_year
    )


class TestPerson(unittest.TestCase):

    def test_factory_w_keyword_arguments(self):
        a_person = dict(
            first_name=choose(
                'jane', 'joe', 'john', 'person',
            ),
            last_name=choose(
                'doe', 'smith', 'blow', 'public',
            ),
            sex=choose('F', 'M'),
        )
        year_of_birth = random_year_of_birth()

        reality = src.person.factory(
            **a_person,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(
            **a_person,
            age=calculate_age(year_of_birth),
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_w_optional_arguments(self):
        first_name = choose(
            'jane', 'joe', 'john', 'person'
        )
        year_of_birth = random_year_of_birth()

        reality = src.person.factory(
            first_name=first_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(
            first_name=first_name,
            sex='M',
            last_name='doe',
            age=calculate_age(year_of_birth),
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_person_say_hello(self):
        first_name = choose(
            'jane', 'joe', 'john', 'person',
        )
        last_name = choose(
            'doe', 'smith', 'blow', 'public',
        )
        sex = choose('F', 'M')
        year_of_birth = random_year_of_birth()

        a_random_person = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        )

        reality = src.person.say_hello(a_random_person)
        my_expectation = (
            f'Hi, my name is {first_name} {last_name}'
            f' and I am {calculate_age(year_of_birth)}'
        )
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError