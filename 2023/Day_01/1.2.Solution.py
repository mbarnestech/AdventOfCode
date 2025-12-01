import re

sum = 0
numDict = {"one": 1, 
           "two": 2, 
           "three": 3, 
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7, 
           "eight": 8,
           "nine": 9,
           "1": 1, 
           "2": 2, 
           "3": 3, 
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7, 
           "8": 8,
           "9": 9}
with open("1.1.Input.txt", "r") as file:
    with open("1.2.Output.txt", "a") as newFile:
        for line in file:
            num = 0
            for i in range(len(line)):
                m = re.match(r"\d|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)", line[i:])
                if m:
                    num += numDict[m.group(0)]*10
                    break
            for i in range(len(line)-1, -1, -1):
                m = re.match(r"\d|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)", line[i:])
                if m:
                    num += numDict[m.group(0)]
                    break
            sum += num
            newFile.write(f"{line}: num: {num}, sum: {sum} \n")
print(sum)