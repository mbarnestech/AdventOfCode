contraption = []
energy = []
with open('16.Input.txt') as file:
    for row in file:
        contraption.append([])
        energy.append([])
        for char in row[:-1]:
            contraption[-1].append(char)
            energy[-1].append('.')

# for row in contraption:
#     print(row)
# print('break')
# for row in energy:
#     print(row)
# last & current -> (row, column)
def lightMove(lastRow, lastColumn, currentRow, currentColumn):
    while 0 <= currentRow < len(contraption[0]) and 0 <= currentColumn < len(contraption):
        # if 0 <= lastRow < len(contraption[0]) and 0 <= lastColumn < len(contraption):
        #     if contraption[lastRow][lastColumn] == '|' or contraption[lastRow][lastColumn] == '-':
        #         energy[lastRow][lastColumn] = contraption[lastRow][lastColumn]
        if (contraption[currentRow][currentColumn] == '-' or contraption[currentRow][currentColumn] == '|') and energy[currentRow][currentColumn] != '.':
            break
        # if energy[currentRow][currentColumn] != '.' and energy[currentRow][currentColumn+1] != '.' and energy[currentRow][currentColumn-1] != '.' and energy[currentRow+1][currentColumn] != '.' and energy[currentRow-1][currentColumn] != '.':
        #     break
        energy[currentRow][currentColumn] = '#'
        nextStraight = (currentRow-(lastRow-currentRow), currentColumn-(lastColumn-currentColumn))
        nextUp = [currentRow-1, currentColumn]
        nextDown = [currentRow+1, currentColumn]
        nextRight = [currentRow, currentColumn+1]
        nextLeft = [currentRow, currentColumn-1]
        if contraption[currentRow][currentColumn] == '.':
            # print(f'before: {lastRow=}, {lastColumn=}, {currentRow=}, {currentColumn=}')
            lastRow, lastColumn = currentRow, currentColumn
            # print(f'middle: {lastRow=}, {lastColumn=}, {currentRow=}, {currentColumn=}')
            currentRow, currentColumn = nextStraight
            # print(f'end: {lastRow=}, {lastColumn=}, {currentRow=}, {currentColumn=}')

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

lightMove(0,-1,0,0)

for row in contraption:
    print(row)
print('break')
total = 0
for row in energy:
    total += row.count('#')
    print(row)

print(total)