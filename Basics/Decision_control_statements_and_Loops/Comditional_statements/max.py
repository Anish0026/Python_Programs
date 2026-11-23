# program to find the greatest number between three number
num1=int(input("Enter the first number :- "))
num2=int(input("Enter the second number :- "))
num3=int(input("Enter the third number :- "))
if num1>num2 and num1>num3:
    print("The greatest number is :- ",num1)
elif num3>num2 and num3>num1:
    print("The greatest number is :- ",num3)
else:
    print("The greatest number is :- ",num2)