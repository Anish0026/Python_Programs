print("\n\n")
text=input("Enter the text to know the number of vowels in it :- ")
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count+=1
print(f"The number of the vowels in the {text} is :- ",count)
print("\n\n")
