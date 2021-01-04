import math

def binaryPartition(code,low,high):
	#print("Code: "+code+" low: "+ str(low) + " high: "+str(high))
	if len(code) > 0:
		curCode = code[0:1]
		if (curCode == "F") or (curCode == "L"):
			return binaryPartition(code[1:],low,math.floor(((high-low)/2)+low))
		else:
			return binaryPartition(code[1:],math.ceil(((high-low)/2)+low),high)
	else:
		return low

filename = "inputs\\2020\\input-day5.txt"
with open(filename) as f:
    lines = f.readlines()
highestSeatId = -1

for line in lines:
	row = binaryPartition(line[0:7],0,127)
	col = binaryPartition(line[7:],0,7)
	seatId = (row * 8) + col
	#print("Result:  row:"+str(row)+"  col:"+str(col) + " seatId:"+str(seatId))
	if (seatId > highestSeatId):
    		highestSeatId = seatId
print("Highest Seat ID: "+str(highestSeatId))