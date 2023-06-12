def buy(item):
	good = False
	while not good:
		good = True
		for cost_entry in get_cost(item):
			while cost_entry[0] == Items.Hay and num_items(Items.Hay) < cost_entry[1]:
				good = False
				plant_grass()
				while not can_harvest():
					pass
				harvest()
			if cost_entry[0] == Items.Carrot and num_items(Items.Carrot) < cost_entry[1]:
				good = False
				plant_a_carrot()
				while not can_harvest():
					pass
				harvest()
			if cost_entry[0] == Items.Wood and num_items(Items.Wood) < cost_entry[1]:
				good = False
				plant_wood()
				while not can_harvest():
					pass
				harvest()
			if cost_entry[0] == Items.Pumpkin and num_items(Items.Pumpkin) < cost_entry[1]:
				good = False
				plant_a_pumpkin()
	trade(item)					