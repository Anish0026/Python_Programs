# Check and  count the number of the odd and even number from 1 to 10
ev=0
od=0
for i in range(1,11):
    if i%2==0:
        ev+=1
    else:
        od+=1
print("The number of the even numbers from 1 to 10 is :- ",ev)
print("The number of the odd numbers from 1 to 10 is :- ",od)
