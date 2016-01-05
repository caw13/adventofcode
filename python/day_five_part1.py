import re

def isNice(passedString):
	containsDirtyWord = re.search(r'.*(ab)|(cd)|(pq)|(xy).*',passedString)
	containsDoubleLetter = re.search(r'([A-Za-z])\1',passedString)
	contains3Vowels = re.search(r'.*[a|e|i|o|u].*[a|e|i|o|u].*[a|e|i|o|u].*',passedString)
	if not containsDirtyWord and containsDoubleLetter and contains3Vowels:
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