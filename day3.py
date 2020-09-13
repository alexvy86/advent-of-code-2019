import utils

wire_paths = utils.read_lines(3)

x_step = {"U": 0, "D": 0, "R": 1, "L": -1}
y_step = {"U": 1, "D": -1, "R": 0, "L": 0}

visited = set()
intersections = set()
steps_wire_1 = {}
steps_wire_2 = {}

path_1 = wire_paths[0]
current_x = current_y = steps = 0
for direction, distance in ((instruction[0], int(instruction[1:])) for instruction in path_1.split(",")):
	for _ in range(distance):
		current_x += x_step[direction]
		current_y += y_step[direction]
		steps += 1
		visited.add((current_x, current_y))
		if (current_x, current_y) not in steps_wire_1:
			steps_wire_1[(current_x, current_y)] = steps

path_2 = wire_paths[1]
current_x = current_y = steps = 0
for direction, distance in ((instruction[0], int(instruction[1:])) for instruction in path_2.split(",")):	
	for _ in range(distance):
		current_x += x_step[direction]
		current_y += y_step[direction]
		steps += 1
		if (current_x, current_y) in visited:
			intersections.add((current_x, current_y))
		if (current_x, current_y) not in steps_wire_2:
			steps_wire_2[(current_x, current_y)] = steps

best_distance = best_sum_of_steps = 1e10
for candidate in intersections:
	distance = abs(candidate[0]) + abs(candidate[1])
	best_distance = min(best_distance, distance)
	best_sum_of_steps = min(best_sum_of_steps, steps_wire_1[candidate] + steps_wire_2[candidate])

print(best_distance)
print(best_sum_of_steps)