def findClosestDeparture(departureTime, busId):
    waitTime = busId - (departureTime % busId)
    return waitTime

filename = "inputs\\2020\\input-day13.txt"
with open(filename) as f:
    lines = f.readlines()

departureTime = int(lines[0].strip())
busIds = lines[1].split(",")

minWaitTime = 1000000
minBusId = -1

for busId in busIds:
    if not busId == "x":
        waitTime = findClosestDeparture(departureTime,int(busId.strip())) 
        if waitTime < minWaitTime:
            minWaitTime = waitTime
            minBusId = busId

print("Min wait: " + str(minWaitTime) + " minBusId: " + minBusId)
print("Answer: " + str(int(minBusId) * minWaitTime))