from collections import deque

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

def sendBroadcast(signal, order=order, ffStatus=ffStatus, conStatus=conStatus):
    low = 0
    high = 0
    if signal == 'low':
            low += 1
    elif signal == 'high':
        high += 1
    queue = deque()
    for destination in order['broadcaster']:
        queue.append(['broadcaster', destination, signal])
    while queue:
        # print(queue)
        origin, module, signal = queue.popleft()
        if signal == 'low':
            low += 1
        elif signal == 'high':
            high += 1
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
                else:
                    print('something went wrong, signal is not low or high')
            if conStatus[module][0] == 0:
                for mod in order[module]:
                    queue.append([module, mod, 'low'])
            else:
                for mod in order[module]:
                    queue.append([module, mod, 'high'])
    return low, high



sumLow = 0
sumHigh = 0
for _ in range(1000):
    low, high = sendBroadcast('low')
    sumLow += low
    sumHigh += high
print(sumLow, sumHigh)
print(sumLow*sumHigh)
