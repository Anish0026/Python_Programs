# the sum of the series 1/2 + 2/3 ...n/n+1
n=int(input("Enter the number or value of the n :- "))
s=0
for i in range(1,n+1):
    a=i/(i+1)
    s+=a
print("The value of the sum is :- ",s)