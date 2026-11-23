#a program using the while loop to and terminate the loop by -1 and then count the number of pime number and composite number
totalprimenumber=0
totalcompositenumber=0

while(1):
    n=int(input("Enter the number (-1 for exit):- "))
    if(n==-1):
        break
    iscomposite=0
    for i in range(2,n):
        if(n%i==0):
            iscomposite=1
            break
    if(iscomposite):
        totalcompositenumber+=1
    else:
        totalprimenumber+=1
print("The total number of the composite numbers given by the user is :- ",totalcompositenumber)
print("The total number of the prime number given by the user :- ",totalprimenumber)