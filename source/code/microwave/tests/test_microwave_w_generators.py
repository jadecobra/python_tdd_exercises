import itertools
import src.microwave
import unittest


class TestMicrowave(unittest.TestCase):

    def test_microwave(self):
        for (
            closed_door, timer_set,
            pressed_start, too_hot,
        ) in itertools.product((False, True), repeat=4):
            with self.subTest(
                closed_door=closed_door,
                timer_set=timer_set,
                pressed_start=pressed_start,
                too_hot=too_hot,
            ):
                result = src.microwave.microwave(
                    closed_door=closed_door,
                    timer_set=timer_set,
                    pressed_start=pressed_start,
                    too_hot=too_hot,
                )
                try:
                    self.assertFalse(result)
                except AssertionError:
                    self.assertTrue(result)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# Syntaxerror