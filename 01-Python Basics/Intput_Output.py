# 1. Output in Python
# The print() function is used to display text or values on the screen.

print("Hello World")
print("Welcome to Python Programming")

# 2. Input in Python
# The input() function is used to take input from the user.

name = input("Enter your name: ")
print("Hello", name)

# 3. Taking Numeric Input
# By default, input() stores data as a string, so we need to convert it to numbers using int() or float().

age = int(input("Enter your age: "))
print("Your age is:", age)

# 4. Multiple Inputs

# You can take multiple inputs from the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum is:", sum)

# 5. Formatted Output
# Python allows formatted output for better readability.

name = "Prajakta"
age = 20

print(f"My name is {name} and I am {age} years old.")
