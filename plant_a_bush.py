def plant_a_bush():
	if get_entity_type() != Entities.Bush:
		if get_entity_type() != None:
			while not can_harvest() and get_entity_type() != Entities.Grass:
				pass
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Bush)
		hydrate()	