import time
import BlackJackMoves
import Dealer
def playing():
    move = "start"
    status = ""
    while True:
        status = input("Type 'Start' to deal the hand\n")
        if (status.lower() == "start"):
            game_going = True
            PlayersHand = Dealer.getPlayerHand()
            DealerHand = Dealer.getPlayerHand()
            while game_going:
                print("Here is your hand " + str(PlayersHand))
                print("Current Total: " + str(BlackJackMoves.getSum(PlayersHand)))
                print("\nHere is one of the Dealers cards")
                print(str(DealerHand[0]))
                gameStatus = BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand))
                if(gameStatus == 1 and move.lower() != 'stand'):
                    move = input("\nWhat would you like to do?\nType hit to add a card to your hand\nType stand to keep the hand you have\n")
                    if (move.lower() == "hit"):
                        BlackJackMoves.hitPlayerHand(PlayersHand)
                        if(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand)) == 2):
                            print("You have Black Jack!")
                            print("Dealer hand: " + str(DealerHand))
                            print("Here is your hand " + str(PlayersHand))
                            if(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(DealerHand)) == 2):
                                print("Deal also has blackjack it is a tie")
                            game_going = False
                        elif(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(PlayersHand)) == 0):
                            print("Here is your hand " + str(PlayersHand))
                            print("Bust!")
                            print("Dealer hand: " + str(DealerHand))
                            game_going = False
                if(gameStatus == 1 and move.lower() == 'stand'):
                    print("Here is the full hand of the Dealer")
                    print(DealerHand)
                    time.sleep(2)
                    while(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(DealerHand)) == 1 and BlackJackMoves.getSum(DealerHand) < 17):
                        time.sleep(1)
                        BlackJackMoves.hitPlayerHand(DealerHand)
                        print(DealerHand)
                    if(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(DealerHand)) == 2):
                        print("Dealer has blackjack!")
                        game_going = False
                    elif(BlackJackMoves.checkIfBust(BlackJackMoves.getSum(DealerHand)) == 1):
                        if(BlackJackMoves.getSum(DealerHand) < BlackJackMoves.getSum(PlayersHand)):
                            print("Player Wins")
                            game_going = False
                        elif(BlackJackMoves.getSum(DealerHand) > BlackJackMoves.getSum(PlayersHand)):
                            print("Dealer Wins")
                            game_going = False
                        elif(BlackJackMoves.getSum(DealerHand) == BlackJackMoves.getSum(PlayersHand)):
                            print("It is a tie")
                            game_going = False
                    
playing()