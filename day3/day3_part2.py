''' define Claim object class (I knew I should have done this this first time!) '''
	
class Claim:

	# attributes
	def __init__(self, id, x, y, width, height):
		self.id = int(id)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.overlap = False
		
	def __str__(self):
		return "Claim %s" % (self.id)
		
		
''' check range overlap '''

def overlap(start1, end1, start2, end2):
	# Does the range (start1, end1) overlap with (start2, end2)?
	return end1 >= start2 and end2 >= start1
	

''' create list of claims '''

claims = []

with open("puzzle_input.txt", "r") as f:
	for item in f:
		
		id = item.split()[0][1:]
		
		coords = item.split()[2].split(',')
		x = int(coords[0])
		y = int(coords[1][:-1])
		
		size = item.split()[3].split('x')
		width = int(size[0])
		height = int(size[1])
		
		c = Claim(id, x, y, width, height)
		claims.append(c)
		

''' compare each claim to others; check to see if both the x range and y range overlap '''

for a in claims:	
	# only compare to items after a in the list to avoid checking combinations twice
	for b in claims[a.id:]:
		if (overlap(a.x, a.x + a.width, b.x, b.x + b.width) and overlap(a.y, a.y + a.height, b.y, b.y + b.height)):
			a.overlap = True
			b.overlap = True
		else:
			pass

		
''' create list of claims with no overlap '''
unique = [c for c in claims if c.overlap == False]

'''confirm there is only one '''
print('Found %s claim(s) with no overlap:' % (len(unique)))

for c in unique:
	print(c)