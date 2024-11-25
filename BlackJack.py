import BlackJackMoves
import Dealer
def playing():
    move = "start"
    while True:
        status = input("Type 'Start' to deal the hand\n")
        if (status.lower() == "start"):
            game_going = True
            PlayersHand = Dealer.getPlayerHand()
            while game_going:
                print("Here is your hand \n" + str(PlayersHand))
                print(BlackJackMoves.getSum(PlayersHand))
                gameStatus = BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand))
                if(gameStatus == 1 and move.lower() != 'stand'):
                    move = input("What would you like to do?\nType hit to add a card to your hand\nType stand to keep the hand you have\n")
                    if (move.lower() == "hit"):
                        BlackJackMoves.hitPlayerHand(PlayersHand)
                        if(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand)) == 2):
                            print("Black Jack!")
                            game_going = False
                        elif(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand)) == 0):
                            print("Bust!")
                            game_going = False
                    else:
                        print("Standing")
playing()