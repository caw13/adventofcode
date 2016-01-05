import re

def isNice(line):
	containsDoubleRepeat = re.search(r'(..).*\1',line)
	containsOneSepRepeat = re.search(r'.*(.).\1.*',line)
	if containsDoubleRepeat and containsOneSepRepeat:
		return True
	else:
		return False
		
filename = "..\inputs\day_five_input.txt"
with open(filename) as f:
    lines = f.readlines()
niceWords = 0
for input_line in lines:
	if isNice(input_line):
		niceWords += 1
print("Number of nice words: "+str(niceWords))