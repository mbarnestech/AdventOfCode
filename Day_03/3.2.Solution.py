from collections import defaultdict

engine = []
with open("3.1.Input.txt") as file:
    for line in file:
        engine.append(f".{line[:-1]}.\n")

engine.insert(0,f"{'.'*(len(engine[1])-1)}\n")
engine.append('.'*(len(engine[0])-1))

check = [['.']*len(engine[0]), ['.']*len(engine[0]), ['.']*len(engine[0])]

starNo = 0
starDict = {'symbol': []}
for i in range(1, len(engine)-2):
    check.append(['.']*len(engine[0]))
    for j in range(1, len(engine[i])-2):
        if engine[i][j] in '1234567890.':
            continue
        elif engine[i][j] == '*':
            check[i][j] = f'star_{starNo}'
            starDict[f'star_{starNo}'] = []
            starNo += 1
        else: 
            check[i][j] = 'symbol'




open("3.2.check.txt", "w").close()
with open("3.2.check.txt", "a") as file:
    for line in check:
        file.write(f'{(line)}\n')

for i in range(1, len(engine)-1):
    num = ''
    start = 0
    end = 0
    for j in range(1, len(engine[i])-1):
        if engine[i][j].isdigit():
            num = num+engine[i][j]
            if not engine[i][j-1].isdigit():
                start = j
            if not engine[i][j+1].isdigit():
                end = j
        else:
            if num:
                for k in [i-1, i, i+1]:
                    for l in range(start-1, end+2):
                        # print(k,l,engine[k][l], num)
                        if check[k][l] != '.':
                            starDict[check[k][l]].append(int(num))
            num = ''

total = 0
for symbol, nums in starDict.items():
    # print(symbol, nums)
    if symbol == 'symbol' or len(nums) != 2:
        # for num in nums:
        #     total += num
        continue
    else:
        # print("I'm an else!")
        total += nums[0]*nums[1]
print(total)






