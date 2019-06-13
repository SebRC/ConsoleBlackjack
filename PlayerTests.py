# test module for Player class

import unittest
from Player import Player
from Card import Card

class PlayerTests(unittest.TestCase):
    '''This is a test class for testing the Player class methods'''
    
    ace_card = Card('Heart', 'Ace')
    jack_card = Card('Heart', 'Jack')

    player = Player(1000, [Card('Heart', 10),Card('Heart', 5)])
    split_player = Player(1000, [[Card('Heart', 10),Card('Heart', 5)], [Card('Heart', 4),Card('Heart', 7)]])

    def test_calc_total_rank(self):
        self.assertEqual(self.player.calculate_total_rank(), 15, 'Should be 15')

    def test_calc_split_rank(self):
        self.assertEquals(self.split_player.calculate_split_rank(0), 15, 'Should be 15')
        self.assertEquals(self.split_player.calculate_split_rank(1), 11, 'Should be 11')

    def test_check_rank_aces(self):
        self.assertEquals(self.player.check_rank(self.ace_card), 1, 'Should be 1')

    def test_check_rank_face_cards(self):
        self.assertEquals(self.player.check_rank(self.jack_card), 10, 'Should be 10')

    def test_init(self):
        self.assertRaises(ValueError, Player(-1, []))
        self.assertRaises(TypeError, Player('Seb', []))
        self.assertRaises(TypeError, Player(1000, 1))