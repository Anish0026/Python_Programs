# factorial of number using for loop
n=int(input("Enter the number for which you want to know the factorial :- "))
k=1
for i in range(1,n+1):
    k=k*i
print("The factorial of the number",n,":- ",k)