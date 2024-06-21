import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababa")
for match in matcher:
    count+=1 #1,2,3
    print(match.start(),"...",match.end(),"...",match.group())
    print("the number of occurences: ",count)