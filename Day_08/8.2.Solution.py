import re
from math import lcm

nodes = {}
with open('8.Nodes.txt') as file:
    for line in file:
        node, left, right = re.findall(r'[A-Z]{3}', line)
        nodes[node] = [left, right]

instructions = ''
with open('8.Instructions.txt') as file:
    for line in file:
        instructions = line

count = 0
totalCount = 0
current = []
for node in nodes:
    if node[2] == 'A':
        current.append(node)

nums = []
for node in current:
    currentNode = node
    count = 0
    totalCount = 0
    while True:
        if instructions[count] == 'L':
            currentNode = nodes[currentNode][0]
        elif instructions[count] == 'R':
            currentNode = nodes[currentNode][1]
        totalCount += 1
        if currentNode[2] == 'Z':
            nums.append(totalCount)
            break
        count += 1
        if count == len(instructions):
            count = 0
        if count == 0 and currentNode == node:
            break

print(lcm(*nums))

