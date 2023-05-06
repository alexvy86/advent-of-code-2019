min = 108457
max = 562041

effective_min = 111111
effective_max = 559999

how_many_passwords = 0

for candidate in range(effective_min, effective_max + 1):
	candidate_string = str(candidate)

	meets_criteria = True

	adjacent_equal_digits = False
	
	for c in range(len(candidate_string)-1):
		if int(candidate_string[c+1]) < int(candidate_string[c]):
			meets_criteria = False		
		
		adjacent_equal_digits |= candidate_string[c+1] == candidate_string[c]
	
	if not adjacent_equal_digits:
		meets_criteria = False

	if meets_criteria:
	  how_many_passwords += 1

print(how_many_passwords)

