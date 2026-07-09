import src.telephone


def test_passing_none():
    reality = src.telephone.text(None)
    my_expectation = 'I got: None'
    assert reality == my_expectation


def test_passing_booleans():
    reality = src.telephone.text(False)
    my_expectation = 'I got: False'
    assert reality == my_expectation

    reality = src.telephone.text(True)
    my_expectation = 'I got: True'
    assert reality == my_expectation


def test_passing_an_integer():
    an_integer = 1234

    reality = src.telephone.text(an_integer)
    my_expectation = f'I got: {an_integer}'
    assert reality == my_expectation


def test_passing_a_float():
    a_float = 5.678

    reality = src.telephone.text(a_float)
    my_expectation = f'I got: {a_float}'
    assert reality == my_expectation


def test_passing_a_string():
    a_string = 'hello'

    reality = src.telephone.text(a_string)
    my_expectation = f'I got: {a_string}'
    assert reality == my_expectation


def test_passing_a_tuple():
    a_tuple = (0, 1, 2, 'n')

    reality = src.telephone.text(a_tuple)
    my_expectation = f'I got: {a_tuple}'
    assert reality == my_expectation


def test_passing_a_list():
    a_list = [0, 1, 2, 'n']

    reality = src.telephone.text(a_list)
    my_expectation = f'I got: {a_list}'
    assert reality == my_expectation


def test_passing_a_set():
    a_set = {0, 1, 2, 'n'}

    reality = src.telephone.text(a_set)
    my_expectation = f'I got: {a_set}'
    assert reality == my_expectation


def test_passing_a_dictionary():
    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }

    reality = src.telephone.text(a_dictionary)
    my_expectation = f'I got: {a_dictionary}'
    assert reality == my_expectation


def test_passing_a_class():
    reality = src.telephone.text(object)
    my_expectation = "I got: <class 'object'>"
    assert reality == my_expectation

    reality = src.telephone.text(bool)
    my_expectation = "I got: <class 'bool'>"
    assert reality == my_expectation

    reality = src.telephone.text(int)
    my_expectation = "I got: <class 'int'>"
    assert reality == my_expectation

    reality = src.telephone.text(float)
    my_expectation = "I got: <class 'float'>"
    assert reality == my_expectation

    reality = src.telephone.text(str)
    my_expectation = "I got: <class 'str'>"
    assert reality == my_expectation

    reality = src.telephone.text(tuple)
    my_expectation = "I got: <class 'tuple'>"
    assert reality == my_expectation

    reality = src.telephone.text(list)
    my_expectation = "I got: <class 'list'>"
    assert reality == my_expectation

    reality = src.telephone.text(set)
    my_expectation = "I got: <class 'set'>"
    assert reality == my_expectation

    reality = src.telephone.text(dict)
    my_expectation = "I got: <class 'dict'>"
    assert reality == my_expectation


# Exceptions seen
# AssertionError
# NameError
# TypeError
# ModuleNotFoundError
# AttributeError