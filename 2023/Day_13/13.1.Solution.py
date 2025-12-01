mirrors = [[]]

with open('13.Input.txt') as file:
    for line in file:
        if len(line)>1:
            mirrors[-1].append(line[:-1])
        else:
            mirrors.append([])

# for mirror in mirrors:
#     print('NEW MIRROR')
#     for line in mirror:
#         print(line)

total = 0

for mirror in mirrors:
    print(mirror)
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
                total += 100*i
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
                    total += i
                    matched = True


    

print(total)