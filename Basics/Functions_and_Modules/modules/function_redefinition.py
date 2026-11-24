# this program illustrate the redefinition of any function
import datetime
def showmessage(msg):
    print(msg)
showmessage("Hello!")
def showmessage(msg):
    now=datetime.datetime.now()
    print(msg,end=" ")
    print(now)
showmessage("Current date and time is :- ")
