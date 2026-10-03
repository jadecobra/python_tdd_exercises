def numbers_only(function):
    def decorator(first_input, second_input):
        bad_data_types = (str, list, bool)
        error_message = 'brmph?! Numbers only. Try again...'

        for value in (first_input, second_input):
            if (
                value is None
                or
                isinstance(value, bad_data_types)
            ):
                return error_message

        try:
            return function(first_input, second_input)
        except TypeError:
            return error_message
    return decorator


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
