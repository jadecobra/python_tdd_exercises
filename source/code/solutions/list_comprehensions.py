def for_loop(iterable):
    result = []
    for item in iterable:
        result.append(item)
    return result


def list_comprehension(iterable):
    return [item for item in iterable]


def get_even_numbers(iterable):
    return [item for item in iterable if item % 2 == 0]


def get_odd_numbers(iterable):
    return [item for item in iterable if item % 2 != 0]