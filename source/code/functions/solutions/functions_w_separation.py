def unknown_number_of_arguments(
    *positional, **keyword
):
    return positional, keyword


def optional_arguments(
    first_input, last_input='doe',
):
    return first_input, last_input


def args_and_kwargs(argument, last_input):
    return argument, last_input


def keyword_arguments(first_input, last_input):
    return first_input, last_input


def positional_arguments(first_input, last_input):
    return first_input, last_input


def identity(argument):
    return argument


def constant():
    return 'the same thing'


def return_leaves_the_function():
    return None


def w_return_none():
    return None


def w_return():
    return None


def w_pass():
    return None