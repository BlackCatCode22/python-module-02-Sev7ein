#9/7/25
#s.n
def largestNumber(num1, num2, num3, largest):
    print("Message to User: You entered three numbers,", num1, ",", num2, ", and", num3,
          ". The first number was num1,", num1,
          ", the second was num2,", num2,
          ", and the third was num3,", num3,
          ". The largest number you entered was", largest)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

largestNumber(num1, num2, num3, largest)
