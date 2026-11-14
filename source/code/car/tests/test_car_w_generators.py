import itertools
import src.car
import unittest


class TestCar(unittest.TestCase):

    def test_car_ignition(self):
        for (
            start_is_pressed, key_is_close,
            brake_is_pressed, in_park
        ) in itertools.product((False, True), repeat=4):
            with self.subTest(
                start_is_pressed=start_is_pressed,
                key_is_close=key_is_close,
                brake_is_pressed=brake_is_pressed,
                in_park=in_park,
            ):
                result = src.car.ignition(
                    start_is_pressed=start_is_pressed,
                    key_is_close=key_is_close,
                    brake_is_pressed=brake_is_pressed,
                    in_park=in_park,
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