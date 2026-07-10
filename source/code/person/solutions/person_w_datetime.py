import datetime


class Person:

    def __init__(
        self, first_name, last_name,
        sex, year_of_birth=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        assert year_of_birth is not None
        self.year_of_birth = year_of_birth
        self.sex = sex

    def get_age(self):
        return (
            datetime.datetime.now().year
          - self.year_of_birth
        )

    def say_hello(self):
        return (
            f'Hello, my name is {self.first_name}'
            f' {self.last_name} and I am'
            f' {self.get_age()}.'
        )


def say_hello(
    first_name, last_name, year_of_birth
):
    return (
        f'Hello, my name is {first_name}'
        f' {last_name} and I am'
        f' {2026-year_of_birth}.'
    )


def factory(
        first_name, last_name,
        sex, year_of_birth
    ):
    return (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )