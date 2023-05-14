def main():
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
	max_x = 1
	max_y = 1
	while True:
		goal = goals()
		goal = [goal, num_unlocked(goal) + 1]
		goal_cost_src = get_cost(goal[0])
		goal_cost = []
		for i in goal_cost_src:
			for j in get_cost(i[0]):
				if num_unlocked(Unlocks.Sunflowers) > 0 and get_world_size() >= 6:
					goal_cost.append([Items.Power, 100])
				goal_cost.append([j[0], j[1] * i[1]])
			if num_unlocked(Unlocks.Sunflowers) > 0 and get_world_size() >= 6:
				goal_cost.append([Items.Power, 100])
			goal_cost.append(i)			
		while num_unlocked(goal[0]) < goal[1]:
			for goal_line in goal_cost:
				if num_unlocked(goal[0]) < goal[1]:
					unlock(goal[0])
				while num_items(goal_line[0]) < goal_line[1]:
					plantme = goal_line[0]
					my_x = get_pos_x()
					my_y = get_pos_y()
					if num_unlocked(Unlocks.Expand) > 0:
						if num_unlocked(Unlocks.Expand) == 1:
							max_x = 1
							max_y = 3
						else:
							max_x = get_world_size()
							max_y = get_world_size()
					if plantme == Items.Carrot or plantme == Items.Wood or plantme == Items.Hay:
						comp_plant(plantme)
					else:
						if plantme == Items.Pumpkin:
							plant_a_pumpkin()
						else:
							if plantme == Items.Power:
								real_power()
							else:
								if plantme == Items.Gold:
									harvest_all()
									goto([my_x, my_y])
									while num_items(Items.Fertilizer) < 100:
										buy(Items.Fertilizer)
									goto([my_x, my_y])
									plant_a_bush()
									goto([my_x, my_y])
									while get_entity_type() == Entities.Bush:
										use_item(Items.Fertilizer)
									if get_entity_type() != Entities.Bush:
										maze()
			if num_unlocked(goal[0]) < goal[1]:
				unlock(goal[0])
			goal_cost = get_cost(goal[0])
		if num_unlocked(Unlocks.Reset) > 0:
			reset()
			max_x = 1
			max_y = 1
			