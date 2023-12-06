
How to create a person: Tests and Solution
============================================


tests
-----

Here is the code in ``tests/test_person_factory.py``

.. code-block:: python

    import unittest
    import person
    import datetime

    def this_year():
        return datetime.datetime.now().year


    class TestPersonFactory(unittest.TestCase):

        def test_person_factory(self):
            self.assertEqual(
                person.factory(
                    first_name="sibling",
                    last_name="last_name",
                    year_of_birth=this_year(),
                    sex="F"
                ),
                {
                    "first_name": "sibling",
                    "last_name": "last_name",
                    "sex": "F",
                    "age": this_year() - this_year()
                }
            )

        def test_person_factory_takes_in_variable_inputs(self):
            first_name = "me"
            last_name = "my_last_name"
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
                }
            )

        def test_person_factory_with_default_keyword_arguments(self):
            first_name = "child_a"
            sex = "M"
            year_of_birth = 2014
            self.assertEqual(
                person.factory(
                    first_name=first_name,
                    year_of_birth=year_of_birth,
                    sex=sex,
                ),
                {
                    "first_name": first_name,
                    "last_name": "last_name",
                    "sex": sex,
                    "age": this_year() - year_of_birth
                }
            )

        def test_person_factory_with_sex_default_keyword_arguments(self):
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
                    "sex": "M"
                }
            )

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError

solution
---------

Here is the solution in ``person.py``

.. code-block:: python

    import datetime

    def factory(
        first_name=None, last_name="last_name",
        year_of_birth=None, sex="M"
    ):
        return {
            'age': datetime.datetime.now().year  - year_of_birth,
            'first_name': first_name,
            'last_name': last_name,
            'sex': sex,
        }