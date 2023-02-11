# changing a string
# changing a "raw string" to a "normalised string"
# but what is "normal"
# Author: MAry Metcalfe

raw_string = input("please enter a string: ")
normalised_string = raw_string.strip ().lower()

print ("{} is normalised to : {}".format( raw_string, normalised_string))

print ("the sting normalised is: {}".format(normalised_string))