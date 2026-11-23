# program to classify a number in prime or composite
n=int(input("Enter the number to know it is prime or composite number :- "))
iscomposite=0
if(n==1):
    print("The number is neither prime nor composite")
else:
    for i in range(2,n):
        if(n%i==0):
            iscomposite=1
            break
    if(iscomposite==1):
        print("The number is composite number")
    else:
        print("The number is prime number")
