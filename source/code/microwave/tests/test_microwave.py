import src.microwave
import unittest


class TestMicrowave(unittest.TestCase):

    def test_too_hot_w_timer_set_closed_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=True,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertTrue(
            src.microwave.microwave(
                closed_door=True,
                timer_set=True,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_timer_set_closed_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=True,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=True,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_timer_set_closed_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=False,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=False,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_timer_set_closed_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=False,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                timer_set=False,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_timer_set_open_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=True,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=True,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_timer_set_open_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=True,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=True,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_timer_set_open_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=False,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=False,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_timer_set_open_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=False,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                timer_set=False,
                pressed_start=False,
                too_hot=False,
            )
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError