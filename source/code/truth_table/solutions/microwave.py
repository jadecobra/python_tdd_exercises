def microwave(
        door_is_open, start_is_pushed,
        timer_is_set=False, too_hot=False,
    ):
    off = 'OFF'

    if too_hot:
        return off
    if not timer_is_set:
        return off
    if not start_is_pushed:
        return off
    if door_is_open:
        return off

    return 'HEATING'

    if (
        not door_is_open
        and start_is_pushed
        and timer_is_set
        and not too_hot
    ):
        return 'HEATING'

    return 'OFF'