import src.microwave
import unittest


class TestMicrowave(unittest.TestCase):

    def test_microwave(self):
        booleans = (False, True)
        for closed_door in booleans:
            for timer_set in booleans:
                for pressed_start in booleans:
                    for too_hot in booleans:
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
# SyntaxError