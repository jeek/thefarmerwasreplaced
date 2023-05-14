def handle_companion(companion_data):
	if companion_data == None or len(companion_data) < 1:
		return
	goto([companion_data[1], companion_data[2]])
	if companion_data[0] == Entities.Carrots:
		plant_a_carrot()
	else:
		if companion_data[0] == Entities.Bush:
			plant_a_bush()
		else:
			if companion_data[0] == Entities.Tree:
				plant_a_tree()
			else:
				if companion_data[0] == Entities.Grass:
					plant_grass()