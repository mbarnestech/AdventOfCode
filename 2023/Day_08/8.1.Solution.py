import re

# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#     def PrintTree(self):
#         print(f'{self.data=}')

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
current = 'AAA'

while True:
    print(f'{totalCount=}, {count=}, {instructions[count]=},{current=}, {nodes[current]=} ')
    if instructions[count] == 'L':
        current = nodes[current][0]
    elif instructions[count] == 'R':
        current = nodes[current][1]
    totalCount += 1
    if current == 'ZZZ':
        print(f'{totalCount=}')
        break
    count += 1
    if count == len(instructions):
        count = 0