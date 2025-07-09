def w_pass():
    pass


def w_return():
    return


def w_return_none():
    return None


def constant():
    return 'the same thing'


def identity(argument):
    return argument


def w_positional_arguments(x, y):
    return x, y


def w_unknown_positional_arguments(*arguments):
    return arguments


def w_keyword_arguments(x, y):
    return x, y


def w_unknown_keyword_arguments(**keyword_arguments):
    return keyword_arguments


def w_positional_and_keyword_arguments(x, y='Doe'):
    return x, y


def w_unknown_positional_and_keyword_arguments(*arguments, **keyword_arguments):
    return arguments, keyword_arguments