def microwave(
        closed_door=False, pressed_start=False,
        timer_is_set=False, too_hot=False,
    ):
    return (
        closed_door
        and timer_is_set
        and not too_hot
        and pressed_start
    )