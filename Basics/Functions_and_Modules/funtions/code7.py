 # a program to calculate the the sum of the series :- 1/1! + 4/2! + 27/3! + ...........
def fact(n):
    f=1
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the limit :- "))
s=0
for i in range(1,n+1):
    s+=(i**i)/(fact(i))
print("The sum of the series is :- ",s)