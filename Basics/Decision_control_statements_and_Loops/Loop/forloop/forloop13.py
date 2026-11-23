# write a program to generate the calender of a month given the start day and the number of the days in that month
startday=int(input("Enter the start day of the month (1 to 7)(1 for Sunday, 2 for Monday, up to 7 for Saturday annd so on) :- "))
numof_days=int(input("Enter the numbers of the days in the month :- "))
print("Sun  Mon  Tues Wed  Thurs  Fri  Sat")
print("-----------------------------------")
for i in range(startday-1):
    print("     ",end="")
for i in range(1,numof_days+1):
    print(f"{i:>3}  ",end="")
    if((i+startday-1)%7==0):
        print()
