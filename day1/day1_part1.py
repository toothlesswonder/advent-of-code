with open("freq_changes_list.txt", "r") as f:
	frequency = 0
	for item in f:
		item = int(item)
		frequency = frequency + item
print(frequency)