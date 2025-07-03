def function_w_pass():
    pass


def function_w_return():
    return


def function_w_return_none():
    return None


def constant():
    return 'the same thing'


def constant_w_inputs(*arguments):
    return constant()


def identity(argument):
    return argument


def take_positional_arguments(first, second):
    return first, second


def take_unknown_positional_arguments(*arguments):
    return arguments


def take_keyword_arguments(first_name, last_name):
    return first_name, last_name


def take_unknown_keyword_arguments(**keyword_arguments):
    return keyword_arguments


def take_positional_and_keyword_arguments(first_name, last_name='Doe'):
    return first_name, last_name


def take_unknown_positional_and_keyword_arguments(*arguments, **keyword_arguments):
    return arguments, keyword_arguments