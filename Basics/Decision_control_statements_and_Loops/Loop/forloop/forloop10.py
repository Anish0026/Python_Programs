# the sum of the series 1/1 + 2^2/2 ...n^n/n
n=int(input("Enter the number or value of the n :- "))
s=0
for i in range(1,n+1):
    a=(i**i)/i
    s+=a
print("The value of the sum is :- ",s)