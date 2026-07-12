import datetime


class Person:

    def __init__(
        self, first_name, last_name,
        sex, year_of_birth=None,
        is_citizen=True,
        passed_test=False,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.sex = sex
        self.is_citizen = is_citizen
        self.passed_test = passed_test
        self.age = calculate_age(year_of_birth)

    def can_get_license(self):
        return self.check_age(
            self.age, self.passed_test
        )

    def can_vote(self):
        return self.check_age(
            self.age, self.is_citizen
        )

    @staticmethod
    def check_age(age, response):
        if age < 18:
            return False
        return response

    def say_hello(self):
        return (
            f'Hello, my name is {self.first_name}'
            f' {self.last_name} and I am'
            f' {self.age}.'
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