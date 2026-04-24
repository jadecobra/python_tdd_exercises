import src.microwave
import unittest


OFF = 'OFF'


class TestMicrowave(unittest.TestCase):

    def test_door_open_timer_set_w_overheating(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False,
            ),
            OFF
        )

    def test_door_open_timer_not_set_w_overheating(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            ),
            OFF
        )

    def test_door_closed_timer_set_w_overheating(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            ),
            'HEATING'
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False
            ),
            OFF
        )

    def test_door_closed_timer_not_set_w_overheating(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            ),
            OFF
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError