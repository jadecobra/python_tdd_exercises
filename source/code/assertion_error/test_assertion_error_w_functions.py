def assert_equal(x, y):
    assert x == y


def assert_not_equal(x, y):
    assert x != y


def assert_is_not(x, y):
    assert x is not y


def assert_is_not_none(x):
    assert_is_not(x, None)


def assert_is_not_false(x):
    assert_is_not(x, False)


def assert_is_not_true(x):
    assert_is_not(x, True)


def test_assert_keyword():
    assert_equal(1+1, 2)
    assert_equal('1'+'1', '11')
    assert_equal('I am'+' alive', 'I am alive')


def test_assertion_error_w_none():
    assert None is None

    assert_is_not_none(False)
    assert_is_not_none(True)
    assert_is_not_none(0)
    assert_is_not_none(0.0)
    assert_is_not_none('')
    assert_is_not_none(())
    assert_is_not_none([])
    assert_is_not_none(set())
    assert_is_not_none({})


def test_assertion_error_w_false():
    assert False is False

    assert_is_not_false(None)
    assert_is_not_false(True)
    assert_is_not_false(0)
    assert_is_not_false(0.0)
    assert_is_not_false('')
    assert_is_not_false(())
    assert_is_not_false([])
    assert_is_not_false(set())
    assert_is_not_false({})


def test_assertion_error_w_true():
    assert True is True

    assert_is_not_true(None)
    assert_is_not_true(False)
    assert_is_not_true(0)
    assert_is_not_true(0.0)
    assert_is_not_true('')
    assert_is_not_true(())
    assert_is_not_true([])
    assert_is_not_true(set())
    assert_is_not_true({})


def test_assertion_error_w_equality():
    assert_equal(None, None)
    assert_not_equal(False, None)
    assert_not_equal(False, True)
    assert_equal(False, False)
    assert_not_equal(True, None)
    assert_equal(True, True)


def test_assertion_error_w_is_vs_equal():
    assert_is_not(0, 0.0)
    assert_equal(0, 0.0)


def will_not_run():
    # will not run because
    # the name does not start with test
    assert_equal(False, True)


def test_failure():
    # assert_equal(False, True)
    assert_not_equal(False, True)


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