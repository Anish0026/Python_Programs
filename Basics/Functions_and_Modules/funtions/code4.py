# write a program to convert the time into minute
def time_to_min(hrs,min):
    res=hrs*60+min
    return res
h=int(input("Enter the hrs :- "))
m=int(input("Enter the minute :- "))
print("The time in minute is :- ",time_to_min(h,m))