import datetime


def this_year():
    return datetime.datetime.today().year


def factory(
        first_name, year_of_birth,
        last_name='doe', sex='M',
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': this_year() - year_of_birth,
    }


def hello(person):
    return (
        f'Hi, my name is {person.get("first_name")} '
        f'{person.get("last_name")} '
        f'and I am {person.get("age")}'
    )


def update_year_of_birth(person, new_year_of_birth):
    return factory(
        first_name=person.get('first_name'),
        last_name=person.get('last_name'),
        sex=person.get('sex'),
        year_of_birth=new_year_of_birth
    )


class Person:

    def __init__(
            self, first_name, last_name=None,
            year_of_birth=None, sex=None,
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        return None

    def hello(self):
        return (
            f'Hi, my name is {self.first_name} '
            f'{self.last_name} and I am {self.get_age()}'
        )

    def get_age(self):
        return this_year() - self.year_of_birth