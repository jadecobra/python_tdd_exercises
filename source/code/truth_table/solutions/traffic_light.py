def show(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):
    red, yellow, green = 'RED', 'YELLOW', 'GREEN'
    walk, no_walk = 'WALK', 'NO WALK'

    if not timer_done:
        return current_light, (
            no_walk if current_light != red
            else walk
        )

    if current_light == green:
        return yellow, no_walk

    if current_light == red:
        return (
            (green, no_walk) if not walk_button
            else (red, walk)
        )

    return red, walk
