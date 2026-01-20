import datetime


def factory(
        first_name, last_name='doe',
        year_of_birth=None, sex='M',
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': datetime.datetime.today().year - year_of_birth,
    }