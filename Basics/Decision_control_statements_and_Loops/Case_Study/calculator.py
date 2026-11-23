import math
print(" -----------------------calculaot---------------------------")
def sum(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
def squ(a):
    c=math.sqrt(a)
    return c
while(True):
    print("\nChoose the operation you to perform")
    print("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.SQUARE ROOT\n6.EXIT")
    n=int(input("Enter your choice please :- "))
    if(n==6):
        break
    elif(n==1):
        a=int(input("\nEnter the first number :- "))
        b=int(input("\nEnter the second number :- "))
        res=sum(a,b)
        print("\nThe sum of the two number is :- ",res)
    elif(n==2):
        a=int(input("Enter the first number :- "))
        b=int(input("Enter the second number :- "))
        res=sub(a,b)
        print("\nThe subtraction of the two number is :- ",res)
    elif(n==3):
        a=int(input("\nEnter the first number :- "))
        b=int(input("\nEnter the second number :- "))
        res=mul(a,b)
        print("\nThe multiplication of the two number is :- ",res)
    elif(n==4):
        a=int(input("\nEnter the first number :- "))
        b=int(input("\nEnter the second number :- "))
        res=div(a,b)
        print("\nThe division of the two number is :- ",res)
    elif(n==5):
        a=int(input("\nEnter the  number :- "))
        res=squ(a)
        print("\nThe square root of the  number is :- ",res)
    else:
        print("\nEnter the write choice please!")
print("\n\nYou choose to exit.Thank you\n\n")