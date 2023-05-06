import utils
from intcode_computer import IntcodeComputer

program = [int(x) for x in utils.read_lines(5)[0].split(",")]

computer = IntcodeComputer()
computer.load_program_from_int_array(program)

computer.execute([1])