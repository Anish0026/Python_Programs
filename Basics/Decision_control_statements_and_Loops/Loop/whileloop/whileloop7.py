# convert binary to decimal
bin=int(input("Enter the binary number :- "))
dec=0
num=bin
i=0
while(bin!=0):
    rem=bin%10
    dec=dec+(rem*(2**i))
    bin=bin//10
    i=i+1
print(f"The decimal equivalent of the number {num} is :- ",dec)