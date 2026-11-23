# calcualte the sum of the cubes of the number from 1 to n
n=int(input("Enter the limit :- "))
s=0
for i in range(1,n+1):
    a=i**3
    s+=a
print(f"The sum of the cubes of the numbers from 1 to {n} is :- ",s)
