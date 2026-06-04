import datetime


def say_hello(a_dictionary):
    return (
        f'Hi, my name is {a_dictionary.get("first_name")}'
        f' {a_dictionary.get("last_name")}'
        f' and I am {a_dictionary.get("age")}'
    )


def factory(
        first_name, year_of_birth,
        last_name='doe', sex='M',
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': (
            datetime.datetime.today().year
           -year_of_birth
        ),
    }


class Person:

    def __init__(
            self, first_name, last_name='doe',
            year_of_birth=None, sex=None,
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        return None

    def say_hello(self, person):
        age = (
            datetime.datetime.today().year
          - self.year_of_birth
        )
        return (
            f'Hi, my name is {self.first_name}'
            f' {self.last_name} and I am {age}'
        )