import src.person


def test_joe():
    first_name = 'joe'
    last_name = 'blow'
    sex = 'M'
    year_of_birth = 1996

    reality = src.person.factory(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    my_expectation = (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )
    assert reality == my_expectation


def test_jane():
    first_name = 'jane'
    last_name = 'doe'
    sex = 'F'
    year_of_birth = 1991

    reality = src.person.factory(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    my_expectation = (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )
    assert reality == my_expectation


def test_john():
    first_name = 'john'
    last_name = 'smith'
    sex = 'M'
    year_of_birth = 1580

    reality = src.person.factory(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    my_expectation = (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )
    assert reality == my_expectation


def test_mary():
    first_name = 'mary'
    last_name = 'public'
    sex = 'F'
    year_of_birth = 2000

    reality = src.person.factory(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )
    my_expectation = (
        f'{first_name}, {last_name},'
        f' {sex}, {year_of_birth}'
    )
    assert reality == my_expectation


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError