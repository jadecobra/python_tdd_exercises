def withdraw(
        pin_is_right, enough_balance,
        above_daily_limit=False, card_expired=False,
    ):
    denial = 'DENIED'

    if card_expired:
        return denial
    if not pin_is_right:
        return denial
    if not enough_balance:
        return denial
    if above_daily_limit:
        return denial

    return 'CASH'