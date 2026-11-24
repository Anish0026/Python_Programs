# a program of function to check whether a number is odd or even with return statement
def check(a):
    if(a%2==0):
        return 1
    else:
        return -1
n=int(input("Enter a number to know whether it is odd or even :- "))
k=check(n)
if(k==1):
    print("The number is an even number ")
else:
    print("The number is an odd number")
