def real_power(target):
	if target < 2000:
		target = 2000
	target *= 1.1
	countdown = get_world_size() * get_world_size()
	while num_items(Items.Carrot) < 10 * countdown:
		comp_plant(Items.Carrot, 10 * countdown)
	while num_items(Items.Sunflower_Seed) < countdown:
		buy(Items.Sunflower_Seed)
	queue = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goto([i, j])
			harvest()
			if num_items(Items.Sunflower_Seed) == 0:
				buy(Items.Sunflower_Seed)
			if num_items(Items.Sunflower_Seed) > 0:
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
		while not can_harvest() and get_entity_type() != None:
			queue[len(queue)-1].append(queue[len(queue)-1].pop(0))
			goto(queue[len(queue)-1][0])
		harvest()
		if num_unlocked(Unlocks.Expand) * 100 > num_items(Items.Power) and num_items(Items.Power) < target + 200 * get_world_size() and can_afford(Items.Sunflower_Seed):
			buy(Items.Sunflower_Seed)
			goto(queue[len(queue)-1][0])
		queue[len(queue)-1].pop(0)
		while len(queue) > 0 and len(queue[len(queue)-1]) == 0:
			queue.pop()
		if num_unlocked(Unlocks.Sunflowers) < 4 or (get_world_size() * 300 > num_items(Items.Power) and num_items(Items.Power) < target + 200 * get_world_size()):
			if num_items(Items.Power) < target:
				if num_items(Items.Sunflower_Seed) == 0 and can_afford(Items.Sunflower_Seed):
					buy(Items.Sunflower_Seed)
				plant(Entities.Sunflower)
			hydrate()
			if get_entity_type() == Entities.Sunflower:
				while measure() >= len(queue):
					queue.append([])
				queue[measure()].append([get_pos_x(), get_pos_y()])