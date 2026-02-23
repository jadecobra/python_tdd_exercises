def check_input(function):
    def wrapper(first_input, second_input):
        if isinstance(
            first_input,
            (dict, set, list, tuple, str, bool)
        ) or first_input is None:
            return 'brmph?! Numbers only. Try again...'
        return function(first_input, second_input)
    return wrapper


@check_input
def add(first_input, second_input):
    return first_input + second_input


@check_input
def divide(first_input, second_input):
    return first_input / second_input


@check_input
def multiply(first_input, second_input):
    return first_input * second_input


@check_input
def subtract(first_input, second_input):
    return first_input - second_input