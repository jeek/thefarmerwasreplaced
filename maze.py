def maze(my_x, my_y):
	#harvest_all()
	#while num_items(Items.Carrot) < 1000:
	#		comp_plant(Items.Carrot)
	#	while num_items(Items.Pumpkin) < 1000:
	#		plant_a_pumpkin()
	goto([my_x, my_y])
	while num_items(Items.Fertilizer) < 100:
		buy(Items.Fertilizer)
	goto([my_x, my_y])
	plant_a_bush()
	goto([my_x, my_y])
	while num_items(Items.Fertilizer) > 0 and get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)
	if get_entity_type() != Entities.Bush:
		directions = [North, East, South, West]
		z = 0
		while get_entity_type() != Entities.Treasure:
			my_x = get_pos_x()
			my_y = get_pos_y()
			move(directions[z % 4])
			if z > 12 * get_world_size() * get_world_size():
				return
			if my_x != get_pos_x() or my_y != get_pos_y():
				z += 1
			else:
				z += 3
		harvest()
		unlock(Unlocks.Reset)
		if num_unlocked(Unlocks.Reset) > 0:
			reset()