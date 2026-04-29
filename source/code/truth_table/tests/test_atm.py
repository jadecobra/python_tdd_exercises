import src.atm
import unittest


DENIED = 'DENIED'


class TestATM(unittest.TestCase):

    def test_withdraw_w_not_expired_card_w_right_pin(self):
        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            ),
            'CASH'
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            ),
            DENIED
        )

    def test_withdraw_w_expired_card_w_right_pin(self):
        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            ),
            DENIED
        )

    def test_withdraw_w_expired_card_w_wrong_pin(self):
        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            ),
            DENIED
        )

    def test_withdraw_w_not_expired_card_w_wrong_pin(self):
        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            ),
            DENIED
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError