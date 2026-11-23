# calcualte the investment input an inital value of invest ment and annual interest and calculae the value of the invextment over the time
initialvalue=int(input("Enter the inital value of the investment :- "))
roi=int(input("Enter the rate of interest :- "))
yrs=int(input("Enter the number of years fjor wahich investent has to done :- "))
futurevalue=initialvalue
print("\tyear\t\t value")
print("------------------   ------------------")
for i in range(1,yrs+1):
    futurevalue*=(1+roi/100)
    print(i,"\t\t       ",futurevalue)
