def only_takes_numbers(function):
    def wrapper(first_input, second_input):
        good_types = (int, float)
        error_message = 'Excuse me?! numbers only. Try again...'

        for value in (first_input, second_input):
            if isinstance(value, bool) or not isinstance(value, good_types):
                return error_message

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
        return 'undefined: I cannot divide by 0'


@only_takes_numbers
def add(first_input, second_input):
    return first_input + second_input