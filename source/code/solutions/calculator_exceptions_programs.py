def subtract(first_input, second_input):
    return first_input - second_input


def multiply(first_input, second_input):
    return first_input * second_input


def divide(first_input, second_input):
    try:
        return first_input / second_input
    except ZeroDivisionError:
        return 'brmph?! cannot divide by 0. Try again...'


def add(first_input, second_input):
    return first_input + second_input