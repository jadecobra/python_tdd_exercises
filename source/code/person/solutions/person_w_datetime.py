import datetime


class Person:

    def __init__(
        self, first_name, last_name,
        sex, year_of_birth=None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.sex = sex

    def say_hello(self):
        return (
            f'Hello, my name is {self.first_name}'
            f' {self.last_name} and I am'
            f' {calculate_age(self.year_of_birth)}.'
        )


def calculate_age(year_of_birth):
    assert isinstance(year_of_birth, int)
    age = (
        datetime.date.today().year
      - year_of_birth
    )
    assert age <= 120
    return age


def say_hello(
    first_name, last_name, year_of_birth,
):
    return (
        f'Hello, my name is {first_name}'
        f' {last_name} and I am'
        f' {calculate_age(year_of_birth)}.'
    )


def factory(
        first_name, last_name,
        sex, year_of_birth,
    ):
    return (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )