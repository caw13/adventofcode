import re


def addBag(bagLine, bagDictionary):
	#print("bagLine: "+bagLine+"  bagDictionary: "+str(bagDictionary))
	parts = bagLine.split("s contain ")
	bagName = parts[0]
	contents = re.findall("[\w]+ [\w]+ bag", parts[1]) 
	#print("bag: '"+bagName+"'  contents: "+str(contents))
	bagDictionary[bagName] = contents

# recursively check to see if can contain passed bag
def canContain(bagPassed, bagToContain, bagDictionary):
	result = False
	#print("bagPassed:"+bagPassed+" bagContained:"+bagToContain+" bagDictionary:"+str(bagDictionary))
	bagsCanContain = bagDictionary[bagPassed]
	for bag in bagsCanContain:
		if bag == bagToContain:
			result = True
			break
		elif bag == "no other bag":
			result = False
			break
		else:
			result = canContain(bag,bagToContain,bagDictionary)
			if result == True:
    				break
	return result
		
filename = "inputs\\2020\\input-day7.txt"
with open(filename) as f:
    lines = f.readlines()

bagDictionary = {}

for line in lines:
	#line = "light red bags contain 1 bright white bag, 2 muted yellow bags."
	addBag(line, bagDictionary)

bagToContain = "shiny gold bag"
bagCount = 0
for k, v in bagDictionary.items():
	if canContain(k,bagToContain,bagDictionary):
		bagCount += 1
		#print(k+" could contain it")
	#else:
		#print(k+" could NOT contain it")	

print("Number that can contain: "+str(bagCount))
