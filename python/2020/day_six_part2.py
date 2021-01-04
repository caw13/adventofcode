def getPersonSet(line):
    #print("Line "+line)
    curSet = set(())
    for curChar in line:
        curSet.add(curChar)
    #print("Set: "+str(curSet))
    return curSet

filename = "inputs\\2020\\input-day6.txt"
with open(filename) as f:
    lines = f.readlines()

group = None
sum = 0
for line in lines:
    if len(line.strip()) == 0:
        sum += len(group)
        group = None
    else:
        curSet = getPersonSet(line.strip())
        if group == None:
            group = curSet
        else:
            group = group.intersection(curSet)
 
curSet = getPersonSet(line.strip())
if group == None:
    group = curSet
else:
    group = group.intersection(curSet)
sum += len(group)
print("Sum: "+str(sum))