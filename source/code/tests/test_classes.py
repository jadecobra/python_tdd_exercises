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
        self.random_last_name = random.choice((
            'doe', 'smith', 'blow', 'public',
        ))
        self.random_year_of_birth = random.randint(
            this_year()-120, this_year()
        )
        self.random_sex = random.choice(('F', 'M'))
        self.random_factory_person = src.person.factory(
            first_name=self.random_first_name,
            last_name=self.random_last_name,
            year_of_birth=self.random_year_of_birth,
            sex=self.random_sex,
        )
        self.random_class_person = src.person.Person(
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

    def test_introduce(self):
        self.assertEqual(
            src.person.introduce(self.random_factory_person),
            f'Hi! My name is {self.random_factory_person.get("first_name").title()} {self.random_factory_person.get("last_name").title()}, I am {self.random_factory_person.get("age")} years old'
        )

    def test_update_birthday(self):
        with self.assertRaises(KeyError):
            self.random_factory_person['birthday']

        self.assertEqual(
            src.person.update_birthday(
                self.random_factory_person, 'June 2nd'
            ),
            {
                'age': self.random_factory_person.get('age'),
                'birthday': self.random_factory_person.get('birthday'),
                'first_name': self.random_first_name,
                'last_name': self.random_last_name,
                'sex': self.random_sex,
            }
        )

    def test_person_class(self):
        self.assertEqual(self.random_class_person.first_name, self.random_first_name)
        self.assertEqual(self.random_class_person.last_name, self.random_last_name)
        self.assertEqual(self.random_class_person.sex, self.random_sex)
        self.assertEqual(
            self.random_class_person.get_age(),
            this_year()-self.random_year_of_birth
        )

    def test_person_introduces(self):
        self.assertEqual(
            self.random_class_person.introduce(),
            f'Hi! My name is {self.random_first_name.title()} {self.random_last_name.title()}, I am {this_year()-self.random_year_of_birth} years old'
        )

    def test_person_has_birthday(self):
        with self.assertRaises(AttributeError):
            self.random_class_person.birthday

        birthday = '06/02'
        self.random_class_person.add_birthday(birthday)
        self.assertEqual(
            self.random_class_person.get_birthday(),
            birthday
        )

    def test_person_dictionary(self):
        self.assertEqual(
            self.random_class_person.to_dict(),
            {
                'age': this_year()-self.random_year_of_birth,
                'birthday': '20/20',
                'first_name': self.random_first_name,
                'last_name': self.random_last_name,
                'sex': self.random_sex,
            }
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
                'add_birthday',
                'get_age',
                'get_birthday',
                'introduce',
                'to_dict',
                'today',
            ]
        )


# Exceptions Encountered
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError


# what is the cost to create multiple people with the factory vs class
# use loop for instance test before abstraction to random_factory_person
# use loop for instance test before abstraction to random_class_person