import src.elevator
import unittest


NOT_MOVE = 'NOT MOVE'


class TestElevator(unittest.TestCase):

    def test_doors_clear_number_pushed_w_emergency(self):
        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=True,
                above_weight_limit=True,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=True,
                above_weight_limit=True,
                emergency=False,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=True,
                above_weight_limit=False,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=True,
                above_weight_limit=False,
                emergency=False,
            ),
            'MOVE'
        )

    def test_doors_clear_number_not_pushed_w_emergency(self):
        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=False,
                above_weight_limit=True,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=False,
                above_weight_limit=True,
                emergency=False,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=False,
                above_weight_limit=False,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=True,
                number_pushed=False,
                above_weight_limit=False,
                emergency=False,
            ),
            NOT_MOVE
        )

    def test_doors_not_clear_number_pushed_w_emergency(self):
        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=True,
                above_weight_limit=True,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=True,
                above_weight_limit=True,
                emergency=False,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=True,
                above_weight_limit=False,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=True,
                above_weight_limit=False,
                emergency=False,
            ),
            NOT_MOVE
        )

    def test_doors_not_clear_number_not_pushed_w_emergency(self):
        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=False,
                above_weight_limit=True,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=False,
                above_weight_limit=True,
                emergency=False,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                number_pushed=False,
                above_weight_limit=False,
                emergency=True,
            ),
            NOT_MOVE
        )

        self.assertEqual(
            src.elevator.elevator(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=False,
                emergency=False,
            ),
            NOT_MOVE
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError