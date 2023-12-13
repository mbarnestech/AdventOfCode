import re

maps = []
conditions = []
count = []
with open('12.NewTests.txt') as file:
    for line in file:
        maps.append("")
        conditions.append([])
        count.append(0)
        map, points = line[:-1].split(' ')
        map = map.strip('.')
        for i in range(len(map)):
            if i > 0 and map[i] == '.' and map[i-1] == '.':
                continue
            maps[-1] = maps[-1] + map[i]
        data = points.split(',')
        for datum in data:
            conditions[-1].append(int(datum))

def getCount(count, map, conditions):
    if len(conditions) == 1:
        # print(f'final condition: {conditions[0]} for map {map}')
        if '#' in map:
            idx1 = map.index('#')
            end = min(idx1+conditions[0]+1, len(map)) 
            idx2 = idx1
            if '#' in map[idx1+1:end]:
                for i in range(end-1, idx1, -1):
                    if map[i] == '#':
                        idx2 = i
                        break
            start = max(idx2-conditions[0], 0)
            if end < len(map) and '#' in map[end:]:
                print(f'too many # in map: num: {conditions[0]} for map: {map}')
                return count
            print(f'adjusting map for # - old: {map}, new: {map[start:end]}')
            map = map[start:end]
        for i in range(len(map)-conditions[0]-1):
            if re.match(rf'(\.|\?){{1}}(\?|\#){{{conditions[0]}}}(\.|\?){{1}}', map[i:i+conditions[0]+2]):
                count +=1
                print(f'count matched for {map[i:i+conditions[0]+2]} (i={i}): count at {count}')
        # print(f'return count check(final condition): count of {count}')
        return count
    else:
        stop = len(map)-len(conditions)-sum(conditions)
        print(f'{map=}, {conditions=}, {stop=}')
        for i in range(stop):
            if re.match(rf'(\.|\?){{1}}(\?|\#){{{conditions[0]}}}(\.|\?){{1}}', map[i:i+conditions[0]+2]):
                print(f'first of {conditions} matched for map {map} at index {i}, section {map[i:i+conditions[0]+2]}, new map {map[i+conditions[0]+1:]}')
                print(f'input check: count:{count}, map:{map[i+conditions[0]+1:]}, conditions: {conditions[1:]} ')
                count = getCount(count, map[i+conditions[0]+1:], conditions[1:])
        print(f'return count check(multiple conditions): count of {count}')
        return count


for i in range(len(maps)):
# for i in range(40, 41):
    print(f'{i=}, {maps[i]=}, {len(maps[i])=}, {conditions[i]=}, {count[i]=}')

    removing = True
    while conditions[i] and removing:
        removing = False
        # remove easy to diagnose rows with one option
        if sum(conditions[i]) + len(conditions[i]) - 1 == len(maps[i]):
            print(f'row {i} removed on basic math: {sum(conditions[i])} + {len(conditions[i])} - 1 = {len(maps[i])}')
            maps[i] = ''
            conditions[i] = []
            count[i] = 1
            

        # remove dead space from end
        elif '.' in maps[i][-conditions[i][-1]:]:
            print(f"'.' in {maps[i][-conditions[i][-1]:]} of {maps[i][-conditions[i][-1]:]} with count of {conditions[i][-1]}")
            while True:
                check = maps[i][-1]
                maps[i] = maps[i][:-1]
                if check == '.':
                    break
            removing = True
        
        # remove final condition if fixed
        elif maps[i][-1] == '#':
            print(f'removing {maps[i][-conditions[i][-1]-1:]} from {maps[i]} to save {maps[i][:-conditions[i][-1]-1]}')
            maps[i] = maps[i][:-conditions[i][-1]-1]
            conditions[i].pop()
            removing = True 
            print(maps[i])

        # remove dead space from beginning
        elif '.' in maps[i][:conditions[i][0]]:
            print(maps[i][:conditions[i][0]], conditions[i][0])
            maps[i] = maps[i][maps[i].index('.')+1:]
            removing = True
        
        # remove first condition if fixed
        elif maps[i][0] == '#':
            print(f'hi {maps[i]=}, {conditions[i][0]=}')
            maps[i] = maps[i][conditions[i][0]+1:]
            conditions[i] = conditions[i][1:]
            print(f'now {maps[i]=}')
            removing = True
        
        #remove first ? if it must be a .
        elif len(maps[i]) > conditions[i][0] and maps[i][0] == '?' and maps[i][conditions[i][0]] == '#':
            print(f'removing starting ? ({maps[i][0]=}, {conditions[i][0]=}, {maps[i][conditions[i][0]]=})')
            maps[i] = maps[i][1:]
            removing = True
    
        # split if each condition is separate
        elif '.' in maps[i] and maps[i].count('.') == len(conditions[i]) - 1:
            parts = maps[i].split('.')
            print(f'{parts=}, {conditions[i]=}')
            total = 1
            for j in range(len(parts)):
                total *= len(parts[j]) - (conditions[i][j] - 1)
            conditions[i] = []
            maps[i] = ''
            count[i] = total
            break

        # if all chars are ?
        elif set(char for char in maps[i]) == {'?'}:
            # if len(conditions[i]) == 2:
            #     n = len(maps[i]) - (conditions[i][0] + 1)
            #     # print(f'{maps[i]=}, {conditions[i]=}')
            #     total = (n * (n+1)) // 2
            #     count[i] = total
            #     maps[i] = ''
            #     conditions[i] = []
            #     break
            # elif len(conditions[i]) == 1:
            #     # print(f'{maps[i]=}, {conditions[i]=}')
            #     total = len(maps[i]) - (conditions[i][0] - 1)
            #     count[i] = total
            #     maps[i] = ''
            #     conditions[i] = []
            #     break
            startNum = len(maps[i]) - sum(conditions[i])
            print(f'testing: map is {maps[i]}, length {len(maps[i])}, conditions are {conditions[i]}, sum {sum(conditions[i])}, length {len(conditions[i])}, startNum is {startNum}')
            total = 0
            for num in range(1, len(conditions[i])):
                n = startNum - num
                total += (n * (n+1)) // 2
                print(n, total)
            count[i] = total
            maps[i] = ''
            conditions[i] = []

    if conditions[i]:
        # print(f'going into getCount with {len(conditions[i])} conditions and map {maps[i]}')
        maps[i] = "." + maps[i] + "."
        count[i] = getCount(count[i], maps[i], conditions[i])
        maps[i] = ''
        conditions[i] = []

    if not count[i]:
        count[i] = 1
    print(f'******{i=}, {maps[i]=}, {conditions[i]=}, {count[i]=}*****')


        
total = sum(count)
print(total)

# 8690 - Too high
# 8172 - incorrect