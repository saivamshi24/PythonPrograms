import re 
str=re.match(r'Welcome','Welcome to python programming' )
print(str)
print(str.start()) # 0
print(str.end()) #6+1 =7
print(str.group()) #Welcome