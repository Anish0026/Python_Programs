# calcualte the sum of the each number of the digit
n=int(input("Enter the digit :- "))
num=n
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print(f"The sum of the each number of the digit {num} is :- ",s)