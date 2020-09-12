import utils

tape = [int(x) for x in utils.read_lines(2)[0].split(",")]

# print(tape)

# Init to "1202 program alarm" state
tape[1] = 12
tape[2] = 2

# Execute program
current_index = 0
current_op_code = tape[current_index]

while(current_op_code != 99):
	pos1 = tape[current_index + 1]
	pos2 = tape[current_index + 2]
	pos3 = tape[current_index + 3]
	if current_op_code == 1:
		tape[pos3] = tape[pos1] + tape[pos2]
	elif current_op_code == 2:
		tape[pos3] = tape[pos1] * tape[pos2]
	current_index += 4
	current_op_code = tape[current_index]

print(tape[0])