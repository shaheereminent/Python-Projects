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
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').upper().split()

random_word = random.choice(words)

selected_letters = ""

assigned_index = ""

for l in random_word:
    selected_letters += "_"

duplicate = []

index_checker = 0

dup_container = 0

wrong_guess = 0

guess_count = 0

while guess_count < len(HANGMANPICS) and random_word != selected_letters:
    print(selected_letters)
    guess = input("Guess the letter: ").capitalize()
    
    if guess in selected_letters:
        index_checker += 1
        for d in range(random_word.index(guess) + index_checker, len(random_word)):
            if guess == random_word[d]:
                duplicate.append(d)
        selected_letters_list = list(selected_letters)
        selected_letters_list[duplicate[dup_container]] = guess
        selected_letters = "".join(selected_letters_list)
        dup_container += 1
        
    elif selected_letters == random_word:
        print(selected_letters)
    elif guess in random_word:
        selected_letters_list = list(selected_letters)
        assigned_index = selected_letters_list[random_word.index(guess)] = guess
        selected_letters = "".join(selected_letters_list)
    else:
        if wrong_guess == 0:
            print(HANGMANPICS[wrong_guess])
            wrong_guess += 1
        else:
            print(HANGMANPICS[wrong_guess])
            wrong_guess += 1
    
    guess_count += 1

if selected_letters == random_word:
    print(f"You won: Your guess {selected_letters} was right")
else:
    print(HANGMANPICS[-1])
    print("You lost")