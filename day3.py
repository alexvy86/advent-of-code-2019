import utils

wire_paths = utils.read_lines(3)

visited = set()
intersections = set()

path_1 = wire_paths[0]
current_x = current_y = 0
for instruction in path_1.split(","):
	direction = instruction[0]
	distance = int(instruction[1:])
	if direction == "U":
		for _ in range(distance):
			current_y += 1
			visited.add((current_x, current_y))
	elif direction == "R":
		for _ in range(distance):
			current_x += 1
			visited.add((current_x, current_y))
	elif direction == "D":
		for _ in range(distance):
			current_y -= 1
			visited.add((current_x, current_y))
	elif direction == "L":
		for _ in range(distance):
			current_x -= 1
			visited.add((current_x, current_y))

path_2 = wire_paths[1]
current_x = current_y = 0
for instruction in path_2.split(","):
	direction = instruction[0]
	distance = int(instruction[1:])
	if direction == "U":
		for _ in range(distance):
			current_y += 1
			if (current_x, current_y) in visited:
				intersections.add((current_x, current_y))
	elif direction == "R":
		for _ in range(distance):
			current_x += 1
			if (current_x, current_y) in visited:
				intersections.add((current_x, current_y))
	elif direction == "D":
		for _ in range(distance):
			current_y -= 1
			if (current_x, current_y) in visited:
				intersections.add((current_x, current_y))
	elif direction == "L":
		for _ in range(distance):
			current_x -= 1
			if (current_x, current_y) in visited:
				intersections.add((current_x, current_y))

answer = 1e10
for candidate in intersections:
	distance = abs(candidate[0]) + abs(candidate[1])
	answer = min(answer, distance)

print(answer)