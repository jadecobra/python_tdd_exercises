import src.car
import unittest


OFF = 'OFF'


class TestCar(unittest.TestCase):

    def test_key_close_brake_pressed_w_gear(self):
        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pushed=True,
                in_park=True,
            ),
            'ON'
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pushed=True,
                in_park=False,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pushed=False,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pushed=False,
                in_park=False,
            ),
            OFF
        )

    def test_key_close_brake_not_pressed_w_gear(self):
        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pushed=True,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pushed=True,
                in_park=False,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pushed=False,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pushed=False,
                in_park=False,
            ),
            OFF
        )

    def test_key_far_brake_pressed_w_gear(self):
        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pushed=True,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pushed=True,
                in_park=False,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pushed=False,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pushed=False,
                in_park=False,
            ),
            OFF
        )

    def test_key_far_brake_not_pressed_w_gear(self):
        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pushed=True,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pushed=True,
                in_park=False,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pushed=False,
                in_park=True,
            ),
            OFF
        )

        self.assertEqual(
            src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pushed=False,
                in_park=False,
            ),
            OFF
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError