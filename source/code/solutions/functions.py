def function_w_pass():
    pass


def function_w_return():
    return


def function_w_return_none():
    return None


def constant():
    return 'the same thing'


def constant_w_inputs(*args):
    return constant()


def identity(argument):
    return argument


def function_w_positional_arguments(
        first, second
    ):
    return first, second


def function_w_unknown_positional_arguments(*arguments):
    return arguments


def function_w_keyword_arguments(first_name, last_name):
    return ('first_name', 'last_name')


def function_w_unknown_keyword_arguments(**keyword_arguments):
    return keyword_arguments