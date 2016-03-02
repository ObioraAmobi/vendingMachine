
def give_change(denominations, amount):
    denominations = sorted(denominations, reverse=True)
    change = []

    for coin in denominations:
        while coin <= amount:
            change.append(coin)
            amount -= coin

    if amount > 0:
        change.append(min(denominations))

    return change