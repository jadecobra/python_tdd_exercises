def subtract(first_input, second_input):
    return first_input - second_input


def multiply(first_input, second_input):
    return first_input * second_input


def divide(first_input, second_input):
    try:
        return first_input / second_input
    except ZeroDivisionError:
        return 'undefined: I cannot divide by 0'


def add(first_input, second_input):
    return first_input + second_input