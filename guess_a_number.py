#the task is to write a code that generates a random number and the user has to guess it
#the user gets 5 lives
#if the guessed number is lesser or greater than the actual number, then the code says it and the user loses 1 life
#if the guessed number is correct, then the user wins or if he's out of lives, he loses

import random

def game():
    
    actual_number = random.randint(1,100) #restricting the range of the number generated from 1 to 100 so that it gives the user a bit of edge
    
    
    lives = 5
    
    
    while lives > 0:
        guessed_number = int(input("guess a number between 1 to 100: "))

        if guessed_number == actual_number:
            print("yaay! ya win ")
            return
        elif guessed_number < actual_number:
            print("nah man, try something higher than that.")
        else:
            print("nah, try something lower than that.")
        
        lives -= 1
    
    print(f"ya lose! the number was {actual_number}.")

if __name__ == "__main__":
    game()
