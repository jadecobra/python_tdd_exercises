import datetime


def say_hello(a_dictionary):
    return (
        f'Hi, my name is {a_dictionary.get("first_name")}'
        f' {a_dictionary.get("last_name")} '
        f'and I am {a_dictionary.get("age")}'
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
        )
    }