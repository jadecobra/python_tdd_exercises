def withdraw(
        right_pin, enough_money,
        above_daily_limit=False, card_expired=False,
    ):
    denied = 'DENIED'

    if card_expired:
        return denied

    if above_daily_limit:
        return denied

    if not right_pin:
        return denied

    if not enough_money:
        return denied

    return 'CASH'