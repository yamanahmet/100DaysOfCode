import random
from art import logo 
print(logo)

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
chosen = input("Chose a difficulty. Type 'easy' or 'hard': ")

if chosen == "easy":
  attempt = 10
elif chosen == "hard":
  attempt = 5
computer_choice = random.randint(1, 100)
is_continue = True

while attempt > 0 and is_continue:
  guess = int(input("Make a guess: "))
  #random vs chosen
  if guess == computer_choice:
    # is_finish  = True
    is_continue = False
    print("You Win!")
  elif guess > computer_choice:
    print("Too high.\nGuess again.")
    attempt -= 1
    print(f"You have {attempt} attemps remaining to guess the number.")
  elif guess < computer_choice:
    print("Too low.\nGuess again.")
    attempt -= 1
    print(f"You have {attempt} attemps remaining to guess the number.")    

if attempt == 0:
  print("You've run out of guesses, you lose.")