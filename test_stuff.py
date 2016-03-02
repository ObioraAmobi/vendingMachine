import unittest

import vending_machine

EURO_COINS = [1, 2, 5, 10, 20, 50, 100, 200]
USD_COINS = [1, 5, 10, 25, 50, 100]

class TestVendingMachine(unittest.TestCase):

    def test_return_no_change(self):
        coins = vending_machine.give_change([1], 0)
        self.assertEquals(coins, [])

    def test_return_one_cent(self):
        coins = vending_machine.give_change([1], 1)
        self.assertEquals(coins, [1])

    def test_return_enough_ones(self):
        coins = vending_machine.give_change([1], 3)
        self.assertEquals(coins, [1, 1, 1])

    def test_return_one_of_each_higher_denomination(self):
        coins = vending_machine.give_change([1, 2, 5, 10], 8)
        self.assertEquals(coins, [5, 2, 1])

    def test_return_more_than_one_of_denomination(self):
        coins = vending_machine.give_change([1, 2, 5, 10], 29)
        self.assertEquals(coins, [10, 10, 5, 2, 2])

    def test_return_right_denominations(self):
        coins = vending_machine.give_change([1, 2, 5, 10], 57)
        self.assertEquals(coins, [10, 10, 10, 10, 10, 5, 2])

    def test_cant_give_exact_change(self):
        coins = vending_machine.give_change([2, 5, 10], 16)
        self.assertEquals(coins, [10, 5, 2])

    def test_give_EURO_change(self):
        coins = vending_machine.give_change(EURO_COINS, 82)
        self.assertEquals(coins, [50, 20, 10, 2])

    def test_give_USD_change(self):
        coins = vending_machine.give_change(USD_COINS, 82)
        self.assertEquals(coins, [50, 25, 5, 1, 1])
