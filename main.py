def main():
	bootstrap()
	max_x = 1
	max_y = 1
	while True:
		goal = goals()
		goal = [goal, num_unlocked(goal) + 1]
		goal_cost_src = get_cost(goal[0])
		goal_cost = []
		z = 0
		zz = 0
		for i in goal_cost_src:
			if i[0] == Items.Power:
				z += 1
				zz += i[1]
			else:
				for j in get_cost(i[0]):
					if j[0] == Items.Power:
						z += 1
						zz += j[1]
					if num_unlocked(Unlocks.Sunflowers) > 0: # and get_world_size() >= 6:
						z += 1
					goal_cost.append([j[0], j[1] * i[1]])
			if num_unlocked(Unlocks.Sunflowers) > 0: # and get_world_size() >= 6:
				z += 1
			goal_cost.append(i)
		if z > 0:
			goal_cost.insert(0, [Items.Power, 500 + z * 100 + zz])
		print(goal)
		print(goal_cost)
		if num_unlocked(goal[0]) < goal[1]:
			#print(goal, goal_cost)
			for goal_line in goal_cost:
				if num_unlocked(goal[0]) < goal[1]:
					unlock(goal[0])
				if num_items(goal_line[0]) < goal_line[1]:
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
						comp_plant(plantme, goal_line[1])
					else:
						if plantme == Items.Pumpkin:
							plant_a_pumpkin()
						else:
							if plantme == Items.Power:
								real_power(goal_line[1])
							else:
								if plantme == Items.Gold:
									maze(my_x, my_y)
			if num_unlocked(goal[0]) < goal[1]:
				unlock(goal[0])
			goal_cost = get_cost(goal[0])
		if num_unlocked(Unlocks.Reset) > 0:
			reset()
			max_x = 1
			max_y = 1
			