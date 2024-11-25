import Cards
def playing():
    while True:
        status = input("Type 'Start' to deal the hand\n")
        if (status.lower() == "start"):
            game_going = True
            PlayersHand = Cards.getPlayerHand()
            while game_going:
                print("Here is your hand \n" + str(PlayersHand))
                print(Cards.getSum(PlayersHand))
                gameStatus = Cards.checkIfBust(Cards.getSum(PlayersHand))
                print(gameStatus)
                if(gameStatus == 1 and move.lower() != 'stand'):
                    move = input("What would you like to do?\nType hit to add a card to your hand\nType stand to keep the hand you have\n")
                    if (move.lower() == "Hit"):
                        Cards.hitPlayerHand(PlayersHand)
                    else:
                        print("Standing")
playing()





