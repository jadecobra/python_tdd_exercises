GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
WALK, NOT_WALK = 'WALK', 'DO NOT WALK'
FAILSAFE = RED, RED, NOT_WALK


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
            return YELLOW, RED, NOT_WALK
        if parallel == RED:
            return RED, GREEN, NOT_WALK
    if red_phase == 'parallel':
        if cross == GREEN:
            return RED, YELLOW, NOT_WALK
        if cross == RED:
            return GREEN, RED, WALK
    return FAILSAFE


def control(
        timer_done, red_phase='parallel',
        current_parallel=RED, current_cross=RED,
    ):
    if triggers_failsafe(current_parallel, current_cross):
        return FAILSAFE

    if not timer_done:
        if red_phase == 'cross' and current_parallel == GREEN:
            return current_parallel, current_cross, WALK
        return current_parallel, current_cross, NOT_WALK

    if timer_done:
        return next_light(
            red_phase, current_parallel, current_cross
        )

    return FAILSAFE