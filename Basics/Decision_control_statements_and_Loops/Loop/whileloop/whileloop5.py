# check whetether a number is a armstrong  or not
n=int(input("Enter the number :- "))
i=len(str(n))
num=n
s=0
while(n!=0):
    r=n%10
    s=s+(r**i)
    n=n//10
if(num==s):
    print(f"The number {num} is armstrong number")
else:
    print(f"The number {num} is not armstrong number")
