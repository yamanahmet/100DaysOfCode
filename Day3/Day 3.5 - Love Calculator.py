# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name3 = name1 + name2
lower_case_name3 = name3.lower()

score1 = 0
score2 = 0

score1 += lower_case_name3.count("t")
score1 += lower_case_name3.count("r")
score1 += lower_case_name3.count("u")
score1 += lower_case_name3.count("e")

score2 += lower_case_name3.count("l")
score2 += lower_case_name3.count("o")
score2 += lower_case_name3.count("v")
score2 += lower_case_name3.count("e")

love_score = int(str(score1) + str(score2))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
