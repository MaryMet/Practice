# the guessing game using while loop
# Author : Mary Metcale

number_to_guess = 30

guess = int(input ("Please guess a number : "))

while guess != number_to_guess :
    if guess < number_to_guess :
        print ("Wrong Answer - too low")
    else :
        print ("Wrong Answer - too High")
    guess = int (input ("Please guess again : "))

print (" Correct. Your guess was correct" ,number_to_guess)
