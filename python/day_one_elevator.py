directions = input("Enter elevator directions:\n")
cur_floor = 0
for c in directions:
	if c == ")":
		cur_floor -= 1
	elif c == "(":
		cur_floor += 1
print("Resulting floor "+str(cur_floor));