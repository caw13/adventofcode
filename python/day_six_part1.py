import re
		
filename = "..\inputs\day_six_input.txt"
#filename = "temp_input.txt"
with open(filename) as f:
    lines = f.readlines()
lights = [[0 for x in range(1000)] for x in range(1000)] 
for line in lines:
	searchObj = re.search(r'(turn on|turn off|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)',line)
	if searchObj:
		startx = int(searchObj.group(2))
		starty = int(searchObj.group(3))
		endx = int(searchObj.group(4))
		endy = int(searchObj.group(5))
		for x in range(startx,endx+1):
			for y in range(starty,endy+1):
				if searchObj.group(1) == "turn on":
					lights[x][y]=1
				elif searchObj.group(1) == "turn off":
					lights[x][y]=0
				elif searchObj.group(1) == "toggle":
					lights[x][y]=(1+lights[x][y])%2
				else:
					print("Unexpected instruction: "+searchObj.group(1))
# Count number on
numberOn = 0
for x in range(len(lights)):
	for y in range(len(lights[0])):
		numberOn += lights[x][y]
print("Number still on: "+str(numberOn))