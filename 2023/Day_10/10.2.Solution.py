pipes = []

with open('10.2.PaddedInput.txt') as file:
    for line in file:
        pipes.append([])
        for char in line[:-1]:
            pipes[-1].append(char)

pipes2 = []
for line in pipes:
    pipes2.append([])
    for char in line:
        pipes2[-1].append(char)

# last & current = (row, column)
def getNext(last, current):
    err = None
    next = None
    pipe = pipes[current[0]][current[1]]
    if pipe == '|':
        if last[0] > current[0]:
            next = (current[0]-2, current[1])
            pipes[current[0]-1][current[1]] = 'P'
            pipes2[current[0]-1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[0] < current[0]:
            next = (current[0]+2, current[1])
            pipes[current[0]+1][current[1]] = 'P'
            pipes2[current[0]+1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        else:
            err = True
    elif pipe == '-':
        if last[1] > current[1]:
            next = (current[0], current[1]-2)
            pipes[current[0]][current[1]-1] = 'P'
            pipes2[current[0]][current[1]-1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[1] < current[1]:
            next = (current[0], current[1]+2)
            pipes[current[0]][current[1]+1] = 'P'
            pipes2[current[0]][current[1]+1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
    elif pipe == 'L':
        if last[0] < current[0]:
            next = (current[0], current[1]+2)
            pipes[current[0]][current[1]+1] = 'P'
            pipes2[current[0]][current[1]+1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[1] > current[1]:
            next = (current[0]-2, current[1])
            pipes[current[0]-1][current[1]] = 'P'
            pipes2[current[0]-1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        else:
            err = True
    elif pipe == 'J':
        if last[0] < current[0]:
            next = (current[0], current[1]-2)
            pipes[current[0]][current[1]-1] = 'P'
            pipes2[current[0]][current[1]-1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[1] < current[1]:
            next = (current[0]-2, current[1])
            pipes[current[0]-1][current[1]] = 'P'
            pipes2[current[0]-1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        else:
            err = True
    elif pipe == '7':
        if last[1] < current[1]:
            next = (current[0]+2, current[1])
            pipes[current[0]+1][current[1]] = 'P'
            pipes2[current[0]+1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[0] > current[0]:
            next = (current[0], current[1]-2)
            pipes[current[0]][current[1]-1] = 'P'
            pipes2[current[0]][current[1]-1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        else:
            err = True
    elif pipe == 'F':
        if last[1] > current[1]:
            next = (current[0]+2, current[1])
            pipes[current[0]+1][current[1]] = 'P'
            pipes2[current[0]+1][current[1]] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        elif last[0] > current[0]:
            next = (current[0], current[1]+2)
            pipes[current[0]][current[1]+1] = 'P'
            pipes2[current[0]][current[1]+1] = 'P'
            pipes[current[0]][current[1]] = 'P'
            pipes2[current[0]][current[1]] = 'P'
        else:
            err = True
    elif pipe == '.' or pipe == '#':
        err = True
    elif pipe == 'P':
        pipes[current[0]][current[1]] = 'P'
        pipes2[current[0]][current[1]] = 'P'
        next = current
    return current, next, err
    
def find_S(pipes=pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == 'S':
                return (i, j)
            
i, j = find_S()
print(i,j, pipes[i][j], pipes2[i][j])

start = (i, j) 
last = start
current = (i, j+2)
pipes[i][j:j+2] = ['P']*2
pipes2[i][j:j+2] = ['P']*2
while current != start:
    last, current, err = getNext(last, current)
    if err == True:
        print(f'Found an Error: {count=}, {last=}, pipe={pipes[last[0]][last[1]]}')
        break
for i in range(1, len(pipes2)-1):
    for j in range(1, len(pipes2[i])-1):
        if pipes2[i][j] != 'P':
            pipes2[i][j] = '.'
pipes2[-1] = ['#']*281
change = True
while change:
    change = False
    for i in range(len(pipes2)-1):
        for j in range(len(pipes2[1])-1):
            if pipes2[i][j] != 'P' and pipes2[i][j] != '#':
                if pipes2[i-1][j] == '#' or pipes2[i][j-1] == '#' or pipes2[i+1][j] == '#' or pipes2[i][j+1] == '#':
                    change = True
                    pipes2[i][j] = '#'



count = 0

for i in range(1, len(pipes2), 2):
    for j in range(1, len(pipes2[i]), 2):
        if pipes2[i][j] == '.':
            count += 1

print(count)


open('10.2.Pipes.txt', 'w').close()

with open('10.2.Pipes.txt', 'a') as file:
    for line in pipes2:
        file.write(f'{"".join(line)}\n')

