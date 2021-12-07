from game_data import data
from art import logo, vs
from random import randint
from replit import clear

print(logo)
def rand_function():
  return randint(0, 49)

chosen1= data[rand_function()]

current_score = 0
is_continue = True
while is_continue:
  clear()
  print(logo)
  if current_score != 0:
    print(f"You're right! Current score: {current_score}.")    
  print(f"Compare A: {chosen1['name']}, {chosen1['description']}, {chosen1['country']}.")
  print(vs)
  chosen2 = data[rand_function()]
  print(f"Compare B: {chosen2['name']}, {chosen2['description']}, {chosen2['country']}.")

  who = input("Who has more followers? Type 'A' or 'B': ").lower()
  if who == "a":
    if chosen1["follower_count"] > chosen2["follower_count"]:
      current_score += 1
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {current_score}")
      is_continue = False
  elif who == "b":
    if chosen1["follower_count"] < chosen2["follower_count"]:
      chosen1 = chosen2
      current_score += 1
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {current_score}")
      is_continue = False
  else:
    print("You entered wrong. Please make the selection again")