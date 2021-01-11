# returns if any seat changes occured and the updated seat map
def applyRules(seatMap):
    updatedSeatMap = seatMap.copy()
    seatsChanged = False
    adjacencyMatrix = createAdjacencyMatrix(seatMap)
    #outputMatrix(seatMap)
    #outputMatrix(adjacencyMatrix)
    for row in range(len(seatMap)):
        for col in range(len(seatMap[0])):
            if seatMap[row][col] == "L" and adjacencyMatrix[row][col] == 0:
                updatedSeatMap[row][col] = "#"
                seatsChanged = True
            elif seatMap[row][col] == "#" and adjacencyMatrix[row][col] >= 5:
                updatedSeatMap[row][col] = "L"
                seatsChanged = True
    return [seatsChanged,updatedSeatMap]

def countAdjacencies(seatCol, seatRow, seatMap):
    numAdjacent = 0
    for rowIncrement in range(-1,2,1):
        for colIncrement in range(-1,2,1):
            if not (rowIncrement == 0 and colIncrement == 0):
                numAdjacent += numInSightLine(seatCol,seatRow,seatMap,colIncrement,rowIncrement)
    return numAdjacent

# Check sight line recursively until either empty or occupied seen
def numInSightLine(seatCol, seatRow, seatMap, colIncrement, rowIncrement):
    #print(str(seatCol) +" " + str(seatRow) +" " + str(colIncrement) +" " + str(rowIncrement))
    if (colIncrement + seatCol) < 0 or ((colIncrement + seatCol) > len(seatMap[0]) -1) or ((rowIncrement + seatRow) < 0 or ((rowIncrement + seatRow) > len(seatMap) -1)):
       return 0
    elif seatMap[seatRow + rowIncrement][seatCol + colIncrement] == "#":
        return 1
    elif seatMap[seatRow + rowIncrement][seatCol + colIncrement] == "L":   
        return 0
    else:
        return numInSightLine(seatCol + colIncrement, seatRow + rowIncrement, seatMap, colIncrement, rowIncrement) 
  
        
def createAdjacencyMatrix(seatMap):
    adjMatrix = [[0 for col in range(len(seatMap[0]))] for row in range(len(seatMap))] 
    for row in range(len(seatMap)):
        for col in range(len(seatMap[0])):
            adjMatrix[row][col] = countAdjacencies(col,row,seatMap)
    return adjMatrix

def outputMatrix(passedMatrix):
    for i in range(len(passedMatrix)) :  
        for j in range(len(passedMatrix[i])) :  
            print(passedMatrix[i][j], end=" ") 
        print()

def getNumOccupied(seatMap):
    numOccupied = 0
    for row in range(len(seatMap)):
        for col in range(len(seatMap[0])):
            if seatMap[row][col] == "#":
                numOccupied += 1
    return numOccupied

filename = "inputs\\2020\\input-day11.txt"
with open(filename) as f:
    lines = f.readlines()

seatMap = []
for line in lines:
    seatMap.append(list(line))

rounds = 0
currentSeatMap = seatMap.copy()
state = [True,currentSeatMap]

while state[0]:
    rounds += 1
    state = applyRules(currentSeatMap)
    currentSeatMap = state[1]
    #outputMatrix(currentSeatMap)
    #if (rounds == 2):
    #    break

print("Number of rounds: " + str(rounds))
print("Number occupied: " + str(getNumOccupied(currentSeatMap)))