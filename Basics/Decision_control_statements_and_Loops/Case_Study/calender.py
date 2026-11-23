# generate a calender
import calendar
y=int(input("Enter the year :- "))
m=1
print("*******************************************calender**************************************************")
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while(i<=12):
    cal.prmonth(y,i)
    i+=1
