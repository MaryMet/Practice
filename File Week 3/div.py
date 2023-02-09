# this was supposed to be fast
# division
# Author : Mary Metcalfe

a = int (input ("please enter first number: "))
b = int (input ("please enter the number that you want to divide into the first number: "))

answer = int (a//b)
remainder = a%b


print ("{} divided by {} is {} with remainder {}" .format(a, b, answer, remainder))