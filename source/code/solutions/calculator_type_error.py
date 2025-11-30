def check_input(function):
    def wrapper(input_1, input_2):
        error_message = 'I only work with numbers'
        if isinstance(input_1, str) or isinstance(input_2, str):
            return error_message
        try:
            return function(input_1, input_2)
        except TypeError:
            return error_message
    return wrapper


@check_input
def subtract(input_1, input_2):
    return input_1 - input_2


@check_input
def multiply(input_1, input_2):
    return input_1 * input_2


@check_input
def divide(input_1, input_2):
    return input_1 / input_2


@check_input
def add(input_1, input_2):
    return input_1 + input_2