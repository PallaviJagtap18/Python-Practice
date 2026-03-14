# Operators in Python
# Operators are special symbols used to perform operations on variables and values.

# 1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical calculations like addition, subtraction, multiplication, etc.

a = 10
b = 3

print("Addition: ", a + b )
print("Subtraction: ", a - b )
print("Multiplication: ", a * b )
print("Division: ", a / b )
print("Modulus: ", a % b )
print("Power: ", a ** b )
print("floor division: ", a // b )

# 2. Comparison Operators
# Comparison operators are used to compare two values.
# They return either True or False.

x = 5
y = 3 

print( x > y )
print( y > x )
print( x == y )
print( x != y)
print( x >= y ) 
print( x <= y )

# 3. Logical Operators
# Logical operators are used to combine conditional statements.

a = 10 
b = 20

print( a > b and b > 30 )
print( a > 5 or b > a )
print(not ( a > 5 ) ) 

# 4. Assignment Operators
# Assignment operators are used to assign values to variables.

x = 10

x += 5
print(x)

x -= 5 
print(x)

x *= x
print(x)

x /= 5
print(x)

# 5. Bitwise Operators
# Used to perform operations on binary numbers (bits).

a = 5
b = 3

print( a & b )       #Bitwise AND
print( a | b )       #Bitwise OR 
print( a ^ b )       #Bitwise XOR
print(~ a )          #Bitwise NOT

# 6. Identity Operators
# Used to compare the memory location of two objects.

x = [ 1, 2, 3, 4, 5, 6] 
y = x 
z = [ 1, 2, 3]

print(x is y )
print( x is z )
print ( x is not  z)

# 7. Membership Operators
#Used to test if a value exists in a sequence (list, tuple, string, etc.).

number = [ 1, 2, 3, 4, 5]
print( 3 in number )
print( 10 in number ) 
