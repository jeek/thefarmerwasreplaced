def comp_plant(plantme, goal):
	orig = plantme
	#for i in get_cost(plantme):
	#	comp_plant(i[0])
	start_hay = num_items(Items.Hay)
#	while num_unlocked(Unlocks.Watering) > 0 and can_afford(Items.Empty_Tank) and num_items(Items.Carrot) > (num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)) * 5:
#		trade(Items.Empty_Tank)
	if num_unlocked(Unlocks.Polyculture) == 0:
		while num_unlocked(Unlocks.Watering) > 0 and num_items(Items.Water_Tank) < 100 and can_afford(Items.Empty_Tank):
			trade(Items.Empty_Tank)
	else:
		while num_unlocked(Unlocks.Watering) > 0 and num_items(Items.Water_Tank) < 1000 and can_afford(Items.Empty_Tank):
			trade(Items.Empty_Tank)
	queue = []
	harvest_queue = []
	z = get_world_size()
	my_x = get_pos_x()
	my_y = get_pos_y()
	zz = my_x * z + my_y
	planted = []
	while len(planted) < z * z:
		planted.append(None)
	while num_items(orig) < goal:
		plantme = orig
		if False and num_unlocked(Unlocks.Polyculture) > 0:
			if num_items(Items.Pumpkin) < num_items(Items.Carrot) and num_items(Items.Carrot) > 5 * get_world_size() * get_world_size():
				while num_items(Items.Pumpkin) < num_items(Items.Carrot) and num_items(Items.Carrot) > 5 * get_world_size() * get_world_size():
					while len(harvest_queue) > 0:
						goto([harvest_queue[0] // z, harvest_queue[0] % z])
						harvest()
						planted[harvest_queue[0]] = None
						harvest_queue.pop(0)
					plant_a_pumpkin()
				if num_unlocked(Unlocks.Mazes) > 0 and num_items(Items.Gold) * 5 < num_items(Items.Hay):
					while len(harvest_queue) > 0:
						goto([harvest_queue[0] // z, harvest_queue[0] % z])
						harvest()
						planted[harvest_queue[0]] = None
						harvest_queue.pop(0)
					maze(my_x, my_y)
			plantme = Items.Hay
			if num_unlocked(Unlocks.Trees) > 0 or num_unlocked(Unlocks.Plant) > 0:
				if num_items(Items.Wood) < num_items(Items.Hay):
					plantme = Items.Wood
				if num_unlocked(Unlocks.Carrots) > 0:
					if num_items(Items.Carrot) < num_items(Items.Hay) and num_items(Items.Carrot) < num_items(Items.Wood):
						plantme = Items.Carrot
			else:
				if num_unlocked(Unlocks.Carrots) > 0:
					if num_items(Items.Carrot) < num_items(Items.Hay):
						plantme = Items.Carrot
		while num_unlocked(Unlocks.Fertilizer) > 0 and num_items(Items.Pumpkin) < z * z * 10 and num_items(Items.Carrot) > 5 * z * z:
			while len(harvest_queue) > 0:
				goto([harvest_queue[0] // z, harvest_queue[0] % z])
				harvest()
				planted[harvest_queue[0]] = None
				harvest_queue.pop(0)
			plant_a_pumpkin()
		if num_unlocked(Unlocks.Fertilizer) > 0 and num_items(Items.Pumpkin) < z * z * 10 and num_items(Items.Carrot) < 5 * z * z:			
			plantme = Items.Carrot
		if plantme == Items.Carrot and num_items(Items.Wood) < 100:
			plantme = Items.Wood
		if plantme == Items.Carrot and num_items(Items.Hay) < 100:
			plantme = Items.Hay
		comp_queue = []
		zzz = zz
		zz = (zz + 1) % (z * z)
		while planted[zz] != None: # or (plantme == Items.Wood and (zz // z + zz % z) % 2 == 0 and num_unlocked(Unlocks.Trees) > 0):
#			zzz += 1
#			if zzz > z * z:
#				goto([zz // z, zz % z])
#				harvest()
#				planted[zz] = None
#			if can_harvest() and len(harvest_queue) > 0 and zz == harvest_queue[0]:
#				goto([zz // z, zz % z])
#				harvest()
#				harvest_queue.pop(0)
#				planted[zz] = None
			zz = (zz + 1) % (z * z)
		goto([zz // z, zz % z])
		harvest_queue.append(zz)
		hydrate()
		if plantme == Items.Wood:
			plant_wood()
			planted[zz] = Items.Wood
		if plantme == Items.Carrot:
			plant_a_carrot()
			planted[zz] = Items.Carrot
		if plantme == Items.Hay:
			plant_grass()
			planted[zz] = Items.Hay
		if num_unlocked(Unlocks.Polyculture) > 0:
			comp_queue = [get_companion()]
			while len(comp_queue) > 0 and comp_queue[len(comp_queue)-1] != None and comp_queue[len(comp_queue)-1][0] != None and comp_queue[len(comp_queue)-1][0] != Entities.Bush:
				while len(planted) - 1 < comp_queue[len(comp_queue)-1][1] * z + comp_queue[len(comp_queue)-1][2]:
					planted.append(None)
				if len(comp_queue[len(comp_queue)-1]) > 2 and planted[comp_queue[len(comp_queue)-1][1] * z + comp_queue[len(comp_queue)-1][2]] == None:
					harvest_queue.append(comp_queue[len(comp_queue)-1][1] * z + comp_queue[len(comp_queue)-1][2])
					companion_data = comp_queue[len(comp_queue) - 1]
					if companion_data != None and len(companion_data) > 0:
						goto([companion_data[1], companion_data[2]])
						if companion_data[0] == Entities.Carrots:
							plant_a_carrot()
							planted[companion_data[1] * z + companion_data[2]] = Items.Carrot
							comp_queue.append(get_companion())
						else:
							if companion_data[0] == Entities.Grass:
								planted[companion_data[1] * z + companion_data[2]] = Items.Hay
								plant_grass()
								comp_queue.append(get_companion())
							else:
								plant_wood()
								planted[companion_data[1] * z + companion_data[2]] = Items.Wood
								comp_queue.append(get_companion())
					else:
						comp_queue.append(None)
				else:
					comp_queue.append(None)
			#	print(comp_queue)
		#while (len(queue) == 0 and len(harvest_queue) > 0): # or (num_unlocked(Unlocks.Polyculture) > 0 and len(harvest_queue) > 0 and len(harvest_queue) > len(queue)):
		while (len(harvest_queue) > z * z / 1.5 and num_unlocked(Unlocks.Polyculture)>0) or (len(harvest_queue) > (z * z - 1) and num_unlocked(Unlocks.Polyculture)==0) or (len(harvest_queue) > 0 and num_items(orig) >= goal):
			goto([harvest_queue[0] // z, harvest_queue[0] % z])
			if can_harvest():
				while get_entity_type() != None and not can_harvest() and get_entity_type() != Entities.Grass:
					if num_unlocked(Unlocks.Fertilizer) > 0 and get_entity_type() != Entities.Bush:
						if num_items(Items.Fertilizer) == 0 and num_items(Items.Pumpkin) > 10:
							buy(Items.Fertilizer)
						if num_items(Items.Fertilizer) > 0:
							use_item(Items.Fertilizer)
					hydrate()
				harvest()
				planted[harvest_queue.pop(0)] = None
			else:
				if get_entity_type() == None:
					planted[harvest_queue[0]] = None
					harvest_queue.pop(0)
				else:
					harvest_queue.append(harvest_queue.pop(0))
		zz = get_pos_x() * z + get_pos_y()
	if num_items(orig) < goal:
		comp_plant(orig, goal)