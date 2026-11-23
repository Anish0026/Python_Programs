# gcd of two number
num1=int(input("Enter the 1st number :- "))
num2=int(input("Enter the 2nd number :- "))
if(num1>num2):
    divi=num1
    divis=num2
else:
    divi=num2
    divis=num1
while(divis!=0):
    rem=divi%divis
    divi=divis
    divis=rem
print(f"The gcd of two numbers {num1} and {num2} is :- ",divi)
