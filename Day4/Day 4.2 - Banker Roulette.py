# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

number_of_people = len(names)

chosen_person = names[random.randint(1, number_of_people) - 1]

print(f"{chosen_person} is going to buy the meal today!")
