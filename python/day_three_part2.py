class PresentDeliverer:
	present_locations = {}
	def __init__(self, name):
		self.name = name
		self.x = 0
		self.y = 0
		self.present_locations[self.get_key()]=1
		
	def get_key(self):
		return str(self.x)+"-"+str(self.y)
	
	def status(self):
		print(self.name + " x: "+str(self.x)+" y: "+str(self.y))
		
	def move(self,instruction):
		if instruction == ">":
			self.x += 1
		elif instruction == "<":
			self.x -= 1
		elif instruction == "^":
			self.y += 1
		else:
			self.y -= 1
		self.present_locations[self.get_key()]=1
		
	def unique_houses(self):
		print("Unique houses: "+str(len(self.present_locations.keys())))


filename = "..\inputs\day_three_input.txt"
f = open(filename)
input_line = f.readline()

santa = PresentDeliverer("Santa")
robo = PresentDeliverer("RoboSanta")

instruction_count = 0
for c in input_line:
	instruction_count += 1
	if (instruction_count % 2):
		santa.move(c)
	else:
		robo.move(c)
santa.unique_houses()