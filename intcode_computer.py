from typing import List

class IntcodeComputer:
	def __init__(self):
		self.program = []

	def load_program_from_string(self, tape: str):
		self.program = [int(x) for x in tape.split(",")]

	def load_program_from_int_array(self, program: List[int]):
		self.program = [address for address in program]

	def print_program(self):
		print(self.program)

	def execute(self):
		instruction_pointer = 0
		op_code = self.program[instruction_pointer]

		while(op_code != 99):
			if op_code == 1:
				p1, p2, p3 = self.program[instruction_pointer + 1 : instruction_pointer + 4]
				self.program[p3] = self.program[p1] + self.program[p2]
				instruction_pointer += 4
			elif op_code == 2:
				p1, p2, p3 = self.program[instruction_pointer + 1 : instruction_pointer + 4]
				self.program[p3] = self.program[p1] * self.program[p2]
				instruction_pointer += 4
			op_code = self.program[instruction_pointer]

	def get_address(self, address: int):
		return self.program[address]

	def set_address(self, address: int, value: int):
		self.program[address] = value
