import datetime
import src.person
import unittest


def this_year():
    return datetime.datetime.now().year


class TestPerson(unittest.TestCase):

    def assertFactoryWorks(
        self, first_name=None, last_name='doe',
        sex='M', year_of_birth=None,
    ):
        self.assertEqual(
            src.person.factory(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                year_of_birth=year_of_birth
            ),
            {
                'first_name': first_name,
                'last_name': last_name,
                'sex': sex,
                'age': this_year() - year_of_birth
            }
        )

    def test_person_factory(self):
        self.assertFactoryWorks(
            first_name='baby',
            last_name='last_name',
            sex='F',
            year_of_birth=this_year(),
        )

    def test_person_factory_w_variable_inputs(self):
        self.assertFactoryWorks(
            first_name='john',
            last_name='doe',
            sex='M',
            year_of_birth=1942,
        )

    def test_person_factory_w_last_name_default_argument(self):
        self.assertFactoryWorks(
            first_name='child_a',
            sex='M',
            year_of_birth=2014,
        )

    def test_person_factory_w_sex_default_argument(self):
        self.assertFactoryWorks(
            first_name='person',
            year_of_birth=1900,
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError