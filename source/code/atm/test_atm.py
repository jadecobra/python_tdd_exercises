import src.atm
import unittest


DENIED = 'DENIED'


class TestATM(unittest.TestCase):

    def test_right_pin_enough_cash_w_card(self):
        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=True,
                above_daily_limit=True,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=True,
                above_daily_limit=True,
                card_expired=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=True,
                above_daily_limit=False,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=True,
                above_daily_limit=False,
                card_expired=False,
            ),
            'CASH'
        )

    def test_right_pin_not_enough_cash_w_card(self):
        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=True,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=True,
                card_expired=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=False,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=False,
                card_expired=True,
            ),
            DENIED
        )

    def test_wrong_pin_enough_cash_w_card(self):
        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=True,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=True,
                card_expired=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=False,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=False,
                card_expired=False,
            ),
            DENIED
        )

    def test_wrong_pin_not_enough_cash_w_card(self):
        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=True,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=True,
                card_expired=False,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=False,
                card_expired=True,
            ),
            DENIED
        )

        self.assertEqual(
            src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=False,
                card_expired=False,
            ),
            DENIED
        )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError