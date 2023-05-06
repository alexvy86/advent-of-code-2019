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

	def execute(self, inputs: List[int] = []):
		instruction_pointer = 0
		op_code = self.program[instruction_pointer]

		while(op_code != 99):
			op_code = self.program[instruction_pointer]
			param_modes = list(str(op_code // 100))
			param_modes.reverse()
			op_code = op_code % 100

			#print(f"op_code: {op_code}")
			if op_code == 1:
				params = self._get_parameter_values(2, instruction_pointer)
				output_address = self.program[instruction_pointer + 3]
				self.program[output_address] = params[0] + params[1]
				instruction_pointer += 4
			
			elif op_code == 2:
				params = self._get_parameter_values(2, instruction_pointer)
				output_address = self.program[instruction_pointer + 3]
				self.program[output_address] = params[0] * params[1]
				instruction_pointer += 4
			
			elif op_code == 3:
				p1 = self.program[instruction_pointer + 1]
				self.program[p1] = inputs[0]
				inputs.pop(0)
				instruction_pointer += 2
			
			elif op_code == 4:
				params = self._get_parameter_values(1, instruction_pointer)
				print(params[0])
				instruction_pointer += 2

			elif op_code == 5:
				params = self._get_parameter_values(2, instruction_pointer)
				instruction_pointer = params[1] if params[0] != 0 else instruction_pointer + 3
				
			elif op_code == 6:
				params = self._get_parameter_values(2, instruction_pointer)
				instruction_pointer = params[1] if params[0] == 0 else instruction_pointer + 3
				
			elif op_code == 7:
				params = self._get_parameter_values(2, instruction_pointer)
				output_address = self.program[instruction_pointer + 3]
				self.program[output_address] = 1 if params[0] < params[1] else 0
				instruction_pointer += 4

			elif op_code == 8:
				params = self._get_parameter_values(2, instruction_pointer)
				output_address = self.program[instruction_pointer + 3]
				self.program[output_address] = 1 if params[0] == params[1] else 0
				instruction_pointer += 4

	def get_address(self, address: int):
		return self.program[address]

	def set_address(self, address: int, value: int):
		self.program[address] = value

	def _get_parameter_values(self, num_params, ip):
		params = self.program[ip + 1 : ip + 1 + num_params]
		param_modes = list(str(self.program[ip] // 100))
		param_modes.reverse()
		for i in range(len(params)):	
			if i >= len(param_modes) or param_modes[i] == "0":
				params[i] = self.program[params[i]]
		return params