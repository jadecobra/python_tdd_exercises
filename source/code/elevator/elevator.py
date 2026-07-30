def controller(
    number_pushed, doors_closed=False,
    above_weight=False, emergency=False,
):
    if (
        not (number_pushed and doors_closed)
        or above_weight
        or emergency
    ):
        return False
    return True