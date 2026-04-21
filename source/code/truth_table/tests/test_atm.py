import src.atm
import unittest


class TestATM(unittest.TestCase):

    def test_atm_withdrawal(self):
        my_expectation = 'CASH'
        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        my_expectation = 'DENIED'

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=False
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_has_expired=False,
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=False,
            ),
            my_expectation
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError