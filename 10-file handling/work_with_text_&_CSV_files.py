# Work with Text and CSV Files

# Text Files (.txt)
# Text files store plain text data.

# Example:
# Writing to text file

with open("data.txt", "w") as file:
    file.write("Name: John\nAge: 20")

# Reading text file
with open("data.txt", "r") as file:
    print(file.read())

# CSV Files (.csv)

CSV = Comma Separated Values
Used for storing tabular data (like Excel).

Python uses the built-in csv module.

# Writing CSV File:

import csv

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 20])
    writer.writerow(["Alice", 22])

# Reading CSV File:

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)

# Using Dictionary (Advanced):

import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["Name"], row["Age"])