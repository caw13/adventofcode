def calculate_surface(x,y,z):
	return 2*x*y + 2*x*z + 2*y*z

def min_side(x,y,z):
	side_values = [x*y, x*z, y*z]
	return min(side_values)

def min_perimeter(x,y,z):
	perimeters = [2*x+2*y, 2*x+2*z, 2*y+2*z]
	return min(perimeters)
	
def volume(x,y,z):
	return x*y*z

#filename = input("Input file with dimensions in format 2x3x4:\n")
filename = "..\inputs\day_two_input.txt"
with open(filename) as f:
    lines = f.readlines()
wrapping_paper_total = 0
ribbon_total = 0
for input_line in lines:
	dimensions = input_line.split('x')
	x = int(dimensions[0])
	y = int(dimensions[1])
	z = int(dimensions[2])
	wrapping_paper_total += calculate_surface(x,y,z) + min_side(x,y,z)
	ribbon_total += min_perimeter(x,y,z) + volume(x,y,z)
print("Wrapping paper total: "+str(wrapping_paper_total)+" sqft")
print("Ribbon total: "+str(ribbon_total)+" sqft")

