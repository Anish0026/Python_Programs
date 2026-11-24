# fibonacci series with recursion
def fibbo(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)
n=int(input("Enter the limit you want to get in the fibonacci series :- "))
print("The series is :-",end=" ")
for i in range(n):
    print(fibbo(i),"\t",end="")
