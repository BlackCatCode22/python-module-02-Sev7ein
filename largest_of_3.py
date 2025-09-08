#9/6/25
#s.n

import math

# Program to find the largest of three integers using nested if statements

# Get three integers from the user
numOne= int(input("Enter the first integer: "))
numTwo = int(input("Enter the second integer: "))
numThree = int(input("Enter the third integer: "))

# Nested if logic
if numOne >= numTwo:
    if numOne >= numThree:
        largest = numOne
    else:
        largest = numThree
else:
    if numTwo >= numThree:
        largest = numTwo
    else:
        largest = numThree

# Output the result
print("The largest number is:", largest)
