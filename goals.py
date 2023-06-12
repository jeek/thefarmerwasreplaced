def goals():
	#if get_world_size() > 9:
		#return Unlocks.Reset
	second_pass = second_pass_calc(first_pass_calc())
	# Sort
	for i in range(len(second_pass)-2, -1, -1):
		if second_pass[i][0] > second_pass[i+1][0]:
			temp = second_pass[i]
			second_pass[i] = second_pass[i+1]
			second_pass[i+1] = temp
	if len(second_pass) == 0:
		return Unlocks.Speed
	return second_pass[0][1]