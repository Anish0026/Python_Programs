''' print the following patterns / you can also do that with n number of input 
    *
    **
    ***
    ****
    ***** '''
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

n=int(input("Enter the number of the limit :- "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()