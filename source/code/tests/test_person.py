import datetime
import random
import src.person
import unittest


def a_random_first_name():
    return random.choice((
        'john', 'joe', 'jane', 'person'
    ))


def a_random_year():
    return random.randint(
        1900, this_year()
    )


def this_year():
    return datetime.datetime.now().year


class TestPerson(unittest.TestCase):

    def test_person_factory_keyword_arguments(self):
        first_name = a_random_first_name()
        last_name = random.choice((
            'doe', 'smith', 'blow', 'public'
        ))
        sex = random.choice(('F', 'M'))
        year_of_birth = a_random_year()

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth,
            ),
            {
                'first_name': first_name,
                'last_name': last_name,
                'sex': sex,
                'age': this_year() - year_of_birth,
            }
        )

    def test_person_factory_w_default_keyword_arguments(self):
        first_name = a_random_first_name()
        year_of_birth = a_random_year()

        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ),
            {
                "first_name": first_name,
                "last_name": "doe",
                "sex": 'M',
                "age": this_year() - year_of_birth
            }
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError