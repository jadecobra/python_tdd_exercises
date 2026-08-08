RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'


def is_not_safe(parallel, cross):
    return (
        (parallel == cross != RED)
        or (parallel == GREEN and cross == YELLOW)
        or (parallel == YELLOW and cross == GREEN)
    )


def is_not_light(light):
    return not (
        light == GREEN or light == YELLOW or light == RED
    )


def triggers_failsafe(parallel, cross):
    return (
        is_not_light(parallel) or is_not_light(cross)
        or is_not_safe(parallel, cross)
    )


def next_light(red_phase, parallel, cross):
    if red_phase == 'cross':
        if parallel == GREEN:
            return YELLOW, RED
        if parallel == RED:
            return RED, GREEN
    if red_phase == 'parallel':
        if cross == GREEN:
            return RED, YELLOW
        if cross == RED:
            return GREEN, RED
    return RED, RED


def control(
        timer_done, red_phase='parallel',
        current_parallel=RED, current_cross=RED,
    ):
    if triggers_failsafe(current_parallel, current_cross):
        return RED, RED

    if not timer_done:
        return current_parallel, current_cross

    if timer_done:
        return next_light(
            red_phase, current_parallel, current_cross
        )

    return RED, RED