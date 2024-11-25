import random
Suits = ["♥","♦","♠","♣"]
Numbers = ['2','3','4','5','6','7','8','9','J','Q','K','A']
def getPlayerHand():
    i = 0
    playerHand =['','']
    while (i < 2):
        playerHand[i] = random.choice(Numbers) + random.choice(Suits)
        i += 1
    return playerHand