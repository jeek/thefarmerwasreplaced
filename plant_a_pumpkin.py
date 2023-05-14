def plant_a_pumpkin():
	while num_items(Items.Carrot) < 4 * get_world_size() * get_world_size():
		comp_plant(Items.Carrot)
	queue = []
	got_there = False
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			queue.append([i, j])
	while len(queue) > 0:
		while num_items(Items.Power) >= 1 and get_active_power() < 10:
			use_item(Items.Power)
		goto(queue[0])
		if got_there == False and get_pos_x() == get_world_size() and get_pos_y() == get_world_size():
			got_there = True
		if get_entity_type() == Entities.Pumpkin:
			if can_harvest():
				queue.pop(0)
			else:
				while got_there and num_items(Items.Water_Tank) > num_items(Items.Empty_Tank) and get_water() <= .75:
					use_item(Items.Water_Tank)
				queue.append(queue.pop(0))
		else:
			harvest()
			while num_items(Items.Pumpkin_Seed) == 0:
				my_x = get_pos_x()
				my_y = get_pos_y()
				buy(Items.Pumpkin_Seed)
				goto([my_x, my_y])
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Pumpkin)
	harvest()
	if get_world_size() < 10:
		unlock(Unlocks.Expand)
		unlock(Unlocks.Pumpkins)