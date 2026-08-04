import src.traffic_light
import unittest


RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
DONT_WALK = 'DONT WALK'
WALK = (RED, 'WALK')
YELLOW_DONT_WALK = (YELLOW, DONT_WALK)
GREEN_DONT_WALK = (GREEN, DONT_WALK)


class TestTrafficLight(unittest.TestCase):

    def test_red_light_timer_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=RED,
                timer_done=True,
                walk_button=True,
            ),
            GREEN_DONT_WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=RED,
                timer_done=True,
                walk_button=False,
            ),
            GREEN_DONT_WALK
        )

    def test_red_light_timer_not_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=RED,
                timer_done=False,
                walk_button=True,
            ),
            WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=RED,
                timer_done=False,
                walk_button=False,
            ),
            WALK
        )

    def test_yellow_light_timer_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            ),
            WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            ),
            WALK
        )

    def test_yellow_light_timer_not_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            ),
            YELLOW_DONT_WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            ),
            YELLOW_DONT_WALK
        )

    def test_green_light_timer_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            ),
            YELLOW_DONT_WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            ),
            YELLOW_DONT_WALK
        )

    def test_green_light_timer_not_done_w_walk(self):
        self.assertEqual(
            src.traffic_light.control(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            ),
            GREEN_DONT_WALK
        )
        self.assertEqual(
            src.traffic_light.control(
                current_light=GREEN,
                timer_done=False,
                walk_button=False,
            ),
            GREEN_DONT_WALK
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError