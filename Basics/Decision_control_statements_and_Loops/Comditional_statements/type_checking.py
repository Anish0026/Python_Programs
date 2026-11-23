# take input from the user and check whether it is digit or character if it is vcharacter which tyoe of character
n=input("Enter the input :- ")
if(n.isalpha()):
    print("The input is a character")
    if(n>='a')and(n<='z'):
        print("The character is a lower case character")
    else:
        print("The character is a upper case character")
elif(n.isdigit()):
    print("The input is digit")
else:
    print("The input is a whitespace")
