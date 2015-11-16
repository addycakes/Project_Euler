'''
Euler Problem 54

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).

But if two ranks tie, for example, both players have a pair of queens, then
highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's
cards and the last five are Player 2's cards. You can assume that all hands are valid
(no invalid characters or repeated cards), each player's hand is in no specific order, and in
each hand there is a clear winner.

How many hands does Player 1 win?
'''

def handWithHighCard(handOne,handTwo):
    handOneValues = []
    handTwoValues = []
    
    for card in handOne:
        value = cards.index(card[0]) + 1
        handOneValues += [value]
        
    for card in handTwo:
        value2 = cards.index(card[0]) + 1
        handTwoValues += [value2]

    handOneValues.sort(reverse=True)
    handTwoValues.sort(reverse=True)

    for i in range(len(handOneValues)):
        if handOneValues[i] > handTwoValues[i]:
            return handOne
        elif handOneValues[i] < handTwoValues[i]:
            return handTwo

    return None

def isHandOnePair(hand):
    pairValues = []
    for card in hand:
        value = cards.index(card[0]) + 1

        if value in pairValues:
            return True, value
        else:
            pairValues += [value]

    return False, 0
        
def isHandTwoPair(hand):
    usedCards = []
    pairValues = []
    onePair = False
    
    for card in hand:
        value = cards.index(card[0]) + 1
        if value in usedCards:
            pairValues += [value]
            if not onePair:
                onePair = True
            else:
                return True, pairValues
        else:
            usedCards += [value]

    return False, []

def isHandFullHouse(hand):
    fullHouse = {}
    for card in hand:
        value = cards.index(card[0]) + 1
        if value in fullHouse:
            fullHouse[value] += 1
        else:
            fullHouse[value] = 1

    if len(fullHouse) == 2:
        for item in fullHouse:
            if fullHouse == 3:
                return True, item

    return False, 0

def isHandFlush(hand):
    flushSuit = ''
    for card in hand:
        suit = card[1]
        if flushSuit == '':
            flushSuit = suit
        elif suit != flushSuit:
            return False

    return True

def isHandStraight(hand):
    straightValues = []
    
    for card in hand:
        value = cards.index(card[0]) + 1
        straightValues += [value]

    straightValues.sort()
    start = straightValues[0]

    for i in range(start,start+5):
        if i not in straightValues:
            return False
        
    return True

def isHandThreeOfKind(hand):
    threeKindValue = ''
    fifthCard = False
    fourthCard = False
    
    for card in hand:
         value = cards.index(card[0]) + 1
         
         if threeKindValue == '':
             threeKindValue = value
         elif threeKindValue != value:
             if not fifthCard:
                 threeKindValue = value
                 fifthCard = True
             elif not fourthCard:
                 threeKindValue = value
                 fourthCard = True
             else:
                 return False, 0

    return True, threeKindValue

def isHandFourOfKind(hand):
    fourKindValue = ''
    fifthCard = False
    for card in hand:
         value = cards.index(card[0]) + 1
         
         if fourKindValue == '':
             fourKindValue = value
         elif fourKindValue != value:
             if not fifthCard:
                 fourKindValue = value
                 fifthCard = True
             else:
                 return False, 0

    return True, fourKindValue
             
def isHandStraightFlush(hand):
    if isHandStraight(hand) and isHandFlush(hand):
        return True
    return False

def isHandRoyalFlush(hand):
    flushSuit = ''
    neededCards = ['T','J','Q','K','A']
    for card in hand:
        suit = card[1]
        value = cards.index(card[0]) + 1

        if value not in neededCards:
            return False
        else:
            neededCards.remove(value)
            
        if flushSuit == '':
            flushSuit = suit
        elif suit != flushSuit:
            return False
        
    return True


def determineWinner(handOne, handTwo):
    
    #check if royal flush
    if isHandRoyalFlush(handOne):
        return handOne
    if isHandRoyalFlush(handTwo):
        return handTwo

    #check if straight flush
    oneStraightFlush = isHandStraightFlush(handOne)
        
    if isHandStraightFlush(handTwo):
        if not oneStraightFlush:
            return handTwo
        else:
            return handWithHighCard(handOne, handTwo)
    elif oneStraightFlush:
        return handOne

    #check if four of a kind
    oneFourKind, v = isHandFourOfKind(handOne)
    twoFourKind, v2 = isHandFourOfKind(handTwo)

    if twoFourKind:
        if not oneFourKind:
            return handTwo
        else:
            if v > v2:
                return handOne
            else:
                return handTwo
    elif oneFourKind:
        return handOne

    #check if full house
    oneFullHouse, v = isHandFullHouse(handOne)
    twoFullHouse, v2 = isHandFullHouse(handTwo)

    if twoFullHouse:
        if not oneFullHouse:
            return handTwo
        else:
            if v > v2:
                return handOne
            else:
                return handTwo
    elif oneFullHouse:
        return handOne

    #check if flush
    oneFlush = isHandFlush(handOne)
        
    if isHandFlush(handTwo):
        if not oneFlush:
            return handTwo
        else:
            return handWithHighCard(handOne, handTwo)
    elif oneFlush:
        return handOne

    #check if straight
    oneStraight = isHandStraight(handOne)
        
    if isHandStraight(handTwo):
        if not oneStraight:
            return handTwo
        else:
            return handWithHighCard(handOne, handTwo)
    elif oneStraight:
        return handOne

    #check if three kind
    oneThreeKind, v = isHandThreeOfKind(handOne)
    twoThreeKind, v2 = isHandThreeOfKind(handTwo)

    if twoThreeKind:
        if not oneThreeKind:
            return handTwo
        else:
            if v > v2:
                return handOne
            else:
                return handTwo
    elif oneThreeKind:
        return handOne
    
    #check if two pair
    oneTwoPair, v = isHandTwoPair(handOne)
    twoTwoPair, v2 = isHandTwoPair(handTwo)

    if twoTwoPair:
        if not oneTwoPair:
            return handTwo
        else:
            if (v[0] >= v2[0] and v[0] >= v2[1]) or (v[1] >= v2[0] and v[1] >= v2[1] ):
                return handOne
            elif (v2[0] >= v[0] and v2[0] >= v[1]) or (v2[1] >= v[0] and v2[1] >= v[1]) :
                return handTwo
            else:
                return handWithHighCard(handOne, handTwo)
    elif oneTwoPair:
        return handOne

    #check if one pair
    oneOnePair, v = isHandOnePair(handOne)
    twoOnePair, v2 = isHandOnePair(handTwo)

    if twoOnePair:
        if not oneOnePair:
            return handTwo
        else:
            if v > v2:
                return handOne
            elif v < v2:
                return handTwo
            else:
                return handWithHighCard(handOne, handTwo)
    elif oneOnePair:
        return handOne

    #return high card hand 
    return handWithHighCard(handOne, handTwo)
    
hands = open('/Users/adam/Desktop/poker.txt', 'r')
playerOne = {}
playerTwo = {}

i = 1
for line in hands.readlines():
    cards = line.split(' ')
    playerOne[i] = cards[:5]
    playerTwo[i] = cards[5:]

    #print playerOne
    #print playerTwo

    i += 1
hands.close()

cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

playerOneWins = 0
for j in range(1,1001):
    winner = determineWinner(playerOne[j],playerTwo[j])

    if winner == playerOne[j]:
        playerOneWins += 1

print playerOneWins

