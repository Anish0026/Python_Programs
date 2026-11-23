# program to print the numbers from m to n and classify them into odd and even numbers
m=int(input("Enter the number m :- "))
n=int(input("Enter the number n :- "))
for i in range (m,n+1):
    if(i%2==0):
        print(f"{i} is an even number")
    else:
        print(f"{i}  is an odd number")
