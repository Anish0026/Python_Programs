# exponent by recursion
def ex(x,y):
    if(y==0):
        return 1
    else:
        return x*ex(x,y-1)
x=int(input("Enter the value of the x :- "))
y=int(input("Enter the value of the y :- "))
print("The value of x^y is :- ",ex(x,y))
