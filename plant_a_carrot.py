def plant_a_carrot():
	if get_entity_type() != Entities.Carrots:
		if get_entity_type() != None:
			while not can_harvest() and get_entity_type() != Entities.Grass:
				pass
			harvest()
		if num_items(Items.Carrot_Seed) == 0:
			buy(Items.Carrot_Seed)
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Carrots)