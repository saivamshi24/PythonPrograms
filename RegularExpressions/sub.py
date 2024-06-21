import re
str=re.sub(r'Python','Java',"Pyhton programming Python")
print(str)

str=re.subn(r'Python','Java',"Python programming Python")
print(str)

str=re.sub('[a-z]','#','a1b2c3d4')
print(str)
str=re.subn('[a-z]','#','a1B2c3D4')
print(str)