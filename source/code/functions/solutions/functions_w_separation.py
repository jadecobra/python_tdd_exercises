def w_pass():
    pass


def w_return():
    return


def w_return_none():
    return None


def return_leaves_the_function():
    return None
    return 'only one way for this line to run'


def constant():
    return 'the same thing'


def identity(the_input):
    return the_input


def positional_arguments(first_input, last_input):
    return first_input, last_input


def keyword_arguments(first_input, last_input):
    return first_input, last_input


def args_and_kwargs(first_input, last_input):
    return first_input, last_input


def optional_arguments(
    first_input, last_input='doe',
):
    return first_input, last_input


def unknown_number_of_arguments(
    *positional_arguments, **keyword_arguments
):
    return positional_arguments, keyword_arguments