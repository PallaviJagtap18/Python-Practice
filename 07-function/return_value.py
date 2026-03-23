# Return Values
# A function can return a result using the return statement.

# Example 1

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# Example 2
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))