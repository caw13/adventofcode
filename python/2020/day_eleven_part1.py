# returns if any seat changes occured and the updated seat map
def applyRules(seatMap):
    updatedSeatMap = seatMap.copy()
    seatsChanged = False
    adjacencyMatrix = createAdjacencyMatrix(seatMap)
#    outputMatrix(seatMap)
#    outputMatrix(adjacencyMatrix)
    for row in range(len(seatMap)):
        for col in range(len(seatMap[0])):
            if seatMap[row][col] == "L" and adjacencyMatrix[row][col] == 0:
                updatedSeatMap[row][col] = "#"
                seatsChanged = True
            elif seatMap[row][col] == "#" and adjacencyMatrix[row][col] >= 4:
                updatedSeatMap[row][col] = "L"
                seatsChanged = True
    return [seatsChanged,updatedSeatMap]

def countRowAdjacencies(seatCol, seatRow, seatMap, includeGiven):
    numAdjacent = 0
    if seatCol > 0 and seatMap[seatRow][seatCol-1] == "#":
        numAdjacent += 1
    if seatMap[seatRow][seatCol] == "#" and includeGiven:
        numAdjacent += 1
    if seatCol < (len(seatMap[seatRow])-1) and seatMap[seatRow][seatCol+1] == "#":
        numAdjacent += 1
    return numAdjacent

def countAdjacencies(seatCol, seatRow, seatMap):
    #print(str(seatCol) +"   " + str(seatRow) + "  row:" + seatMap[seatRow])
    numAdjacent = 0
    if seatRow > 0:
        numAdjacent += countRowAdjacencies(seatCol,seatRow - 1, seatMap, True)
    numAdjacent += countRowAdjacencies(seatCol,seatRow, seatMap, False)
    if seatRow < (len(seatMap) - 1):
        numAdjacent += countRowAdjacencies(seatCol,seatRow + 1, seatMap, True) 
    return numAdjacent   
        
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

print("Number of rounds: " + str(rounds))
print("Number occupied: " + str(getNumOccupied(currentSeatMap)))