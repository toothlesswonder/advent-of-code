''' build list of coordinates that have been claimed: each is a tuple of x,y coodinates, multiple claims are added to the list multiple times '''

claims = []

with open("puzzle_input.txt", "r") as f:
	for item in f:
		
		start = item.split()[2].split(',')
		xstart = int(start[0])
		ystart = int(start[1][:-1])
		
		size = item.split()[3].split('x')
		width = int(size[0])
		height = int(size[1])
		
		coordinates = [(x, y) for x in range(xstart, xstart + width) for y in range(ystart, ystart + height)]

		claims += coordinates
		
		
''' exploration '''

# how many sq inches claimed (includes multiple counts for overlapping claims)		
print(len(claims))

# look at format of head of list to make sure it looks right
print(claims[0:10])

#what is our biggest x?
x_values = [c[0] for c in claims]
print(max(x_values))

#what is our biggest y?
y_values = [c[1] for c in claims]
print(max(y_values))


''' time to count! '''

from collections import Counter

# count number of claims on each square inch
counts = Counter(claims)

multiple_claims = [c for c in counts if counts[c] > 1]

print(len(multiple_claims))