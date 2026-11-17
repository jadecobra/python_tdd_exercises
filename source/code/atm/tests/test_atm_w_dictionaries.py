import itertools
import src.atm
import unittest


class TestATM(unittest.TestCase):

    def test_atm(self):
        denials = {
            'card_expired': 'DENIED: Card Expired',
            'above_daily_limit': 'DENIED: Exceeded daily withdrawal limit',
            'not_right_pin': 'DENIED: Wrong PIN. Try again...',
            'not_enough_cash': 'DENIED: Not enough CASH in Account',
        }

        for (
            right_pin, enough_cash,
            above_daily_limit, card_expired
        ) in itertools.product((False, True), repeat=4):
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
                          result, denials['card_expired']
                      )
                  elif above_daily_limit:
                      self.assertEqual(
                          result, denials['above_daily_limit']
                      )
                  elif not right_pin:
                      self.assertEqual(
                          result, denials['not_right_pin']
                      )
                  elif not enough_cash:
                      self.assertEqual(
                          result, denials['not_enough_cash']
                      )
                  else:
                      self.assertEqual(result, 'CASH')


# Exceptions seen
# AssertionError
# NameError
# AttributeError
# TypeError
# SyntaxError