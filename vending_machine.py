
def give_change(denominations, amount):
    denominations = sorted(denominations, reverse=True)
    change = []

    ones = [1] * amount

    for coin in denominations:
        while len(ones) >= coin:
            change.append(coin)
            ones = ones[coin:]

    return change
