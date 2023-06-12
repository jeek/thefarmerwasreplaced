def first_pass_calc():
	first_pass = [Unlocks.Grass]
	if num_unlocked(Unlocks.Speed) > 0 and (num_unlocked(Unlocks.Expand) < 2 or num_unlocked(Unlocks.Pumpkins) > 0):
		first_pass.append(Unlocks.Expand)
	if num_unlocked(Unlocks.Speed) > 0 and num_unlocked(Unlocks.Plant) == 0:
		first_pass.append(Unlocks.Plant) # Yes / No
	if num_unlocked(Unlocks.Plant) > 0:
		first_pass.append(Unlocks.Carrots)
	if num_unlocked(Unlocks.Carrots) > 0 and num_unlocked(Unlocks.Watering) == 0:
		first_pass.append(Unlocks.Watering) # Yes / No?
	if num_unlocked(Unlocks.Watering) < 1:
		return first_pass
	if num_unlocked(Unlocks.Carrots) > 0: # and num_unlocked(Unlocks.Trees)
		first_pass.append(Unlocks.Trees)
	if num_unlocked(Unlocks.Expand) > 0:
		first_pass.append(Unlocks.Pumpkins)
	if num_unlocked(Unlocks.Fertilizer) > 0 and num_unlocked(Unlocks.Trees) > 0:
		first_pass.append(Unlocks.Sunflowers)
	if num_unlocked(Unlocks.Pumpkins) > 0 and num_unlocked(Unlocks.Fertilizer) == 0:
		first_pass.append(Unlocks.Fertilizer) # Yes / No
	if num_unlocked(Unlocks.Sunflowers) < 1:
		return first_pass
	first_pass.append(Unlocks.Speed)
	if num_unlocked(Unlocks.Pumpkins) > 0 and num_unlocked(Unlocks.Polyculture) == 0:
		return ([Unlocks.Polyculture])
		first_pass.append(Unlocks.Polyculture) # Yes / No
	if num_unlocked(Unlocks.Fertilizer) > 0:
		first_pass.append(Unlocks.Mazes)
#	if num_unlocked(Unlocks.Watering) > 0 and num_unlocked(Unlocks.Multi_Trade) == 0:
	#	first_pass.append(Unlocks.Multi_Trade) # Yes / No
	#if num_unlocked(Unlocks.Multi_Trade) > 0:
	if num_unlocked(Unlocks.Mazes) >= 1 or num_items(Items.Gold) > 10000:
		first_pass.append(Unlocks.Reset)
	return first_pass