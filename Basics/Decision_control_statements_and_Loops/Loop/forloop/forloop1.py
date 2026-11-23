# a program to calculate the avg of first n natural numbers
n=int(input("Enter the number value of n :- "))
s=0
for i in range(n+1):
    s=s+i
avg=s/n
print("The avg of the first n natural numbers is :- ",avg)
