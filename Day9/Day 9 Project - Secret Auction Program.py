# from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# from art import logo
# bidders = []
# def add_new_action(new_name, new_bid):
#   new_action = {}
#   new_action["name"] = new_name
#   new_action["bid"] = new_bid
#   bidders.append(new_action)

# print(logo)
# print("Welcome to the secret auction program.")
# result = True

# while result:
#   name = input("What is your name?: ")
#   bid = int(input("What's your bid?: $"))

#   add_new_action(name, bid)
#   situation = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

#   if situation == "yes":
#     result = True
#     clear()
#   elif situation == "no":
#     result = False

# temp = 0
# for bidder in bidders:
#   if bidder["bid"] > temp:
#     temp = bidder["bid"]
#     name = bidder["name"]

# print(f"The winner is {name} with a bid of ${temp}.")

##########

from replit import clear
from art import logo

print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_ record = {"Angela" : 123, "James" : 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?")
  price = int(input("What is your bir? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
