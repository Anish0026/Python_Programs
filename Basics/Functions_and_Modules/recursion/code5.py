# a program to count how many time a recursion function call itself
def fun(n,count=0):
    if n==0:
        return count
    else:
        return fun(n-1,count+1)
print("Number of recursive function call it self is :- ",fun(100))