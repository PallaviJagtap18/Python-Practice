# Parameters:
# Variables listed in the function definition.

#  Arguments:
# Values passed to the function when calling it.

# Types of Arguments:

# 1.Positional Arguments
def add(a, b):
    print(a + b)

add(2, 3)

# 2.Keyword Arguments
add(a=2, b=3)

# 3.Default Arguments
def greet(name="Guest"):
    print("Hello", name)

greet()          # uses default
greet("Amit")

# 4.Variable-length Arguments
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)
