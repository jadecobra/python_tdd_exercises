def elevator(
        doors_clear, number_pushed,
        above_weight_limit=False,
    ):
    not_move = 'NOT MOVE'

    if not doors_clear:
        return not_move

    if not number_pushed:
        return not_move

    return 'MOVE'