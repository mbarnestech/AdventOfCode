import re

springs = []
conditions = []
with open('12.Input.txt') as file:
    for line in file:
        springs.append("")
        conditions.append([])
        spring, points = line[:-1].split(' ')
        spring = spring.strip('.')
        for i in range(len(spring)):
            if i > 0 and spring[i] == '.' and spring[i-1] == '.':
                continue
            springs[-1] = springs[-1] + spring[i]
        # springs[-1] = '.' + springs[-1] + '.'
        data = points.split(',')
        for datum in data:
            conditions[-1].append(int(datum))

# def triangle(numQ, conditions, count):
#     if len(conditions) == 1:
#         total = numQ - (conditions[0] - 1)
#         count += total
#         return("", [], count)
#     else:
#         n = numQ - (sum(conditions)-1) - len(conditions)
#         print(numQ, conditions, n)
#         total = n+1
#         for _ in range(len(conditions)-1):
#             total += (n*(n+1))//2
#         count += total
#         return("", [], count)

def reduce(spring, conditions, count):
    removing = True
    while conditions and removing:
        removing = False
        # remove easy to diagnose rows with one option
        if sum(conditions) + len(conditions) - 1 == len(spring):
            print(f'row {i} removed on basic math: {sum(conditions)} + {len(conditions)} - 1 = {len(spring)}')
            spring = ''
            conditions = []
            count += 1

        # remove dead space from beginning
        elif '.' in spring[:conditions[0]]:
            print(f"removed {spring[:conditions[0]]} from {spring} as first condition is {conditions[0]}")
            spring = spring[spring.index('.')+1:]
            removing = True

        # remove dead space from end
        elif '.' in spring[-conditions[-1]:]:
            print(f"'.' in {spring[-conditions[-1]:]} of {spring} with final condition of {conditions[-1]}")
            while True:
                check = spring[-1]
                spring = spring[:-1]
                if check == '.':
                    break
            removing = True

        # remove first condition if fixed
        elif spring[0] == '#':
            print(f'hi {spring=}, {conditions[0]=}')
            spring = spring[conditions[0]+1:]
            conditions = conditions[1:]
            print(f'now {spring=}')
            removing = True

        # remove final condition if fixed
        elif spring[-1] == '#':
            print(f'removing {spring[-conditions[-1]-1:]} from {spring} to save {spring[:-conditions[-1]-1]}')
            spring = spring[:-conditions[-1]-1]
            conditions.pop()
            removing = True 
            
        # remove first ? if it must be a .
        elif len(spring) > conditions[0] and spring[0] == '?' and spring[conditions[0]] == '#':
            print(f'removing starting ? from {spring} as first condition is {conditions[0]}')
            spring = spring[1:]
            removing = True

        # remove final ? if it must be a .
        elif len(spring) > conditions[-1] and spring[-1] == '?' and spring[-(conditions[-1]+1)] == '#':
            print(f'removing final ? from {spring} as first condition is {conditions[-1]}')
            spring = spring[:-1]
            removing = True
        
        # elif set(char for char in spring) == {'?'}:
        #     spring, conditions, count = triangle(len(spring), conditions, count)
            
    return [spring, conditions, count]

def getCount(spring, conditions, count):
    # base case - 1 final condition (first conditions were 3,2,1, now we only have 1)
    if len(conditions) == 1:
        # check to see if there are (too many) broken springs; either break or reduce spring object
        if '#' in spring:
            print("'#' in spring")
            idx1 = spring.index('#')
            end = min(idx1+conditions[0]+1, len(spring)) 
            idx2 = idx1
            if '#' in spring[idx1+1:end]:
                for i in range(end-1, idx1, -1):
                    if spring[i] == '#':
                        idx2 = i
                        break
            start = max(idx2-conditions[0], 0)
            if end < len(spring) and '#' in spring[end:]:
                print(f'too many # in spring: num: {conditions[0]} for spring: {spring}')
                return count
            print(f'adjusting spring for # - old: {spring}, new: {spring[start:end]}')
            spring = spring[start:end]
        # for loop(over the whole spring at this point)
        for i in range(len(spring)-conditions[0]-1):
            if re.match(rf'(\.|\?){{1}}(\?|\#){{{conditions[0]}}}(\.|\?){{1}}', spring[i:i+conditions[0]+2]):
                count += 1
                print(f'yay this worked, count is now {count}; match at {spring[i:i+conditions[0]+2]} (i={i})')
            # for each place 1 can be, count += 1
        #return count
        return count
    # not base case - find first place where first condition is met, redo get count without that condition and spring removed
    else:
        # for loop - for range(0, stopping point for that particular condition)
        stop = len(spring)-len(conditions)-sum(conditions)
        if '#' in spring:
            stop = min(stop, spring.index('#')+1)
        print(f'{spring=}, {conditions=}, {stop=}')
        # check regex to see if that point has a match
        for i in range(stop):
            # re.match - looks for match starting only at first character, re.search looks throughout string
            if re.match(rf'(\.|\?){{1}}(\?|\#){{{conditions[0]}}}(\.|\?){{1}}', spring[i:i+conditions[0]+2]):
                # if yes, count = getCount(spring(after match point), conditions[1:], count)
                # print(f'first of {conditions} matched for spring {spring} at index {i}, section {spring[i:i+conditions[0]+2]}, new spring {spring[i+conditions[0]+1:]}')
                print(f'input check: count:{count}, spring:{spring[i+conditions[0]+1:]}, conditions: {conditions[1:]} ')
                count = getCount(spring[i+conditions[0]+1:], conditions[1:], count)
        # print(f'return count check(multiple conditions): count of {count}')
        return count
    
total = 0
high = []
for i in range(len(springs)):
# for i in range(900, 901):
    print(springs[i], conditions[i])

    # springs[i], conditions[i], count = reduce(springs[i], conditions[i], 0)
    
    if conditions[i]:
        springs[i] = '.' + springs[i] + '.'
        count = getCount(springs[i], conditions[i], 0)
    if count == 0:
        count = 1
    high.append(count)
    total += count
    print(f'total: {total}, count: {count} for {springs[i]} & {conditions[i]}')

print(f'{total=}')
print(max(high), high.index(max(high)), min(high), high.index(min(high)))