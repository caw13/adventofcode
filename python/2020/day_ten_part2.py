import concurrent.futures
import logging

# Call recursively, with dynamic programming
def howManyArrangementsWork(curVoltage,listNumbers,solutions):
    key = "curVoltage: "+str(curVoltage)+" "+str(listNumbers)
    if key in solutions:
        return solutions[key]
    # How many arrangements worked
    if len(listNumbers) == 1:
        solutions[key] = 1
        return 1
    result = 0
    curIndex = 0
    while (listNumbers[curIndex] <= (curVoltage + 3)) and (curIndex < len(listNumbers)):
        result += howManyArrangementsWork(listNumbers[curIndex],listNumbers[curIndex+1:], solutions)
        curIndex += 1
    solutions[key] = result
    return result

filename = "inputs\\2020\\input-day10.txt"
with open(filename) as f:
    lines = f.readlines()

# convert list of strings to list of ints
listNumbers = list(map(int, lines)) 

maxNum = max(listNumbers)
listNumbers.append(maxNum + 3)
listNumbers.sort()

curVoltage = 0
curIndex = 0

solutions = {}
numArrangements = howManyArrangementsWork(0,listNumbers,solutions)
print("Result: " + str(numArrangements))