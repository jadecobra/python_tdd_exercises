def ignition(
        start_is_pressed, key_is_close=False,
        brake_is_pressed=False, in_park=False,
    ):
    if (
        start_is_pressed
        and key_is_close
        and brake_is_pressed
    ):
        return in_park
    return False