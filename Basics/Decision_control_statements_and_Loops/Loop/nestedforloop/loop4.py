''' print the following pattern / you can also do this for n number of inputs 
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 '''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

n=int(input("Enter the number of the limit :- "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()