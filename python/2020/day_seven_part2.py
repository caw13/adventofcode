import re


def addBag(bagLine, bagDictionary):
	#print("bagLine: "+bagLine+"  bagDictionary: "+str(bagDictionary))
	parts = bagLine.split("s contain ")
	bagName = parts[0]
	contents = re.findall("(no other bag|[0-9]+ [\w]+ [\w]+ bag)", parts[1]) 
	#print("bag: '"+bagName+"'  contents: "+str(contents))
	bagDictionary[bagName] = contents

# recursively check to see how many bags must be contained in the passed bag
def numberContained(bagPassed, bagDictionary):
	numContained = 0
	bagsCanContain = bagDictionary[bagPassed]
	for bag in bagsCanContain:
		if bag == "no other bag":
			break
		else:
			count = int(re.findall("[0-9]+", bag)[0] )
			bagName = re.findall("[\w]+ [\w]+ bag", bag)[0]
			numContained += (count * (1 + numberContained(bagName,bagDictionary)))
	return numContained
		
filename = "inputs\\2020\\input-day7.txt"
with open(filename) as f:
    lines = f.readlines()

bagDictionary = {}

for line in lines:
	addBag(line, bagDictionary)

bagInQuestion = "shiny gold bag"
bagCount = numberContained(bagInQuestion,bagDictionary)
print("Bag count: "+str(bagCount))
