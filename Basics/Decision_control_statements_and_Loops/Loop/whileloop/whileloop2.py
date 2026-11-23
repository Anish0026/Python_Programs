# a program that can read the numbers until -1 is encountered and count the number of positive numbers, zeros and negative numbers 
negative=positive=zero=0
print("--------Enter -1 to exit -------")
while(1):
    n=int(input("Enter the number :- "))
    if(n==-1):
        break
    elif(n==0):
        zero+=1
    elif(n>0):
        positive+=1
    else:
        negative+=1
print("The total number of zeros enterd is :- ",zero)
print("The total numberof positive number enterd is :- ",positive)
print("The total number of negative number entered is :- ",negative)
