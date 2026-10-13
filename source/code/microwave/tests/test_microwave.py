import src.microwave
import unittest


class TestMicrowave(unittest.TestCase):

    def test_too_hot_w_set_timer_closed_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=True,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertTrue(
            src.microwave.microwave(
                closed_door=True,
                set_timer=True,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_set_timer_closed_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=True,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=True,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_set_timer_closed_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=False,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=False,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_set_timer_closed_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=False,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=True,
                set_timer=False,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_set_timer_open_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=True,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=True,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_set_timer_open_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=True,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=True,
                pressed_start=False,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_set_timer_open_door_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=False,
                pressed_start=True,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=False,
                pressed_start=True,
                too_hot=False,
            )
        )

    def test_too_hot_w_not_set_timer_open_door_not_pressed_start(self):
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=False,
                pressed_start=False,
                too_hot=True,
            )
        )
        self.assertFalse(
            src.microwave.microwave(
                closed_door=False,
                set_timer=False,
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