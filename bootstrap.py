def bootstrap():
	while num_items(Items.Hay) < 20:
		while not can_harvest():
			pass
		harvest()
	unlock(Unlocks.Speed)
	while num_items(Items.Hay) < 30:
		while not can_harvest():
			pass
		harvest()
	unlock(Unlocks.Expand)
	while num_items(Items.Hay) < 50:
		if can_harvest():
			harvest()
		move(North)
	unlock(Unlocks.Plant)
	while num_items(Items.Wood) < 20:
		if can_harvest():
			harvest()
		plant_a_bush()
		move(North)
	unlock(Unlocks.Expand)