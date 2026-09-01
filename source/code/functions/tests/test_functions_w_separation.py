import src.functions


def assert_equal(input_1, input_2):
    assert input_1 == input_2


def assert_is_none(something):
    assert something is None


def test_making_a_function_w_pass():
    assert_is_none(src.functions.w_pass())


def test_making_a_function_w_return():
    assert_is_none(src.functions.w_return())


def test_making_a_function_w_return_none():
    assert_is_none(src.functions.w_return_none())


def test_what_happens_after_functions_return():
    assert_is_none(
        src.functions.return_leaves_the_function()
    )


def test_constant_function():
    assert_equal(
        src.functions.constant(), 'the same thing'
    )


def test_identity_function():
    assert_is_none(src.functions.identity(None))
    assert_equal(src.functions.identity(object), object)


def test_why_use_a_function():
    def add_x(number):
        return 3 + number

    assert_equal(add_x(0), 3)
    assert_equal(add_x(1), 4)
    assert_equal(add_x(2), 5)
    assert_equal(add_x(3), 6)
    assert_equal(add_x(4), 7)
    assert_equal(add_x(5), 8)
    assert_equal(add_x(6), 9)
    assert_equal(add_x(7), 10)
    assert_equal(add_x(8), 11)
    assert_equal(add_x(9), 12)


def test_positional_arguments():
    positional_arguments = src.positional_arguments

    first, last = 'first', 'last'

    assert_equal(
        positional_arguments(first, last),
        (first, last)
    )
    assert_equal(
        positional_arguments(last, first),
        (last, first)
    )

    assert_equal(
        positional_arguments(0, 1), (0, 1)
    )

    a_tuple = (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']
    assert_equal(
        positional_arguments(a_tuple, a_list),
        (a_tuple, a_list)
    )

    a_set = {0, 1, 2, 'n'}
    a_dictionary = {'key': 'value'}
    assert_equal(
        src.functions.keyword_arguments(
            a_set, a_dictionary,
        ),
        (a_set, a_dictionary)
    )


def test_keyword_arguments():
    keyword_arguments = src.functions.keyword_arguments
    first, last = 'first', 'last'

    assert_equal(
        keyword_arguments(
            first_input=first, last_input=last,
        ),
        (first, last)
    )
    assert_equal(
        keyword_arguments(
            last_input=last, first_input=first,
        ),
        (first, last)
    )

    assert_equal(
        keyword_arguments(
            last_input=0, first_input=1,
        ),
        (1, 0)
    )

    a_tuple = (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']
    assert_equal(
        keyword_arguments(
            first_input=a_tuple,
            last_input=a_list,
        ),
        (a_tuple, a_list)
    )

    a_set = {0, 1, 2, 'n'}
    a_dictionary = {'key': 'value'}
    assert_equal(
        src.functions.positional_arguments(
            last_input=a_dictionary,
            first_input=a_set,
        ),
        (a_set, a_dictionary)
    )


def test_args_and_kwargs():
    first, last = 'first', 'last'

    assert_equal(
        src.functions.args_and_kwargs(
            first, last_input=last
        ),
        (first, last)
    )


def test_optional_arguments():
    optional_arguments = src.functions.optional_arguments
    first_name, last_name = 'jane', 'doe'
    assert_equal(
        optional_arguments(
            first_name,
        ),
        (first_name, last_name)
    )

    first_name, blow = 'joe', 'blow'
    assert_equal(
        optional_arguments(
            first_name, blow
        ),
        (first_name, blow)
    )

    first_name = 'john'
    assert_equal(
        optional_arguments(
            first_input=first_name,
        ),
        (first_name, last_name)
    )

    last_name = 'smith'
    assert_equal(
        optional_arguments(
            last_input=last_name,
            first_input=first_name,
        ),
        (first_name, last_name)
    )


def test_unknown_number_of_arguments():
    unknown_number_of_arguments = (
        src.functions.unknown_number_of_arguments
    )
    a_tuple = (0, 1)
    a_dictionary = {'a': 2, 'b': 3}
    assert_equal(
        unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        ),
        (a_tuple, a_dictionary)
    )

    a_dictionary = {'a': 2, 'b': 3, 'c': 4}
    assert_equal(
        unknown_number_of_arguments(
            *a_tuple, **a_dictionary,
        ),
        (a_tuple, a_dictionary)
    )

    a_tuple = (0, 1, 2)
    a_dictionary = {'a': 3, 'b': 4, 'c': 5}
    assert_equal(
        unknown_number_of_arguments(
            *a_tuple, **a_dictionary
        ),
        (a_tuple, a_dictionary)
    )

    a_tuple = (0, 1, 2, 'n')
    assert_equal(
        unknown_number_of_arguments(*a_tuple),
        (a_tuple, {})
    )

    a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 'n'}
    assert_equal(
        unknown_number_of_arguments(**a_dictionary),
        ((), a_dictionary)
    )

    assert_equal(
        unknown_number_of_arguments(), ((), {})
    )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# SyntaxError