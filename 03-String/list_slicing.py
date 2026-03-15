# List Slicing
"""List Slicing (in Python) is the process of extracting a portion of a list by specifying a range of 
indices using the slicing operator :. It allows you to create a new list containing selected elements from the original list."""

name = "Hello World"

print(name[0 : 4])  # 0 is included and 4 in excluded
print(name[0 : -5]) # -5 = len(name) - 5
print(name[3 : 7])