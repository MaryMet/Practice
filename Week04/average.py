# so we will input numbers
# until the user enters a 0
# then we print them out
# and their average
# Author : MAry Metcalfe

numbers = []

number = int(input("enter number (0 to quit) : " ))

while number != 0:
    numbers.append(number)

    number = int (input ("enter another (0 to quit) : "))

for value in numbers :
    print (value)

average = float(sum(numbers)/len(numbers))

print (f"The average is {average}")