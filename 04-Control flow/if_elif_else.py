# if elif else

# if – A conditional statement used to execute a block of code when a specified condition is True.
# elif – Short for “else if”; used to check another condition if the previous if condition is False.
# else – Executes a block of code when none of the above conditions are True.

# Example 1

num = int(input("enter the number:  "))

if(num > 0):
    print("Positive number")
elif( num == 0 ):
    print("Number is zero")
else:
    print("Negative number")

# Example 2 

import time 
hour = int(time.strftime('%H))
if (hour<12)
    print("Good Morning")
elif(hour<17):
    print("Good Afternoon")
else:
    print("Good Evening")
