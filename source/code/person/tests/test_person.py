import datetime
import src.person
import unittest
import random


def pick_one(*choices):
    return random.choice(choices)


def get_random_name():
    return pick_one(
        'jane', 'joe', 'john', 'person',
        'doe', 'smith', 'blow', 'public',
    )


def get_current_year():
    return datetime.datetime.now().year


def calculate_age(year_of_birth):
    return (
        get_current_year()
      - year_of_birth
    )


def get_random_year_of_birth():
    this_year = get_current_year()
    return random.randint(
        this_year-120, this_year
    )


class TestPerson(unittest.TestCase):

    def test_factory_w_keyword_arguments(self):
        a_person = dict(
            first_name=get_random_name(),
            last_name=get_random_name(),
            sex=pick_one('F', 'M'),
        )
        year_of_birth = get_random_year_of_birth()

        reality = src.person.factory(
            **a_person,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(
            a_person,
            age=calculate_age(year_of_birth),
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_w_optional_arguments(self):
        first_name = get_random_name()
        year_of_birth = get_random_year_of_birth()

        reality = src.person.factory(
            first_name=first_name,
            year_of_birth=year_of_birth,
        )
        my_expectation = dict(
            first_name=first_name,
            last_name='doe',
            sex='M',
            age=calculate_age(year_of_birth),
        )
        self.assertEqual(reality, my_expectation)

    def test_factory_person_says_hello(self):
        first_name = 'joe'
        last_name = 'blow'
        year_of_birth = get_random_year_of_birth()
        age = calculate_age(year_of_birth)

        joe = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        reality = src.person.say_hello(joe)
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am {age}'
        )
        self.assertEqual(reality, my_expectation)

        first_name = 'jane'
        year_of_birth = get_random_year_of_birth()
        age = calculate_age(year_of_birth)

        jane = src.person.factory(
            first_name=first_name,
            sex='F',
            year_of_birth=year_of_birth
        )

        reality = src.person.say_hello(jane)
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' doe and I am {age}'
        )
        self.assertEqual(reality, my_expectation)

        first_name = 'john'
        last_name = 'smith'
        year_of_birth = get_random_year_of_birth()
        age = calculate_age(year_of_birth)

        john = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )

        reality = src.person.say_hello(john)
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am {age}'
        )
        self.assertEqual(reality, my_expectation)

        first_name = 'mary'
        last_name = 'public'
        year_of_birth = get_random_year_of_birth()
        age = calculate_age(year_of_birth)

        mary = src.person.factory(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
            sex='F',
        )

        reality = src.person.say_hello(mary)
        my_expectation = (
            f'Hello, my name is {first_name}'
            f' {last_name} and I am {age}'
        )
        self.assertEqual(reality, my_expectation)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError