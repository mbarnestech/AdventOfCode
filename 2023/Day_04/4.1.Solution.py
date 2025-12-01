total = 0
with open("4.1.Input.txt") as file:
    for line in file:
        splits = line.split(':')
        groups = splits[1][:-1].split('|')
        winning = set(groups[0].strip().split(' '))
        mine = set(groups[1].strip().split(' '))
        winning.discard('')
        mine.discard('')
        matches = winning & mine   
        sum = 0   
        if matches:
            sum = 2**(len(matches)-1)
        total+=sum
print(total)