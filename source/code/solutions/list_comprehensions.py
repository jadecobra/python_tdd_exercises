def for_loop(container):
    result = []
    for thing in container:
        result.append(thing)
    return result


def list_comprehension(collection):
    return [element for element in collection]


def is_even(number):
    return number % 2 == 0


def get_even_numbers(numbers):
    return [number for number in numbers if is_even(number)]


def get_odd_numbers(numbers):
    return [number for number in numbers if not is_even(number)]


def square(numbers):
    return [number**2 for number in numbers]