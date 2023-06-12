def second_pass_calc(first_pass):
	print(first_pass)
	second_pass = []
	for i in range(len(first_pass)):
		good = True
		total = 0
		if first_pass[i] == Unlocks.Expand and num_unlocked(Unlocks.Expand) > 9:
			good = False
		if True:
			if first_pass[i] == Unlocks.Grass:
				if num_items(Items.Hay) > 50000:
					good = False
				if num_unlocked(Unlocks.Grass) * 3 > num_unlocked(Unlocks.Speed):
					good = False
#				if num_items(Items.Wood) > 0 and num_items(Items.Hay) > num_items(Items.Wood):
#					good = False
			else:
				if first_pass[i] == Unlocks.Trees:
					if num_unlocked(Unlocks.Grass) < num_unlocked(Unlocks.Trees):
						good = False
					if num_unlocked(Unlocks.Trees) * 2 > num_unlocked(Unlocks.Speed):
						good = False
					if num_items(Items.Wood) > 50000:
						good = False
				else:
					if first_pass[i] == Unlocks.Carrots:
						if num_unlocked(Unlocks.Grass) < num_unlocked(Unlocks.Carrots):
							good = False
						if num_items(Items.Carrot) > 50000:
							good = False
						if num_unlocked(Unlocks.Grass) * 2 > num_unlocked(Unlocks.Speed):
							good = False
					if first_pass[i] == Unlocks.Pumpkins:
						if num_unlocked(Unlocks.Pumpkins) * 3 > num_unlocked(Unlocks.Speed):
							good = False
						if num_items(Items.Pumpkin) > 50000:
							good = False
					if first_pass[i] == Unlocks.Mazes:
						if num_items(Items.Gold) > 10000:
							good = False
						if num_items(Items.Gold) * 5 > num_items(Items.Hay):
							good = False
		#if num_unlocked(first_pass[i]) > 1 and num_unlocked(Unlocks.Expand) < 5 and (first_pass[i] == Unlocks.Pumpkins or first_pass[i] == Unlocks.Carrots or first_pass[i] == Unlocks.Trees or first_pass[i] == Unlocks.Mazes or first_pass[i] == Unlocks.Grass):
		#	good = False
		if num_unlocked(first_pass[i]) > 1 and first_pass[i] != Unlocks.Expand and num_unlocked(Unlocks.Polyculture) == 0:
			good = False
			#if first_pass[i] == Unlocks.Speed:
			#if get_cost(Unlocks.Speed)[0][0] == Items.Power:
			#	good = False
#			if num_unlocked(Unlocks.Grass) * 2 < num_unlocked(Unlocks.Speed):
#				good = False
#		if num_unlocked(first_pass[i]) > 11 and first_pass[i] != Unlocks.Expand:
	#		good = False
		if num_unlocked(first_pass[i]) > 1 and first_pass[i] == Unlocks.Mazes:
			good = False
		if num_unlocked(first_pass[i]) > 1 and first_pass[i] == Unlocks.Sunflowers:
			good = False
		if good:
			for j in get_cost(first_pass[i]):
				if j[0] == Items.Gold and (num_unlocked(Items.Fertilizer) == 0 or num_unlocked(Unlocks.Mazes) == 0):
					good = False
				if num_unlocked(j[0]) == 0:
					good = False
				if first_pass[i] != Unlocks.Reset and j[1] >= 50000:
					good = False
				if first_pass[i] != Unlocks.Reset and j[0] == Items.Gold and j[1] >= 5000:
					good = False
				#if first_pass[i] != Unlocks.Speed and first_pass[i] != Unlocks.Expand and num_unlocked(first_pass[i]) > 9:
				#	good = False
				if j[0] == Items.Power and j[1] > 2100:
					good = False
				#if j[0] == Items.Power and get_world_size() < 6:
				#	good = False
				#if first_pass[i] == Unlocks.Expand and num_unlocked(Unlocks.Expand) == 8:
				#	good = True
				if first_pass[i] == Unlocks.Speed and num_unlocked(Unlocks.Speed) > 19:
					good = False
				total += j[1]
				for k in get_cost(j[0]):
					if j[1] * k[1] - num_items(k[0]) > 0:
						total += j[1] * k[1] - num_items(k[0])
		#if num_unlocked(first_pass[i]) > 5 and first_pass[i] != Unlocks.Expand and first_pass[i] != Unlocks.Speed:
		#	good = False
		#if first_pass[i] == Unlocks.Expand:
		#	total /= 5
		#if first_pass[i] == Unlocks.Polyculture:
		#	total /= 10
		#if first_pass[i] == Unlocks.Reset:
		#	total /= 10
#		print(second_pass)
		if good:
			x = num_unlocked(first_pass[i])
			#if first_pass[i] == Unlocks.Expand or first_pass[i] == Unlocks.Polyculture or first_pass[i] == Unlocks.Reset:
			#	x = 1
			second_pass.append([total / (1 - x/(x+1)) , first_pass[i]])
	return second_pass