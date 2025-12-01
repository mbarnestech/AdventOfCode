value = {'A': 13, 
         'K': 12, 
         'Q': 11, 
         'J': 10, 
         'T': 9, 
         '9': 8, 
         '8': 7, 
         '7': 6, 
         '6': 5, 
         '5': 4, 
         '4': 3, 
         '3': 2,  
         '2': 1}

hands = {}

with open('7.Input.txt') as file:
    for line in file:
        elements = line.strip().split(' ')
        hand = (elements[0][0],elements[0][1],elements[0][2],elements[0][3],elements[0][4])
        rank = int(elements[1])
        hands[hand] = rank

five = []
four = []
full = []
three = []
two = []
one = []
high = []


for hand in hands:
    if len(set(hand)) == 1:
        five.append(hand)
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            four.append(hand)
        else:
            full.append(hand)
    elif len(set(hand)) == 3:
        for card in hand:
            if hand.count(card) == 3:
                three.append(hand)
                break
            if hand.count(card) == 2:
                two.append(hand)
                break
    elif len(set(hand)) == 4:
        one.append(hand)
    elif len(set(hand)) == 5:
        high.append(hand)

def rankHands(handType):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(1, len(handType)):
            for j in range(5):
                if value[handType[i-1][j]] > value[handType[i][j]]:
                    break
                if value[handType[i-1][j]] == value[handType[i][j]]:
                    continue
                if value[handType[i-1][j]] < value[handType[i][j]]:
                    handType[i-1], handType[i] = handType[i], handType[i-1]
                    sorted = False
                    break

rankHands(five)
rankHands(four)
rankHands(full)
rankHands(three)
rankHands(two)
rankHands(one)
rankHands(high)

rank = 1
total = 0
for hand in high[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in one[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in two[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in three[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in full[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in four[::-1]:
    total += hands[hand] * rank
    rank += 1
for hand in five[::-1]:
    total += hands[hand] * rank
    rank += 1








print(total, rank)