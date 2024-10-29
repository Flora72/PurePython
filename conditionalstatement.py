# python script that checks if a number is even or odd

num=int(input("Enter number"))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


# create a program that prints the largest of three numbers
num2=int(input("Enter the first number"))
num3=int(input("Enter the second number"))
num4=int(input("Enter the third number"))

if (num2 >= num3) and (num2 >= num4):
   largest = num2
elif (num3 >= num2) and (num3 >= num4):
   largest = num3
else:
   largest = num4

print("The largest number is", largest)

