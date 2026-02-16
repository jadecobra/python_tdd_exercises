def numbers_only(function):
    def wrapper(first_input, second_input):
        good_types = (int, float)
        error_message = 'brmph?! Numbers only. Try again...'

        for value in (first_input, second_input):
            if isinstance(value, bool) or not isinstance(value, good_types):
                return error_message

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