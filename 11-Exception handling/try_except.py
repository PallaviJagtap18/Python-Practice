# try / except

# The try block contains code that may raise an exception.
# The except block handles the error.

# Syntax

# try:
#     # risky code
# except ExceptionType:
#     # handling code

# Example

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")