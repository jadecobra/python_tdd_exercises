import datetime
import random
import src.person
import unittest


def this_year():
    return datetime.datetime.now().year


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))

    def test_factory_takes_keyword_arguments(self):
        keyword_arguments = dict(
            first_name=self.first_name,
            last_name=random.choice((
                'doe', 'smith', 'blow', 'public',
            )),
            sex=random.choice(('F', 'M')),
        )

        self.assertEqual(
            src.person.factory(
                **keyword_arguments,
                year_of_birth=self.year_of_birth,
            ),
            dict(
                **keyword_arguments,
                age=this_year()-self.year_of_birth,
            )
        )

    def test_factory_w_default_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.first_name,
                year_of_birth=self.year_of_birth,
            ),
            dict(
                first_name=self.first_name,
                last_name='doe',
                sex='M',
                age=this_year()-self.year_of_birth,
            )
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError