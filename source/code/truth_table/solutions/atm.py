def withdraw(
        pin_is_correct, balance_is_enough,
        above_daily_limit=False, card_has_expired=False,
    ):
    denial = 'DENIED'

    if card_has_expired:
        return denial
    if not pin_is_correct:
        return denial
    if not balance_is_enough:
        return denial
    if above_daily_limit:
        return denial
    return 'CASH'