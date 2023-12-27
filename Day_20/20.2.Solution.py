from collections import deque
from math import lcm

order = {}
ffStatus = {}
conStatus = {}

with open('20.Input.txt') as file:
    for line in file:
        elements = line[:-1].split(' -> ')
        destinations = elements[1].split(', ')
        type = elements[0][0]
        if type != 'b':
            name = elements[0][1:]
        else:
            name = elements[0]
        order[name] = destinations
        if type == '%':
            ffStatus[name] = 'off'
        if type == '&':
            conStatus[name] = [0, {}]

for conModule in conStatus:
    for switch, destinations in order.items():
        if conModule in destinations:
            conStatus[conModule][1][switch] = 'low'
    conStatus[conModule][0] = len(conStatus[conModule][1])

multiples = {}
def sendBroadcast(order=order, ffStatus=ffStatus, conStatus=conStatus):
    status = False
    substatus = False
    queue = deque()
    for destination in order['broadcaster']:
        queue.append(['broadcaster', destination, 'low'])
    while queue:
        # print(queue)
        origin, module, signal = queue.popleft()
        if module == 'rx' and signal == 'low':
            print('yayyyyy')
            status = True
        if module in ffStatus and signal == 'low':
            if ffStatus[module] == 'off':
                ffStatus[module] = 'on'
                for mod in order[module]:
                    queue.append([module, mod, 'high'])
            elif ffStatus[module] == 'on':
                ffStatus[module] = 'off'
                for mod in order[module]:
                    queue.append([module, mod, 'low'])
        elif module in conStatus:
            if signal != conStatus[module][1][origin]:
                conStatus[module][1][origin] = signal
                if signal == 'low':
                    conStatus[module][0] += 1
                elif signal == 'high':
                    conStatus[module][0] -= 1
                    if module == 'rs':
                        print(origin, conStatus[module][1][origin])
                        if origin not in multiples:
                            substatus = origin
                else:
                    print('something went wrong, signal is not low or high')
            if conStatus[module][0] == 0:
                for mod in order[module]:
                    queue.append([module, mod, 'low'])
            else:
                for mod in order[module]:
                    queue.append([module, mod, 'high'])
    return status, substatus

count = 1
interval = 10000
def checkRX(count, interval):
    for i in range(count, count + interval):
        status, substatus = sendBroadcast()
        if status == True:
            print(f'woohoo: {i}')
            return i
        if substatus:
            multiples[substatus] = i
        if len(multiples) == len(conStatus['rs'][1]):
            print(f'answer = {lcm(*[num for num in multiples.values()])}')
            break
    return count + interval

newCount = checkRX(count, interval)
print('the end')
