def withdraw(
        pin_is_right, enough_balance,
        above_daily_limit=False, card_expired=False,
    ):
    denied = 'DENIED'

    if (
        not card_expired and pin_is_right
        and enough_balance and not above_daily_limit
    ):
        return 'CASH'
    return denied

    if card_expired:
        return denied
    if not pin_is_right:
        return denied
    if not enough_balance:
        return denied
    if above_daily_limit:
        return denied

    return 'CASH'
