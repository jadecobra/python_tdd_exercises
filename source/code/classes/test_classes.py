class WPass: pass


class WParentheses(): pass


class WObject(object): pass


def test_making_a_class_w_pass():
    assert isinstance(WPass(), object)
    assert issubclass(WPass, object)


def test_making_a_class_w_parentheses():
    assert isinstance(WParentheses(), object)
    assert issubclass(WParentheses, object)


def test_making_a_class_w_object():
    assert isinstance(WObject(), object)
    assert issubclass(WObject, object)


def test_none_v_object():
    assert isinstance(None, object)
    # fails because None is not a class
    # assert issubclass(None, object)


def test_is_a_boolean_an_object():
    assert isinstance(bool, object)
    assert issubclass(bool, object)


def test_is_an_integer_an_object():
    assert isinstance(int, object)
    assert issubclass(int, object)


def test_is_a_float_an_object():
    assert isinstance(float, object)
    assert issubclass(float, object)


def test_is_a_string_an_object():
    assert isinstance(str, object)
    assert issubclass(str, object)


def test_is_a_tuple_an_object():
    assert isinstance(tuple, object)
    assert issubclass(tuple, object)


def test_is_a_list_an_object():
    assert isinstance(list, object)
    assert issubclass(list, object)


def test_is_a_set_an_object():
    assert isinstance(set, object)
    assert issubclass(set, object)


def test_is_a_dictionary_an_object():
    assert isinstance(dict, object)
    assert issubclass(dict, object)


def test_dir_object():
    reality = dir(object)
    my_expectation = [
        '__class__', '__delattr__', '__dir__',
        '__doc__', '__eq__', '__format__', '__ge__',
        '__getattribute__', '__getstate__', '__gt__',
        '__hash__', '__init__', '__init_subclass__',
        '__le__', '__lt__', '__ne__', '__new__',
        '__reduce__', '__reduce_ex__', '__repr__',
        '__setattr__', '__sizeof__', '__str__',
        '__subclasshook__'
    ]
    assert reality == my_expectation


# Exceptions seen
# AssertionError
# NameError
# TypeError