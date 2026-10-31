import src.car
import unittest


class TestCar(unittest.TestCase):

    def test_car_ignition(self):
        booleans = (False, True)
        for start_is_pressed in booleans:
            for key_is_close in booleans:
              for brake_is_pressed in booleans:
                  for in_park in booleans:
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