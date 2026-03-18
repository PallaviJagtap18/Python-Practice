# While loop 

# A while loop is used to repeat a block of code as long as a condition is True.
# The loop stops when the condition becomes False.

# Write a program to calculate the sum of numbers from 1 to n using a while loop.

n = int(input("enter the valur of n :"))
i = 1
sum =0 
while(i<=n):
    sum = sum +i
    i= i+1
print(sum)
