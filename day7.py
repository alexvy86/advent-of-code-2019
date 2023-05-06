from itertools import permutations 
from intcode_computer import IntcodeComputer

import utils

program = [int(x) for x in utils.read_lines(7)[0].split(",")]

computer = IntcodeComputer(print_outputs=False)

max_thruster_signal = 0

for sequence in permutations(range(0, 5)):
	computer.load_program_from_int_array(program)
	outputs = computer.execute([sequence[0], 0])

	computer.load_program_from_int_array(program)
	outputs = computer.execute([sequence[1], outputs[0]])

	computer.load_program_from_int_array(program)
	outputs = computer.execute([sequence[2], outputs[0]])

	computer.load_program_from_int_array(program)
	outputs = computer.execute([sequence[3], outputs[0]])

	computer.load_program_from_int_array(program)
	outputs = computer.execute([sequence[4], outputs[0]])

	max_thruster_signal = max(max_thruster_signal, outputs[0])

print(max_thruster_signal)