import random

words = ['abyss','blackbird','attention','euphoria','nightcrawler','imagination','renaissance']

stick_figure_states = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def letter_placement(guessed_letters, wadissit):
    for char in wadissit:
        if char in guessed_letters: #if the letter the user guessed is in the original word, then we reveal the position of that particular letter in the word
            print(char, end=' ')
        else:
            print('_', end=' ')
    print()

def game():
    wadissit = random.choice(words)
    guessed_letters = []
    lives = 6

    print("let's get started!")
    letter_placement(guessed_letters, wadissit)#using this function on an empty list shows the number of letters in the word to the user

    while lives > 0:
        letter = input('guess a letter: ').lower()

        if not letter.isalpha() or len(letter) != 1: #makin sure the user only enters one LETTER and is not entering any numbers
            print("please enter a single valid letter.")
            continue

        if letter in guessed_letters: #makes sure blind users dont enter the same letter that they guessed before cuz even if the letter repeats, the position of those letters is revealed the first try itself
            print("you already guessed that letter.")
            continue

        if letter in wadissit:
            guessed_letters.append(letter)
            print("correct!")
        else:
            guessed_letters.append(letter)
            print("wrong!")
            lives -= 1
            print(stick_figure_states[6 - lives]) #if the guessed letter is wrong, the stick figure starts to materialize

        letter_placement(guessed_letters, wadissit)

        # checkin winnin condition
        if all(char in guessed_letters for char in wadissit):
            print("yaayy! you guessed the word:", wadissit)
            break
    else:
        print("ahhhh ya lost! the word was:", wadissit)

if __name__ == "__main__":
    game()
