contraption = []
energy = []
with open('16.Input.txt') as file:
    for row in file:
        contraption.append([])
        energy.append([])
        for char in row[:-1]:
            contraption[-1].append(char)
            energy[-1].append('.')

def lightMove(lastRow, lastColumn, currentRow, currentColumn):
    while 0 <= currentRow < len(contraption[0]) and 0 <= currentColumn < len(contraption):
        if (contraption[currentRow][currentColumn] == '-' or contraption[currentRow][currentColumn] == '|') and energy[currentRow][currentColumn] != '.':
            break
        energy[currentRow][currentColumn] = '#'
        nextStraight = (currentRow-(lastRow-currentRow), currentColumn-(lastColumn-currentColumn))
        nextUp = [currentRow-1, currentColumn]
        nextDown = [currentRow+1, currentColumn]
        nextRight = [currentRow, currentColumn+1]
        nextLeft = [currentRow, currentColumn-1]
        if contraption[currentRow][currentColumn] == '.':
            lastRow, lastColumn = currentRow, currentColumn
            currentRow, currentColumn = nextStraight
        elif contraption[currentRow][currentColumn] == '|':
            if lastColumn != currentColumn:
                lightMove(currentRow, currentColumn, *nextDown)
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextUp
            else:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextStraight
        elif contraption[currentRow][currentColumn] == '-':
            if lastRow != currentRow:
                lightMove(currentRow, currentColumn, *nextLeft)
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextRight
            else:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextStraight
        elif contraption[currentRow][currentColumn] == '/':
            if lastColumn > currentColumn:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextDown
            elif lastColumn < currentColumn:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextUp
            elif lastRow < currentRow:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextLeft
            else:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextRight
        elif contraption[currentRow][currentColumn] == '\\':
            if lastColumn > currentColumn:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextUp
            elif lastColumn < currentColumn:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextDown
            elif lastRow < currentRow:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextRight
            else:
                lastRow, lastColumn = currentRow, currentColumn
                currentRow, currentColumn = nextLeft

def resetEnergy(energy):
    for i in range(len(energy)):
        for j in range(len(energy[i])):
            energy[i][j] = '.'

total = 0
for i in range(len(contraption)):
    resetEnergy(energy)
    lightMove(i,-1,i,0)
    subTotal = 0
    for row in energy:
        subTotal += row.count('#')
    total = max(total, subTotal)
    resetEnergy(energy)
    lightMove(i,len(contraption[0]),i,len(contraption[0])-1)
    subTotal = 0
    for row in energy:
        subTotal += row.count('#')
    total = max(total, subTotal)

for i in range(len(contraption[0])):
    resetEnergy(energy)
    lightMove(-1,i,0,i)
    subTotal = 0
    for row in energy:
        subTotal += row.count('#')
    total = max(total, subTotal)
    resetEnergy(energy)
    lightMove(len(contraption[0]),i,len(contraption)-1, i)
    subTotal = 0
    for row in energy:
        subTotal += row.count('#')
    total = max(total, subTotal)

print(total)