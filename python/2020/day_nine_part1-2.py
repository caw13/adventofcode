# Recursively check to see if there is a combination that adds to the number match
def checkCurNum(listNumbers,numToMatch):
    #print("Num match: "+str(numToMatch)+ " list: "+str(listNumbers))
    if len(listNumbers) < 2:
        return False
    matchFound = False
    baseNum = listNumbers[0]
    for curNum in listNumbers[1:]:
        if (baseNum + curNum) == numToMatch:
            return True
    # No match found so keep going
    return checkCurNum(listNumbers[1:],numToMatch)

filename = "inputs\\2020\\input-day9.txt"
with open(filename) as f:
    lines = f.readlines()

# convert list of strings to list of ints
listNumbers = list(map(int, lines)) 

windowSize = 25
invalidNumber = 0

# Starting at curIndex check each number through the end of the list
for curIndex in range(windowSize,len(listNumbers)):
    matchFound = checkCurNum(listNumbers[curIndex-windowSize:curIndex+1],listNumbers[curIndex])
    if not matchFound:
        print("Number " + str(listNumbers[curIndex]) + " is invalid")
        invalidNumber = listNumbers[curIndex]

startIndex = 0
endIndex = 0

# Find contiguous range that adds to invalid number
for curIndex in range(len(listNumbers)):
    sum = listNumbers[curIndex]
    sumFound = False
    for secondIndex in range(curIndex+1, len(listNumbers)):
        sum += listNumbers[secondIndex]
        if sum == invalidNumber:
            startIndex = curIndex
            endIndex = secondIndex
            sumFound = True
            break
        elif sum > invalidNumber:
            break
    if sumFound:
        break

print("Match list: " + str(listNumbers[startIndex:endIndex+1]))
minNum = min(listNumbers[startIndex:endIndex+1])
maxNum = max(listNumbers[startIndex:endIndex+1])
print("Weakness: " + str(minNum + maxNum))
