import src.atm
import unittest


class TestATM(unittest.TestCase):

    def test_withdraw_w_not_expired_card_when_pin_is_right(self):
        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            ),
            'CASH'
        )

        my_expectation = 'DENIED'

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            ),
            my_expectation
        )

    def test_withdraw_w_expired_card_w_right_pin(self):
        my_expectation = 'DENIED'

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            ),
            my_expectation
        )

    def test_withdraw_w_expired_card_w_wrong_pin(self):
        my_expectation = 'DENIED'

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            ),
            my_expectation
        )

    def test_withdraw_w_not_expired_card_when_pin_is_wrong(self):
        my_expectation = 'DENIED'

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            ),
            my_expectation
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            ),
            my_expectation
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError