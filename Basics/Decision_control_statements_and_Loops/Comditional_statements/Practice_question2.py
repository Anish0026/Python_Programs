# print the index and the character from the string " Today India will win against SA" untill first s appears
text="Today India will win against SA"
for index,char in enumerate(text):
    if char=="S" or char =="s":
        break
    else:
        print(index,char)
