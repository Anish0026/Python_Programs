import getpass

while(True):
    password=getpass.getpass(prompt="Enter the password :- ")
    if password=="success":
        print("Wellcome to the world of Anish!")
        break
    else:
        print("Incorrect password please try again later")
