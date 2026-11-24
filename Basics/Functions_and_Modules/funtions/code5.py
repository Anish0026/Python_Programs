# calculate a simple interest 
def interest(p,y,s):
    if(s=="y" or s=="Y"):
        si=float((p*12*y)/100)
    else:
        si=float((p*10*y)/100)
    return si
p=int(input("Enter the principle amountn :- "))
y=int(input("Enter the number of years :- "))
senior=input("is customer senior or not?\n :- ")
print("The amount of interest is goten by the user is :- ",interest(p,y,senior))