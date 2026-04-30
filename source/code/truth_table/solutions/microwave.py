def microwave(
        door_is_open, start_is_pushed,
        timer_is_set=False, too_hot=False
    ):
    if (
        not door_is_open
        and start_is_pushed
        and timer_is_set
    ):
        return 'HEATING'
    return 'OFF'