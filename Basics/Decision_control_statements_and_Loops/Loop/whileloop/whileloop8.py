# take character from the user count the number of the space,lower case and the upper case exit when * is encountered

up_count=0
low_count=0
spa_count=0
num_count=0
print("For exit press * ")
while(1):
    ch=input("Enter the charecter :- ")
    if(ch=="*"):
        break
    elif(ch>='a') and (ch<='z'):
        low_count+=1
    elif(ch>='A') and (ch<='Z'):
        up_count+=1
    elif(ch>='0')and (ch<='9'):
        num_count+=1
    else:
        spa_count+=1
print("The total number of uppercase entered by the user is :- ",up_count)
print("The total number of lowercase entered by the user is :- ",low_count)
print("The total number of digit entered by the user is :- ",num_count)
print("The total number of space entered by the user is :- ",spa_count)
