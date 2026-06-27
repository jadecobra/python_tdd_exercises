def say_hi(
    first_name, last_name, year_of_birth
):
    return (
        f'Hi, my name is {first_name}'
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