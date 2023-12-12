galaxy = []
count = 0
with open('11.Input.txt') as file:
    for line in file:
        galaxy.append([])
        for char in line[:-1]:
            if char == '#':
                galaxy[-1].append(count)
                count += 1
            else:
                galaxy[-1].append(char)

rowsWithGalaxies = set()
columnsWithGalaxies = set()
for i in range(len(galaxy)):
    for j in range(len(galaxy[i])):
        if type(galaxy[i][j]) == int:
            rowsWithGalaxies.add(i)
            columnsWithGalaxies.add(j)
rows = set(range(0, len(galaxy))) - rowsWithGalaxies
columns = set(range(0, len(galaxy[0]))) - columnsWithGalaxies

rows = sorted(list(rows), reverse=True)
columns = sorted(list(columns), reverse=True)
# for column in columns:
#     for row in galaxy:
#         row[column:column+1] = ['.']*1000000


# for row in rows:
#     galaxy[row:row+1] = (['.']*len(galaxy[0]))*1000000

# print()
galaxyDict = {}
for i in range(len(galaxy)):
    for j in range(len(galaxy[i])):
        if type(galaxy[i][j]) == int:
            rowNum = i
            columnNum = j
            for row in rows:
                if row < i:
                    rowNum += 1000000 -1
            for column in columns:
                if column < j:
                    columnNum += 1000000 -1 
            galaxyDict[galaxy[i][j]] = (rowNum, columnNum)

pathSum = 0

for i in range(0, count-1):
    for j in range(i+1, count):
        pathSum += max(galaxyDict[j][0],galaxyDict[i][0]) - min(galaxyDict[j][0],galaxyDict[i][0]) + max(galaxyDict[j][1],galaxyDict[i][1]) - min(galaxyDict[j][1],galaxyDict[i][1])

print(pathSum)

