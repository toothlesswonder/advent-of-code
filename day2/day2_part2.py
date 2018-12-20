import difflib
id_list = []

with open("puzzle_input.txt", "r") as f:
	for item in f:
		id_list.append(item)

for id in id_list:
	idx = id_list.index(id)
	compare_list = id_list[(idx+1):]
	lowest_diff = len(id)
	lowest_str = ''
	for item in compare_list:
		output_list = [li for li in difflib.ndiff(id, item) if li[0] != ' ']
		if len(output_list) < lowest_diff:
			lowest_diff = len(output_list)
			lowest_str = item
		if len(output_list) == 2:
			print('solved!')
			print(id, 'and', item)
			break
	if len(output_list) == 2:
		break
		
print(output_list)