import concurrent.futures
import logging

# This solution provides example of using threads, but wasn't used as dynamic programming much better solution


# Call recursively
def howManyArrangementsWork(curVoltage,listNumbers,threadNum):
    #print("thread=" + str(threadNum)+" curVoltage="+str(curVoltage)+" listRemaining:" + str(listNumbers))
    # How many arrangements worked
    if len(listNumbers) == 1:
        return 1
    result = 0
    curIndex = 0
    while (listNumbers[curIndex] <= (curVoltage + 3)) and (curIndex < len(listNumbers)):
        result += howManyArrangementsWork(listNumbers[curIndex],listNumbers[curIndex+1:], threadNum)
        curIndex += 1
    return result

def multiThreadArrangementsWork(curVoltage,listNumbers):
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(0,3):
            params = [curVoltage,listNumbers[index:],index]
            futures.append(executor.submit(lambda p: howManyArrangementsWork(*p), params))
    
    result = 0
    #print("Done " + str(futures))
    for f in futures:
        #print("f result : " + str(f.result()))
        result += f.result()
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

numArrangements = howManyArrangementsWork(0,listNumbers,-1)
#numArrangements = multiThreadArrangementsWork(0,listNumbers)
print("Result: " + str(numArrangements))