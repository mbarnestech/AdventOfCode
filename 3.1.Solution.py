engine = []
with open("3.1.Input.txt") as file:
    for line in file:
        engine.append(f".{line[:-1]}.\n")

engine.insert(0,f"{'.'*(len(engine[1])-1)}\n")
engine.append('.'*(len(engine[0])-1))

# with open("3.1.Output.txt", "a") as file:
#     for line in engine:
#         file.write(line)

check = [['.']*len(engine[0]), ['.']*len(engine[0])]

# with open("3.1.check.txt", "a") as file:
#     for line in check:
#         file.write(f'{(line)}\n')
#     file.write('\n')
for i in range(1, len(engine)-2):
    check.append(['.']*len(engine[0]))
    for j in range(1, len(engine[i])-2):
        if engine[i][j] in '1234567890.':
            continue
        else:
            # print(i, j, engine[i][j], check[i][j])
            check[(i-1)][(j+1)] = True
            check[(i-1)][(j)] = True
            check[(i-1)][(j-1)] = True
            check[i][j+1] = True
            check[i][j] = engine[i][j]
            check[i][(j-1)] = True
            check[(i+1)][(j+1)] = True
            check[(i+1)][(j)] = True
            check[(i+1)][(j-1)] = True



open("3.1.check.txt", "w").close()
with open("3.1.check.txt", "a") as file:
    for line in check:
        file.write(f'{(line)}\n')

total = 0

for i in range(1, len(engine)-1):
    num = ''
    counts = False
    for j in range(1, len(engine[i])-1):
        if engine[i][j].isdigit():
            num = num+engine[i][j]
            if check[i][j] == True:
                counts = True
        else:
            if num and counts == True:
                total += int(num)
            num = ''
            counts = False

print(total)






