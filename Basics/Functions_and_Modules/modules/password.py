import getpass

while(True):
    password=getpass.getpass(prompt="Enter the password :- ")
    if password=="success":
        print("Wwellcome to the world of anish ")
        break
    else:
        print("Incorrect password please try again later")