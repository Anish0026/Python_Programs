import calendar
''' print the single month with the given year and month which is given by the user '''

n=int(input("Enter the year :- "))
m=int(input("Enter the specific month number :- "))
print(f"The calender of the month {m} of the year {n} is :- \n\n")
print(calendar.month(n,m))

''' print the whole year calender of the user provided year '''

n=int(input("\n\nEnter the year : "))
print(f"\n\nThe 12 months of the year {n} is :- \n")
for i in range(1,13):
    print(calendar.month(n,i))
