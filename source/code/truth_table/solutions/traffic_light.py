def show(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):
    red, yellow, green = 'RED', 'YELLOW', 'GREEN'
    next_light = red
    walk = 'NO WALK'

    if timer_done:
        if current_light == green:
            next_light = yellow
            return yellow, walk
        if current_light == red:
            if walk_button:
                next_light = red
            else:
                next_light = green
    if not timer_done:
        next_light = current_light

    if next_light == red:
        walk = 'WALK'

    return next_light, walk
