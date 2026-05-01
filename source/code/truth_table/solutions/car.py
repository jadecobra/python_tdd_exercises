def starter(
        key_is_close, start_is_pushed,
        brake_is_pressed=False, in_park=False,
    ):
    if not (
        key_is_close
        and start_is_pushed
        and brake_is_pressed
        and in_park
    ):
        return 'OFF'

    return 'ON'