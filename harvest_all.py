def harvest_all():
	while num_items(Items.Power) >= 1 and get_active_power() < 5:
		use_item(Items.Power)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goto([i, j])
			harvest()