def get_key(x, y):
	return str(x)+"-"+str(y)

#input_line = input("Enter input:\n")
filename = "..\inputs\day_three_input.txt"
f = open(filename)
input_line = f.readline()
x = 0
y = 0
present_locations = {}
present_locations[get_key(x,y)]=1
for c in input_line:
	if c == ">":
		x += 1
	elif c == "<":
		x -= 1
	elif c == "^":
		y += 1
	else:
		y -= 1
	present_locations[get_key(x,y)]=1

print("Unique houses: "+str(len(present_locations.keys())))
