def plant_a_tree():
	if get_entity_type() != Entities.Tree:
		if get_entity_type() != None:
			while not can_harvest() and get_entity_type() != Entities.Grass:
				pass
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()
		plant(Entities.Tree)
		use_item(Items.Water_Tank)