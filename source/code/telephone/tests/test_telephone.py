def text(the_input):
    return f'I got: {the_input}'


def test_passing_none():
    assert text(None) == 'I got: None'


def test_passing_booleans():
    assert text(False) == 'I got: False'
    assert text(True) == 'I got: True'


def test_passing_an_integer():
    an_integer = 1234
    assert text(an_integer) == f'I got: {an_integer}'


def test_passing_a_float():
    a_float = 5.678
    assert text(a_float) == f'I got: {a_float}'


def test_passing_a_string():
    a_string = 'hello'
    assert text(a_string) == f'I got: {a_string}'


def test_passing_a_tuple():
    a_tuple = (0, 1, 2, 'n')
    assert text(a_tuple) == f'I got: {a_tuple}'


def test_passing_a_list():
    a_list = [0, 1, 2, 'n']
    assert text(a_list) == f'I got: {a_list}'


def test_passing_a_set():
    a_set = {0, 1, 2, 'n'}
    assert text(a_set) == f"I got: {a_set}"


def test_passing_a_dictionary():
    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }
    reality = text(a_dictionary)
    my_expectation = f'I got: {a_dictionary}'
    assert reality == my_expectation


def test_passing_a_class():
    assert text(object) == "I got: <class 'object'>"
    assert text(bool) == "I got: <class 'bool'>"
    assert text(int) == "I got: <class 'int'>"
    assert text(float) == "I got: <class 'float'>"
    assert text(str) == "I got: <class 'str'>"
    assert text(tuple) == "I got: <class 'tuple'>"
    assert text(list) == "I got: <class 'list'>"
    assert text(set) == "I got: <class 'set'>"
    assert text(dict) == "I got: <class 'dict'>"


# Exceptions seen
# AssertionError
# NameError
# TypeError