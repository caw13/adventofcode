
filename = "inputs\\2020\\input-day10.txt"
with open(filename) as f:
    lines = f.readlines()

# convert list of strings to list of ints
listNumbers = list(map(int, lines)) 

maxNum = max(listNumbers)
listNumbers.append(maxNum + 3)
listNumbers.sort()

joltDiff1 = 0
joltDiff3 = 0

curVoltage = 0
curIndex = 0
while curVoltage < (maxNum + 3):
    #print("curVoltage="+str(curVoltage)+" listRemaining:" + str(listNumbers[curIndex:]))
    if (listNumbers[curIndex] - curVoltage) == 1:
        joltDiff1 += 1
    elif (listNumbers[curIndex] - curVoltage) == 3:
        joltDiff3 += 1
    else:
        print("Shouldn't get here...")
    curVoltage = listNumbers[curIndex]
    curIndex += 1
    
print(str(joltDiff1) + "  " + str(joltDiff3))
print("Output:  " + str(joltDiff1 * joltDiff3))