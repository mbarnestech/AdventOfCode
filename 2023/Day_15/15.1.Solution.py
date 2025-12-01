sequences = []
with open('15.Input.txt') as file:
    for line in file:
        sequences = line.strip().split(',')


print(sequences)

sequenceResults = []
for sequence in sequences:
    current = 0
    for char in sequence:
        current += ord(char)
        current *= 17
        current %= 256
    sequenceResults.append(current)
print(sequenceResults)
print(sum(sequenceResults))

