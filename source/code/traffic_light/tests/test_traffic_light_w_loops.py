import src.traffic_light
import unittest


GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
WALK, NOT_WALK = 'WALK', 'DO NOT WALK'


class TestTrafficLight(unittest.TestCase):

    def test_traffic_light_control(self):
        for row in (
            ('cross', GREEN, RED, False, (GREEN, RED, WALK)),
            ('cross', GREEN, RED, True, (YELLOW, RED, NOT_WALK)),
            ('cross', YELLOW, RED, False, (YELLOW, RED, NOT_WALK)),
            ('cross', YELLOW, RED, True, (RED, RED, NOT_WALK)),
            ('cross', RED, RED, False, (RED, RED, NOT_WALK)),
            ('cross', RED, RED, True, (RED, GREEN, NOT_WALK)),
            ('parallel', RED, GREEN, False, (RED, GREEN, NOT_WALK)),
            ('parallel', RED, GREEN, True, (RED, YELLOW, NOT_WALK)),
            ('parallel', RED, YELLOW, False, (RED, YELLOW, NOT_WALK)),
            ('parallel', RED, YELLOW, True, (RED, RED, NOT_WALK)),
            ('parallel', RED, RED, False, (RED, RED, NOT_WALK)),
            ('parallel', RED, RED, True, (GREEN, RED, WALK)),
        ):
            red_phase = row[0]
            current_parallel = row[1]
            current_cross = row[2]
            timer_done = row[3]

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
                    row[4]
                )

    def test_traffic_light_failsafe(self):
        inputs = (GREEN, YELLOW, 'bad input')
        for red_phase in ('cross', 'parallel', 'bad input'):
            for current_parallel in inputs:
                for current_cross in inputs:
                    for timer_done in (False, True):
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