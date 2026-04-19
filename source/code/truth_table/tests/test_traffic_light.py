import src.traffic_light
import unittest


RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
NO_WALK = 'NO WALK'
WALK = (RED, 'WALK')
YELLOW_NO_WALK = (YELLOW, NO_WALK)
GREEN_NO_WALK = (GREEN, NO_WALK)


class TestTrafficLight(unittest.TestCase):

    def test_traffic_light_when_red_w_walk_button(self):
        self.assertEqual(
            src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            ),
            WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                timer_done=True,
                walk_button=False,
            ),
            GREEN_NO_WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            ),
            WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            ),
            WALK
        )

    def test_traffic_light_when_yellow_w_walk_button(self):
        self.assertEqual(
            src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            ),
            WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            ),
            WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            ),
            YELLOW_NO_WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            ),
            YELLOW_NO_WALK
        )

    def test_traffic_light_when_green_w_walk_button(self):
        self.assertEqual(
            src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            ),
            YELLOW_NO_WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            ),
            YELLOW_NO_WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            ),
            GREEN_NO_WALK
        )

        self.assertEqual(
            src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=False,
            ),
            GREEN_NO_WALK
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError