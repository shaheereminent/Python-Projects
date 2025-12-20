import random

HANGMANPICS = ['''
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
========='''
]

# List of words
word_list = ["Witches", "Snitches", "Bitches"]

# Choosing random word from the list of words
chosen_word = random.choice(word_list).lower()

# Printing chosen word
print(chosen_word)

# Creating placeholder to display
placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

hangman_lives = len(HANGMANPICS) 


# Initializing Game State Once False Game will End.
game_state = True

# Keeping list of already added letters in the display
prev_state = []

# Asking while hangman live exist
while game_state: 
    # Asking player to guess a letter
    guessed_letter = input("Guess a letter: ").lower()
    
    # Checking if guessed letter by player is a letter not a number. ~ If number ask again
    while not guessed_letter.isalpha():
        guessed_letter = input("Guess a letter: ").lower()
        
    # Creating display to show player if he guessed the right letter and where it occurs
    display = ""    
    
    # Check if the guessed letter is in the word; reveal it in the display, otherwise show _.
    for letter in chosen_word:
        if guessed_letter == letter:
            display += letter
            prev_state.append(letter)
        elif letter in prev_state:
            display += letter
        else:
            display += "_"
        
    if guessed_letter not in chosen_word:
        print(HANGMANPICS[-hangman_lives])
        hangman_lives -= 1
        if hangman_lives < 1:
            game_state = False
            print("You made the man hanged!")
    elif "_" not in display:
        print("You won")
        game_state = False
    
    print(display)
        