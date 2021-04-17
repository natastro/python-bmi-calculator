# Project from https://theinsightfulcoder.com/5-more-python-projects-that-can-be-built-in-under-5-minutes

# Uses pounds and inches

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in lbs: "))
BMI = (weight / (height)**2) * 703

print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")