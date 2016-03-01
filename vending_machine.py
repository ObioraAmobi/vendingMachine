
def give_change(denominations, amount):
    l = [1,2,3]
    denominations = sorted(denominations, reverse=True)
    change = []

    ones = [1] * amount

    for coin in denominations:
        while len(ones) >= coin:
            change.append(coin)
            ones = ones[coin:]

    return change
