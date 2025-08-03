import datetime
import random
import src.person
import unittest


def this_year():
    return datetime.datetime.now().year


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.random_first_name = random.choice((
            'jane', 'joe', 'john', 'person',
        ))
        self.random_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.new_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.random_last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        self.random_sex = random.choice(('F', 'M'))
        self.age = this_year() - self.random_year_of_birth
        self.random_factory_person = src.person.factory(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
            sex=self.random_sex,
        )
        self.random_classy_person = src.person.Person(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
            sex=self.random_sex,
        )

    def test_takes_keyword_arguments(self):
        self.assertEqual(
            src.person.factory(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                year_of_birth=self.random_year_of_birth,
            ),
            dict(
                first_name=self.random_first_name,
                last_name=self.random_last_name,
                sex=self.random_sex,
                age=this_year()-self.random_year_of_birth,
            )
        )

    def test_function_w_default_keyword_arguments(self):
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
        self.assertEqual(
            src.person.factory(
                first_name=self.random_first_name,
            ),
            dict(
                first_name=self.random_first_name,
                last_name='doe',
                sex='M',
                age=0,
            )
        )

    def test_factory_person_introduction(self):
        self.assertEqual(
            src.person.introduce(self.random_factory_person),
            f'Hi! My name is {self.random_first_name} '
            f'{self.random_last_name} '
            f'and I am {self.age} years old'
        )

    def test_classy_person_introduction(self):
        self.assertEqual(
            self.random_classy_person.introduce(),
            f'Hi! My name is {self.random_first_name} '
            f'{self.random_last_name} '
            f'and I am {self.age} years old'
        )

    def test_factory_update_year_of_birth(self):
        self.assertEqual(
            self.random_factory_person.get('age'),
            self.age
        )
        self.original_age = this_year() - self.random_year_of_birth
        self.assertEqual(self.random_factory_person.get('age'), self.original_age)
        with self.assertRaises(KeyError):
            self.random_factory_person['year_of_birth']

        self.random_factory_person['year_of_birth'] = self.new_year_of_birth
        self.assertEqual(
            self.random_factory_person.get('age'),
            self.original_age
        )

        self.assertEqual(
            src.person.update_year_of_birth(
                self.random_factory_person,
                self.new_year_of_birth
            ),
            {
                'first_name': self.random_factory_person.get('first_name'),
                'last_name': self.random_factory_person.get('last_name'),
                'sex': self.random_factory_person.get('sex'),
                'age': this_year()-self.new_year_of_birth
            }
        )

    def test_person_class_update_year_of_birth(self):
        self.assertEqual(
            self.random_classy_person.get_age(),
            self.age
        )
        self.assertIsNone(
            self.random_classy_person.update_year_of_birth(self.new_year_of_birth)
        )
        self.assertEqual(
            self.random_classy_person.get_age(),
            this_year()-self.new_year_of_birth
        )

    def test_attributes_and_methods_of_classes(self):
        self.assertEqual(
            dir(src.person.Person),
            [
                '__class__',
                '__delattr__',
                '__dict__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__firstlineno__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__getstate__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__le__',
                '__lt__',
                '__module__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__setattr__',
                '__sizeof__',
                '__static_attributes__',
                '__str__',
                '__subclasshook__',
                '__weakref__',
                'get_age',
                'introduce',
                'update_year_of_birth'
            ]
        )

# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError