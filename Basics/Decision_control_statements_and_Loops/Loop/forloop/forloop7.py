# a program to calculate pow(x,n)
x=int(input("Enter the number in which you want to calcualte the power : -"))
n=int(input("Enter the power :- "))
re=1
for i in range(n):
    re=re*x
print(f"The {x} to the power {n} is :- ",re)