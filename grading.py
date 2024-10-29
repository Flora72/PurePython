# create a program that checks a student performance
marks=int(input("Enter Marks"))

if 100 >= marks >= 80:
      print("You have an A")
elif 79 >= marks >=60:
     print("You have an B")
elif marks<=59 and marks>=40:
    print("You have an C")
elif marks <=39 and marks>=0:
    print("You have failed")
else:
    print("invalid Marks")

# create a program that is going to calculate BMI

# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display the result
print(f"\nYour BMI is: {round(bmi, 2)}")
print(f"Category: {category}")
