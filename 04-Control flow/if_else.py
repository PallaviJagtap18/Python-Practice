# # if else
# # Conditional statement used to execute one block of code if a condition is True and another block of code if the condition is False.

# Example 1 

age= int(input("enter your age:"))
print("Your age is :", age)

if (age > 18):
    print("adult")
else:
    print("not an adult")

# Example 2

price = int(input("enter the price: "))
budget = 500 

if(budget >= price):
    print("add to cart ")
else: 
    print("don't add to cart")