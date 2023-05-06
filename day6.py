import utils

map = dict()
orbit_to_center = dict()

for line in utils.read_lines(6):
	orbitted, orbitting = line.split(")")
	if orbitted not in map:
		map[orbitted] = []
	map[orbitted].append(orbitting)

	orbit_to_center[orbitting] = orbitted

def count_orbits(center, current_level):
	orbit_count = 0
	if center in map:
		orbit_count += current_level * len(map[center])
		for orbitting in map[center]:
			orbit_count += count_orbits(orbitting, current_level + 1)
	return orbit_count

total_orbits = count_orbits("COM", 1)
print(total_orbits)

path_from_YOU = dict()

current_object = orbit_to_center["YOU"]
distance_to_YOU = 0
while current_object != "COM":
	path_from_YOU[current_object] = distance_to_YOU
	current_object = orbit_to_center[current_object]
	distance_to_YOU += 1

current_object = orbit_to_center["SAN"]
distance_from_SAN_to_path_from_YOU = 0
while current_object not in path_from_YOU:
	current_object = orbit_to_center[current_object]
	distance_from_SAN_to_path_from_YOU += 1

print(path_from_YOU[current_object] + distance_from_SAN_to_path_from_YOU)

