def control(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):
    red, yellow, green = 'RED', 'YELLOW', 'GREEN'
    dont_walk = 'DONT WALK'

    if not timer_done and current_light != red:
        return current_light, dont_walk

    if timer_done:
        if current_light == green:
            return yellow, dont_walk
        if current_light == red:
            return green, dont_walk

    return red, 'WALK'