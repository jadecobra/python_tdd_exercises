def numbers_only(function):
    def wrapper(first_input, second_input):
        error_message = 'brmph?! Numbers only. Try again...'
        if isinstance(first_input, str) or isinstance(second_input, str):
            return error_message
        else:
            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
    return wrapper


@numbers_only
def subtract(first_input, second_input):
    return first_input - second_input


@numbers_only
def multiply(first_input, second_input):
    return first_input * second_input


@numbers_only
def divide(first_input, second_input):
    try:
        return first_input / second_input
    except ZeroDivisionError:
        return 'brmph?! I cannot divide by 0. Try again...'


@numbers_only
def add(first_input, second_input):
    return first_input + second_input