# form a list from 1 to 50 and stop when the number is grater than 19
print("\n\n")
list=[i for i in range(1,51)]
print("The list is :-",list)
for num in list:
    if num>19:
        print("stop")
        break
    else:
        print(num)
print("\n\n")