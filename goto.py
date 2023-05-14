def goto(location):
	while get_pos_x() != location[0]:
		move(East)
	while get_pos_y() != location[1]:
		move(North)