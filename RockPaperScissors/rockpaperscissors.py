# ROCK PAPER SCISSORS
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

game_image = [rock, paper, scissors]

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number You lose!")
else:
    print(f"you chose: \n {game_image[player_choice]}")

computer_choice = random.randint(0, 2)

print(f"Computer chose: \n {game_image[computer_choice]}")


if player_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose")
elif computer_choice == player_choice:
    print("It is a draw")
else:
    print("You lose!")
