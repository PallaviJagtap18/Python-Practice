# Built-in Modules
# Python provides many pre-installed modules.

# (a) math module
# Used for mathematical operations

import math
print(math.sqrt(36))   
print(math.factorial(5)) 
print(math.pi)         

# b) random module
# Used for generating random values

import random
print(random.randint(1, 10))  
print(random.choice([1, 2, 3]))  

# (c) datetime module
# Used for date and time

import datetime

now = datetime.datetime.now()
print(now)   

print(now.date()) 
print(now.time())  
