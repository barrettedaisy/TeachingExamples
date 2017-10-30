# guessing game   

import random

def main():
    #generate random number
    mystery = random.randint(1,100)

    print("I'm thinking of a number between 1 and 100.")
    guess = int( input("Guess a number: ") )

    #this loop keeps going til they guess the correct number
    while guess != mystery:

        if guess > mystery:
            print("too high")
            
        else:
            print("too low")
            
        #have the user guess again
        #change the variable to their new guess
        guess = int( input("Guess a number: ") )
        
    #we only get to this code once guess is equal to the mystery number
    print("You got it! The number was", mystery)


#call the main function to start the program
main()
    
