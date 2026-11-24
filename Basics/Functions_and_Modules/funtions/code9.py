''' print the following patterns using the default arguments
    %%%%%%
    ^^^^^^
    ^^^^^^^^^^
    ^^^^^^^^^^^^^^
    ^^^^^^^^^^^^^^
'''
def pattern(c="%",r=1,co=6):
    for i in range(r):
        print()
        for j in range(co):
            print(c,end="")
n=input("Enter the character to be displayed :- ")
r=int(input("Enter the number of rows :- "))
c=int(input("Enter the number of column :- "))
pattern()
pattern(n)
pattern(n,r)
pattern(n,r,c)
