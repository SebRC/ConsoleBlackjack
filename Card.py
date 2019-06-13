
class Card:
    '''This is a class used for modelling a card in the game of blackjack'''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit} {self.rank}'
