# calculate the bill amounnt of an item where its quantitysold,value ,discount and tax is given
q=float(input("Enter the quantity of the item :- "))
value=float(input("Enter the value of the item :- "))
dis=float(input("Enter the discount :- "))
tax=float(input("Enter the tax :- "))
am=q*value
dis_am=(am*dis)/100
sub_total=am-dis_am
tax_am=(sub_total*tax)/100
total=sub_total+tax_am
print("\n\n***************  BILL  ****************")
print("\nQuantity sold   :-\t",q)
print("\nPrice per item :-\t",value)
print("\n              \t----------------------")
print("\nAmount          :-\t",am)
print("\nDiscount        :-\t-",dis_am)
print("\n              \t----------------------")
print("\nDiscount total  :-\t",sub_total)
print("\nTax             :-\t+",tax_am)
print("\n              \t----------------------")
print("\nTotal amount to be paid :- ",total)
print("\n\n")


