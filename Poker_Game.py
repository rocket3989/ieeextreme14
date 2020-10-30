# Collin Pearce, 100%
# performance is complicated, upper bound ~O(12 ^ 9)

# recursively generate all hands that pass all rules, then find the highest value hand that is smallest lexicographically 

# to make a computer work hard, run this input
# 1 9
# A
# n

from collections import Counter

N, K = [int(x) for x in input().split()]

cards = '23456789XJQKA'

lookup = {cards[i]:i for i in range(13)}

deck = {card: 4 for card in cards}

deal = input().strip()

deal_counts = Counter(deal)

choices = input().strip()

hand = []

# this loop was added after the competition. It seeds the starting hand with required cards,
# and takes out cards that cannot be used
# previous code checked validity of card hand at the end of recursion
# MUCH less expensive to do all of the work ahead of time AND avoid recurring on invalid states

for card, choice in zip(deal, choices):
    if choice == 'n':
        if deck[card] != 4:
            print('impossible')
            exit()
    
        deck[card] = 0
        continue
        
    if deck[card] == 4:
        deck[card] -= 1
        hand.append(card)
        
        if deal_counts[card] == 4:
            print('impossible')
            exit()
     
for card in deal:
    deck[card] -= 1

def keyHand(dealt):
    dealt = sorted(dealt, key=lambda x: lookup[x])
    
    val = 0
    for card in dealt:
        val *= 14
        val += lookup[card]
    
    return val


def scoreHand(test, deal):
    curr = Counter(test + deal)
    scores = [0, 0, 1, 20, 1760]
    
    score = 0
    for val in curr.values():
        score += scores[val]
        
    return score
    

def makeHand(depth, last, deal, choices):
    if depth < 0:
        return [0, '']
        # too many cards seeded into hand

    if depth == 0:
        
        handStr = ''.join(hand)
        
        points = scoreHand(handStr, deal)
        
        return [points, handStr]
             
    bestHand = [0, '']
    
    for val in cards[lookup[last]:]:
        if deck[val] > 0:
            hand.append(val)
            deck[val] -= 1
            contender = makeHand(depth - 1, val, deal, choices)
            
            if contender[0] == bestHand[0]:
                bestHand[1] = min((bestHand[1], contender[1]), key=keyHand)
            
            if contender[0] > bestHand[0]:
                bestHand = contender
            
            # lesson in recursion: the deeper you are, the more expensive operations are
            # original code had the above comparisons swapped, meaning the equality check
            # would always be true. With deep searches, this *doubled* execution time
            
            hand.pop()
            deck[val] += 1
            
    return bestHand


ans = makeHand(K - len(hand), '2', deal, choices)

if ans[1] == '':
    print('impossible')

else:
    print(*sorted(ans[1], key=lambda x: lookup[x]), sep='')
