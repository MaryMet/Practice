# print out 10 random numbers
# print out top three numbers
# lists
# Author: Mary Metcalfe

import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers = []

for i in range (0, how_many) :
    numbers.append (random.randint(range_from, range_to))

print (f"{how_many} random numbers\t\n {numbers}")

top_how_many = numbers.sort(reverse = True)

top_ones = numbers.copy



print(f"The top three digits are: ")
#print ("The top {top_how_many} are\t\t{top_one: [top_how_many]}")