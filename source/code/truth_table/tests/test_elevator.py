import src.elevator
import unittest


NOT_MOVE = 'NOT MOVE'


class TestElevator(unittest.TestCase):

    def test_weight_w_doors_clear_number_pushed(self):
        my_expectation = 'MOVE'
        reality = src.elevator.elevator(
            doors_clear=True,
            above_weight_limit=False,
            number_pushed=True,
        )
        self.assertEqual(reality, my_expectation)

        reality = src.elevator.elevator(
            doors_clear=True,
            above_weight_limit=True,
            number_pushed=False,
        )
        self.assertEqual(reality, NOT_MOVE)

    def test_weight_w_doors_clear_number_not_pushed(self):
        reality = src.elevator.elevator(
            doors_clear=True,
            above_weight_limit=True,
            number_pushed=False,
        )
        self.assertEqual(reality, NOT_MOVE)

        reality = src.elevator.elevator(
            doors_clear=True,
            above_weight_limit=False,
            number_pushed=False,
        )
        self.assertEqual(reality, NOT_MOVE)

    def test_weight_w_doors_not_clear_number_pushed(self):
        reality = src.elevator.elevator(
            doors_clear=False,
            above_weight_limit=True,
            number_pushed=True,
        )
        self.assertEqual(reality, NOT_MOVE)

    def test_weight_w_doors_not_clear_number_not_pushed(self):
        reality = src.elevator.elevator(
            doors_clear=False,
            above_weight_limit=True,
            number_pushed=False,
        )
        self.assertEqual(reality, NOT_MOVE)

        reality = src.elevator.elevator(
            doors_clear=False,
            above_weight_limit=False,
            number_pushed=False,
        )
        self.assertEqual(reality, NOT_MOVE)


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError