# Lambda Functions
# A lambda function is a small anonymous (nameless) function written in one line.

# Syntax:
# lambda arguments: expression

#  Examples

square = lambda x: x * x
print(square(5))


# 1. Addition

add = lambda a, b: a + b
print(add(3, 4))

# 2. Using with map()

nums = [1, 2, 3]
result = list(map(lambda x: x*2, nums))
print(result)