blocks = []

with open('17.SampleInput.txt') as file:
    for row in file:
        blocks.append([])
        for num in row[:-1]:
            blocks[-1].append(int(num))

start = (0,0)
end = (0,0)

# Realizing this is going to be a doozy; sticking a pin in it for later as I'm doing catch up. On to day 18!
print(blocks)