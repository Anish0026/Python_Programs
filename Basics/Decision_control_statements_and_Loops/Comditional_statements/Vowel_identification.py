# Use of enumaerate function
string="Hello world"
vowels="AEIOUaeiou"
for index,char in enumerate(string):
    if char in vowels:
        print(f"The vowel {char} is present at index {index} in the string {string}")
