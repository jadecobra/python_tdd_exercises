import datetime


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


def say_hello(person):
    first_name = person.get('first_name')
    last_name = person.get('last_name')
    age = person.get('age')

    return (
        f'Hi, my name is {first_name} {last_name}'
        f' and I am {age}'
    )