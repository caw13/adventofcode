filename = "..\inputs\day_one_input.txt"
f = open(filename)
directions = f.readline()
cur_floor = 0
direction_num = 0
basement_reached = False
for c in directions:
	direction_num += 1
	if c == ")":
		cur_floor -= 1
	elif c == "(":
		cur_floor += 1
	if cur_floor < 0 and not basement_reached:
		print("Reached basement with direction num: "+str(direction_num))
		basement_reached = True
print("Resulting floor "+str(cur_floor));