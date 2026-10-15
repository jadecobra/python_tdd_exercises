import src.traffic_light
import unittest


GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'


class TestTrafficLight(unittest.TestCase):

    def test_parallel_green_cross_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=GREEN,
                current_cross=RED,
                timer_done=False,
            ),
            (GREEN, RED)
        )

    def test_parallel_green_cross_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=GREEN,
                current_cross=RED,
                timer_done=True,
            ),
            (YELLOW, RED)
        )

    def test_parallel_yellow_cross_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=YELLOW,
                current_cross=RED,
                timer_done=False,
            ),
            (YELLOW, RED)
        )

    def test_parallel_yellow_cross_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=YELLOW,
                current_cross=RED,
                timer_done=True,
            ),
            (RED, RED)
        )

    def test_parallel_red_cross_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=RED,
                current_cross=RED,
                timer_done=False,
            ),
            (RED, RED)
        )

    def test_parallel_red_cross_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='cross',
                current_parallel=RED,
                current_cross=RED,
                timer_done=True,
            ),
            (RED, GREEN)
        )

    def test_cross_green_parallel_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=GREEN,
                timer_done=False,
            ),
            (RED, GREEN)
        )

    def test_cross_green_parallel_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=GREEN,
                timer_done=True,
            ),
            (RED, YELLOW)
        )

    def test_cross_yellow_parallel_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=YELLOW,
                timer_done=False,
            ),
            (RED, YELLOW)
        )

    def test_cross_yellow_parallel_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=YELLOW,
                timer_done=True,
            ),
            (RED, RED)
        )

    def test_cross_red_parallel_red_timer_not_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=RED,
                timer_done=False,
            ),
            (RED, RED)
        )

    def test_cross_red_parallel_red_timer_done(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='parallel',
                current_parallel=RED,
                current_cross=RED,
                timer_done=True,
            ),
            (GREEN, RED)
        )

    def test_failsafe(self):
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel='BAP',
                current_cross=RED,
                timer_done=False,
            ),
            (RED, RED)
        )
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel=RED,
                current_cross='POW',
                timer_done=False,
            ),
            (RED, RED)
        )
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel=GREEN,
                current_cross=GREEN,
                timer_done=False,
            ),
            (RED, RED)
        )
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel=GREEN,
                current_cross=YELLOW,
                timer_done=False,
            ),
            (RED, RED)
        )
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel=YELLOW,
                current_cross=GREEN,
                timer_done=False,
            ),
            (RED, RED)
        )
        self.assertEqual(
            src.traffic_light.control(
                red_phase='BOOM',
                current_parallel=YELLOW,
                current_cross=YELLOW,
                timer_done=False,
            ),
            (RED, RED)
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError