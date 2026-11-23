# for a list of numbers you keep on suming on as long as you get only negative numbers if you encountered posetive numbers break their ....
num=[-1,-2,-4,5,-6,-7]
s=0
for i in num:
    if i<0:
        s=s+i
    else:
        continue
print("sum is :-",s)
