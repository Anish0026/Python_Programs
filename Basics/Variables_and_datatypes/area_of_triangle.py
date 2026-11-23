# calcualte a area of a triangle using heron's formula
a=float(input("Enter the 1st side of the triangle :- "))
b=float(input("Enter the 2nd side of the triangle :- "))
c=float(input("Enter the 3rdd side of the triangle :- "))
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of the triangle is :-", round(area, 2))
