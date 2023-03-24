# Week 09 - Errors, testing and logging
# fibonacci sequence
# Author : Mary Metcalfe        
import logging
logging.basicConfig (level = logging.DEBUG)

def fibonacci (number):
    a = 0
    b = 1

    fibonacci_sequence = [0]
    for i in range (1, number):
        fibonacci_sequence.append(b)
        a, b=b, a+b
        logging.debug("%d:% 5s", number, fibonacci_sequence )
    if number == 0:
        return []
    if number <0:
        raise value_error ('Number must be > 0')  

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,1,2,3,5,8,13,21,34,55]

assert fibonacci (7) == return7
assert fibonacci (11) == return11
assert fibonacci (0) == []
assert fibonacci (0) ==[0]

#try:
  #  fibonacci (-1)
#except: value_error
#pass
    #else:
     #assert false , "fibonacci missing value_error"


    



#if _name_=='_main'
#print ("All Good")