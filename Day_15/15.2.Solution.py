sequences = []
with open('15.Input.txt') as file:
    for line in file:
        sequences = line.strip().split(',')

boxes = {}
for i in range(256):
    boxes[i] = []

sequenceResults = []

def findBox(sequence):
    current = 0
    for char in sequence:
        current += ord(char)
        current *= 17
        current %= 256
    return current

for sequence in sequences:
    if '=' in sequence:
        box = findBox(sequence[:sequence.index('=')])
        added = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == sequence[:sequence.index('=')]:
                boxes[box][i][1] = sequence[sequence.index('=')+1:]
                added = True
                break
        if added == False:
            boxes[box].append([sequence[:sequence.index('=')], sequence[sequence.index('=')+1:]])

    if '-' in sequence:
        box = findBox(sequence[:sequence.index('-')])
        for lens in boxes[box]:
            if lens[0] == sequence[:sequence.index('-')]:
                boxes[box].pop(boxes[box].index(lens))
                break

for box in boxes:
    if boxes[box]:
        for i in range(len(boxes[box])):
            power = box + 1
            power *= (i+1)
            power *= int(boxes[box][i][1])
            sequenceResults.append(power)

    
print(sum(sequenceResults))

