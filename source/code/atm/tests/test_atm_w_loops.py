import src.atm
import unittest


class TestATM(unittest.TestCase):

    def test_atm(self):
        booleans = (False, True)
        for right_pin in booleans:
            for enough_cash in booleans:
                for above_daily_limit in booleans:
                    for card_expired in booleans:
                        with self.subTest(
                            right_pin=right_pin,
                            enough_cash=enough_cash,
                            above_daily_limit=above_daily_limit,
                            card_expired=card_expired,
                        ):
                            result = src.atm.withdraw(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=card_expired,
                            )
                            if card_expired:
                                self.assertEqual(
                                    result,
                                    'DENIED: Card Expired'
                                )
                            elif above_daily_limit:
                                self.assertEqual(
                                    result,
                                    'DENIED: Exceeded daily withdrawal limit'
                                )
                            elif not right_pin:
                                self.assertEqual(
                                    result,
                                    'DENIED: Wrong PIN. Try again...'
                                )
                            elif not enough_cash:
                                self.assertEqual(
                                    result,
                                    'DENIED: '
                                    'Not enough CASH in Account'
                                )
                            else:
                                self.assertEqual(
                                    result,
                                    'CASH'
                                )


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError