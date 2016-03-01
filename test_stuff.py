import unittest
import vending_machine

class TestVendingMachine(unittest.TestCase):

    def test_return_no_change(self):
        coins = vending_machine.give_change([], 0)
        self.assertEquals(coins, [])

    def test_return_one_coin(self):
        coins = vending_machine.give_change([1], 1)
        self.assertEquals(coins, [1])

    def test_return_enough_ones(self):
        coins = vending_machine.give_change([1], 3)
        self.assertEquals(coins, [1, 1, 1])

    def test_return_right_denominations(self):
        coins = vending_machine.give_change([1, 2, 5, 10], 57)
        self.assertEquals(coins, [10, 10, 10, 10, 10, 5, 2])
