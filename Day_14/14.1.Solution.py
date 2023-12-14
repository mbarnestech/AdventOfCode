panel = []

with open('14.Input.txt') as file:
    for line in file:
        panel.append([])
        for char in line[:-1]:
            panel[-1].append(char)

sliding = True
while sliding:
    sliding = False
    for i in range(1, len(panel)):
        for j in range(len(panel[i])):
            if panel[i][j] == 'O' and panel[i-1][j] == '.':
                panel[i][j], panel[i-1][j] = panel[i-1][j], panel[i][j]
                sliding = True

maxLoad = len(panel) + 1
totalLoad = 0
for row in panel:
    maxLoad -= 1
    for item in row:
        if item == 'O':
            totalLoad += maxLoad

print(totalLoad)
