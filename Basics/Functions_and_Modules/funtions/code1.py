# programing to check whetheer two numbers are equal or not
def check_relation(a,b):
    if(a==b):
        print("The numbers are same")
    elif(a>b):
        print(f"The numbers are not equal and the number {a} is greater than number {b}")
    else:
        print(f"The numbers are not equal and the number {b} is greater than number {a}")

a=int(input("Enter the first number :- "))
b=int(input("Enter the second number :- "))
check_relation(a,b)