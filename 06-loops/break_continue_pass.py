# break 
# break is used to immediately stop the loop, even if the loop condition is still True.

# Example 

print("table of 5")
for i in range(1,20):
    if(i == 11):
        break
    print("5 X",i,"=",(5*i))

# continue 
# continue is used to skip the current iteration and move to the next iteration of the loop.

for i in range(1,9):
    if(i == 5):
        continue
    print(i)

# Pass 
# pass is a null statement. It does nothing, but it allows the program to run without error when a statement is required.

for i in range(5):
    if i == 3:
        pass
    print(i)