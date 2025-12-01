mirrors = [[]]

with open('13.Input.txt') as file:
    for line in file:
        if len(line)>1:
            mirrors[-1].append([])
            for char in line[:-1]:
                mirrors[-1][-1].append(char)
        else:
            mirrors.append([])

# FIND OLD LINES - CAN'T REUSE

oldLines = []
for mirror in mirrors:
    oldLines.append([])
    matched = False
    for i in range(1, len(mirror)):
        if mirror[i] == mirror[i-1]:
            same = True
            top = i-2
            bottom = i+1
            while top >= 0 and bottom < len(mirror):
                if mirror[bottom] != mirror[top]:
                    same = False
                    break
                top -= 1
                bottom += 1
            if same:
                print(f'Horizontal match at rows {i-1} and {i}')
                oldLines[-1] = ('H', i-1, i)
                matched = True
    if not matched:
        flippedMirror = []
        for i in range(len(mirror)):
            for j in range(len(mirror[i])):
                if len(flippedMirror) < j+1:
                    flippedMirror.append([])
                flippedMirror[j].append(mirror[i][j])
        for i in range(1, len(flippedMirror)):
            if flippedMirror[i] == flippedMirror[i-1]:
                same = True
                top = i-2
                bottom = i+1
                while top >= 0 and bottom < len(flippedMirror):
                    if flippedMirror[bottom] != flippedMirror[top]:
                        same = False
                        break
                    top -= 1
                    bottom += 1
                if same:
                    print(f'Vertical match at columns {i-1} and {i}')
                    oldLines[-1] = ('V', i-1, i)
                    matched = True

#### Find Smudge & Total


total = 0
check = [0]*len(mirrors)
for i in range(len(mirrors)):
# for i in range(2,3):
    matched = False
    for j in range(1, len(mirrors[i])):
        if oldLines[i][0] == 'H' and oldLines[i][2] == j:
            continue
        checkMirror = []
        for row in mirrors[i]:
            checkMirror.append([])
            for char in row:
                checkMirror[-1].append(char)
        cleaned = False
        if checkMirror[j] != checkMirror[j-1]:
            for k in range(len(checkMirror[j])):
                if checkMirror[j][k] != checkMirror[j-1][k]:
                    checkMirror[j][k] = checkMirror[j-1][k]
                    print(f"{''.join(checkMirror[j])}, {j=}, {k=}")
                    cleaned = True
                    break
        if checkMirror[j] == checkMirror[j-1]:
            same = True
            top = j-2
            bottom = j+1
            while top >= 0 and bottom < len(checkMirror):
                if not cleaned:
                    if checkMirror[bottom] != checkMirror[top]:
                        for k in range(len(checkMirror[bottom])):
                            if checkMirror[bottom][k] != checkMirror[top][k]:
                                checkMirror[bottom][k] = checkMirror[top][k]
                                print(f'{checkMirror[bottom]=}, {bottom=}, {k=}')
                                cleaned = True
                                break
                if checkMirror[bottom] != checkMirror[top]:
                    same = False
                    break
                top -= 1
                bottom += 1
            if same:
                print(f'Horizontal match at rows {j-1} and {j}')
                total += 100*j
                check[i] = 100*j
                matched = True
    if not matched:
        flippedMirror = []
        for j in range(len(mirrors[i])):
            for k in range(len(mirrors[i][j])):
                if len(flippedMirror) < k+1:
                    flippedMirror.append([])
                flippedMirror[k].append(mirrors[i][j][k])
        for j in range(1, len(flippedMirror)):
            if oldLines[i][0] == 'V' and oldLines[i][2] == j:
                continue
            checkMirror = []
            for row in flippedMirror:
                checkMirror.append([])
                for char in row:
                    checkMirror[-1].append(char)
            cleaned = False
            if checkMirror[j] != checkMirror[j-1]:
                for k in range(len(checkMirror[j])):
                    if checkMirror[j][k] != checkMirror[j-1][k]:
                        checkMirror[j][k] = checkMirror[j-1][k]
                        print(f"{''.join(flippedMirror[j])},{''.join(checkMirror[j])}, {j=}, {k=}")
                        cleaned = True
                        break
            if checkMirror[j] == checkMirror[j-1]:
                same = True
                top = j-2
                bottom = j+1
                while top >= 0 and bottom < len(checkMirror):
                    if not cleaned:
                        if checkMirror[bottom] != checkMirror[top]:
                            for k in range(len(checkMirror[bottom])):
                                if checkMirror[bottom][k] != checkMirror[top][k]:
                                    checkMirror[bottom][k] = checkMirror[top][k]
                                    print(f'{checkMirror[bottom]=}, {bottom=}, {k=}')
                                    cleaned = True
                                    break
                    if checkMirror[bottom] != checkMirror[top]:
                        same = False
                        break
                    top -= 1
                    bottom += 1
                if same:
                    print(f'Vertical match at columns {j-1} and {j}')
                    total += j
                    check[i] = j
                    matched = True

    print(total)

    # 42406 - too low