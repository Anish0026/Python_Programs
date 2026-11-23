# a program to calculate the sum from m to n 
m=int(input("Enter the value of m :- "))
n=int(input("Enter the value of n :- "))
s=0
while(m<=n):
    s+=m
    m+=1
print(f"The sum form {m} to {n} is :- ",s,"\n\n")