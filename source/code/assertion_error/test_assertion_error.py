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
    assert False == True


def test_failure():
    # assert False == True
    assert False == False


# NOTES
# a dictionary is not True
# a dictionary is not False
# a dictionary is not None
# a set is not True
# a set is not False
# a set is not None
# a list is not True
# a list is not False
# a list is not None
# a tuple is not True
# a tuple is not False
# a tuple is not None
# a string is not True
# a string is not False
# a string is not None
# a float is not True
# a float is not False
# a float is not None
# an integer is not True
# an integer is not False
# an integer is not None
# True is True and equal to True
# True is not False and NOT equal to False
# True is not None and NOT equal to None
# False is not True and NOT equal to True
# False is False and equal to False
# False is not None and NOT equal to None
# None is not True and NOT equal to True
# None is not False and NOT equal to True
# None is None and equal to None


# Exceptions seen
# AssertionError