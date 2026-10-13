import src.elevator
import unittest


class TestElevator(unittest.TestCase):

    def test_emergency_w_above_weight_doors_closed_number_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=True,
                above_weight=True,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=True,
                above_weight=True,
                emergency=False,
            )
        )

    def test_emergency_w_below_weight_doors_closed_number_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=True,
                above_weight=False,
                emergency=True,
            )
        )
        self.assertTrue(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=True,
                above_weight=False,
                emergency=False,
            )
        )

    def test_emergency_w_above_weight_doors_open_number_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=False,
                above_weight=True,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=False,
                above_weight=True,
                emergency=False,
            )
        )

    def test_emergency_w_below_weight_doors_open_number_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=False,
                above_weight=False,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=True,
                doors_closed=False,
                above_weight=False,
                emergency=False,
            )
        )

    def test_emergency_w_above_weight_doors_closed_number_not_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=True,
                above_weight=True,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=True,
                above_weight=True,
                emergency=False,
            )
        )

    def test_emergency_w_below_weight_doors_closed_number_not_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=True,
                above_weight=False,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=True,
                above_weight=False,
                emergency=False,
            )
        )

    def test_emergency_w_above_weight_doors_open_number_not_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=False,
                above_weight=True,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=False,
                above_weight=True,
                emergency=False,
            )
        )

    def test_emergency_w_below_weight_doors_open_number_not_pushed(self):
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=False,
                above_weight=False,
                emergency=True,
            )
        )
        self.assertFalse(
            src.elevator.controller(
                number_pushed=False,
                doors_closed=False,
                above_weight=False,
                emergency=False,
            )
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError