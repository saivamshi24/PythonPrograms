import re 
str=re.search(r'Welcome',' Hello Welcome to python programming' )
print(str)
print(str.start()) # 0
print(str.end()) #6+1 =7
print(str.group()) #Welcome