fp=open("File1.txt",'r')

#data=fp.read() #char by char
data=fp.readline() #single line charecter by charecter
#data=fp.readlines() #lines 

for i in data:
    print(i)

fp.close()