# a program to calculate the avg of the positive and the negative number entered by the user stop when the -1 is encountered
pos_count=0
pos_num=0
neg_count=0
neg_num=0
while(1):
    n=int(input("Enter the nuber (-1 to exit):-"))
    if(n==-1):
        break
    elif(n>0):
        pos_count+=1
        pos_num+=n
    else:
        neg_count+=1
        neg_num+=n
pos_avg=float(pos_num)/pos_count
neg_avg=float(neg_num)/neg_count
print("The average of the positive mumber entered by the  user is :- ",pos_avg)
print("The average of the negative number entered by the user is :- ",neg_avg)