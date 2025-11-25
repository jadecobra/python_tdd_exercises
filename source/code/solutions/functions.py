def w_pass():
    pass


def w_return():
    return


def w_return_none():
    return None


def constant():
    return 'the same thing'


def identity(the_input):
    return the_input


def w_positional_arguments(first_input, last_input):
    return first_input, last_input


def w_keyword_arguments(first_input, last_input):
    return first_input, last_input


def w_positional_and_keyword_arguments(first_input, last_input):
    return first_input, last_input


def w_default_arguments(first_name, last_name='doe'):
    return first_name, last_name


def w_unknown_arguments(*arguments, **keyword_arguments):
    return the_inputs, keyword_arguments