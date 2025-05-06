import random

three_choices = ['rock','paper','scissors'] #creatin a list which has the three obvious choices in this game

def comp_choice():
    my_choice = random.choice(three_choices) #choosin one random word among those three for the computer to play with 
    return my_choice

def game(ur_choice,my_choice):
    if ur_choice.lower() == 'rock' and my_choice == 'paper':
        print("Paper beats rock and YOU LOSE")
    elif ur_choice.lower() == 'rock' and my_choice == 'scissors':
        print("well rock beats scissors. so YOU WIN")
    elif ur_choice.lower() == 'paper' and my_choice == 'rock':
        print('Paper beats rock so YOU WIN')
    elif ur_choice.lower() == 'paper' and my_choice == 'scissors':
        print('Scissors cut through paper so YOU LOSE')
    elif ur_choice.lower() == 'scissors' and my_choice == 'rock':
        print("Rock beats paper, YOU LOSE")
    elif ur_choice.lower() == 'scissors' and my_choice == 'paper':
        print("Scissors beat paper, YOU WIN")
    else:
        print("Nothing happens here, so let's just move on")

if __name__ == "__main__":
    my_choice = comp_choice()
    ur_choice = input("Rock paper scissor shoot : ")
    game(ur_choice,my_choice)
