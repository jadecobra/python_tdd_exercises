import datetime


def factory(
        first_name, year_of_birth,
        last_name='doe', sex='M',
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': datetime.datetime.today().year - year_of_birth,
    }