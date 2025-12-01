import re

input = []
with open('6.Input.txt') as file:
    for line in file:
        elements = int("".join([num for num in re.findall(r'\d+', line)]))
        input.append(elements)


print(f'{input=}')


count = 0
started = False
for i in range(1, input[0]):
    if started == True:
        if (input[0]-i)*i > input[1]:
            count += 1
        if (input[0]-i)*i <= input[1]:
            break
    elif (input[0]-i)*i > input[1]:
        count += 1 
        started = True

print(f'{count=}')