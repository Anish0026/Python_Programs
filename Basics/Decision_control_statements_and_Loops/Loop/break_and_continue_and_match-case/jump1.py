# write a program to calculate the square root of any program 
import math
while(1):
    num=int(input("Enter the number (exit by -1 ) : -"))
    if(num==-1):
        break
    elif(num<0):
        print("quare root of the negative number is not calcualte here")
        continue
    else:
        print(f"The square root of the number {num} is :- ",math.sqrt(num))