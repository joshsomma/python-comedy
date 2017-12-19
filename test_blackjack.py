# import libs
import unittest

from blackjack import TheDeck
"""
Test cases
"""
class BlackJackTestCases(unittest.TestCase):
    def setUp(self):
        self.d = TheDeck()

    def test_TheDeck(self):
        self.assertTrue(len(self.d.deck) == 52)

    def test_shuffle(self):
        self.shuffle = self.d.shuffleDeck()
        self.assertFalse(self.d.deck == self.shuffle)
