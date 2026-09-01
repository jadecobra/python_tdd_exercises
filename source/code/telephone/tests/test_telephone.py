def assert_equal(a, b):
    assert a == b


def text(the_input):
    return f'I got: {the_input}'


def test_passing_none():
    assert_equal(text(None), 'I got: None')


def test_passing_booleans():
    assert_equal(text(False), 'I got: False')
    assert_equal(text(True), 'I got: True')


def test_passing_an_integer():
    an_integer = 1234
    assert_equal(text(an_integer), f'I got: {an_integer}')


def test_passing_a_float():
    a_float = 5.678
    assert_equal(text(a_float), f'I got: {a_float}')


def test_passing_a_string():
    a_string = 'hello'
    assert_equal(text('hello'), f'I got: {a_string}')


def test_passing_a_tuple():
    a_tuple = (0, 1, 2, 'n')
    assert_equal(text(a_tuple), f"I got: {a_tuple}")


def test_passing_a_list():
    a_list = [0, 1, 2, 'n']
    assert_equal(text(a_list), f'I got: {a_list}')


def test_passing_a_set():
    a_set = {0, 1, 2, 'n'}
    assert_equal(text(a_set), f'I got: {a_set}')


def test_passing_a_dictionary():
    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }
    reality = text(a_dictionary)
    my_expectation = f'I got: {a_dictionary}'
    assert_equal(reality, my_expectation)


def test_passing_a_class():
    assert_equal(
        text(object), "I got: <class 'object'>"
    )
    assert_equal(text(bool), "I got: <class 'bool'>")
    assert_equal(text(int), "I got: <class 'int'>")
    assert_equal(text(float), "I got: <class 'float'>")
    assert_equal(text(str), "I got: <class 'str'>")
    assert_equal(text(tuple), "I got: <class 'tuple'>")
    assert_equal(text(list), "I got: <class 'list'>")
    assert_equal(text(set), "I got: <class 'set'>")
    assert_equal(text(dict), "I got: <class 'dict'>")


# Exceptions seen
# AssertionError
# NameError
# TypeError