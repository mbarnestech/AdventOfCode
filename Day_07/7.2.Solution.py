from collections import Counter


value = {'A': 13, 
         'K': 12, 
         'Q': 11, 
         'T': 10, 
         '9': 9, 
         '8': 8, 
         '7': 7, 
         '6': 6, 
         '5': 5, 
         '4': 4, 
         '3': 3,  
         '2': 2,
         'J': 1 
         }

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
    h = Counter(hand)
    j = 0
    if 'J' in h.keys() and len(h) > 1:
        j = h['J']
        del h['J']
    pattern = h.values()
    pattern = sorted(pattern)
    pattern[-1] += j

    if pattern == [5]:
        five.append(hand)
    elif pattern == [1,4]:
        four.append(hand)
    elif pattern == [2,3]:
        full.append(hand)
    elif pattern == [1,1,3]:
        three.append(hand)
    elif pattern == [1,2,2]: 
        two.append(hand)
    elif pattern == [1,1,1,2]:
        one.append(hand)
    elif pattern == [1,1,1,1,1]:
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