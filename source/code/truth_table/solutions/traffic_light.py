def show(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):
    red, yellow, green = 'RED', 'YELLOW', 'GREEN'
    walk = (red, 'WALK')
    no_walk = 'NO WALK'

    if not timer_done and current_light != red:
        return current_light, no_walk

    if timer_done:
        if current_light == green:
            return yellow, no_walk
        if current_light == red and not walk_button:
            return green, no_walk

    return walk