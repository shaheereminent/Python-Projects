import random

# Rule #1 Rock Wins Against Scissors
# Rule #2 Scissors win against Paper.
# Rule #3 Paper wins against rock.

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

# Player Taking Decision
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player = options[player_choice]

# Computer Taking Decision
computer = random.choice(options)

if player == options[0] and computer == options[2]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You won")
elif player == options[2] and computer == options[1]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You won")
elif player == options[1] and computer == options[0]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You won")
elif computer == options[0] and player == options[2]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You lose")
elif computer == options[2] and player == options[1]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You lose")
elif computer == options[1] and player == options[0]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n You lose")
elif computer == options[0] and player == options[0]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n It's a Tie")
elif computer == options[1] and player == options[1]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n It's a Tie")
elif computer == options[2] and player == options[2]:
    print(f"You chose {player_choice}:\n{player}\n Computer chose:\n{computer}\n It's a Tie")