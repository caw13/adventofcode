import re

def isValid(passedPassport):
	byrPresent = passedPassport.find("byr:") >= 0
	iyrPresent = passedPassport.find("iyr:") >= 0
	eyrPresent = passedPassport.find("eyr:") >= 0
	hgtPresent = passedPassport.find("hgt:") >= 0
	hclPresent = passedPassport.find("hcl:") >= 0
	eclPresent = passedPassport.find("ecl:") >= 0
	pidPresent = passedPassport.find("pid:") >= 0
	#cidPresent = passedPassport.find("cid:") >= 0  # Not required
	return byrPresent and iyrPresent and eyrPresent and hgtPresent and hclPresent and eclPresent and pidPresent



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