import random
Suits = ["♥","♦","♠","♣"]
Numbers = ['2','3','4','5','6','7','8','9','J','Q','K','A']
isAce = False
AddedAce = False
def hitPlayerHand(cards):
    cards.append(random.choice(Numbers) + random.choice(Suits))   
    return cards
def checkIfBust(handSum):
    #Returns values of 0 1 or 2 and 0 is bust 1 is safe 2 is blackjack
    if(handSum == 21):
        return 2
    if(handSum < 22):
        return 1
    else:
        return 0
def getSum(cards):
    handSize = len(cards)
    i = 0
    handSum = 0
    while (i < handSize):
        value = cards[i][0]
        if (value == 'J' or value == 'K' or value =='Q'):
            value = 10
        elif (value == 'A'):
            value = 1
            isAce = True
        handSum += int(value)
        i += 1
    if (isAce and ((int(value) + 10) <= 21)):
        AddedAce = True
        handSum += 10
    if(isAce and AddedAce and (handSum > 21)):
        handSum -= 10
        AddedAce = False
    return handSum