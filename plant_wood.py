def plant_wood():
	if (get_pos_x() + get_pos_y()) % 2 == 0 or not num_unlocked(Unlocks.Trees) > 0:
		plant_a_bush()
	else:
		plant_a_tree()