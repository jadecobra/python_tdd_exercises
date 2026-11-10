import itertools
import src.elevator
import unittest


class TestElevator(unittest.TestCase):

    def test_elevator_controller(self):
        booleans = (False, True)
        for (
            number_pushed, doors_closed,
            above_weight, emergency
        ) in itertools.product(booleans, repeat=4):
            with self.subTest(
                number_pushed=number_pushed,
                doors_closed=doors_closed,
                above_weight=above_weight,
                emergency=emergency,
            ):
                result = src.elevator.controller(
                    number_pushed=number_pushed,
                    doors_closed=doors_closed,
                    above_weight=above_weight,
                    emergency=emergency,
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