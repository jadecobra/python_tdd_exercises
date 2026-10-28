def test_assert_keyword():
    assert 1 + 1 == 2

    assert '1' + '1' == '11'

    assert 'I am' + ' alive' == 'I am alive'


def test_assertion_error_w_none():
    assert None is None

    assert False is not None

    assert True is not None

    assert 0 is not None

    assert 0.0 is not None

    assert '' is not None

    assert () is not None

    assert [] is not None

    assert set() is not None

    assert {} is not None


def test_assertion_error_w_false():
    assert None is not False

    assert False is False

    assert True is not False

    assert 0 is not False

    assert 0.0 is not False

    assert '' is not False

    assert () is not False

    assert [] is not False

    assert set() is not False

    assert {} is not False


def test_assertion_error_w_true():
    assert None is not True

    assert False is not True

    assert True is True

    assert 0 is not True

    assert 0.0 is not True

    assert '' is not True

    assert () is not True

    assert [] is not True

    assert set() is not True

    assert {} is not True


def test_assertion_error_w_equality():
    assert None == None

    assert False != None

    assert False != True

    assert False == False

    assert True != None

    assert True == True


def test_assertion_error_w_is_vs_equal():
    assert 0 is not 0.0

    assert 0 == 0.0


def will_not_run():
    # will not run because
    # the name does not start with test
    assert False == True


def test_failure():
    # assert False == True
    assert False != True


# NOTES
# a dictionary is not the same object as True
# a dictionary is not the same object as False
# a dictionary is not the same object as None
# a set is not the same object as True
# a set is not the same object as False
# a set is not the same object as None
# a list is not the same object as True
# a list is not the same object as False
# a list is not the same object as None
# a tuple is not the same object as True
# a tuple is not the same object as False
# a tuple is not the same object as None
# a string is not the same object as True
# a string is not the same object as False
# a string is not the same object as None
# a float is not the same object as True
# a float is not the same object as False
# a float is not the same object as None
# an integer is not the same object as True
# an integer is not the same object as False
# an integer is not the same object as None
# True is True and equal to True
# True is not equal to False
# True is not the same object as False
# True is not equal to None
# True is not the same object as None
# False is not equal to True
# False is not the same object as True
# False is False and equal to False
# False is not equal to None
# False is not the same object as None
# None is not equal to True
# None is not the same object as True
# None is not equal to False
# None is not the same object as False
# None is None and equal to None

# Exceptions seen
# AssertionError
# IndentationError