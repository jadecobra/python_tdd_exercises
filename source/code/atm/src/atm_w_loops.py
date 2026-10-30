def withdraw(
        right_pin, enough_cash,
        above_daily_limit=False, card_expired=False,
    ):
    if card_expired:
        return 'DENIED: Card Expired'
    if above_daily_limit:
        return 'DENIED: Exceeded daily withdrawal limit'
    if not right_pin:
        return 'DENIED: Wrong PIN. Try again...'
    if not enough_cash:
        return 'DENIED: Not enough CASH in Account'
    return 'CASH'