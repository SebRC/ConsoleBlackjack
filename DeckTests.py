# test module for Deck class

import unittest
from Deck import Deck

class DeckTests(unittest.TestCase):
    '''This is a test class for testing the methods of the Deck class'''
    deck = Deck()

    deck.cards = []

    def test_make_suit(self):
        self.assertEquals(self.deck.make_suit([], 'Hearts')[0].suit, 'Hearts', 'Should be Hearts')
        self.assertEquals(self.deck.make_suit([], 'Spades')[0].suit, 'Spades', 'Should be Spades')
        self.assertEquals(self.deck.make_suit([], 'Clubs')[0].suit, 'Clubs', 'Should be Clubs')
        self.assertEquals(self.deck.make_suit([], 'Diamonds')[0].suit, 'Diamonds', 'Should be Diamonds')
             