import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('Choose Rock, Paper, or scissors.\n')

if computer_choice == user_choice:
   print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
   print("Rock beats Scissors, You WIN.")
elif user_choice == 'rock' and computer_choice == 'paper':
   print("Computer threw Paper over rock, YOU LOSE")
elif user_choice == 'scissors' and computer_choice == 'rock':
   print("Computer crsuhes scissors with a rock, YOU LOSE!")
elif user_choice == 'scissors' and computer_choice == 'paper':
   print("You cut through paper, YOU WIN!")
elif user_choice == 'paper' and computer_choice == 'scissors':
   print("Computer cuts through your paper with ease, YOU LOSE!")
elif user_choice == 'paper' and computer_choice == 'rock':
   print("You threw paper over a rock, YOU WIN!")
