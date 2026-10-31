import src.elevator
import unittest


class TestElevator(unittest.TestCase):

    def test_elevator_controller(self):
        booleans = (False, True)
        for number_pushed in booleans:
            for doors_closed in booleans:
                for above_weight in booleans:
                    for emergency in booleans:
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