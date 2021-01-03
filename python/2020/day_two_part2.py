import re

def isValid(passedString):
	parts = re.split("\s", passedString)
	hyphenPos = parts[0].find("-")
	firstPos = int(parts[0][:hyphenPos])
	secondPos = int(parts[0][hyphenPos+1:])
	charMatch = parts[1][0]
	# Check the positions
	if (charMatch == parts[2][firstPos-1]) and (charMatch != parts[2][secondPos-1]):
		return True
	elif (charMatch != parts[2][firstPos-1]) and (charMatch == parts[2][secondPos-1]):
		return True
	else:
		return False


filename = "inputs\\2020\\input-day2.txt"
with open(filename) as f:
    lines = f.readlines()
validPasswords = 0
for input_line in lines:
	if isValid(input_line):
		validPasswords += 1
print("Number of valid passwords: "+str(validPasswords))