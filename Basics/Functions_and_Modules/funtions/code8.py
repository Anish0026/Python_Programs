# write a program to add the values passed by the function use docstring and variable length arguments
def add(*args):
    '''Function returns the sum of the passed variables '''
    s=0
    for i in  args:
        s+=i
    return s
print(add.__doc__)# used to print the docstring of the function
print("Sum :- ",add(1,2,3))
