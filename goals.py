def goals():
	#if get_world_size() == 10:
	#	return Unlocks.Reset
	# First Pass, can it be unlocked?
	first_pass = [Unlocks.Grass, Unlocks.Speed]
	if num_unlocked(Unlocks.Speed) > 0:
		first_pass.append(Unlocks.Expand)
	if num_unlocked(Unlocks.Speed) > 0 and num_unlocked(Unlocks.Plant) == 0:
		first_pass.append(Unlocks.Plant) # Yes / No
	if num_unlocked(Unlocks.Expand) > 0:
		first_pass.append(Unlocks.Pumpkins)
	if num_unlocked(Unlocks.Plant) > 0:
		first_pass.append(Unlocks.Carrots)
	if num_unlocked(Unlocks.Pumpkins) > 0 and num_unlocked(Unlocks.Polyculture) == 0:
		return (Unlocks.Polyculture)
		first_pass.append(Unlocks.Polyculture) # Yes / No
	if num_unlocked(Unlocks.Pumpkins) > 0 and num_unlocked(Unlocks.Fertilizer) == 0:
		first_pass.append(Unlocks.Fertilizer) # Yes / No
	if num_unlocked(Unlocks.Fertilizer) > 0:
		first_pass.append(Unlocks.Mazes)
	if num_unlocked(Unlocks.Carrots) > 0: # and num_unlocked(Unlocks.Trees)
		first_pass.append(Unlocks.Trees)
	if num_unlocked(Unlocks.Carrots) > 0 and num_unlocked(Unlocks.Watering) == 0:
		first_pass.append(Unlocks.Watering) # Yes / No?
	if num_unlocked(Unlocks.Trees) > 0:
		first_pass.append(Unlocks.Sunflowers)
	if num_unlocked(Unlocks.Watering) > 0 and num_unlocked(Unlocks.Multi_Trade) == 0:
		first_pass.append(Unlocks.Multi_Trade) # Yes / No
	if num_unlocked(Unlocks.Multi_Trade) > 0:
		first_pass.append(Unlocks.Reset)
	# Second Pass, have we unlocked all of the ingredients? Anything over 50000?
	second_pass = []
	for i in range(len(first_pass)):
		good = True
		total = 0
		for j in get_cost(first_pass[i]):
			if num_unlocked(j[0]) == 0:
				good = False
			if first_pass[i] != Unlocks.Reset and j[1] >= 50000:
				good = False
			if first_pass[i] != Unlocks.Reset and j[0] == Items.Gold and j[1] > 5000:
				good = False
			#if first_pass[i] != Unlocks.Speed and first_pass[i] != Unlocks.Expand and num_unlocked(first_pass[i]) > 9:
			#	good = False
			if j[0] == Items.Power and j[1] > 1900:
				good = False
			if j[0] == Items.Power and get_world_size() < 6:
				good = False
			if first_pass[i] == Unlocks.Expand and num_unlocked(Unlocks.Expand) == 8:
				good = True
			#if first_pass[i] == Unlocks.Speed and num_unlocked(Unlocks.Speed) > 19:
			#	good = False
			total += j[1]
			for k in get_cost(j[0]):
				total += j[1] * k[1]
		if first_pass[i] == Unlocks.Expand:
			total /= 4
		if first_pass[i] == Unlocks.Polyculture:
			total /= 5
#		print(second_pass)
		if good:
			x = num_unlocked(first_pass[i])
			if first_pass[i] == Unlocks.Expand or first_pass[i] == Unlocks.Polyculture:
				x = 1
			second_pass.append([total / (1 - x/(x+1)) , first_pass[i]])
	# Sort
	for i in range(len(second_pass)-2, -1, -1):
		if second_pass[i][0] > second_pass[i+1][0]:
			temp = second_pass[i]
			second_pass[i] = second_pass[i+1]
			second_pass[i+1] = temp
	return second_pass[0][1]