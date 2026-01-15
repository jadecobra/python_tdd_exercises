def only_takes_numbers(function):
    def wrapper(first_input, second_input):
        good_types = (int, float)
        error_message = 'Excuse me?! Numbers only! try again...'

        if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
            return error_message
        else:
            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
    return wrapper


@only_takes_numbers
def subtract(first_input, second_input):
    return first_input - second_input


@only_takes_numbers
def multiply(first_input, second_input):
    return first_input * second_input


@only_takes_numbers
def divide(first_input, second_input):
    try:
        return first_input / second_input
    except ZeroDivisionError:
        return 'brmph?! cannot divide by 0. Try again...'


@only_takes_numbers
def add(first_input, second_input):
    return first_input + second_input