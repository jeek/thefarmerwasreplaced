def plant_a_pumpkin():
	while num_items(Items.Carrot) < 4 * get_world_size() * get_world_size():
		comp_plant(Items.Carrot, 4 * get_world_size() * get_world_size())
	queue = []
	z = get_world_size()
	my_x = get_pos_x()
	my_y = get_pos_y()
	for i in range(z):
		for j in range(z):
			queue.append([(my_x + i) % z, (my_y + j) % z])
	while len(queue) > 0:
		goto(queue[0])
		if get_entity_type() == Entities.Pumpkin:
			if can_harvest():
				queue.pop(0)
			else:
				hydrate()
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
			hydrate()
	harvest()
##	if get_world_size() < 9:
	#	unlock(Unlocks.Expand)
#		unlock(Unlocks.Pumpkins)