day=int(input("Enter the day number to know the day name:- "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")  # Acts like 'default'
