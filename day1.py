import functools
from utils import read_lines

def get_fuel_req_for_mass(mass):
  return mass//3 - 2

def get_module_fuel_req(module_mas):
	result = get_fuel_req_for_mass(module_mas)
	leftover = result
	while leftover > 0:
		next_additional_fuel = get_fuel_req_for_mass(leftover)
		if next_additional_fuel >= 0:
			result += next_additional_fuel
		leftover = next_additional_fuel
	
	return result

masses = read_lines(1)
fuel_reqs = (get_module_fuel_req(int(x)) for x in masses)
total_fuel_mass = functools.reduce(lambda x,y: x + y, fuel_reqs, 0)
print(total_fuel_mass)
