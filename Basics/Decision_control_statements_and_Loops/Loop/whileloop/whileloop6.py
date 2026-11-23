# convert a decimal to its equivalent binary number 
dec=int(input("Enter the decimal number to convert it into the equivalent binary number :- "))
bin=0
num=dec
i=0
while(dec!=0):
    r=dec%2
    bin=bin+(r*(10**i))
    dec=dec//2
    i=i+1
print(f"The binary equivalent of the number {num} is :- ",bin)