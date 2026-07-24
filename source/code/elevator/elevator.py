def elevator(
        doors_clear, number_pushed,
        above_weight_limit=False, emergency=False,
    ):
    if (
        emergency
        or above_weight_limit
        or not (
            doors_clear
            and
            number_pushed
        )
    ):
        return 'NOT MOVE'

    return 'MOVE'

    not_move = 'NOT MOVE'

    if emergency:
        return not_move

    if above_weight_limit:
        return not_move

    if not doors_clear:
        return not_move

    if not number_pushed:
        return not_move

    return 'MOVE'