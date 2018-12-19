changes_list = []
with open("freq_changes_list.txt", "r") as f:
	for item in f:
		changes_list.append(int(item))

#print(changes_list)
frequency_list = [0]
frequency = 0

i = 1
#limit to 300 loops so this doesn't run forever if I've missed something :)
while (i < 300):
	print('starting iteration # ', i, '. . .')
	for f in changes_list:
		frequency = frequency + f
		if frequency in frequency_list:
			print('YAY! this one is in twice!!', frequency)
			i = i + 10000
			break
		frequency_list.append(frequency)
	print('ended at frequency', frequency)
	print('length of list ', len(frequency_list))
	i = i + 1