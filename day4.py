min = 108457
max = 562041

effective_min = 111111
effective_max = 559999

how_many_passwords = 0

for candidate in range(effective_min, effective_max + 1):
	candidate_string = str(candidate)

	non_decreasing_digits = True

	for c in range(len(candidate_string)-1):
		if int(candidate_string[c+1]) < int(candidate_string[c]):
			non_decreasing_digits = False		

	if not non_decreasing_digits:
		continue

	idx = 0
	has_sequence_of_exactly_2_equal_digits = False

	while idx < len(candidate_string):
		current_digit = candidate_string[idx]
		seq_length = 0
		while idx < len(candidate_string) and candidate_string[idx] == current_digit:
			idx += 1
			seq_length += 1
		if seq_length == 2:
			has_sequence_of_exactly_2_equal_digits = True
			break
		
	if not has_sequence_of_exactly_2_equal_digits:
		continue
	
	how_many_passwords += 1

print(how_many_passwords)

