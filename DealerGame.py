import Game
import random

def start_dealer_game(player, dealer, deck):
    '''This is the module used for playing the game as a dealer'''
    #player places a random bet
    player.bet = 1#random.randrange(1, player.wallet, 1)
    print("\nPlayer bets " + str(player.bet))
    
    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)
    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)

    print('\nPlayer has ', player.calculate_total_rank())
    
    game_in_progress = True

    while game_in_progress:
        game_in_progress = ai_choices(player, dealer, deck)

    if (player.is_splitting):
        print('\nPlayer has first hand ', player.calculate_split_rank(0))
        print('Player has second hand ', player.calculate_split_rank(1))
        if(player.splitWon):
            Game.player_wins_pool(player, dealer)
            player.is_splitting = False
            print("Player won $", player.bet, " on second hand!\n")
        else:
            Game.dealer_wins_pool(player, dealer)
            player.is_splitting = False
            print("Dealer lost $", player.bet, " on second hand...\n")


    if(player.hasWon):
        Game.player_wins_pool(player, dealer)
        print("Player won $", player.bet, " ...\n")
        print("Player total is now: ", player.wallet)
        print("Dealer total is now: ", dealer.wallet, "\n")

    elif(player.is_surrendering):
        player.wallet -= player.bet / 2
        dealer.wallet += player.bet / 2
        player.is_surrendering = False

    else:
        Game.dealer_wins_pool(player, dealer)
        print("You won $", player.bet, "!!!\n")
        print("Player total is now: ", player.wallet)
        print("Dealer total is now: ", dealer.wallet, "\n")

def ai_choices(player, dealer, deck):
    if(player.check_rank(player.hand[0]) > 7 and player.check_rank(player.hand[1]) == player.check_rank(player.hand[0]) ):
        print("Player splits")
        return Game.split(player, dealer, deck)
    elif(player.wallet > player.bet * 2):
        print("Player doubles down")
        return Game.double_down(player, dealer, deck)
    elif(player.calculate_total_rank() == 16 and len(player.hand) == 2):
        print("Player surrenders")
        return Game.surrender(player, dealer)
    elif(player.calculate_total_rank() >= 19):
        print("Player stands")
        return Game.stand(player, dealer, deck)
    else:
        print("Player hits")
        return Game.hit(player, dealer, deck)
