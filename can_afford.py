def can_afford(item):
	for i in get_cost(item):
		if num_items(i[0]) < i[1]:
			return False
	return True