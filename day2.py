import utils
from intcode_computer import IntcodeComputer

program = [int(x) for x in utils.read_lines(2)[0].split(",")]

computer = IntcodeComputer()
computer.load_program_from_int_array(program)

# Init to "1202 program alarm" state
computer.set_address(1, 12)
computer.set_address(2, 2)

computer.execute()

print(computer.get_address(0))

computer = IntcodeComputer()
for noun, verb in ((i, j) for i in range(0,100) for j in range(0,100)):
	print(f"Processing ({noun},{verb})")
	computer.load_program_from_int_array(program)
	computer.set_address(1, noun)
	computer.set_address(2, verb)

	computer.execute()

	if computer.get_address(0) == 19690720:
		print(f"{noun}, {verb} - {100*noun + verb}")
		break
