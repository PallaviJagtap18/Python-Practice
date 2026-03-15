# Strings

# A string is a sequence of characters used to store text.
# Strings can contain letters, numbers, symbols, and spaces.

# In Python, strings are written inside single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

# Creating Strings
name = "Alice"
city = 'Mumbai'
message = "Python is easy to learn"

print(name)
print(city)
print(message)

# Accessing Characters in a String
# Each character in a string has an index number starting from 0.

text = "Python"

print(text[0])   # First character
print(text[3])   # Fourth character
print(text[-1])  # Last character

# String Concatenation
# Concatenation means joining two or more strings using the + operator.

first_name = "PRAJAKTA"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)

# String Repetition
# The * operator can repeat a string multiple times.

word = "Hi "

print(word * 3)

# Common String Methods
# Python provides many built-in methods to work with strings.

text = "hello python"
word = "###python###"
str1 = "Welcome to Python"

print(text.upper())                       # Converts string to uppercase
print(text.lower())                       # Converts string to lowercase
print(text.replace("python", "world"))    #	Replaces part of a string
print(word.strip("#"))                    # Removes spaces from beginning and end / remove particular part
print(text.split())                       # Splits string into a list
print(hello.capitalize())                 # First character of a string to uppercase and all remaining characters to lowercase.
print(str1.center(50))                    # Align a string in the center of a specified width by adding padding characters (spaces by default) on both sides.
print(str1.count(o))

# String Length
# The len() function is used to find the length of a string.

language = "Python"

print(len(language))

# String Formatting
# String formatting allows inserting variables into strings.

name = "Prajakta"
age = 20

print(f"My name is {name} and I am {age} years old.")
