def hydrate():
	#while num_unlocked(Items.Fertilizer) > 0 and num_items(Items.Fertilizer) * 50 < num_items(Items.Pumpkin):
	#	buy(Items.Fertilizer)
	while (get_entity_type() == Entities.Sunflower or get_water() < .25) and get_entity_type() != None and get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Grass and get_entity_type() != Entities.Bush and not can_harvest() and num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
	while num_items(Items.Water_Tank) > num_items(Items.Empty_Tank) and get_water() <= .75:
		use_item(Items.Water_Tank)