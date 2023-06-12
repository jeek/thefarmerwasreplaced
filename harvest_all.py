def harvest_all():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goto([i, j])
			harvest()