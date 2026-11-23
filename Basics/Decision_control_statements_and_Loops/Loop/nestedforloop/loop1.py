''' print the following pattern
pass 1- 1 2 3 4 5 
pass 2- 1 2 3 4 5 
pass 3- 1 2 3 4 5 
pass 4- 1 2 3 4 5 
pass 5- 1 2 3 4 5 '''

for i in range(1,6):
    print("pass ",i,"-",end="")
    for j in range(1,6):
        print(j,end=" ")
    print()