import math 
from math_functions import chinese_remainder_theorem

#filename = "inputs\\2020\\input-day13.txt"
filename = "..\..\inputs\\2020\\input-day13.txt"
with open(filename) as f:
    lines = f.readlines()

departureTime = int(lines[0].strip())
busIds = lines[1].split(",")

busSet = {}
for i in range(len(busIds)):
    busId = busIds[i]
    if busId != "x":
        busSet.update({int(busIds[i]): -i})

print(str(busSet))
result = chinese_remainder_theorem(busSet)
print("CRT result: " + str(result))