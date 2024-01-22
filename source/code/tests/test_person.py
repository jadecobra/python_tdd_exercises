import datetime
import person
import unittest

def this_year():
    return datetime.datetime.now().year


class TestPersonFactory(unittest.TestCase):
    def test_person_factory(self):
        first_name = "baby"
        last_name = "last_name"
        sex = "F"
        year_of_birth = this_year()

        self.assertEqual(
            person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            {
                "first_name": first_name,
                "last_name": last_name,
                "sex": sex,
                "age": this_year() - year_of_birth,
            },
        )

    def test_person_factory_takes_in_variable_inputs(self):
        first_name = "john"
        last_name = "doe"
        sex = "M"
        year_of_birth = 1983

        self.assertEqual(
            person.factory(
                first_name=first_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                sex=sex,
            ),
            {
                "first_name": first_name,
                "last_name": last_name,
                "sex": sex,
                "age": this_year() - year_of_birth,
            },
        )

    def test_person_factory_with_default_keyword_arguments(self):
        first_name = "child_a"
        sex = "M"
        year_of_birth = 2014

        self.assertEqual(
            person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
                sex=sex
            ),
            {
                "first_name": first_name,
                "last_name": "last_name",
                "sex": sex,
                "age": this_year() - year_of_birth,
            },
        )

    def test_person_factory_with_sex_default_keyword_argument(self):
        first_name = "person"
        year_of_birth = 1900

        self.assertEqual(
            person.factory(
                first_name=first_name,
                year_of_birth=year_of_birth,
            ),
            {
                "first_name": first_name,
                "last_name": "last_name",
                "age": this_year() - year_of_birth,
                "sex": "M",
            },
        )

# Exceptions Encountered
# AssertionError
# AttributeError
# NameError
# TypeError
