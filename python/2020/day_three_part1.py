filename = "inputs\\2020\\input-day3.txt"
with open(filename) as f:
    lines = f.readlines()

# Given slope
right = 3
down = 1

curPos = 0
treeCount = 0
# Go down the slope
for row in lines:
    if row[curPos % len(row.strip())] == "#":
        treeCount += 1
    curPos += right
print("Number of trees: " + str(treeCount))

