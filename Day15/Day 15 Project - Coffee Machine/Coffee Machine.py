MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

total = 0
is_continue = True
while (choice == "espresso" or choice == "latte" or choice == "cappuccino") and is_continue:
  print("Please insert coins.")
  quartes = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total += quartes * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
  drink_cost = MENU[choice]["cost"]
  # print(f"Total: {total}") 
  # print(f"Dirink cost: {drink_cost}")
  total -= drink_cost

  if total > 0:
    print(f"Here is ${round(total,2)} in change.")
    print(f"Here is your {choice} ☕. Enjoy! \n")
  else:
    print("Sorry that's not enough money. Money refunded.")
    
  choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

  #Not enought

  resources["water"] -= MENU[choice]["ingredients"]["water"]
  resources["milk"] -= MENU[choice]["ingredients"]["milk"]
  resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
  
  if resources["water"] < 0:
    print("Sorry there is not enough water.")
  elif resources["milk"] < 0:
    print("Sorry there is not enough milk.")
  elif resources["coffee"] < 0:
    print("Sorry there is not enough coffee.")
