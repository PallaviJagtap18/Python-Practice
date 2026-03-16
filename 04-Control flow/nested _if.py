# nested if
# nested if is a conditional structure where an if statement is placed inside another if statement to check additional conditions after the first condition is satisfied.

# example

num = int(input("enter any number between (1-30) :"))

if(num < 0 ):
    print("number is negative")
elif (0 < num <= 30 ):
    print("Positive number")
    if(num <= 10):
        print("number is in between (1-10)")
    elif(num <= 20):
        print("number is in between (11-20)")
    else:
        print("number is in between (21- 30)")
elif ( num > 30 ):
    print(" no is positive ")
    print("greater than 30")
else:
    print("num is zero")
