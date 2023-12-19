digPlan = []
rowMax = 0
rowMin = 0
currentRow = 0
columnMax = 0
columnMin = 0
currentColumn = 0
with open('18.Input.txt') as file:
    for line in file:
        digPlan.append([])
        direction, meters, _ = line[:-1].strip().split(' ')
        digPlan[-1].extend([direction, int(meters)])
        if direction == 'U':
            currentRow -= int(meters)
            rowMin = min(rowMin, currentRow)
        elif direction == 'D':
            currentRow += int(meters)
            rowMax = max(rowMax, currentRow)
        elif direction == 'L':
            currentColumn -= int(meters)
            columnMin = min(columnMin, currentColumn)
        elif direction == 'R':
            currentColumn += int(meters)
            columnMax = max(columnMax, currentColumn)


rowLength = rowMax + 1 - min(0, rowMin)
columnLength = columnMax + 1 - min(0, columnMin)
digSite = [[]]
digSite[0] = ['*'] * (columnLength+2)

for i in range(1, rowLength + 1):
    digSite.append(['*'])
    for _ in range(columnLength):
        digSite[i].append('.')
    digSite[i].append('*')
digSite.append([])
digSite[-1] = ['*'] * (columnLength+2)

def highlightExterior(digSite=digSite):
    digSite[0][:] = ['*']*len(digSite[0]) 
    changing = True
    while changing:
        changing = False
        for i in range(len(digSite)):
            for j in range(len(digSite[i])):
                if digSite[i][j] != '#' and digSite[i][j] != '*':
                    if digSite[i-1][j] == '*' or digSite[i][j-1] == '*' or digSite[i+1][j] == '*' or digSite[i][j+1] == '*':
                        changing = True
                        digSite[i][j] = '*'
    for row in digSite:
        for i in range(len(row)):
            if row[i] == '.':
                row[i] = '#'


            
                



def dig(currentRow, currentColumn, digSite=digSite, digPlan=digPlan):
    digSite[currentRow][currentColumn] = '#'
    for row in digPlan:
        direction, meters = row[0], row[1]
        if direction == 'U':
            for i in range(meters):
                digSite[currentRow-1-i][currentColumn] = '#'
            currentRow -= meters
        elif direction == 'D':
            for i in range(meters):
                digSite[currentRow+1+i][currentColumn] = '#'
            currentRow += meters
        elif direction == 'L':
            digSite[currentRow][currentColumn-meters:currentColumn] = ['#']*meters
            currentColumn -= meters
        elif direction == 'R':
            digSite[currentRow][currentColumn+1:currentColumn+meters+1] = ['#']*meters
            currentColumn += meters
    highlightExterior()

startRow = 0 - rowMin + 1
startColumn = 0 - columnMin + 1
dig(startRow, startColumn)
total = 0
for row in digSite:
    total += row.count('#')

    print(''.join([char for char in row]))

print(total)