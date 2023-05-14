def comp_plant(plantme):
	for i in get_cost(plantme):
		comp_plant(i[0])
	start_hay = num_items(Items.Hay)
	if num_unlocked(Unlocks.Watering) > 0 and num_items(Items.Carrot) > (num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)) * 5:
		trade(Items.Empty_Tank)
	queue = []
	harvest_queue = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if i == 0 or num_unlocked(Unlocks.Expand) >= 2:
				queue.append([i, j])
	while len(queue) > 0:
		while num_items(Items.Power) >= 1 and get_active_power() < 10:
			use_item(Items.Power)
		comp_queue = []
		goto(queue[0])
		harvest_queue.append(queue.pop(0))
		if num_unlocked(Unlocks.Watering) > 0 and get_water() <= .75 and num_items(Items.Water_Tank) > num_items(Items.Empty_Tank):
			use_item(Items.Water_Tank)
		if plantme == Items.Wood:
			plant_wood()
		if plantme == Items.Carrot:
			plant_a_carrot()
		if plantme == Items.Hay:
			plant_grass()
		if num_unlocked(Unlocks.Polyculture) > 0:
			comp_queue = [get_companion()]
			while comp_queue[len(comp_queue)-1] != None:
				found = -1
				for i in range(len(queue)):
					if queue[i][0] == comp_queue[len(comp_queue)-1][1] and queue[i][1] == comp_queue[len(comp_queue)-1][2]:
						found = i
				if found >= 0:
					harvest_queue.append(queue.pop(found))
					handle_companion(comp_queue[len(comp_queue)-1])
				else:
					comp_queue.append(None)
		while (len(queue) == 0 and len(harvest_queue) > 0): # or (num_unlocked(Unlocks.Polyculture) > 0 and len(harvest_queue) > 0 and len(harvest_queue) > len(queue)):
			goto(harvest_queue[0])
			while get_entity_type() != None and not can_harvest() and get_entity_type() != Entities.Grass:
				if num_unlocked(Unlocks.Fertilizer) > 0 and get_entity_type() != Entities.Bush:
					buy(Items.Fertilizer)
					use_item(Items.Fertilizer)
			harvest()
			harvest_queue.pop(0)