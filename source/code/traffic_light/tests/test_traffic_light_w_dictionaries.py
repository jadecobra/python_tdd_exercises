import itertools
import src.traffic_light
import unittest


GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
WALK, NOT_WALK = 'WALK', 'DO NOT WALK'


class TestTrafficLight(unittest.TestCase):

    def test_traffic_light_control(self):
        states = {
            'cross': (
                (GREEN, RED, False, (GREEN, RED, WALK)),
                (GREEN, RED, True, (YELLOW, RED, NOT_WALK)),
                (YELLOW, RED, False, (YELLOW, RED, NOT_WALK)),
                (YELLOW, RED, True, (RED, RED, NOT_WALK)),
                (RED, RED, False, (RED, RED, NOT_WALK)),
                (RED, RED, True, (RED, GREEN, NOT_WALK)),
            ),
            'parallel': (
                (RED, GREEN, False, (RED, GREEN, NOT_WALK)),
                (RED, GREEN, True, (RED, YELLOW, NOT_WALK)),
                (RED, YELLOW, False, (RED, YELLOW, NOT_WALK)),
                (RED, YELLOW, True, (RED, RED, NOT_WALK)),
                (RED, RED, False, (RED, RED, NOT_WALK)),
                (RED, RED, True, (GREEN, RED, WALK)),
            )
        }
        for red_phase in states:
            for (
                current_parallel,
                current_cross, timer_done, result
            ) in states[red_phase]:
                with self.subTest(
                    red_phase=red_phase,
                    current_parallel=current_parallel,
                    current_cross=current_cross,
                    timer_done=timer_done,
                ):
                    self.assertEqual(
                        src.traffic_light.control(
                            red_phase=red_phase,
                            current_parallel=current_parallel,
                            current_cross=current_cross,
                            timer_done=timer_done,
                        ),
                        result
                    )

    def test_traffic_light_failsafe(self):
        inputs = (GREEN, YELLOW, 'bad input')
        for (
            red_phase, current_parallel,
            current_cross, timer_done
        ) in itertools.product(
            ('cross', 'parallel', 'bad input'),
            inputs, inputs, (False, True)
        ):
            with self.subTest(
                red_phase=red_phase,
                current_parallel=current_parallel,
                current_cross=current_cross,
                timer_done=timer_done,
            ):
                self.assertEqual(
                    src.traffic_light.control(
                        red_phase=red_phase,
                        current_parallel=current_parallel,
                        current_cross=current_cross,
                        timer_done=timer_done,
                    ),
                    (RED, RED, NOT_WALK)
                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError