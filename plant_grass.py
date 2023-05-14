def plant_grass():
	if get_entity_type() != Entities.Grass:
		if get_entity_type() != None:
			while not can_harvest():
				pass
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()