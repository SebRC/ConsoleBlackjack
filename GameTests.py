
import unittest
import DealerGame
import PlayerGame

from Player import Player
from Dealer import Dealer
import Game
from Card import Card
from Deck import Deck

class GameTests(unittest.TestCase):
    '''This is a test class for testing the functions of the game module'''

    player_above_21 = Player(100, [Card('Hearts', 4), Card('Clubs', 10), Card('Spades', 10)])
    player_blackjack = Player(100, [Card('Hearts', 10),Card('Clubs', 1), Card('Clubs', 10)])
    player_below_21 = Player(100, [Card('Hearts', 4),Card('Clubs', 5)])
    player_split = Player(100, [Card('Hearts', 10),Card('Clubs', 10)])
    
    dealer_above_21 = Dealer(100, [Card('Hearts', 4), Card('Clubs', 10), Card('Spades', 10)])
    dealer_blackjack = Dealer(100, [Card('Hearts', 10),Card('Clubs', 1), Card('Clubs', 10)])
    dealer_below_21 = Dealer(100, [Card('Hearts', 4),Card('Clubs', 5)])
    dealer_17 = Dealer(100, [Card('Hearts', 7),Card('Diamonds', 10)])

    deck = Deck()

    def test_hit(self):
        #self.assertFalse(Game.evaluate_hit_win_condition(self.player_above_21), 'Should be False')
        #self.assertFalse(Game.evaluate_hit_win_condition(self.player_blackjack), 'Should be False')
        #self.assertTrue(Game.evaluate_hit_win_condition(self.player_below_21), 'Should be True')
        pass

    def test_split(self):
        self.assertFalse(DealerGame.ai_choices(self.player_split, self.dealer_17, self.deck.cards))

    def test_stand(self):
        self.assertFalse(Game.evaluate_stand_win_condition(self.player_above_21, self.dealer_below_21), 'Should be False')
