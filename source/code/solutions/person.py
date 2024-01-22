import datetime


def factory(first_name=None, last_name="last_name", year_of_birth=None, sex="M"):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "sex": sex,
        "age": datetime.datetime.now().year - year_of_birth,
    }