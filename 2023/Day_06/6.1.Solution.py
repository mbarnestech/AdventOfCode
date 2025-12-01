import re

time = []
distance = []
count = 0
with open('6.Input.txt') as file:
    for line in file:
        elements = [int(num) for num in re.findall(r'\d+', line)]
        if count == 0:
            time = elements
            count += 1
        if count == 1:
            distance = elements

print(f'{time=}\n{distance=}')


total = 1
for i in range(len(time)):
    count = 0
    for j in range(1, time[i]):
        if (time[i]-j)*j > distance[i]:
            count += 1
    total *= count

print(f'{total=}')