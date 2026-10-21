def microwave(
        closed_door=True, pressed_start=False,
        timer_set=False, too_hot=False,
    ):
    return (
        closed_door
        and timer_set
        and not too_hot
        and pressed_start
    )