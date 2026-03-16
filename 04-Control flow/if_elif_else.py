# if elif else

# if – A conditional statement used to execute a block of code when a specified condition is True.
# elif – Short for “else if”; used to check another condition if the previous if condition is False.
# else – Executes a block of code when none of the above conditions are True.

num = int(input("enter the number:  "))

if(num > 0):
    print("Positive number")
elif( num == 0 ):
    print("Number is zero")
else:
    print("Negative number")