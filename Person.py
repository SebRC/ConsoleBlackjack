class Person:

    '''This is the superclass of player and dealer. It is used to pass down methods and attributes both classes share'''
    def __init__(self, wallet, hand: list):
        if type(wallet) not in [int, float]:
            raise TypeError('Error. Wallet must be a number')
        elif wallet < 0:
            raise ValueError('Error. Wallet cannot be a negative number')
            
        if type(hand) not in [list]:
            raise TypeError('Error. Hand must be a list')
        
        self.wallet = wallet
        self.hand = hand 


    # calculates the current total on a persons hand
    def calculate_total_rank(self):
        sum_of_rank = 0
        for card in self.hand:
            sum_of_rank += self.check_rank(card)

        return sum_of_rank

    # converts a cards rank to a number
    def check_rank(self, card):
        if card.rank == 'Ace':
            return 1
        elif card.rank == 'Jack':
            return 10
        elif card.rank == 'Queen':
            return 10
        elif card.rank == 'King':
            return 10
        return card.rank