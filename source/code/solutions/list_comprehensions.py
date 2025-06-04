def for_loop(iterable):
    result = []
    for item in iterable:
        result.append(item)
    return result


def list_comprehension(iterable):
    return [item for item in iterable]

def is_even(item):
    return item % 2 == 0


def get_even_numbers(iterable):
    return [item for item in iterable if is_even(item)]


def get_odd_numbers(iterable):
    return [item for item in iterable if not is_even(item)]