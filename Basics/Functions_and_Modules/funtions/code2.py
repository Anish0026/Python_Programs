# a program to swap two numbers
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("\nAfter swapping :- ")
    print("The value of a :- ",a)
    print("The value of b :- ",b)
a=int(input("Enter the first number :- "))
b=int(input("Enter the second number :- "))
print("\nBefore swapping :-")
print("The value of a :- ",a)
print("The value of b :- ",b)
swap(a,b)
