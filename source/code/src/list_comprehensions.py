def a_for_loop(an_iterable):
    result = []
    for stuff in an_iterable:
        result.append(stuff)
    return result


def a_list_comprehension(a_collection):
    return [element for element in a_collection]


def is_even(number):
    return number % 2 == 0


def get_even_numbers(numbers):
    return list(filter(is_even, numbers))
    return [
        number for number in numbers
                if is_even(number)
    ]


def get_odd_numbers(numbers):
    import itertools
    return list(itertools.filterfalse(is_even, numbers))
    return list(
        filter(
            lambda number: not is_even(number),
            numbers
        )
    )
    return [
        number for number in numbers
                if not is_even(number)
    ]


def square(numbers):
    return list(map(lambda number: number**2, numbers))
    return [number**2 for number in numbers]