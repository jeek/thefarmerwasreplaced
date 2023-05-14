def maze():
	while num_items(Items.Power) >= 1 and get_active_power() < 10:
		use_item(Items.Power)
	directions = [North, East, South, West]
	z = 0
	while get_entity_type() != Entities.Treasure:
		my_x = get_pos_x()
		my_y = get_pos_y()
		move(directions[z % 4])
		if z > 2000:
			return
		if my_x != get_pos_x() or my_y != get_pos_y():
			z += 1
		else:
			z += 3
	harvest()
