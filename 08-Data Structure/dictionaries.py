# 4. Dictionaries
# A dictionary stores data in:
# Key-value pairs
# Unordered (Python 3.7+ maintains insertion order)
# Mutable

my_dict = {"name": "John", "age": 20}

# Example

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

print(student["name"])  

# Key Features
# Keys must be unique
# Keys are immutable (string, number, tuple)
# Values can be any data type

# Common Operations

student["age"] = 22           # Update
student["grade"] = "A"        # Add new key
del student["marks"]          # Delete

#  Looping Through Dictionary
for key, value in student.items():
    print(key, value)