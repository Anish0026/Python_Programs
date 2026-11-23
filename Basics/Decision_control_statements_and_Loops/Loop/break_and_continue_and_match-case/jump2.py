# w A P to calculate the total nuberof compositenumber and prime number 
prime=0
com=0

while(1):
    sc=0
    n=int(input("Enter the number ( press -1 to exit this loop) : "))
    if(n==-1):
        break
    for i in range(2,n):
        if(n%i==0):
            sc=1
            break
    if(sc):
        com+=1
    else:
        prime+=1
print("The total number of the prime number is :- ",prime)
print("The total number of composite number is :- ",com)