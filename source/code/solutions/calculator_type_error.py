def only_takes_numbers(function):
    def wrapper(first_input, second_input):
        error_message = 'I am a calculator, I only work with numbers'
        if isinstance(first_input, str) or isinstance(second_input, str):
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
        return 'undefined: I cannot divide by 0'


@only_takes_numbers
def add(first_input, second_input):
    return first_input + second_input