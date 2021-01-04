import re

def validNumericField(field, min, max):
	parts = field.partition(":")
	value = int(parts[2])
	return validNumeric(value, min, max)

def validNumeric(value, min, max):
	return (value >= min) and (value <= max)

def validHeight(field):
	parts = field.partition(":")
	if parts[2].endswith("in"):
		value = int(parts[2][:len(parts[2])-2])
		return validNumeric(value, 59, 76)
	elif parts[2].endswith("cm"):
		value = int(parts[2][:len(parts[2])-2])
		return validNumeric(value, 150, 193)
	return False

def validRegEx(field, expression):
	parts = field.partition(":")
	match = re.search(expression, parts[2])
	#print("exp:" + expression + "  field:"+field+"  match:"+str(match))
	return match != None

def isValid(passedPassport):
	byrValid = False
	iyrValid = False
	eyrValid = False
	hgtValid = False
	hclValid = False
	eclValid = False
	pidValid = False

	parts = re.split("\s", passedPassport)
	for part in parts:
		if part.startswith("byr"):
			byrValid = validNumericField(part,1920, 2002)
		elif part.startswith("iyr"):
			iyrValid = validNumericField(part,2010, 2020)
		elif part.startswith("eyr"):
			eyrValid = validNumericField(part,2020, 2030)
		elif part.startswith("hgt"):
			hgtValid = validHeight(part)
		elif part.startswith("hcl"):
			hclValid = validRegEx(part, "#[0-9,a-f]{6}$")
		elif part.startswith("ecl"):	
			eclValid = validRegEx(part, "amb|blu|brn|gry|grn|hzl|oth")
		elif part.startswith("pid"):
			pidValid = validRegEx(part, "^[0-9]{9}$")
	#cidValid = passedPassport.find("cid:") >= 0  # Not required

	return byrValid and iyrValid and eyrValid and hgtValid and hclValid and eclValid and pidValid



filename = "inputs\\2020\\input-day4.txt"
with open(filename) as f:
    lines = f.readlines()
validPasswords = 0
passportData = ""
for input_line in lines:
	if len(input_line.strip()) == 0:
		if isValid(passportData.strip()):
			validPasswords += 1
		passportData = ""
	else:	
		passportData += input_line.strip() + " "
# Check last one		
if isValid(passportData.strip()):
	validPasswords += 1
print("Number of valid passwords: "+str(validPasswords))