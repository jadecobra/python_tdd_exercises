def microwave(
        closed_door=False, pressed_start=False,
        set_timer=False, too_hot=False,
    ):
    return (
        closed_door
        and set_timer
        and not too_hot
        and pressed_start
    )