workflow = {'A':'A', 'R':'R'}
parts = []

input = 0
with open('19.Input.txt') as file:
    for line in file:
        if input == 0 and len(line) > 2:
            name, info = line[:-2].split('{')
            # info = info[:-1].split(',')
            workflow[name] = info.split(',')
        elif input == 0:
            input += 1
        else:
            parts.append([])
            specs = line[1:-2].split(',')
            for spec in specs:
                cat, rating = spec.split('=')
                parts[-1].append([cat, int(rating)])

# print(workflow, parts)

def runWorkflow(part, workflow=workflow):
    rating = 0
    status = None
    wf = 'in'

    while not status:
        for flow in workflow[wf]:
            wfChanged = False
            # print(workflow[wf])
            if flow[0] == 'R':
                status = 'R'
                break
            elif flow[0] == 'A':
                # print("i'm an A")
                status = 'A'
                for spec in part:
                    rating += spec[1]
                break
            elif ':' not in flow:
                wf = flow
            else:
                parts = flow.split(':')
                # print(parts)
                letter = parts[0][0]
                sign = parts[0][1]
                val = int(parts[0][2:])
                nwf = parts[1]
                # print(nwf)
                for spec in part:
                    # print(f'spec check: {spec}')
                    if spec[0] == letter:
                        # print(f'letter spec check: {letter} {spec[0]}, val check: {val} {spec[1]} ')
                        if sign == '<':
                            if spec[1] < val:
                                # print("check <")
                                wf = nwf
                                wfChanged = True
                                break
                        elif sign == '>':
                            # print("check >")
                            if spec[1] > val:
                                wf = nwf
                                wfChanged = True
                                break
                if wfChanged == True:
                    break

    return [status, rating]

total = 0
for part in parts:
    # print(part)
    status, rating = runWorkflow(part)
    # print(status, rating)
    total += rating

print(total)