# multiplication table of any number given by the user
n=int(input("Enter any number to know its multiplication table :- "))
for i in range(1,11):
    print(f"{n}x{i} = {n*i}")
