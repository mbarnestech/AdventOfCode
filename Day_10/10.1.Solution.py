pipes = []

with open('10.PaddedInput.txt') as file:
    for line in file:
        pipes.append(line[:-1])

# last & current = (row, column)
def getNext(last, current):
    err = None
    next = None
    pipe = pipes[current[0]][current[1]]
    if pipe == '|':
        if last[0] > current[0]:
            next = (current[0]-1, current[1])
        elif last[0] < current[0]:
            next = (current[0]+1, current[1])
        else:
            err = True
    elif pipe == '-':
        if last[1] > current[1]:
            next = (current[0], current[1]-1)
        elif last[1] < current[1]:
            next = (current[0], current[1]+1)
    elif pipe == 'L':
        if last[0] < current[0]:
            next = (current[0], current[1]+1)
        elif last[1] > current[1]:
            next = (current[0]-1, current[1])
        else:
            err = True
    elif pipe == 'J':
        if last[0] < current[0]:
            next = (current[0], current[1]-1)
        elif last[1] < current[1]:
            next = (current[0]-1, current[1])
        else:
            err = True
    elif pipe == '7':
        if last[1] < current[1]:
            next = (current[0]+1, current[1])
        elif last[0] > current[0]:
            next = (current[0], current[1]-1)
        else:
            err = True
    elif pipe == 'F':
        if last[1] > current[1]:
            next = (current[0]+1, current[1])
        elif last[0] > current[0]:
            next = (current[0], current[1]+1)
        else:
            err = True
    elif pipe == '.':
        err = True
    elif pipe == 'S':
        next = current
    return current, next, err
    
def find_S(pipes=pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == 'S':
                return (i, j)
            
i, j = find_S()
# 17, 38 for main input.
start = (i, j) 
def tryPath(last, current):
    count = 0
    while current != start:
        last, current, err = getNext(last, current)
        if err == True:
            print(f'Found an Error: {count=}, {last=}, pipe={pipes[last[0]][last[1]]}')
            count = 0
            break
        count +=1
    return count
# current = (i-1, j)
# print(start, current)
# print(pipes[current[0]][current[1]])
# print(getNext(start, current))
count1 = tryPath(start, (i, j+1))
print(count1)
count2 = tryPath(start, (i, j-1))
print(count2)
count3 = tryPath(start, (i+1, j))
print(count3)
count4 = tryPath(start, (i-1, j))
print(count4)

endCount = max(count1, count2, count3, count4)

print(endCount//2 + 1)

# 6830 -- too low

