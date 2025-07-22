import datetime


def factory(
        first_name, last_name='doe',
        sex='M', year_of_birth=None
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': datetime.datetime.today().year - year_of_birth,
    }


def introduce(person):
    return f'Hi! My name is {person.get("first_name")} {person.get("last_name")} and I am {person.get("age")} years old'


def update_year_of_birth(person, new_year_of_birth):
    return factory(
        first_name=person.get('first_name'),
        last_name=person.get('last_name'),
        sex=person.get('sex'),
        year_of_birth=new_year_of_birth
    )


class Person(object):

    def __init__(self, first_name, year_of_birth,last_name='doe', sex='M'):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.year_of_birth = year_of_birth

    def get_age(self):
        return datetime.datetime.today().year - self.year_of_birth

    def introduce(self):
        return f'Hi! My name is {self.first_name} {self.last_name} and I am {self.get_age()} years old'