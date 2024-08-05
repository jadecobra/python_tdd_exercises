import datetime


def factory(
        first_name=None, last_name='doe',
        sex='M', year_of_birth=None
    ):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'age': datetime.datetime.today().year - year_of_birth,
    }