import re
str=re.fullmatch(r"Welcome","Welcome")
print(str)

str=input("enter a string: ")
result=re.fullmatch(str,"ababab")
if result != None:
    print("full string matched")
else:
    print("full string didn't match")