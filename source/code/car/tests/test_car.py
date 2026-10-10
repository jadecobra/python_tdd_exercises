import src.car
import unittest


class TestCar(unittest.TestCase):

    def test_park_w_brake_pressed_key_close_start_pressed(self):
        self.assertTrue(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=True,
                brake_is_pressed=True,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=True,
                brake_is_pressed=True,
                in_park=False,
            )
        )

    def test_park_w_brake_not_pressed_key_close_start_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=True,
                brake_is_pressed=False,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=True,
                brake_is_pressed=False,
                in_park=False,
            )
        )

    def test_park_w_brake_pressed_key_not_close_start_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=False,
                brake_is_pressed=True,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=False,
                brake_is_pressed=True,
                in_park=False,
            )
        )

    def test_park_w_brake_not_pressed_key_not_close_start_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=False,
                brake_is_pressed=False,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=True,
                key_is_close=False,
                brake_is_pressed=False,
                in_park=False,
            )
        )

    def test_park_w_brake_pressed_key_close_start_not_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
                brake_is_pressed=True,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
                brake_is_pressed=True,
                in_park=False,
            )
        )

    def test_park_w_brake_not_pressed_key_close_start_not_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
                brake_is_pressed=False,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
                brake_is_pressed=False,
                in_park=False,
            )
        )

    def test_park_w_brake_pressed_key_not_close_start_not_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=False,
                brake_is_pressed=True,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=False,
                brake_is_pressed=True,
                in_park=False,
            )
        )

    def test_brake_not_pressed_key_not_close_start_not_pressed(self):
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=False,
                brake_is_pressed=False,
                in_park=True,
            )
        )
        self.assertFalse(
            src.car.ignition(
                start_is_pressed=False,
                key_is_close=False,
                brake_is_pressed=False,
                in_park=False,
            )
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError