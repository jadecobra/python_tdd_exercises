import src.microwave
import unittest


OFF = 'OFF'


class TestMicrowave(unittest.TestCase):

    def test_too_hot_open_door_timer_set(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            ),
            OFF
        )

    def test_too_hot_open_door_timer_not_set(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            ),
            OFF
        )

    def test_too_hot_closed_door_timer_set(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            ),
            'HEATING'
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            ),
            OFF
        )

    def test_too_hot_closed_door_timer_not_set(self):
        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            ),
            OFF
        )

        self.assertEqual(
            src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            ),
            OFF
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError