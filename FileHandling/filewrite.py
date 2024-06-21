fp=open("File1.txt",'w')


line1="Hello welcome"
line2="to Python Programming"
fp.write(line1+"\n"+line2)

# line3="File data changed"
# fp.write("  "+line3)

line3="file data changed"
fp.write("\n"+line3)

print("Content added to the file")
fp.close()