# messing with numpy
# salaries
# Author: Mary Metcalfe

import numpy as np

min_salary = 20000
max_salary = 80000
no_of_entries = 10

salaries = np.random.randint(min_salary,max_salary,no_of_entries)

salaries_plus = salaries + 5000

salaries_mult = salaries * 1.05

new_salaries = salaries_mult.astype(int)

print (salaries)
print (salaries_plus)
print (salaries_mult)
print (new_salaries)