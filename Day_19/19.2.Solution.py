workflow = {'A':'A', 'R':'R'}

with open('19.SampleInput.txt') as file:
    for line in file:
        if len(line) > 2:
            name, info = line[:-2].split('{')
            workflow[name] = info.split(',')
        else:
            break

xmas = {'x':[1,4000],
        'm':[1,4000],
        'a':[1,4000],
        's':[1,4000]
        }

total = 0

def runWorkflow(wf, xmas, total, workflow=workflow):
    
    for flow in workflow[wf]:
        print(xmas)
        newXmas = {}
        for letter, nums in xmas.items():
            newXmas[letter] = nums
        print(f'new workflow: {flow} in {workflow[wf]} for {wf} with xmas of {newXmas}')
        if flow == 'R' or flow[0] == 'R':
            return total
        elif flow == 'A' or flow[0] == 'A':
            # print("i'm an A")
            # print(newXmas)
            total += (newXmas['x'][1] - newXmas['x'][0]+1)*(newXmas['m'][1] - newXmas['m'][0]+1)*(newXmas['a'][1] - newXmas['a'][0]+1)*(newXmas['s'][1] - newXmas['s'][0]+1)
            return total
        elif ':' not in flow:
            total = runWorkflow(flow, newXmas, total)
        else:
            parts = flow.split(':')
            # print(parts)
            letter = parts[0][0]
            sign = parts[0][1]
            val = int(parts[0][2:])
            nwf = parts[1]
            # print(nwf)
            if sign == '<':
                if newXmas[letter][1] >= val:
                    newXmas[letter][1] = val-1
                elif newXmas[letter][0] < val:
                    newXmas[letter][0] = val
            elif sign == '>':
                if newXmas[letter][0] <= val:
                    newXmas[letter][0] = val+1
                elif newXmas[letter][1] > val:
                    newXmas[letter][1] = val
            total = runWorkflow(nwf, newXmas, total)
    return total


hmm = runWorkflow('in', xmas, total)
print(hmm)

6473186580628
167409079868000