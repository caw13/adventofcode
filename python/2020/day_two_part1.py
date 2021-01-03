import re

def isValid(passedString):
	parts = re.split("\s", passedString)
	hyphenPos = parts[0].find("-")
	minNum = int(parts[0][:hyphenPos])
	maxNum = int(parts[0][hyphenPos+1:])
	charMatch = parts[1][0]
	# find count of specified char
	numOccurances = 0
	for curChar in parts[2]:
		if (curChar == charMatch):
			numOccurances += 1
	if (numOccurances >= minNum) and (numOccurances <= maxNum):
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