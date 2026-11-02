import src.traffic_light
import unittest


GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'


class TestTrafficLight(unittest.TestCase):

    def test_traffic_light_control(self):
        for row in (
            ('cross', GREEN, RED, False, (GREEN, RED)),
            ('cross', GREEN, RED, True, (YELLOW, RED)),
            ('cross', YELLOW, RED, False, (YELLOW, RED)),
            ('cross', YELLOW, RED, True, (RED, RED)),
            ('cross', RED, RED, False, (RED, RED)),
            ('cross', RED, RED, True, (RED, GREEN)),
            ('parallel', RED, GREEN, False, (RED, GREEN)),
            ('parallel', RED, GREEN, True, (RED, YELLOW)),
            ('parallel', RED, YELLOW, False, (RED, YELLOW)),
            ('parallel', RED, YELLOW, True, (RED, RED)),
            ('parallel', RED, RED, False, (RED, RED)),
            ('parallel', RED, RED, True, (GREEN, RED)),
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
        colors = (GREEN, YELLOW, 'BOOM', 'BAP', 'POW')
        for red_phase in ('cross', 'parallel', 'BOOM', 'BAP'):
            for current_parallel in colors:
                for current_cross in colors:
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
                                (RED, RED)
                            )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError