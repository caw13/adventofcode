filename = "inputs\\2020\\input-day12.txt"
with open(filename) as f:
    lines = f.readlines()

direction = "0"
switcher = {"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
directionMap = {"0":"E", "90":"S","180":"W","270":"N"}
shipXPos = 0
shipYPos = 0
waypointRelXPos = 10
waypointRelYPos = 1

for line in lines:
    instruction = line[0]
    value = int(line[1:].strip())
    #print("line: "+line)
    if instruction == "L":
        if value == 90:
            prevYPos = waypointRelYPos
            waypointRelYPos = waypointRelXPos
            waypointRelXPos = prevYPos * -1
        elif value == 180:
            waypointRelXPos = waypointRelXPos * -1
            waypointRelYPos = waypointRelYPos * -1
        elif value == 270:
            prevYPos = waypointRelYPos
            waypointRelYPos = waypointRelXPos * -1
            waypointRelXPos = prevYPos
    elif instruction == "R":
        if value == 90:
            prevYPos = waypointRelYPos
            waypointRelYPos = waypointRelXPos * -1
            waypointRelXPos = prevYPos
        elif value == 180:
            waypointRelXPos = waypointRelXPos * -1
            waypointRelYPos = waypointRelYPos * -1
        elif value == 270:
            prevYPos = waypointRelYPos
            waypointRelYPos = waypointRelXPos
            waypointRelXPos = prevYPos * -1
    elif instruction == "F":
        shipXPos += (value * waypointRelXPos)
        shipYPos += (value * waypointRelYPos)
    elif instruction in switcher:
        directionInfo = switcher[instruction]
        waypointRelXPos += (value * directionInfo[0])
        waypointRelYPos += (value * directionInfo[1])
    else:
        print("Shouldn't get here")
    #print("xpos:"+ str(xPos) + "  ypos:"+str(yPos))

print("mahattan distance: " + str(abs(shipXPos) + abs(shipYPos)))