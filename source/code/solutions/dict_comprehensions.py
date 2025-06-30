def for_loop(iterable):
    result = {}
    for item in iterable:
        result[item] = item
    return result


def dict_comprehension(iterable):
    return {item: item for item in iterable}


def square(iterable):
    return {item: item**2 for item in iterable}