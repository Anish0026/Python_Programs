def gcd(a,b):
    rem=a%b
    if(rem==0):
        return b
    else:
        return gcd(b,rem)
a=int(input("Enter the first number :- "))
b=int(input("Enter the second number :- "))
if(a>b):
    print("The gcd of two numbers is :- ",gcd(a,b))
else:
    print("The gcd of two numbers is :- ",gcd(b,a))