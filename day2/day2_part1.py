l2 = 0
l3 = 0

from collections import Counter
with open("puzzle_input.txt", "r") as f:
	for item in f:
		# count the letters
		chars = Counter(list(item))
		# make a list of count values
		counts = []
		for c in chars:
			counts.append(chars[c])
		# count the counts :)
		counts = Counter(counts)
		# does this ID have letters that appear twice?
		if counts[2] > 0:
			l2 = l2 + 1
		# number of letters that appear thrice
		if counts[3] > 0:
			l3 = l3 + 1
		
print(l2*l3)