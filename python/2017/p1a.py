filename = "p1-input.txt"
with open(filename) as f:
    line = f.readline()
#line = input("Enter line: ")
sum = 0
index = 0
for index in range(0,len(line)):
    curNum = line[index]
    if (index+1)<len(line):
        nextNum = line[index+1]
    else:
        nextNum = line[0]
    if curNum == nextNum:
        sum += int(curNum)
print("line: "+line)
print("sum: %d"%sum)
