from collections import defaultdict 
import time

panel = []

with open('14.Input.txt') as file:
    for line in file:
        panel.append([])
        for char in line[:-1]:
            panel[-1].append(char)

# for use in East/West
rowDict = defaultdict(list)
# for use in North/South
columnDict = defaultdict(list)

for i in range(len(panel)):
    for j in range(len(panel[i])):
        if panel[i][j] == '#':
            rowDict[i].append(j)
            columnDict[j].append(i)

for columnData in columnDict.values():
    columnData.append(len(panel))

for rowData in rowDict.values():
    rowData.append(len(panel[0]))
first = None
start_time = time.time()
cycles = 1000
repeats = []
copies = {}
for cycle in range(cycles):
    # North
    for i in range(len(panel[0])):
        if columnDict[i]:
            start = 0
            for row in columnDict[i]:
                stop = row-1
                while start < stop:
                    while panel[start][i] == 'O' and start < stop:
                        start += 1
                    while panel[stop][i] == '.' and start < stop:
                        stop -= 1
                    if start < stop and panel[stop][i] == 'O':
                        panel[start][i] = 'O'
                        panel[stop][i] = '.'
                start = row+1
        else:
            start = 0
            stop = len(panel) - 1
            while start < stop:
                    while panel[start][i] == 'O' and start < stop:
                        start += 1
                    while panel[stop][i] != 'O' and start < stop:
                        stop -= 1
                    if start < stop and panel[stop][i] == 'O':
                        panel[start][i] = 'O'
                        panel[stop][i] = '.'

    # print('After North')
    # for row in panel:
    #     print(row)

    # West
    for i in range(len(panel)):
        if 'O' not in panel[i]:
            continue
        elif rowDict[i]:
            start = 0
            for column in rowDict[i]:
                stop = column
                panel[i][start:stop] = sorted(panel[i][start:stop], reverse = True)
                start = column + 1
        else:
            panel[i] = sorted(panel[i], reverse = True)

    # print('\nAfter West')
    # for row in panel:
    #     print(row)

    # South
    for i in range(len(panel[0])):
        if columnDict[i]:
            start = 0
            for row in columnDict[i]:
                stop = row-1
                while start < stop:
                    while panel[start][i] == '.' and start < stop:
                        start += 1
                    while panel[stop][i] == 'O' and start < stop:
                        stop -= 1
                    if start < stop and panel[start][i] == 'O':
                        panel[start][i] = '.'
                        panel[stop][i] = 'O'
                start = row+1
        else:
            start = 0
            stop = len(panel) - 1
            while start < stop:
                    while panel[start][i] == '.' and start < stop:
                        start += 1
                    while panel[stop][i] == 'O' and start < stop:
                        stop -= 1
                    if start < stop and panel[start][i] == 'O':
                        panel[start][i] = '.'
                        panel[stop][i] = 'O'

    # print('After South')
    # for row in panel:
    #     print(row)

    # East
    for i in range(len(panel)):
            if 'O' not in panel[i]:
                continue
            elif rowDict[i]:
                start = 0
                for column in rowDict[i]:
                    stop = column
                    panel[i][start:stop] = sorted(panel[i][start:stop])
                    start = column + 1
            else:
                panel[i] = sorted(panel[i])
    copy = []
    for row in panel:
        copy.append([])
        for char in row:
            copy[-1].append(char)
    maxLoad = len(panel) + 1
    totalLoad = 0
    for row in panel:
        maxLoad -= 1
        for item in row:
            if item == 'O':
                totalLoad += maxLoad
    if copy in repeats:
        print(f'panel {cycle} in repeats at {repeats.index(copy)} with load of {totalLoad}')
        if not first:
            first = (cycle, repeats.index(copy))
        elif copy == repeats[first[1]]:
            second = cycle
            break
        copies[cycle] = totalLoad
    else:
        repeats.append(copy)
    # print('\nAfter East')
    # for row in panel:
    #     print(row)

end_time = time.time()
elapsed_time = end_time-start_time
print(f'Time elapsed for {cycles} cycles: {elapsed_time}')

print(first, second)
# for i in range(len(repeats)):
#     print(f'Repeats index {i}')
#     for row in repeats[i]:
#         print(row)
# print(rowDict)
# print(columnDict)

for num in range(first[0], second):
    if (1000000000-1-num) % (second-first[0]) == 0:
        print(num, copies[num])

