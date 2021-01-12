filename = "inputs\\2020\\input-day12.txt"
with open(filename) as f:
    lines = f.readlines()

direction = "0"
switcher = {"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
directionMap = {"0":"E", "90":"S","180":"W","270":"N"}
xPos = 0
yPos = 0

for line in lines:
    instruction = line[0]
    value = int(line[1:].strip())
    #print("line: "+line)
    if instruction == "L":
        direction = str((int(direction) - value) % 360)
    elif instruction == "R":
        direction = str((int(direction) + value) % 360)
    elif instruction == "F":
        northSouthDirection = directionMap[direction]    
        directionInfo = switcher[northSouthDirection]
        xPos += (value * directionInfo[0])
        yPos += (value * directionInfo[1])
    elif instruction in switcher:
        directionInfo = switcher[instruction]
        xPos += (value * directionInfo[0])
        yPos += (value * directionInfo[1])
    else:
        print("Shouldn't get here")
    #print("xpos:"+ str(xPos) + "  ypos:"+str(yPos))

print("mahattan distance: " + str(abs(xPos) + abs(yPos)))