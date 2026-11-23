# program to check ehther it is palindrom or not
n=int(input("Enter any digit:- "))
i=len(str(n))
print(i)
num=n
s=0
while(n>0):
    i=i-1
    r=n%10
    s=s+(r*(10**i))
    n=n//10
if(s==num):
    print("The number is palindrom")
else:
    print("The number is not palindrom")

n=int(input("Enter any digit:- "))
p=n
d=0
while(n>0):
    r=n%10
    d=d*10+r
    n=n//10
if(d==p):
    print("The number is palindrom")
else:
    print("The number is not palindrom")

