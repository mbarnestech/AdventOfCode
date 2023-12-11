sum = 0
with open('9.Input.txt') as file:
    for line in file:
        elements = [int(num) for num in line.split(' ')]
        history = [elements]
        while set(history[-1]) != {0}:
            history.append([])
            for i in range(1, len(history[-2])):
                history[-1].append(history[-2][i]-history[-2][i-1])
        history[-1].append(0)
        for i in range(len(history)-2, -1, -1):
            history[i].append(history[i][-1] + history[i+1][-1])
        sum += history[0][-1]
print(sum)