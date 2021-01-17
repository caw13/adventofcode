def findPositions(numSpoken, numsSpoken):
    mostRecent = -1
    mostRecentFound = False
    for index in range(len(numsSpoken)-1,-1,-1):
        if numsSpoken[index] == numSpoken and not mostRecentFound:
            mostRecentFound = True
            mostRecent = index
        elif numsSpoken[index] == numSpoken and mostRecentFound:
            returnPositions = [mostRecent, index]
            return returnPositions
    return [mostRecent, -1]
    

filename = "inputs\\2020\\input-day15.txt"
with open(filename) as f:
    lines = f.readlines()

numsSpoken = []
numSpoken = ""
startingNums = lines[0].strip().split(",")
for index in range(len(startingNums)):
    numSpoken = startingNums[index]
    numsSpoken.append(numSpoken)
    print(str(numSpoken))
print(str(numsSpoken))


for index in range(len(startingNums),2020):
    positions = findPositions(numSpoken,numsSpoken)
    if positions[1] == -1:
        numSpoken = "0"
    else:
        numSpoken = str(int(positions[0]) - int(positions[1]))
    numsSpoken.append(numSpoken)
    #print("Num spoken: " +str(numSpoken) +" curStatus: " + str(numsSpoken))
print("Num spoken: " + numSpoken)