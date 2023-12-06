sum = 0
with open("1.1.Input.txt", "r") as file:
    for line in file:
        first = ""
        last = ""
        for char in line:
            if char in "0123456789":
                first = char
                break
        for char in line[::-1]:
            if char in "0123456789":
                last = char
                break
        sum += int(first+last)

print(sum)