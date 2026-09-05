import src.person


def say_hello(
        first_name, last_name, year_of_birth,
    ):
    return (
        f'Hello, my name is {first_name}'
        f' {last_name} and I am'
        f' {2026-year_of_birth}.'
    )


def assert_equal(left, right):
    assert left == right



def assert_factory_works(
        first_name, last_name,
        sex, year_of_birth,
    ):
    assert_equal(
        src.person.person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        ),
        (
            f'{first_name}, {last_name},'
            f' {sex}, {year_of_birth}'
        )
    )


def assert_say_hello_works(
        first_name, last_name, year_of_birth,
    ):
    assert_equal(
        src.person.say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        ),
        say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
    )


def assert_person_can_say_hello(
        first_name, last_name,
        sex, year_of_birth,
    ):
    assert_equal(
        src.person.Person(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            year_of_birth=year_of_birth,
        ).say_hello(),
        say_hello(
            first_name=first_name,
            last_name=last_name,
            year_of_birth=year_of_birth,
        )
    )



def test_joe():
    first_name = 'joe'
    last_name = 'blow'
    sex = 'M'
    year_of_birth = 1996

    assert_factory_works(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )

    assert_say_hello_works(
        first_name=first_name,
        last_name=last_name,
        year_of_birth=year_of_birth,
    )

    assert_person_can_say_hello(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )


def test_jane():
    first_name = 'jane'
    last_name = 'doe'
    sex = 'F'
    year_of_birth = 1991

    assert_factory_works(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )

    assert_say_hello_works(
        first_name=first_name,
        last_name=last_name,
        year_of_birth=year_of_birth,
    )

    assert_person_can_say_hello(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )


def test_john():
    first_name = 'john'
    last_name = 'smith'
    sex = 'M'
    year_of_birth = 1580

    assert_factory_works(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )

    assert_say_hello_works(
        first_name=first_name,
        last_name=last_name,
        year_of_birth=year_of_birth,
    )

    assert_person_can_say_hello(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )


def test_mary():
    first_name = 'mary'
    last_name = 'public'
    sex = 'F'
    year_of_birth = 2000

    assert_factory_works(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )

    assert_say_hello_works(
        first_name=first_name,
        last_name=last_name,
        year_of_birth=year_of_birth,
    )

    assert_person_can_say_hello(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        year_of_birth=year_of_birth,
    )


def test_dir_person_class():
    reality = dir(src.person.Person)
    my_expectation = [
        '__class__',
        '__delattr__',
        '__dict__',
        '__dir__',
        '__doc__',
        '__eq__',
        '__firstlineno__',
        '__format__',
        '__ge__',
        '__getattribute__',
        '__getstate__',
        '__gt__',
        '__hash__',
        '__init__',
        '__init_subclass__',
        '__le__',
        '__lt__',
        '__module__',
        '__ne__',
        '__new__',
        '__reduce__',
        '__reduce_ex__',
        '__repr__',
        '__setattr__',
        '__sizeof__',
        '__static_attributes__',
        '__str__',
        '__subclasshook__',
        '__weakref__',
        'say_hello'
    ]
    assert reality == my_expectation


def test_dir_person_instance():
    an_instance_of_person = src.person.Person(
        first_name='first_name',
        last_name='last_name',
        sex='M',
        year_of_birth=2026,
    )

    reality = dir(an_instance_of_person)
    my_expectation = [
        '__class__',
        '__delattr__',
        '__dict__',
        '__dir__',
        '__doc__',
        '__eq__',
        '__firstlineno__',
        '__format__',
        '__ge__',
        '__getattribute__',
        '__getstate__',
        '__gt__',
        '__hash__',
        '__init__',
        '__init_subclass__',
        '__le__',
        '__lt__',
        '__module__',
        '__ne__',
        '__new__',
        '__reduce__',
        '__reduce_ex__',
        '__repr__',
        '__setattr__',
        '__sizeof__',
        '__static_attributes__',
        '__str__',
        '__subclasshook__',
        '__weakref__',
        'first_name',
        'last_name',
        'say_hello',
        'sex',
        'year_of_birth',
    ]
    assert reality == my_expectation


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError
# SyntaxError