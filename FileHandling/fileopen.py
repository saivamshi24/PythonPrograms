fp=open("File1.txt",'w')
#'W' --> if the file is existing it will rewrite the existing content
#'W' --> if the file is not exiting it will create a new file

print(fp.closed) # False 
print(fp.name)   # File1.txt
print(fp.mode)   # w

fp.close()
print(fp.closed) #True  
