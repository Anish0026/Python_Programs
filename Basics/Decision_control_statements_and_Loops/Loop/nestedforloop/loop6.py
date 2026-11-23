''' print the following patten / you can also do this with n number of inputs 
    0
    12
    345
    6789  '''
count=0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count,end="")
        count+=1
