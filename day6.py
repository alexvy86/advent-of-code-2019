import utils

map = dict()
for line in utils.read_lines(6):
	orbitted, orbitting = line.split(")")
	if orbitted not in map:
		map[orbitted] = []
	map[orbitted].append(orbitting)

def count_orbits(center, current_level):
	orbit_count = 0
	if center in map:
		orbit_count += current_level * len(map[center])
		for orbitting in map[center]:
			orbit_count += count_orbits(orbitting, current_level + 1)
	return orbit_count

total_orbits = count_orbits("COM", 1)
print(total_orbits)