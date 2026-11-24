def max(numbers):       # global namespace
    print("User defines function max")
    large=-1
    for i in numbers:
        if i>large:
            large=i
    return large
numbers=list(map(int,input("Enter the numbers of the list to find the maximum of the numbers :- ").split()))
print("The largest number from the list is :- ",max(numbers))
print("The sum of the numbers in the list is :- ",sum(numbers))
