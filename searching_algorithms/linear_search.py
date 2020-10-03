# Linear Search

def linear_search(values, target):
	index = 0
	search_res = False

	while index < len(values) and search_res is False:
		if values[index] == target:
			search_res = True
		else:
			index += 1
	return search_res

list = [1, 23, 16, 57, 34, 97]
print(linear_search(list,12))