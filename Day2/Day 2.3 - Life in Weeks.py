# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

years_remaing = 90 - age_as_int
days_remaing = years_remaing * 365
weeks_remaing = years_remaing * 52
months_remaing = years_remaing * 12

message = f"You have {days_remaing} days, {weeks_remaing} weeks, and {months_remaing} months left."

print(message)
