import re
str=re.findall(r'Python','Python programming')
print(str)

search=re.findall('[0-9]','a1B2c3D4')
print(search)
search=re.findall("[a-z]","a1B2c3D4")
print(search)
search=re.findall("[A-Z]","a1B2c3D4")
print(search)