def goto(location):
	location[0] = location[0] % get_world_size()
	if location[0] != get_pos_x():
		queue = []
		if location[0] < get_pos_x():
			queue.append([get_pos_x() - location[0], West])
			queue.append([location[0] + get_world_size() - get_pos_x(), East])
		if location[0] > get_pos_x():
			queue.append([location[0] - get_pos_x(), East])
			queue.append([get_pos_x() - location[0] + get_world_size(), West])
		i = 1
		while i < len(queue):
			if queue[i][0] < queue[0][0]:
				queue.insert(0, queue.pop(i))
			i += 1
		while get_pos_x() != location[0]:
			move(queue[0][1])
	location[1] = location[1] % get_world_size()
	if location[1] != get_pos_y():
		queue = []
		if location[1] < get_pos_y():
			queue.append([get_pos_y() - location[1], South])
			queue.append([location[1] + get_world_size() - get_pos_y(), North])
		if location[1] > get_pos_y():
			queue.append([location[1] - get_pos_y(), North])
			queue.append([get_pos_y() - location[1] + get_world_size(), South])
		i = 1
		while i < len(queue):
			if queue[i][0] < queue[0][0]:
				queue.insert(0, queue.pop(i))
			i += 1
		while get_pos_y() != location[1]:
			move(queue[0][1])