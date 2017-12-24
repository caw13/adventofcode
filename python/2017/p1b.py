filename = "p1-input.txt"
with open(filename) as f:
    line = f.readline()
line = input("Enter line: ")
halfDist = len(line)/2
sum = 0
index = 0
for index in range(0,len(line)):
    curNum = line[index]
    nextNum = line[int((index+halfDist)%len(line))]
    if curNum == nextNum:
        sum += int(curNum)
print("line: "+line)
print("sum: %d"%sum)
