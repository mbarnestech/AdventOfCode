cards = {}

for num in range(1, 212):
    cards[num] = 1

total = 0
with open("4.1.Input.txt") as file:
    for line in file:
        splits = line.split(':')
        cardNum = int(splits[0][5:])
        groups = splits[1][:-1].split('|')
        winning = set(groups[0].strip().split(' '))
        mine = set(groups[1].strip().split(' '))
        winning.discard('')
        mine.discard('')
        matches = winning & mine
        if matches:
            for i in range(1, len(matches)+1):
                cards[cardNum+i] += cards[cardNum]
                print(f'{matches=}, {i=}')
        total += cards[cardNum]

print(total)