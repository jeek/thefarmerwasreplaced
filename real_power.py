def real_power():
	countdown = get_world_size() * get_world_size()
	while num_items(Items.Carrot) < 4 * countdown:
		comp_plant(Items.Carrot)
	while num_items(Items.Sunflower_Seed) < countdown:
		buy(Items.Sunflower_Seed)
	queue = []
	if num_unlocked(Unlocks.Fertilizer) > 0:
		while num_items(Items.Power) >= 1 and get_active_power() < 10:
			use_item(Items.Power)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goto([i, j])
			harvest()
			if num_items(Items.Sunflower_Seed) == 0:
				buy(Items.Sunflower_Seed)
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Sunflower)
	best = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goto([i, j])
			while not can_harvest():
				pass
			while measure() >= len(queue):
				queue.append([])
			queue[measure()].append([i, j])
	while len(queue) > 0:
		goto(queue[len(queue)-1][0])
		while not can_harvest():
			pass
		harvest()
		if num_unlocked(Unlocks.Expand) * 100 > num_items(Items.Power) and num_items(Items.Power) < 1000 + 200 * get_world_size():
			buy(Items.Sunflower_Seed)
			goto(queue[len(queue)-1][0])
		queue[len(queue)-1].pop(0)
		while len(queue) > 0 and len(queue[len(queue)-1]) == 0:
			queue.pop()
		if num_unlocked(Unlocks.Sunflowers) < 4 or (get_world_size() * 300 > num_items(Items.Power) and num_items(Items.Power) < 1000 + 200 * get_world_size()):
			while num_unlocked(Unlocks.Fertilizer) == 0 and num_items(Items.Water_Tank) > num_items(Items.Empty_Tank) and get_water() <= .75:
				use_item(Items.Water_Tank)
			plant(Entities.Sunflower)
			while num_items(Items.Fertilizer) == 0 and num_items(Items.Water_Tank) > 0 and get_water() <= .75:
				use_item(Items.Water_Tank)
			while get_entity_type() != None and get_entity_type() != Entities.Grass and not can_harvest():
				use_item(Items.Fertilizer)
			while num_items(Items.Fertilizer) == 0 and num_items(Items.Water_Tank) > 0 and get_water() <= .75:
				use_item(Items.Water_Tank)
			if get_entity_type() == Entities.Sunflower:
				while measure() >= len(queue):
					queue.append([])
				queue[measure()].append([get_pos_x(), get_pos_y()])