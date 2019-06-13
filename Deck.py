from Card import Card
import random

class Deck:
    '''This is a class used for modelling a deck of blackjack cards'''
    def __init__(self):
        self.cards = self.make_deck()

    # creates a list of cards with the given suit
    # only used in make_deck()
    def make_suit(self, cards, suit):
        cards = [Card(suit, i) for i in range(13)]
       
        for card in cards:
            if card.rank == 0:
                card.rank = 'Ace'
            elif card.rank == 10:
                card.rank = 'Jack'
            elif card.rank == 11:
                card.rank = 'Queen'
            elif card.rank == 12:
                card.rank = 'King'
            else:
                card.rank += 1
            
        return cards

    # create a full deck with all suits
    def make_deck(self):
        cards = []

        cards = cards + self.make_suit([], 'Hearts')
        cards = cards + self.make_suit([], 'Clubs')
        cards = cards + self.make_suit([], 'Spades')
        cards = cards + self.make_suit([], 'Diamonds')

        random.shuffle(cards)

        return cards