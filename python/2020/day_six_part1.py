def getGroupCount(line):
    #print("Line "+line)
    curSet = set(())
    for curChar in line:
        curSet.add(curChar)
    #print("Set: "+str(curSet))
    return len(curSet)

filename = "inputs\\2020\\input-day6.txt"
with open(filename) as f:
    lines = f.readlines()

group = ""
sum = 0
for line in lines:
    if len(line.strip()) == 0:
        sum += getGroupCount(group.strip())
        group = ""
    else:
        group += line.strip()
sum += getGroupCount(group.strip())
print("Sum: "+str(sum))