import random

roll = random.randint(1,10)

guess = int(input('Guess the roll:\n'))

if guess == roll:
   print("You guessed correctly! The roll was " + str(roll) + "!")
else:
   print("Your guess of " + str(guess) + " was incorrect. The roll was " + str(roll) + "!")

# print("The computer rolled a " + str(roll))