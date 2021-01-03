def getTreeCount(right, down, map):
    curPos = 0
    treeCount = 0
    downCount = down
    # Go down the slope
    for row in lines:
        if (downCount == down):
            if row[curPos % len(row.strip())] == "#":
                treeCount += 1
            curPos += right
            downCount = 1
        else:
            downCount += 1
    return treeCount

filename = "inputs\\2020\\input-day3.txt"
with open(filename) as f:
    lines = f.readlines()

print("Number of trees: " + str(getTreeCount(1,1,lines)))
print("Number of trees: " + str(getTreeCount(3,1,lines)))
print("Number of trees: " + str(getTreeCount(5,1,lines)))
print("Number of trees: " + str(getTreeCount(7,1,lines)))
print("Number of trees: " + str(getTreeCount(1,2,lines)))
result = getTreeCount(1,1,lines)
result *= getTreeCount(3,1,lines)
result *= getTreeCount(5,1,lines)
result *= getTreeCount(7,1,lines)
result *= getTreeCount(1,2,lines)
print("Result " + str(result))