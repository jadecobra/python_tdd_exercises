def text(value):
    return f'I got: {value}'


def test_passing_none():
    reality = text(None)
    my_expectation = 'I got: None'
    assert reality == my_expectation


def test_passing_booleans():
    reality = text(False)
    my_expectation = 'I got: False'
    assert reality == my_expectation

    reality = text(True)
    my_expectation = 'I got: True'
    assert reality == my_expectation


def test_passing_an_integer():
    an_integer = 1234

    reality = text(an_integer)
    my_expectation = f'I got: {an_integer}'
    assert reality == my_expectation


def test_passing_a_float():
    a_float = 5.678

    reality = text(a_float)
    my_expectation = f'I got: {a_float}'
    assert reality == my_expectation


def test_passing_a_string():
    a_string = 'hi'

    reality = text(a_string)
    my_expectation = f'I got: {a_string}'
    assert reality == my_expectation


def test_passing_a_tuple():
    a_tuple = (0, 1, 2, 'n')

    reality = text(a_tuple)
    my_expectation = f'I got: {a_tuple}'
    assert reality == my_expectation


def test_passing_a_list():
    a_list = [0, 1, 2, 'n']

    reality = text(a_list)
    my_expectation = f'I got: {a_list}'
    assert reality == my_expectation


def test_passing_a_set():
    a_set = {0, 1, 2, 'n'}

    reality = text(a_set)
    my_expectation = f'I got: {a_set}'
    assert reality == my_expectation


def test_passing_a_dictionary():
    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }

    reality = text(a_dictionary)
    my_expectation = f'I got: {a_dictionary}'
    assert reality == my_expectation


def test_passing_a_class():
    reality = text(object)
    my_expectation = "I got: <class 'object'>"
    assert reality == my_expectation

    reality = text(bool)
    my_expectation = "I got: <class 'bool'>"
    assert reality == my_expectation

    reality = text(int)
    my_expectation = "I got: <class 'int'>"
    assert reality == my_expectation

    reality = text(float)
    my_expectation = "I got: <class 'float'>"
    assert reality == my_expectation

    reality = text(str)
    my_expectation = "I got: <class 'str'>"
    assert reality == my_expectation

    reality = text(tuple)
    my_expectation = "I got: <class 'tuple'>"
    assert reality == my_expectation

    # assert text(list) == "I got: <class 'list'>"
    reality = text(list)
    my_expectation = "I got: <class 'list'>"
    assert reality == my_expectation

    # assert text(set) == "I got: <class 'set'>"
    reality = text(set)
    my_expectation = "I got: <class 'set'>"
    assert reality == my_expectation

    # assert text(dict) == "I got: <class 'dict'>"
    reality = text(dict)
    my_expectation = "I got: <class 'dict'>"
    assert reality == my_expectation


# Exceptions seen
# AssertionError
# NameError
# ModuleNotFoundError
# AttributeError