# Match–Case 
# It is used to compare a value against multiple patterns and execute the matching block of code, similar to a switch-case statement in other programming languages.

x= int(input("enter any number : "))

match x:

    case 0:
        print("value of x is 0")
    case 1:
        print("value of x is 1")
    case 2:
        print("value of x is 2")
    case 3:
        print("value of x is 3")
    case _ :
        print("invalid")
